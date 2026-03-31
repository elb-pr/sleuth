#!/usr/bin/env python3
"""
Drill Artist Discovery

Multi-source research tool for discovering and profiling UK drill artists
during investigations. Generates structured search queries, normalises
multi-platform data into entity profiles, and classifies reach tiers.

Sources (via MCP and web tools at runtime):
  - YouTube: search, channel stats, video metadata, comment sentiment
  - Reddit: r/ukdrill, r/drillshitpost scene discussion
  - Web search: articles, court reports, label pages, event lineups
  - Sherlock/Maigret: cross-reference handles across platforms

Discovery modes:
  - ENTITY_EXPAND: start from a known entity, map their musical connections
  - SCENE_CRAWL: start from a gang/area, find all associated artists
  - COLLAB_TRACE: follow collaboration chains across tracks
  - INCIDENT_LINK: find artists linked to a specific incident or court case

Profile output feeds into assets/entity-database/entities.json.

Usage:
    # As a module
    from discover_artists import build_search_queries, build_artist_profile
    queries = build_search_queries(["Active Gxng"], ["drill"], mode="scene_crawl", area="Brixton")

    # CLI
    python discover_artists.py --mode scene_crawl --seed "Active Gxng" --area "Brixton SW9"
"""

import json
import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict, field

SKILL_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_BASE_PATH = SKILL_DIR / "assets" / "entity-database" / "gang-knowledge-base.json"


# --- Discovery modes ---

MODES = ["entity_expand", "scene_crawl", "collab_trace", "incident_link"]

# --- Reach tiers ---

REACH_TIERS = {
    "underground": (0, 10_000),
    "emerging": (10_000, 100_000),
    "mid_tier": (100_000, 1_000_000),
    "established": (1_000_000, None),
}


@dataclass
class ArtistProfile:
    """Normalised artist profile for entity database insertion."""
    name: str
    aliases: list[str] = field(default_factory=list)
    gang_affiliation: str = ""
    area: str = ""
    postcode: str = ""
    handles: dict = field(default_factory=dict)  # {platform: url}
    reach_tier: str = "underground"
    youtube_views: int = 0
    collaborators: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)
    tracks: list[dict] = field(default_factory=list)  # [{title, url, views, date}]
    incidents: list[str] = field(default_factory=list)  # incident IDs from entity db
    court_cases: list[str] = field(default_factory=list)
    notes: str = ""
    evidence_quality: str = "SPECULATION"  # CONFIRMED, LIKELY, SPECULATION, GAP
    sources: list[str] = field(default_factory=list)


def classify_reach(view_count: int) -> str:
    """Classify artist reach tier from YouTube view count."""
    for tier, (lo, hi) in REACH_TIERS.items():
        if hi is None and view_count >= lo:
            return tier
        if hi is not None and lo <= view_count < hi:
            return tier
    return "underground"


def load_gang_context(gang_name: str) -> Optional[dict]:
    """Load gang info from knowledge base for context."""
    if not KNOWLEDGE_BASE_PATH.exists():
        return None

    with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    gangs = data if isinstance(data, list) else data.get("gangs", [])
    gang_lower = gang_name.lower()

    for gang in gangs:
        name = gang.get("name", "")
        # Check against name and all aliases (separated by / in the name field)
        all_names = [n.strip().lower() for n in name.split("/")]
        if gang_lower in all_names or any(gang_lower in n for n in all_names):
            return gang

    return None


def build_search_queries(
    seed_entities: list[str],
    genre_tags: list[str],
    mode: str = "scene_crawl",
    area: Optional[str] = None,
    gang: Optional[str] = None,
) -> list[dict]:
    """
    Generate search queries for a given discovery mode.

    Claude calls this to get structured queries, then executes them via
    YouTube search, web_search, or Reddit MCP tools.

    Returns list of {query, platform, purpose} dicts.
    """
    queries = []

    if mode == "scene_crawl":
        for entity in seed_entities:
            queries.extend([
                {"query": f'"{entity}" drill music video', "platform": "youtube", "purpose": "find_tracks"},
                {"query": f'"{entity}" UK drill', "platform": "youtube", "purpose": "find_tracks"},
                {"query": f'"{entity}" freestyle', "platform": "youtube", "purpose": "find_tracks"},
                {"query": f'{entity} drill artist site:reddit.com/r/ukdrill', "platform": "web", "purpose": "scene_context"},
                {"query": f'"{entity}" members artists rappers', "platform": "web", "purpose": "find_members"},
            ])
            if area:
                queries.append({"query": f'"{entity}" {area} drill', "platform": "web", "purpose": "area_confirm"})

    elif mode == "entity_expand":
        for entity in seed_entities:
            queries.extend([
                {"query": f'"{entity}" feat OR ft OR x drill', "platform": "youtube", "purpose": "find_collabs"},
                {"query": f'"{entity}" label signed', "platform": "web", "purpose": "find_label"},
                {"query": f'"{entity}" interview', "platform": "youtube", "purpose": "find_context"},
                {"query": f'"{entity}" arrested OR charged OR sentenced', "platform": "web", "purpose": "find_incidents"},
                {"query": f'who is {entity} drill rapper', "platform": "web", "purpose": "background"},
            ])

    elif mode == "collab_trace":
        for entity in seed_entities:
            queries.extend([
                {"query": f'"{entity}" ft OR feat drill', "platform": "youtube", "purpose": "collab_tracks"},
                {"query": f'"{entity}" collaboration drill 2024 OR 2025 OR 2026', "platform": "web", "purpose": "recent_collabs"},
                {"query": f'{entity} collab site:reddit.com/r/ukdrill', "platform": "web", "purpose": "collab_discussion"},
            ])

    elif mode == "incident_link":
        for entity in seed_entities:
            queries.extend([
                {"query": f'"{entity}" crown court sentencing remarks', "platform": "web", "purpose": "court_records"},
                {"query": f'"{entity}" rapper drill arrested OR stabbing OR shooting', "platform": "web", "purpose": "incident_news"},
                {"query": f'"{entity}" drill ban injunction', "platform": "web", "purpose": "legal_orders"},
                {"query": f'{entity} case site:reddit.com/r/ukdrill', "platform": "web", "purpose": "community_intel"},
            ])

    # Add gang context queries if available
    if gang:
        gang_info = load_gang_context(gang)
        if gang_info:
            location = gang_info.get("location", "")
            allies = gang_info.get("allies", [])
            for ally in allies[:3]:
                queries.append({
                    "query": f'"{ally}" drill music video',
                    "platform": "youtube",
                    "purpose": "allied_group_tracks",
                })
            if location:
                queries.append({
                    "query": f'drill {location} music video',
                    "platform": "youtube",
                    "purpose": "area_tracks",
                })

    return queries


