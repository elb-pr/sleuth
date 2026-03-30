# Analysis Tooling

Tools, MCPs, and scripts available for data analysis. Run `python3 scripts/setup.py` to install all dependencies.

---

## setup.py Dependencies (Analysis-Relevant)

### GeoPandas
Spatial data analysis. Extends pandas with geometric types. Reads WKT, GeoJSON, Shapefiles. Spatial joins, buffers, overlays, territory queries.

**Key use:** Querying the geo CSVs (gang-information.csv, gang-deaths.csv, gang-music-videos.csv) which contain WKT geometry data.

**Full reference:** `geopandas.md` in this folder.

### Matplotlib
Visualisation. Timeline plots, territory maps, incident heatmaps, bar charts, scatter plots. Publication-quality output.

**Key use:** Any visual output — plotting timelines, mapping incidents, rendering network graphs alongside NetworkX.

**Full reference:** `matplotlib.md` in this folder.

### NetworkX
Network/graph analysis. Build, manipulate, and analyse complex networks. Centrality measures, shortest paths, community detection, graph I/O.

**Key use:** Relationship mapping between entities. Co-defendant networks, gang alliances, social connections. Identifying bridges, clusters, and central figures.

**Full reference:** `networkx.md` in this folder.

### MarkItDown
Microsoft tool for converting files to markdown. Supports 15+ formats including PDF, DOCX, XLSX, images (with OCR).

**Key use:** Converting seized/collected documents into markdown for analysis. Evidence processing.

**Full reference:** Included in `evidence-assessment.md` in this folder.

---

## MCP Servers (Analysis-Relevant)

### Thinking Toolkit MCP
**Server:** `https://server.smithery.ai/elbpr/thinking-toolkit`

**Key tools:**
- `diagnose` — when stuck on analytical direction
- `diagnose_entity` — when a cognitive surrogate profile needs gap analysis
- `get_technique` — load specific thinking technique for analytical reasoning

**Use when:** Analysis reveals contradictions, unexpected patterns, or you need structured reasoning about what the data shows.

### Notion MCP
**Server:** `https://mcp.notion.com/mcp`

**Use when:** Pushing structured analysis outputs (network maps, timeline data, entity profiles) to the investigation workspace.

---

## Relevant Scripts

| Script | Purpose |
|---|---|
| `scripts/plot_template.py` | Template for matplotlib plot generation |
| `scripts/content_visualizer.py` | Content visualisation utilities |
| `scripts/sentiment_analyzer.py` | Sentiment analysis on text evidence |
| `scripts/text_analyzer.py` | Text analysis utilities |
| `scripts/topic_analyzer.py` | Topic modelling on collected text |

---

## Assets (Analysis-Relevant)

| Asset | Contents | Use |
|---|---|---|
| `assets/geo-database/gang-information.csv` | 5,083 territory polygons in WKT | Territory queries, boundary mapping |
| `assets/geo-database/gang-deaths.csv` | 2,432 death/incident points | Incident mapping, proximity searches |
| `assets/geo-database/gang-music-videos.csv` | 343 music video filming locations | Cross-reference filming against territories |
| `assets/entity-database/entities.json` | Entity records | Network graph seed data |
| `assets/entity-database/relationships.json` | Relationship data | Network graph edges |
