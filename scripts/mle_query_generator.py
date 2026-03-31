#!/usr/bin/env python3
"""
MLE Query Generator

Converts drill slang, gang names, and MLE (Multicultural London English)
terms into structured search queries for investigation tools.

Reads the MLE lexicon from references/thinking/mle-lexicon.md and uses it
to expand, translate, and generate multi-platform search queries.

Usage:
    # As a module (called by Claude during investigation)
    from mle_query_generator import generate_queries
    queries = generate_queries("man got bored on the opp block", platforms=["youtube", "reddit"])

    # CLI
    python mle_query_generator.py "waps out the rambo" --platforms youtube reddit courts
"""

import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

SKILL_DIR = Path(__file__).resolve().parent.parent
LEXICON_PATH = SKILL_DIR / "references" / "thinking" / "mle-lexicon.md"
KNOWLEDGE_BASE_PATH = SKILL_DIR / "assets" / "entity-database" / "gang-knowledge-base.json"


@dataclass
class SearchQuery:
    """A single search query with metadata."""
    query: str
    platform: str
    intent: str  # what we're looking for: incident, entity, location, media, court
    source_term: str  # original MLE term that generated this
    translations: list[str]  # standard English equivalents used


def load_lexicon(path: Optional[Path] = None) -> dict[str, dict]:
    """
    Parse the MLE lexicon markdown table into a lookup dict.

    Returns dict keyed by slang term (lowercase), value is dict with:
        meaning, notes, category
    """
    path = path or LEXICON_PATH
    if not path.exists():
        return {}

    lexicon = {}
    current_category = "uncategorised"

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("###"):
                current_category = line.lstrip("#").strip()
                continue

            if line.startswith("|") and not line.startswith("| ---") and not line.startswith("| Term"):
                parts = [p.strip() for p in line.split("|")]
                parts = [p for p in parts if p]

                if len(parts) >= 2:
                    term = parts[0].lower().strip()
                    meaning = parts[1].strip()
                    notes = parts[2].strip() if len(parts) > 2 else ""

                    lexicon[term] = {
                        "meaning": meaning,
                        "notes": notes,
                        "category": current_category,
                    }

                    if "/" in term:
                        for variant in term.split("/"):
                            v = variant.strip().lower()
                            if v and v not in lexicon:
                                lexicon[v] = lexicon[term]

    return lexicon


def load_gang_names(path: Optional[Path] = None) -> list[dict]:
    """Load gang names and aliases from the knowledge base."""
    path = path or KNOWLEDGE_BASE_PATH
    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "gangs" in data:
        return data["gangs"]
    return []


PLATFORM_TEMPLATES = {
    "youtube": [
        '"{term}" drill',
        '"{term}" UK drill',
        '"{gang}" {term}',
        '{term} music video',
    ],
    "reddit": [
        '"{term}" site:reddit.com/r/ukdrill',
        '"{term}" site:reddit.com/r/drillshitpost',
        '{term} beef explained',
    ],
    "courts": [
        '"{real_name}" crown court',
        '"{real_name}" sentencing remarks',
        '"{real_name}" {postcode} magistrates',
    ],
    "news": [
        '"{real_name}" stabbing OR shooting {area}',
        '"{term}" {area} BBC OR Standard OR Mirror',
        '{area} knife crime {year}',
    ],
    "social": [
        '"{term}" site:instagram.com',
        '"{term}" site:twitter.com',
        '"{term}" snapchat drill',
    ],
}


def translate_phrase(phrase: str, lexicon: dict) -> list[dict]:
    """Find MLE terms in a phrase and return their translations."""
    found = []
    phrase_lower = phrase.lower()

    for term in sorted(lexicon.keys(), key=len, reverse=True):
        if term in phrase_lower:
            found.append({
                "term": term,
                "meaning": lexicon[term]["meaning"],
                "category": lexicon[term]["category"],
                "notes": lexicon[term]["notes"],
            })
            phrase_lower = phrase_lower.replace(term, " " * len(term))

    return found


def classify_intent(translations: list[dict]) -> list[str]:
    """Determine search intent from translated terms."""
    intents = set()

    violence_terms = {"stab", "shoot", "shot", "murder", "kill", "attack", "wound"}
    location_terms = {"block", "estate", "ends", "area", "yard", "trap"}
    media_terms = {"track", "tune", "video", "freestyle", "song"}
    financial_terms = {"food", "pack", "work", "trap", "line", "county"}

    for t in translations:
        meaning_lower = t["meaning"].lower()
        words = set(meaning_lower.split())

        if words & violence_terms:
            intents.add("incident")
            intents.add("court")
        if words & location_terms:
            intents.add("location")
        if words & media_terms:
            intents.add("media")
        if words & financial_terms:
            intents.add("financial")

        if t["category"] in ("Self-Reference & Address", "Opposition & Conflict"):
            intents.add("entity")

    return list(intents) if intents else ["general"]