def build_artist_profile(raw_data: dict) -> ArtistProfile:
    """
    Normalise raw multi-source data into a standard artist profile.

    Input: dict with optional keys from each source:
        youtube: {channel, views, subscribers, videos: [{title, url, views, date}]}
        web: {articles: [{title, url, snippet}]}
        reddit: {mentions: [{title, url, subreddit, score}]}
        handles: {platform: url}
        gang: str
        area: str

    Output: ArtistProfile for entity database insertion.
    """
    profile = ArtistProfile(name=raw_data.get("name", "Unknown"))

    profile.aliases = raw_data.get("aliases", [])
    profile.gang_affiliation = raw_data.get("gang", "")
    profile.area = raw_data.get("area", "")
    profile.postcode = raw_data.get("postcode", "")
    profile.handles = raw_data.get("handles", {})

    # YouTube data
    yt = raw_data.get("youtube", {})
    if yt:
        profile.youtube_views = yt.get("views", 0)
        profile.reach_tier = classify_reach(profile.youtube_views)
        profile.tracks = yt.get("videos", [])

    # Extract collaborators from track titles
    for track in profile.tracks:
        title = track.get("title", "")
        # Look for "X ft Y" or "X x Y" patterns
        for sep in [" ft ", " ft. ", " feat ", " feat. ", " x "]:
            if sep in title.lower():
                parts = title.lower().split(sep)
                if len(parts) > 1:
                    collab = parts[1].split(" - ")[0].split("(")[0].strip()
                    if collab and collab not in profile.collaborators:
                        profile.collaborators.append(collab)

    profile.labels = raw_data.get("labels", [])
    profile.incidents = raw_data.get("incidents", [])
    profile.court_cases = raw_data.get("court_cases", [])
    profile.notes = raw_data.get("notes", "")
    profile.sources = raw_data.get("sources", [])

    # Evidence quality based on source count
    src_count = len(profile.sources)
    if src_count >= 4:
        profile.evidence_quality = "CONFIRMED"
    elif src_count >= 2:
        profile.evidence_quality = "LIKELY"
    else:
        profile.evidence_quality = "SPECULATION"

    return profile


def profile_to_entity(profile: ArtistProfile) -> dict:
    """Convert an ArtistProfile to entity database format."""
    return {
        "id": f"artist-{profile.name.lower().replace(' ', '-')}",
        "type": "individual",
        "subtype": "artist",
        "name": profile.name,
        "aliases": profile.aliases,
        "gang_affiliation": profile.gang_affiliation,
        "area": profile.area,
        "postcode": profile.postcode,
        "handles": profile.handles,
        "reach_tier": profile.reach_tier,
        "youtube_views": profile.youtube_views,
        "collaborators": profile.collaborators,
        "labels": profile.labels,
        "tracks": profile.tracks,
        "incidents": profile.incidents,
        "court_cases": profile.court_cases,
        "notes": profile.notes,
        "evidence_quality": profile.evidence_quality,
        "sources": profile.sources,
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Drill artist discovery tool")
    parser.add_argument("--mode", "-m", choices=MODES, default="scene_crawl", help="Discovery mode")
    parser.add_argument("--seed", "-s", nargs="+", required=True, help="Seed entities (artist/gang names)")
    parser.add_argument("--area", "-a", help="Area/postcode context")
    parser.add_argument("--gang", "-g", help="Gang name for knowledge base lookup")
    parser.add_argument("--format", "-f", choices=["json", "flat"], default="json", help="Output format")

    args = parser.parse_args()

    print(f"Mode: {args.mode}")
    print(f"Seeds: {args.seed}")
    if args.gang:
        gang_info = load_gang_context(args.gang)
        if gang_info:
            print(f"Gang context loaded: {gang_info.get('name')}")
            print(f"  Location: {gang_info.get('location', 'unknown')}")
            print(f"  Allies: {gang_info.get('allies', [])}")
        else:
            print(f"Gang '{args.gang}' not found in knowledge base")

    queries = build_search_queries(
        seed_entities=args.seed,
        genre_tags=["drill"],
        mode=args.mode,
        area=args.area,
        gang=args.gang,
    )

    print(f"\nGenerated {len(queries)} search queries:")
    if args.format == "json":
        print(json.dumps(queries, indent=2))
    else:
        for q in queries:
            print(f"  [{q['platform']}] ({q['purpose']}) {q['query']}")


if __name__ == "__main__":
    main()
