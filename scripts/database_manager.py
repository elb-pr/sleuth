#!/usr/bin/env python3
"""
claude-sleuth :: database manager
Manages the entity database (entities.json, relationships.json).
CRUD operations, integrity checks, import/export, and sync.

Usage:
    from scripts.database_manager import DatabaseManager
    db = DatabaseManager("./assets/entity-database")
    db.add_entity({"type": "person", "name": "John Smith", "id": "P001"})
    db.add_relationship({"source": "P001", "target": "O001", "type": "director_of"})
    db.save()
"""

import json
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


class DatabaseManager:
    """Entity database CRUD and integrity management."""

    def __init__(self, db_dir: str = "./assets/entity-database"):
        self.db_dir = Path(db_dir)
        self.db_dir.mkdir(parents=True, exist_ok=True)
        self.entities_path = self.db_dir / "entities.json"
        self.relationships_path = self.db_dir / "relationships.json"
        self.entities = []
        self.relationships = []
        self.load()

    def load(self):
        """Load database from disk."""
        if self.entities_path.exists():
            data = json.loads(self.entities_path.read_text())
            self.entities = data.get("entities", []) if isinstance(data, dict) else data
        if self.relationships_path.exists():
            data = json.loads(self.relationships_path.read_text())
            self.relationships = data.get("relationships", []) if isinstance(data, dict) else data

    def save(self):
        """Save database to disk with backup."""
        # Backup existing files
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup_dir = self.db_dir / "backups"
        backup_dir.mkdir(exist_ok=True)

        for path in [self.entities_path, self.relationships_path]:
            if path.exists():
                backup = backup_dir / f"{path.stem}_{ts}{path.suffix}"
                shutil.copy2(path, backup)

        # Write current state
        self.entities_path.write_text(json.dumps(
            {"entities": self.entities, "last_modified": datetime.now(timezone.utc).isoformat()},
            indent=2,
        ))
        self.relationships_path.write_text(json.dumps(
            {"relationships": self.relationships, "last_modified": datetime.now(timezone.utc).isoformat()},
            indent=2,
        ))

    # --- Entity CRUD ---

    def add_entity(self, entity: dict) -> str:
        """Add an entity. Returns entity ID."""
        if "id" not in entity:
            prefix = entity.get("type", "E")[0].upper()
            entity["id"] = f"{prefix}{len(self.entities) + 1:04d}"
        entity["created_utc"] = datetime.now(timezone.utc).isoformat()
        entity["modified_utc"] = entity["created_utc"]
        self.entities.append(entity)
        return entity["id"]

    def get_entity(self, entity_id: str) -> Optional[dict]:
        """Get entity by ID."""
        for e in self.entities:
            if e.get("id") == entity_id:
                return e
        return None

    def update_entity(self, entity_id: str, updates: dict) -> bool:
        """Update entity fields."""
        for e in self.entities:
            if e.get("id") == entity_id:
                e.update(updates)
                e["modified_utc"] = datetime.now(timezone.utc).isoformat()
                return True
        return False

    def delete_entity(self, entity_id: str) -> bool:
        """Delete entity and its relationships."""
        original_len = len(self.entities)
        self.entities = [e for e in self.entities if e.get("id") != entity_id]
        # Also remove related relationships
        self.relationships = [
            r for r in self.relationships
            if r.get("source") != entity_id and r.get("target") != entity_id
        ]
        return len(self.entities) < original_len

    def search_entities(self, query: str, field: str = "name") -> list:
        """Search entities by field value."""
        query_lower = query.lower()
        return [e for e in self.entities if query_lower in str(e.get(field, "")).lower()]

    def list_entities(self, entity_type: Optional[str] = None) -> list:
        """List all entities, optionally filtered by type."""
        if entity_type:
            return [e for e in self.entities if e.get("type") == entity_type]
        return self.entities

    # --- Relationship CRUD ---

    def add_relationship(self, relationship: dict) -> str:
        """Add a relationship. Returns relationship ID."""
        if "id" not in relationship:
            relationship["id"] = f"R{len(self.relationships) + 1:04d}"
        relationship["created_utc"] = datetime.now(timezone.utc).isoformat()
        self.relationships.append(relationship)
        return relationship["id"]

    def get_relationships(self, entity_id: str) -> list:
        """Get all relationships for an entity."""
        return [
            r for r in self.relationships
            if r.get("source") == entity_id or r.get("target") == entity_id
        ]

    def delete_relationship(self, rel_id: str) -> bool:
        """Delete a relationship by ID."""
        original_len = len(self.relationships)
        self.relationships = [r for r in self.relationships if r.get("id") != rel_id]
        return len(self.relationships) < original_len

    # --- Integrity ---

    def integrity_check(self) -> dict:
        """Check database integrity."""
        issues = []
        entity_ids = {e.get("id") for e in self.entities}

        # Check for duplicate IDs
        seen_ids = set()
        for e in self.entities:
            eid = e.get("id")
            if eid in seen_ids:
                issues.append({"type": "duplicate_entity_id", "id": eid})
            seen_ids.add(eid)

        # Check relationship references
        for r in self.relationships:
            if r.get("source") not in entity_ids:
                issues.append({"type": "orphan_relationship_source", "relationship": r.get("id"), "missing": r.get("source")})
            if r.get("target") not in entity_ids:
                issues.append({"type": "orphan_relationship_target", "relationship": r.get("id"), "missing": r.get("target")})

        # Check required fields
        for e in self.entities:
            if not e.get("id"):
                issues.append({"type": "missing_id", "entity": e})
            if not e.get("type"):
                issues.append({"type": "missing_type", "id": e.get("id")})

        return {
            "total_entities": len(self.entities),
            "total_relationships": len(self.relationships),
            "issues_found": len(issues),
            "healthy": len(issues) == 0,
            "issues": issues,
        }

    def statistics(self) -> dict:
        """Database statistics."""
        type_counts = defaultdict(int)
        for e in self.entities:
            type_counts[e.get("type", "unknown")] += 1

        rel_type_counts = defaultdict(int)
        for r in self.relationships:
            rel_type_counts[r.get("type", "unknown")] += 1

        return {
            "total_entities": len(self.entities),
            "total_relationships": len(self.relationships),
            "entity_types": dict(type_counts),
            "relationship_types": dict(rel_type_counts),
        }

    # --- Import/Export ---

    def export_for_graph(self) -> dict:
        """Export in format compatible with network_graph.py."""
        return {
            "nodes": [
                {
                    "id": e.get("id"),
                    "label": e.get("name", e.get("id")),
                    "node_type": e.get("type", "object"),
                }
                for e in self.entities
            ],
            "edges": [
                {
                    "source": r.get("source"),
                    "target": r.get("target"),
                    "edge_type": r.get("type", "linked_to"),
                    "weight": r.get("weight", 1.0),
                }
                for r in self.relationships
            ],
        }

    def import_from_graph(self, graph_data: dict):
        """Import from network_graph.py JSON export."""
        for node in graph_data.get("nodes", []):
            if not self.get_entity(node.get("id")):
                self.add_entity({
                    "id": node.get("id"),
                    "type": node.get("node_type", "object"),
                    "name": node.get("label", ""),
                })
        for edge in graph_data.get("edges", []):
            self.add_relationship({
                "source": edge.get("source"),
                "target": edge.get("target"),
                "type": edge.get("edge_type", "linked_to"),
                "weight": edge.get("weight", 1.0),
            })

    def merge(self, other_db_dir: str):
        """Merge another database into this one."""
        other = DatabaseManager(other_db_dir)
        existing_ids = {e.get("id") for e in self.entities}

        for e in other.entities:
            if e.get("id") not in existing_ids:
                self.entities.append(e)
                existing_ids.add(e.get("id"))

        existing_rels = {
            (r.get("source"), r.get("target"), r.get("type"))
            for r in self.relationships
        }
        for r in other.relationships:
            key = (r.get("source"), r.get("target"), r.get("type"))
            if key not in existing_rels:
                self.relationships.append(r)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Entity database manager")
    parser.add_argument("--db", default="./assets/entity-database", help="Database directory")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("stats", help="Show database statistics")
    sub.add_parser("check", help="Run integrity check")
    sub.add_parser("list", help="List all entities")

    add_p = sub.add_parser("add", help="Add entity from JSON string")
    add_p.add_argument("json_str", help="JSON entity data")

    search_p = sub.add_parser("search", help="Search entities")
    search_p.add_argument("query", help="Search query")

    export_p = sub.add_parser("export-graph", help="Export for network graph")
    export_p.add_argument("--output", "-o", required=True, help="Output JSON file")

    merge_p = sub.add_parser("merge", help="Merge another database")
    merge_p.add_argument("other_dir", help="Other database directory")

    args = parser.parse_args()
    db = DatabaseManager(args.db)

    if args.command == "stats":
        print(json.dumps(db.statistics(), indent=2))
    elif args.command == "check":
        result = db.integrity_check()
        print(json.dumps(result, indent=2))
        if not result["healthy"]:
            print(f"\nWARNING: {result['issues_found']} integrity issues found.")
    elif args.command == "list":
        for e in db.list_entities():
            print(f"{e.get('id')}: [{e.get('type')}] {e.get('name', 'unnamed')}")
    elif args.command == "add":
        entity = json.loads(args.json_str)
        eid = db.add_entity(entity)
        db.save()
        print(f"Added entity: {eid}")
    elif args.command == "search":
        results = db.search_entities(args.query)
        for e in results:
            print(f"{e.get('id')}: [{e.get('type')}] {e.get('name', 'unnamed')}")
    elif args.command == "export-graph":
        data = db.export_for_graph()
        Path(args.output).write_text(json.dumps(data, indent=2))
        print(f"Exported {len(data['nodes'])} nodes, {len(data['edges'])} edges to {args.output}")
    elif args.command == "merge":
        db.merge(args.other_dir)
        db.save()
        print(f"Merged. New totals: {db.statistics()}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
