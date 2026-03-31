#!/usr/bin/env python3
"""
claude-sleuth :: entity resolver
POLE entity extraction with deterministic ID matching and probabilistic linkage.
Implements Fellegi-Sunter framework for record deduplication.

Usage:
    from scripts.entity_resolver import EntityResolver
    er = EntityResolver()
    er.add_record({"type": "person", "name": "John Smith", "dob": "1985-03-15", "passport": "GB123456"})
    er.add_record({"type": "person", "name": "J. Smith", "dob": "1985-03-15"})
    clusters = er.resolve()
"""

import json
import uuid
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

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
class EntityRecord:
    record_id: str
    entity_type: str  # person, organisation, location, event, object
    fields: dict = field(default_factory=dict)
    source: str = ""
    confidence: float = 1.0
    cluster_id: Optional[str] = None


# Unique identifiers that guarantee deterministic match
DETERMINISTIC_KEYS = [
    "passport_number",
    "national_id",
    "company_number",
    "lei",
    "email",
    "phone",
    "vin",
    "registration_plate",
    "tax_id",
    "social_security",
    "bank_account",
    "domain",
]


def normalise(value: str) -> str:
    """Normalise a string for comparison."""
    return " ".join(value.upper().strip().split())


def name_similarity(name1: str, name2: str) -> float:
    """Calculate name similarity using best available method."""
    n1 = normalise(name1)
    n2 = normalise(name2)

    if n1 == n2:
        return 1.0

    scores = []

    if HAS_JELLYFISH:
        scores.append(jellyfish.jaro_winkler_similarity(n1, n2))

    if HAS_RAPIDFUZZ:
        scores.append(fuzz.token_sort_ratio(n1, n2) / 100.0)
        scores.append(fuzz.partial_ratio(n1, n2) / 100.0)

    if not scores:
        # Basic fallback
        set1 = set(n1.split())
        set2 = set(n2.split())
        if not set1 or not set2:
            return 0.0
        overlap = len(set1 & set2)
        return overlap / max(len(set1), len(set2))

    return max(scores)


def date_similarity(d1: str, d2: str) -> float:
    """Compare dates. Exact match = 1.0, same year = 0.5, else 0.0."""
    if d1 == d2:
        return 1.0
    try:
        if d1[:4] == d2[:4]:  # Same year
            return 0.5
    except (IndexError, TypeError):
        pass
    return 0.0


