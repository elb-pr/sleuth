#!/usr/bin/env python3
"""
Artist discovery: multi-source research for sourcing and profiling artists.

Sources (via MCP and web tools):
  - YouTube: search, channel stats, video metadata, comment sentiment
  - Web search (Exa/Tavily): articles, interviews, label pages, event lineups
  - Reddit: scene discussion, artist mentions, community sentiment
  - Sherlock: cross-reference handles across platforms

Discovery modes:
  - SCENE_CRAWL: start from known artists, follow collabs/labels/events outward
  - QUERY_SEARCH: keyword-driven search ("dark rolling D&B 2025")
  - GRAPH_EXPAND: expand scene graph edges by researching existing node metadata
  - DEEP_CUT: find artists with <10k views matching a spectral profile

Profile output:
  - Artist metadata (name, handles, labels, events, location)
  - Reach metrics (YouTube views, Spotify monthly, social followers)
  - Scene connections (who they've worked with, shared lineups, label mates)
  - Sonic fingerprint (if audio available: feature vector from analyse_track)

STATUS: STUB — interfaces defined, Claude orchestrates via MCP tools at runtime.
"""

import json
import os
from typing import Dict, List, Optional

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# --- Discovery modes ---
MODES = ["scene_crawl", "query_search", "graph_expand", "deep_cut"]

# --- Reach tiers (for recommendation card badges) ---
REACH_TIERS = {
    "underground": (0, 10_000),         # <10k views
    "emerging": (10_000, 100_000),       # 10k-100k
    "mid_tier": (100_000, 1_000_000),    # 100k-1M
    "established": (1_000_000, None),    # 1M+
}


def classify_reach(view_count: int) -> str:
    """Classify artist reach tier from YouTube view count."""
    for tier, (lo, hi) in REACH_TIERS.items():
        if hi is None and view_count >= lo:
            return tier
        if lo <= view_count < hi:
            return tier
    return "underground"


def build_search_queries(seed_artists: List[str], genre_tags: List[str], mode: str) -> List[str]:
    """Generate search queries for a given discovery mode.

    Claude calls this to get structured queries, then executes them via
    YouTube search, web_search, Exa, or Reddit MCP tools.

    Returns list of query strings.
    """
    raise NotImplementedError


def build_artist_profile(raw_data: Dict) -> Dict:
    """Normalise raw multi-source data into a standard artist profile.

    Input: dict with optional keys from each source (youtube, web, reddit, spotify).
    Output: normalised profile dict for scene graph insertion.
    """
    raise NotImplementedError


def sherlock_cross_reference(handle: str) -> Dict:
    """Cross-reference an artist handle across platforms.

    Given a handle (e.g. 'kanaborgs'), search for matching profiles on:
    YouTube, SoundCloud, Bandcamp, Instagram, Twitter/X, Facebook, Spotify, Beatport.

    Returns dict of {platform: url} for confirmed matches.

    NOTE: This runs through Claude's web_search — not automated Sherlock CLI.
    The name is a nod to the methodology, not the tool.
    """
    raise NotImplementedError


def research_trivia(artist_name: str, track_title: str) -> str:
    """Research trivia for recommendation card 'Trivia' section.

    Claude calls this to generate search queries, then synthesises results into
    2-3 sentences of genuinely interesting context.

    Returns structured trivia prompt for Claude to execute.
    """
    queries = [
        f'"{artist_name}" interview',
        f'"{artist_name}" "{track_title}" behind the scenes',
        f'"{artist_name}" label signed',
        f'"{artist_name}" festival lineup 2025 2026',
    ]
    return json.dumps({"queries": queries, "instruction": "Search these, synthesise into 2-3 sentences of trivia"})


if __name__ == "__main__":
    print("Artist discovery module — stub only.")
    print(f"Modes: {MODES}")
    print(f"Reach tiers: {json.dumps(REACH_TIERS, indent=2)}")
    print(f"\nExample trivia queries for Kanine - Bloodstream:")
    print(research_trivia("Kanine", "Bloodstream"))
