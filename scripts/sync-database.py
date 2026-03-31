#!/usr/bin/env python3
"""
Database Sync

Syncs entity-database and geo-database assets between local files and
Notion via MCP. Also validates database integrity and reports gaps.

The entity database (entities.json, relationships.json) and geo database
(gang-deaths.csv, gang-music-videos.csv) are the investigation's living
records. This script handles:

  1. Validation: schema checks, orphan detection, duplicate detection
  2. Statistics: entity counts, relationship density, geo coverage
  3. Export: flatten to CSV for analysis scripts
  4. Import: merge new entities/relationships from investigation output

Usage:
    python sync-database.py validate
    python sync-database.py stats
    python sync-database.py export --format csv --output ./exports/
    python sync-database.py import --file new-entities.json --merge
"""

import argparse
import csv
import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

SKILL_DIR = Path(__file__).resolve().parent.parent
ENTITY_DB = SKILL_DIR / "assets" / "entity-database"
GEO_DB = SKILL_DIR / "assets" / "geo-database"

ENTITIES_PATH = ENTITY_DB / "entities.json"
RELATIONSHIPS_PATH = ENTITY_DB / "relationships.json"
KNOWLEDGE_BASE_PATH = ENTITY_DB / "gang-knowledge-base.json"
DEATHS_PATH = GEO_DB / "gang-deaths.csv"
MUSIC_VIDEOS_PATH = GEO_DB / "gang-music-videos.csv"


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]
    stats: dict

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0

    def __str__(self) -> str:
        lines = []
        if self.errors:
            lines.append(f"ERRORS ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"  x {e}")
        if self.warnings:
            lines.append(f"WARNINGS ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"  ! {w}")
        lines.append(f"STATS:")
        for k, v in self.stats.items():
            lines.append(f"  {k}: {v}")
        return "\n".join(lines)


def load_json(path: Path) -> any:
    """Load a JSON file, returning empty structure if file is empty or missing."""
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return None
        return json.loads(content)


def count_csv_rows(path: Path) -> int:
    """Count data rows in a CSV (excluding header)."""
    if not path.exists():
        return 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return 0
        return sum(1 for _ in reader)


def validate_entities(data: any) -> tuple[list[str], list[str], dict]:
    """Validate entities.json structure and content."""
    errors, warnings = [], []
    stats = {"total": 0, "by_type": {}}

    if data is None:
        stats["total"] = 0
        return errors, warnings, stats

    # Accept both {"entities": [...]} and bare [...]
    entities = data if isinstance(data, list) else data.get("entities", [])
    stats["total"] = len(entities)

    seen_ids = set()
    for i, entity in enumerate(entities):
        if not isinstance(entity, dict):
            errors.append(f"Entity {i}: not a dict")
            continue

        eid = entity.get("id")
        if not eid:
            errors.append(f"Entity {i}: missing 'id' field")
        elif eid in seen_ids:
            errors.append(f"Entity {i}: duplicate id '{eid}'")
        else:
            seen_ids.add(eid)

        etype = entity.get("type", "unknown")
        stats["by_type"][etype] = stats["by_type"].get(etype, 0) + 1

        if not entity.get("name"):
            warnings.append(f"Entity '{eid}': missing 'name'")

    return errors, warnings, stats


def validate_relationships(data: any, entity_ids: set) -> tuple[list[str], list[str], dict]:
    """Validate relationships.json structure and referential integrity."""
    errors, warnings = [], []
    stats = {"total": 0, "by_type": {}, "orphaned": 0}

    if data is None:
        return errors, warnings, stats

    relationships = data if isinstance(data, list) else data.get("relationships", [])
    stats["total"] = len(relationships)

    for i, rel in enumerate(relationships):
        if not isinstance(rel, dict):
            errors.append(f"Relationship {i}: not a dict")
            continue

        rtype = rel.get("type", "unknown")
        stats["by_type"][rtype] = stats["by_type"].get(rtype, 0) + 1

        source = rel.get("source")
        target = rel.get("target")

        if not source or not target:
            errors.append(f"Relationship {i}: missing source or target")
            continue

        if entity_ids and source not in entity_ids:
            warnings.append(f"Relationship {i}: source '{source}' not in entities")
            stats["orphaned"] += 1
        if entity_ids and target not in entity_ids:
            warnings.append(f"Relationship {i}: target '{target}' not in entities")
            stats["orphaned"] += 1

    return errors, warnings, stats


def validate_geo(path: Path, name: str) -> tuple[list[str], list[str], dict]:
    """Validate a geo CSV file."""
    errors, warnings = [], []
    stats = {"rows": 0, "with_wkt": 0, "missing_wkt": 0}

    if not path.exists():
        errors.append(f"{name}: file not found at {path}")
        return errors, warnings, stats

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "WKT" not in (reader.fieldnames or []):
            errors.append(f"{name}: missing 'WKT' column")
            return errors, warnings, stats

        for i, row in enumerate(reader):
            stats["rows"] += 1
            wkt = row.get("WKT", "").strip()
            if wkt and wkt.startswith("POINT"):
                stats["with_wkt"] += 1
            else:
                stats["missing_wkt"] += 1
                if stats["missing_wkt"] <= 5:
                    warnings.append(f"{name} row {i+1}: invalid or missing WKT")

    return errors, warnings, stats


def validate_all() -> ValidationResult:
    """Run all validations and return combined result."""
    all_errors, all_warnings = [], []
    all_stats = {}

    # Entities
    entities_data = load_json(ENTITIES_PATH)
    e, w, s = validate_entities(entities_data)
    all_errors.extend(e)
    all_warnings.extend(w)
    all_stats["entities"] = s

    # Get entity IDs for relationship validation
    entity_ids = set()
    if entities_data:
        ents = entities_data if isinstance(entities_data, list) else entities_data.get("entities", [])
        entity_ids = {e.get("id") for e in ents if isinstance(e, dict) and e.get("id")}

    # Relationships
    rels_data = load_json(RELATIONSHIPS_PATH)
    e, w, s = validate_relationships(rels_data, entity_ids)
    all_errors.extend(e)
    all_warnings.extend(w)
    all_stats["relationships"] = s

    # Knowledge base
    kb_data = load_json(KNOWLEDGE_BASE_PATH)
    if kb_data is None:
        all_warnings.append("gang-knowledge-base.json: empty or missing")
        all_stats["knowledge_base"] = {"gangs": 0}
    else:
        gangs = kb_data if isinstance(kb_data, list) else kb_data.get("gangs", [])
        all_stats["knowledge_base"] = {"gangs": len(gangs)}

    # Geo databases
    e, w, s = validate_geo(DEATHS_PATH, "gang-deaths.csv")
    all_errors.extend(e)
    all_warnings.extend(w)
    all_stats["deaths"] = s

    e, w, s = validate_geo(MUSIC_VIDEOS_PATH, "gang-music-videos.csv")
    all_errors.extend(e)
    all_warnings.extend(w)
    all_stats["music_videos"] = s

    return ValidationResult(errors=all_errors, warnings=all_warnings, stats=all_stats)


def export_entities_csv(output_dir: Path) -> int:
    """Export entities.json to flat CSV."""
    output_dir.mkdir(parents=True, exist_ok=True)
    data = load_json(ENTITIES_PATH)
    if not data:
        print("No entities to export.")
        return 0

    entities = data if isinstance(data, list) else data.get("entities", [])
    if not entities:
        print("No entities to export.")
        return 0

    output_path = output_dir / "entities.csv"
    # Collect all unique keys across entities
    all_keys = set()
    for e in entities:
        all_keys.update(e.keys())
    all_keys = sorted(all_keys)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_keys, extrasaction="ignore")
        writer.writeheader()
        for e in entities:
            # Flatten nested values to JSON strings
            row = {}
            for k, v in e.items():
                row[k] = json.dumps(v) if isinstance(v, (dict, list)) else v
            writer.writerow(row)

    print(f"Exported {len(entities)} entities to {output_path}")
    return len(entities)


def import_entities(input_path: Path, merge: bool = False) -> int:
    """Import entities from a JSON file, optionally merging with existing."""
    new_data = load_json(input_path)
    if not new_data:
        print(f"No data in {input_path}")
        return 0

    new_entities = new_data if isinstance(new_data, list) else new_data.get("entities", [])

    if merge:
        existing = load_json(ENTITIES_PATH)
        existing_entities = []
        if existing:
            existing_entities = existing if isinstance(existing, list) else existing.get("entities", [])

        existing_ids = {e.get("id") for e in existing_entities if isinstance(e, dict)}
        added = 0
        for ne in new_entities:
            if ne.get("id") not in existing_ids:
                existing_entities.append(ne)
                added += 1

        with open(ENTITIES_PATH, "w", encoding="utf-8") as f:
            json.dump({"entities": existing_entities}, f, indent=2)
        print(f"Merged {added} new entities ({len(new_entities) - added} duplicates skipped)")
        return added
    else:
        with open(ENTITIES_PATH, "w", encoding="utf-8") as f:
            json.dump({"entities": new_entities}, f, indent=2)
        print(f"Imported {len(new_entities)} entities (replaced existing)")
        return len(new_entities)


def print_stats():
    """Print database statistics."""
    result = validate_all()
    s = result.stats

    print("=== Detective Inspector Claude Database Stats ===\n")

    print(f"Entity database:       {s.get('entities', {}).get('total', 0)} entities")
    by_type = s.get("entities", {}).get("by_type", {})
    for t, c in sorted(by_type.items()):
        print(f"  {t}: {c}")

    print(f"Relationships:         {s.get('relationships', {}).get('total', 0)}")
    rel_types = s.get("relationships", {}).get("by_type", {})
    for t, c in sorted(rel_types.items()):
        print(f"  {t}: {c}")

    print(f"Knowledge base:        {s.get('knowledge_base', {}).get('gangs', 0)} gangs")
    print(f"Deaths/incidents:      {s.get('deaths', {}).get('rows', 0)} records ({s.get('deaths', {}).get('with_wkt', 0)} geocoded)")
    print(f"Music video locations: {s.get('music_videos', {}).get('rows', 0)} records ({s.get('music_videos', {}).get('with_wkt', 0)} geocoded)")

    if result.errors:
        print(f"\n{len(result.errors)} validation errors found. Run 'validate' for details.")


def main():
    parser = argparse.ArgumentParser(description="Detective Inspector Claude database management")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Validate all database files")
    sub.add_parser("stats", help="Print database statistics")

    export_p = sub.add_parser("export", help="Export databases to flat files")
    export_p.add_argument("--output", "-o", default="./exports", help="Output directory")

    import_p = sub.add_parser("import", help="Import entities from JSON")
    import_p.add_argument("--file", "-f", required=True, help="JSON file to import")
    import_p.add_argument("--merge", action="store_true", help="Merge with existing (default: replace)")

    args = parser.parse_args()

    if args.command == "validate":
        result = validate_all()
        print(result)
        sys.exit(0 if result.ok else 1)

    elif args.command == "stats":
        print_stats()

    elif args.command == "export":
        export_entities_csv(Path(args.output))

    elif args.command == "import":
        import_entities(Path(args.file), merge=args.merge)


if __name__ == "__main__":
    main()
