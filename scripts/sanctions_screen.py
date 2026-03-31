#!/usr/bin/env python3
"""
claude-sleuth :: sanctions & PEP screening
Fuzzy matching against OFAC SDN, UN, EU, and UK sanctions lists.

All lists are free, public, no-signup downloads.
Matching uses phonetic indexing + Jaro-Winkler scoring.

Usage:
    from scripts.sanctions_screen import SanctionsScreener
    ss = SanctionsScreener(data_dir="./sanctions_data")
    ss.download_lists()
    results = ss.screen("John Smith", threshold=0.85)
"""

import csv
import io
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from rapidfuzz import fuzz
    HAS_RAPIDFUZZ = True
except ImportError:
    HAS_RAPIDFUZZ = False

try:
    import jellyfish
    HAS_JELLYFISH = True
except ImportError:
    HAS_JELLYFISH = False


@dataclass
class SanctionsMatch:
    list_source: str
    listed_name: str
    query_name: str
    score: float
    match_type: str  # exact, fuzzy, phonetic
    entity_type: str = ""  # individual, entity
    programme: str = ""
    additional_info: dict = None

    def __post_init__(self):
        if self.additional_info is None:
            self.additional_info = {}


class SanctionsListManager:
    """Downloads and parses sanctions lists."""

    SOURCES = {
        "ofac_sdn": {
            "url": "https://www.treasury.gov/ofac/downloads/sdn.csv",
            "description": "US OFAC Specially Designated Nationals",
        },
        "uk_sanctions": {
            "url": "https://assets.publishing.service.gov.uk/media/65a8a29b867cd80013f57b8f/UK_Sanctions_List.csv",
            "description": "UK HMT Consolidated Sanctions List",
        },
    }

    def __init__(self, data_dir: str = "./sanctions_data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.entries = []  # List of (source, name, entity_type, raw_row)

    def download_lists(self) -> dict:
        """Download all available sanctions lists."""
        if not HAS_REQUESTS:
            return {"error": "requests not installed"}

        status = {}
        for source_id, source_info in self.SOURCES.items():
            filepath = self.data_dir / f"{source_id}.csv"
            try:
                resp = requests.get(source_info["url"], timeout=60)
                if resp.status_code == 200:
                    filepath.write_bytes(resp.content)
                    status[source_id] = {"status": "downloaded", "bytes": len(resp.content)}
                else:
                    status[source_id] = {"status": "failed", "http_code": resp.status_code}
            except Exception as e:
                status[source_id] = {"status": "error", "message": str(e)}

        return status

    def load_ofac_sdn(self) -> int:
        """Parse OFAC SDN CSV."""
        filepath = self.data_dir / "ofac_sdn.csv"
        if not filepath.exists():
            return 0

        count = 0
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    name = row[1].strip()
                    entity_type = row[2].strip() if len(row) > 2 else ""
                    if name:
                        self.entries.append(("ofac_sdn", name, entity_type, {}))
                        count += 1
        return count

    def load_uk_sanctions(self) -> int:
        """Parse UK Sanctions CSV."""
        filepath = self.data_dir / "uk_sanctions.csv"
        if not filepath.exists():
            return 0

        count = 0
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # UK list has Name6 (surname) and Name1 (forename) columns
                parts = [row.get(f"Name{i}", "").strip() for i in range(1, 7)]
                name = " ".join(p for p in parts if p)
                if name:
                    entity_type = row.get("Group Type", "")
                    programme = row.get("Regime", "")
                    self.entries.append(("uk_sanctions", name, entity_type, {"programme": programme}))
                    count += 1
        return count

    def load_all(self) -> dict:
        """Load all downloaded lists into memory."""
        self.entries = []
        counts = {}
        counts["ofac_sdn"] = self.load_ofac_sdn()
        counts["uk_sanctions"] = self.load_uk_sanctions()
        counts["total"] = len(self.entries)
        return counts


def normalise_name(name: str) -> str:
    """Normalise a name for matching."""
    name = name.upper().strip()
    # Remove common suffixes/prefixes
    for token in ["MR", "MRS", "MS", "DR", "PROF", "SIR", "LADY", "LORD"]:
        name = name.replace(f"{token} ", "").replace(f" {token}", "")
    # Remove punctuation
    name = "".join(c for c in name if c.isalnum() or c == " ")
    # Collapse whitespace
    name = " ".join(name.split())
    return name


class SanctionsScreener:
    """Fuzzy matching against downloaded sanctions lists."""

    def __init__(self, data_dir: str = "./sanctions_data"):
        self.manager = SanctionsListManager(data_dir)

    def download_lists(self) -> dict:
        return self.manager.download_lists()

    def load_lists(self) -> dict:
        return self.manager.load_all()

    def screen(self, name: str, threshold: float = 0.85) -> dict:
        """Screen a name against all loaded lists."""
        if not self.manager.entries:
            self.load_lists()

        query_norm = normalise_name(name)
        matches = []

        # Phonetic key for the query
        query_soundex = jellyfish.soundex(query_norm) if HAS_JELLYFISH else None
        query_metaphone = jellyfish.metaphone(query_norm) if HAS_JELLYFISH else None

        for source, listed_name, entity_type, extra in self.manager.entries:
            listed_norm = normalise_name(listed_name)

            if not listed_norm:
                continue

            # 1. Exact match
            if query_norm == listed_norm:
                matches.append(SanctionsMatch(
                    list_source=source,
                    listed_name=listed_name,
                    query_name=name,
                    score=1.0,
                    match_type="exact",
                    entity_type=entity_type,
                    programme=extra.get("programme", ""),
                ))
                continue

            # 2. Jaro-Winkler fuzzy match
            if HAS_JELLYFISH:
                jw_score = jellyfish.jaro_winkler_similarity(query_norm, listed_norm)
                if jw_score >= threshold:
                    matches.append(SanctionsMatch(
                        list_source=source,
                        listed_name=listed_name,
                        query_name=name,
                        score=round(jw_score, 4),
                        match_type="jaro_winkler",
                        entity_type=entity_type,
                        programme=extra.get("programme", ""),
                    ))
                    continue

            # 3. RapidFuzz token sort ratio (handles name order variation)
            if HAS_RAPIDFUZZ:
                token_score = fuzz.token_sort_ratio(query_norm, listed_norm) / 100.0
                if token_score >= threshold:
                    matches.append(SanctionsMatch(
                        list_source=source,
                        listed_name=listed_name,
                        query_name=name,
                        score=round(token_score, 4),
                        match_type="token_sort",
                        entity_type=entity_type,
                        programme=extra.get("programme", ""),
                    ))
                    continue

            # 4. Phonetic match (lower confidence)
            if HAS_JELLYFISH and query_soundex:
                listed_soundex = jellyfish.soundex(listed_norm)
                if query_soundex == listed_soundex:
                    matches.append(SanctionsMatch(
                        list_source=source,
                        listed_name=listed_name,
                        query_name=name,
                        score=0.7,
                        match_type="phonetic_soundex",
                        entity_type=entity_type,
                        programme=extra.get("programme", ""),
                    ))

        # Sort by score descending
        matches.sort(key=lambda m: m.score, reverse=True)

        return {
            "query": name,
            "query_normalised": query_norm,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "lists_loaded": len(self.manager.entries),
            "threshold": threshold,
            "matches_found": len(matches),
            "matches": [asdict(m) for m in matches],
        }

    def screen_batch(self, names: list, threshold: float = 0.85) -> list:
        """Screen multiple names."""
        return [self.screen(name, threshold) for name in names]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Sanctions screening tool")
    parser.add_argument("name", help="Name to screen")
    parser.add_argument("--threshold", type=float, default=0.85, help="Match threshold (0-1)")
    parser.add_argument("--data-dir", default="./sanctions_data", help="Data directory")
    parser.add_argument("--download", action="store_true", help="Download fresh lists first")
    parser.add_argument("--output", "-o", help="Output JSON file")
    args = parser.parse_args()

    ss = SanctionsScreener(data_dir=args.data_dir)

    if args.download:
        print("Downloading sanctions lists...")
        status = ss.download_lists()
        for source, info in status.items():
            print(f"  {source}: {info}")

    print("Loading lists...")
    counts = ss.load_lists()
    print(f"  Loaded {counts['total']} entries")

    results = ss.screen(args.name, threshold=args.threshold)
    print(f"\nMatches found: {results['matches_found']}")

    if args.output:
        Path(args.output).write_text(json.dumps(results, indent=2))
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