def generate_queries(
    phrase: str,
    platforms: Optional[list[str]] = None,
    gang_context: Optional[str] = None,
    area_context: Optional[str] = None,
    year_context: Optional[str] = None,
    lexicon: Optional[dict] = None,
) -> list[SearchQuery]:
    """
    Generate structured search queries from an MLE phrase.

    Args:
        phrase: raw input text containing MLE/drill slang
        platforms: which platforms to generate queries for (default: all)
        gang_context: known gang name for context
        area_context: known area/postcode for context
        year_context: year for temporal filtering
        lexicon: pre-loaded lexicon (loads from file if not provided)

    Returns:
        List of SearchQuery objects ready for execution
    """
    if lexicon is None:
        lexicon = load_lexicon()

    if platforms is None:
        platforms = list(PLATFORM_TEMPLATES.keys())

    translations = translate_phrase(phrase, lexicon)
    intents = classify_intent(translations)

    queries = []
    translation_strs = [t["meaning"] for t in translations]

    for platform in platforms:
        templates = PLATFORM_TEMPLATES.get(platform, [])

        for template in templates:
            context = {
                "term": phrase,
                "gang": gang_context or "",
                "area": area_context or "",
                "year": year_context or "",
                "real_name": "",
                "postcode": area_context or "",
            }

            # Generate queries using each translated term
            for t in translations:
                ctx = {**context, "term": t["meaning"]}
                try:
                    q = template.format(**ctx)
                except KeyError:
                    continue

                if '""' in q or not q.strip():
                    continue

                q = re.sub(r"\s+", " ", q).strip()
                if len(q) > 3:
                    for intent in intents:
                        queries.append(SearchQuery(
                            query=q, platform=platform, intent=intent,
                            source_term=t["term"], translations=translation_strs,
                        ))

            # Also generate with raw phrase
            try:
                q = template.format(**context)
            except KeyError:
                continue

            q = re.sub(r"\s+", " ", q).strip()
            if q and len(q) > 3 and '""' not in q:
                for intent in intents:
                    queries.append(SearchQuery(
                        query=q, platform=platform, intent=intent,
                        source_term=phrase, translations=translation_strs,
                    ))

    # Deduplicate
    seen = set()
    unique = []
    for sq in queries:
        if sq.query not in seen:
            seen.add(sq.query)
            unique.append(sq)

    return unique


def format_output(queries: list[SearchQuery], fmt: str = "json") -> str:
    """Format query results for output."""
    if fmt == "json":
        return json.dumps([asdict(q) for q in queries], indent=2)
    elif fmt == "flat":
        return "\n".join(f"[{q.platform}] ({q.intent}) {q.query}" for q in queries)
    elif fmt == "grouped":
        by_platform = {}
        for q in queries:
            by_platform.setdefault(q.platform, []).append(q)
        lines = []
        for platform, qs in by_platform.items():
            lines.append(f"\n=== {platform.upper()} ===")
            for q in qs:
                lines.append(f"  [{q.intent}] {q.query}")
        return "\n".join(lines)
    return ""


def main():
    parser = argparse.ArgumentParser(
        description="Generate investigation search queries from MLE/drill slang"
    )
    parser.add_argument("phrase", help="MLE phrase to translate and expand")
    parser.add_argument(
        "--platforms", "-p", nargs="+",
        choices=list(PLATFORM_TEMPLATES.keys()),
        help="Platforms to generate queries for (default: all)"
    )
    parser.add_argument("--gang", "-g", help="Gang name for context")
    parser.add_argument("--area", "-a", help="Area/postcode for context")
    parser.add_argument("--year", "-y", help="Year for temporal filtering")
    parser.add_argument(
        "--format", "-f", choices=["json", "flat", "grouped"],
        default="grouped", help="Output format"
    )
    parser.add_argument(
        "--lexicon-stats", action="store_true",
        help="Print lexicon statistics and exit"
    )

    args = parser.parse_args()
    lexicon = load_lexicon()

    if args.lexicon_stats:
        categories = {}
        for entry in lexicon.values():
            cat = entry["category"]
            categories[cat] = categories.get(cat, 0) + 1
        print(f"Lexicon loaded: {len(lexicon)} terms across {len(categories)} categories")
        for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
            print(f"  {cat}: {count}")
        return

    queries = generate_queries(
        phrase=args.phrase, platforms=args.platforms,
        gang_context=args.gang, area_context=args.area,
        year_context=args.year, lexicon=lexicon,
    )

    translations = translate_phrase(args.phrase, lexicon)
    print(f"Input: {args.phrase}")
    if translations:
        print(f"Translations found: {len(translations)}")
        for t in translations:
            print(f"  {t['term']} -> {t['meaning']} ({t['category']})")
    print(f"Queries generated: {len(queries)}")
    print(format_output(queries, args.format))


if __name__ == "__main__":
    main()
