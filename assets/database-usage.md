# Database Usage Guide

The `assets/` directory contains two persistent databases that accumulate intelligence across investigations. Both databases use JSON files with embedded schema definitions and are managed through `scripts/database_manager.py`.

---

## Entity Database (`entity-database/`)

Two files form the core relational store:

**`entities.json`** — All persons, organisations, locations, events, and objects identified during investigations. Each record follows the POLE schema with mandatory fields: `id`, `type`, `name`, `source`, `source_grade`, `created_utc`. The `id` prefix encodes entity type: `P` for person, `O` for organisation, `L` for location, `E` for event.

**`relationships.json`** — Directed and undirected links between entities. Each relationship carries: `source` and `target` entity IDs, `type` (e.g. `director_of`, `shareholder_of`, `communicated_with`), temporal bounds, confidence weight, and Admiralty source grading.

### CLI Operations

```bash
# Add an entity
python3 scripts/database_manager.py add --type person --name "Jane Doe" --source "Companies House"

# Search
python3 scripts/database_manager.py search --query "Meridian"

# List all entities (or filter by type)
python3 scripts/database_manager.py list
python3 scripts/database_manager.py list --type organisation

# Integrity check (finds orphan relationships, duplicate IDs, missing fields)
python3 scripts/database_manager.py check

# Statistics
python3 scripts/database_manager.py stats

# Merge duplicate records
python3 scripts/database_manager.py merge

# Export for network_graph.py
python3 scripts/database_manager.py export-graph
```

### Maintenance Rules

1. **Every entity must have a source and source grade.** No record enters the database without Admiralty 6x6 grading. Ungraded records are flagged by `check`.
2. **Run `check` before and after bulk operations.** Merges, imports, and manual edits can create orphan relationships or duplicate IDs.
3. **Backups are automatic.** Every `save()` creates a timestamped backup in `entity-database/backups/`. Do not delete these during an active investigation.
4. **IDs are immutable.** Once assigned, an entity ID must not change. Other records, templates, and the evidence register reference these IDs.

---

## Geo Database (`geo-database/`)

Two files store spatial intelligence:

**`locations.json`** — Point locations associated with entities. Each record links to an entity via `entity_ref`, carries coordinates (latitude, longitude, optional altitude), temporal metadata (when the entity was observed there), and provenance (source, source grade, evidence register reference). Populated by `scripts/geolocation.py` EXIF extraction and reverse geocoding, or manually during desk research.

**`areas.json`** — Areas of interest such as residential zones, workplaces, transit corridors, or jurisdictional boundaries. Each area links to one or more entities, carries a centre point and optional radius or GeoJSON boundary, and documents the legal jurisdiction that applies.

### When to Update

- After running `geolocation.py exif` on any image with GPS data — add the extracted coordinates as a location record
- After identifying an address from corporate filings, property records, or social media — add as a location with the relevant entity reference
- After defining jurisdictional boundaries relevant to the investigation — add as an area record
- After any geospatial analysis reveals patterns (e.g. co-location of entities) — document in area records with significance notes

### Schema Notes

Both files contain an embedded `schema` object documenting every field. The schema is documentation only and is ignored by scripts — it will not appear in query results. When adding records, follow the schema field names exactly to ensure compatibility with `network_graph.py` (which can import location nodes) and `chronological_matrix.py` (which can incorporate temporal location data).

---

## Syncing with Notion

For investigations that use Notion as an external collaboration layer:

1. **Export from database:** `python3 scripts/database_manager.py list > entities_export.json`
2. **Push to Notion:** Use the Notion MCP (`event_create` or page creation) to mirror entity records as database entries. Map POLE types to Notion database views.
3. **Pull from Notion:** After collaborative updates in Notion, export the Notion database and re-import into the entity database using `database_manager.py add` with the `--source "Notion sync"` flag.
4. **Conflict resolution:** The entity database uses last-write-wins. If both local and Notion records have been modified, run `database_manager.py check` after sync to identify conflicts.

### Recommended Notion Structure

| Notion Database | Maps to | Key Properties |
|----------------|---------|---------------|
| Entities | `entities.json` | Name, Type, ID, Source Grade, Status |
| Relationships | `relationships.json` | Source Entity, Target Entity, Type, Evidence |
| Locations | `locations.json` | Label, Coordinates, Entity, Source |
| Evidence Log | `evidence-register.md` template | Reference, Hash, Capture Date, Custody |

---

## Cross-Investigation Persistence

These databases persist across investigations. When an investigation concludes:

1. Run `database_manager.py check` for final integrity validation
2. Run `database_manager.py stats` and record the counts in the Case Summary Record
3. Entities and relationships from the concluded investigation remain in the database and are available for future investigations — this enables cross-case link analysis
4. If data isolation is required (e.g. for legal reasons), create a filtered export before removing case-specific records