class EntityResolver:
    """Entity resolution with deterministic and probabilistic matching."""

    def __init__(self, match_threshold: float = 0.80):
        self.records: list[EntityRecord] = []
        self.match_threshold = match_threshold

    def add_record(self, data: dict, source: str = "") -> str:
        """Add a record for resolution. Returns record ID."""
        record_id = data.get("record_id", str(uuid.uuid4())[:8])
        entity_type = data.get("type", data.get("entity_type", "unknown"))

        # Separate type/id from fields
        fields = {k: v for k, v in data.items() if k not in ("record_id", "type", "entity_type")}

        record = EntityRecord(
            record_id=record_id,
            entity_type=entity_type,
            fields=fields,
            source=source,
        )
        self.records.append(record)
        return record_id

    def add_records_batch(self, records: list, source: str = "") -> list:
        """Add multiple records."""
        return [self.add_record(r, source) for r in records]

    def _deterministic_match(self, r1: EntityRecord, r2: EntityRecord) -> bool:
        """Check for deterministic match on unique identifiers."""
        for key in DETERMINISTIC_KEYS:
            v1 = r1.fields.get(key, "").strip()
            v2 = r2.fields.get(key, "").strip()
            if v1 and v2 and normalise(v1) == normalise(v2):
                return True
        return False

    def _probabilistic_score(self, r1: EntityRecord, r2: EntityRecord) -> float:
        """Fellegi-Sunter style probabilistic matching."""
        if r1.entity_type != r2.entity_type:
            return 0.0

        weights = {
            "name": 0.40,
            "dob": 0.20,
            "address": 0.15,
            "nationality": 0.10,
            "occupation": 0.05,
            "other": 0.10,
        }

        total_weight = 0.0
        total_score = 0.0

        # Name comparison
        name1 = r1.fields.get("name", "")
        name2 = r2.fields.get("name", "")
        if name1 and name2:
            total_weight += weights["name"]
            total_score += weights["name"] * name_similarity(name1, name2)

        # Date of birth
        dob1 = r1.fields.get("dob", r1.fields.get("date_of_birth", ""))
        dob2 = r2.fields.get("dob", r2.fields.get("date_of_birth", ""))
        if dob1 and dob2:
            total_weight += weights["dob"]
            total_score += weights["dob"] * date_similarity(dob1, dob2)

        # Address
        addr1 = r1.fields.get("address", "")
        addr2 = r2.fields.get("address", "")
        if addr1 and addr2:
            total_weight += weights["address"]
            total_score += weights["address"] * name_similarity(addr1, addr2)

        # Nationality
        nat1 = r1.fields.get("nationality", "")
        nat2 = r2.fields.get("nationality", "")
        if nat1 and nat2:
            total_weight += weights["nationality"]
            total_score += weights["nationality"] * (1.0 if normalise(nat1) == normalise(nat2) else 0.0)

        if total_weight == 0:
            return 0.0

        return total_score / total_weight

    def resolve(self) -> dict:
        """Run entity resolution across all records."""
        n = len(self.records)
        # Union-Find for clustering
        parent = list(range(n))
        match_log = []

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Pairwise comparison
        for i in range(n):
            for j in range(i + 1, n):
                r1 = self.records[i]
                r2 = self.records[j]

                # Skip different entity types
                if r1.entity_type != r2.entity_type:
                    continue

                # 1. Deterministic match
                if self._deterministic_match(r1, r2):
                    union(i, j)
                    match_log.append({
                        "records": [r1.record_id, r2.record_id],
                        "match_type": "deterministic",
                        "score": 1.0,
                    })
                    continue

                # 2. Probabilistic match
                score = self._probabilistic_score(r1, r2)
                if score >= self.match_threshold:
                    union(i, j)
                    match_log.append({
                        "records": [r1.record_id, r2.record_id],
                        "match_type": "probabilistic",
                        "score": round(score, 4),
                    })

        # Build clusters
        clusters = defaultdict(list)
        for i in range(n):
            cluster_id = find(i)
            clusters[cluster_id].append(i)

        # Format output
        resolved_clusters = []
        for cluster_id, indices in clusters.items():
            cluster_records = []
            for idx in indices:
                r = self.records[idx]
                r.cluster_id = f"cluster_{cluster_id}"
                cluster_records.append(asdict(r))
            resolved_clusters.append({
                "cluster_id": f"cluster_{cluster_id}",
                "size": len(indices),
                "entity_type": self.records[indices[0]].entity_type,
                "records": cluster_records,
            })

        return {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "total_records": n,
            "total_clusters": len(resolved_clusters),
            "duplicates_found": n - len(resolved_clusters),
            "match_threshold": self.match_threshold,
            "match_log": match_log,
            "clusters": resolved_clusters,
        }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Entity resolution pipeline")
    parser.add_argument("input", help="JSON file with records array")
    parser.add_argument("--threshold", type=float, default=0.80, help="Match threshold")
    parser.add_argument("--output", "-o", help="Output JSON file")
    args = parser.parse_args()

    er = EntityResolver(match_threshold=args.threshold)
    records = json.loads(Path(args.input).read_text())

    if isinstance(records, list):
        er.add_records_batch(records)
    elif isinstance(records, dict) and "records" in records:
        er.add_records_batch(records["records"])

    result = er.resolve()
    print(f"Resolved {result['total_records']} records into {result['total_clusters']} clusters")
    print(f"Duplicates found: {result['duplicates_found']}")

    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2))
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
