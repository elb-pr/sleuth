# Research Tooling

Tools, MCPs, and scripts available during research. Run `python3 scripts/setup.py` to install all dependencies.

---

## setup.py Dependencies (Research-Relevant)

### Sherlock (sherlock-project)

Username enumeration across 400+ platforms. Given a username, checks whether accounts exist on each platform.

**Invocation:**
```bash
python3 scripts/sherlock.py [username]
```

**Use when:** You have a username from one platform and want to find accounts on others. Essential first step in entity profiling.

**Output:** List of discovered profile URLs with platform names.

**Notes:** Some sites in the Sherlock database have been removed or produce false positives. See `_archive/sherlock-removed-sites.md` for the removed sites list if you get unreliable results on specific platforms.

### Maigret

Advanced cross-platform profiling. More thorough than Sherlock for certain platforms, with additional metadata extraction.

**Invocation:**
```bash
maigret [username]
```

**Use when:** Sherlock results are insufficient or you need deeper profiling on specific platforms. Maigret excels at extracting profile metadata beyond just confirming account existence.

### Instaloader

Instagram data collection tool. Downloads profile metadata, posts, stories, and comments.

**Invocation:**
```bash
instaloader --no-videos --no-video-thumbnails [profile_name]
```

**Use when:** Collecting Instagram evidence for archival. Particularly important for stories (24hr expiry) and profiles that may be taken down.

**Notes:** Rate-limited by Instagram. Use sparingly and respect platform constraints. Best used for targeted collection after a profile has been identified as relevant, not for broad scanning.

---

## MCP Servers

### Reddit MCP
**Server:** `https://server.smithery.ai/reddit`

**Key tools:**
- `search_across_subreddits` - search for topics across multiple subreddits
- `retrieve_reddit_post` - get a specific post with full content
- `retrieve_post_comments` - get comment threads

**Use when:** Searching r/ukdrill and r/drillshitpost for community knowledge, gang associations, incident discussions, sentencing threads.

### Twitter MCP
**Server:** `https://server.smithery.ai/twitter`

**Use when:** Real-time incident signals, court attendance reactions, artist beef exchanges, memorial activity. Twitter surfaces incidents within minutes.

### Instagram MCP
**Server:** `https://server.smithery.ai/instagram`

**Use when:** Checking profile data, post content, tagged locations. Complements Instaloader for metadata extraction.

### YouTube MCP
**Server:** `https://server.smithery.ai/youtube`

**Use when:** Searching drill tracks, checking video metadata, finding uploads referencing specific incidents or locations. Cross-reference filming locations against geo data.

### Parallel Search MCP
**Server:** `https://server.smithery.ai/parallel/search`

**Use when:** Running broad web searches. Useful for initial scanning and finding court documents, news articles, academic research.

### Thinking Toolkit MCP
**Server:** `https://server.smithery.ai/elbpr/thinking-toolkit`

**Key tools:**
- `diagnose` - describe what you are stuck on, get routed to a thinking technique
- `get_technique` - load a specific thinking technique by ID
- `list_techniques` - see all 12 available techniques

**Use when:** Stuck on a research direction or reasoning problem. Need structured thinking about what evidence means.

### Pigeon Superstition Superposition MCP (PSSP)
**Server:** `https://server.smithery.ai/elbpr/pigeon-superstition-superposition`

**Key tools:**
- `assess` - submit profile state and available evidence, get routed to the right profiling framework with full methodology
- `get_framework` - load a specific profiling framework by ID (16 frameworks for 16 profile sections)
- `list_frameworks` - see all 16 available frameworks
- `get_profiling_toolkit` - load the master profiling system router

**Use when:** Building a cognitive surrogate profile of an investigation subject. The `assess` tool reads your profile state and tells you which section to advance next and how to do it from documentary evidence.

### Notion MCP
**Server:** `https://mcp.notion.com/mcp`

**Use when:** Pushing structured data to the investigation workspace. Entity profiles, evidence metadata, timeline entries, relationship maps, case briefs.

---

## Relevant Scripts

| Script | Purpose |
|---|---|
| `scripts/sherlock.py` | Username enumeration across platforms |
| `scripts/discover_artists.py` | Discover drill artists associated with a gang or postcode |
| `scripts/site-list.py` | Generate site lists for targeted searching |
| `scripts/sites.py` | Site definitions for platform-specific extraction |
| `scripts/setup.py` | Install all pip dependencies |

---

## Assets (Research-Relevant)

| Asset | Contents | Use |
|---|---|---|
| `assets/entity-database/gang-knowledge-base.json` | Structured gang data: names, territories, alliances, rivalries | Cross-reference during entity research |
| `assets/entity-database/entities.json` | Entity records from prior investigations | Check for existing profiles |
| `assets/entity-database/relationships.json` | Known relationship data | Seed network mapping |
| `assets/entity-database/gang-descriptions.md` | London gang narrative descriptions | Context for gang profiling |
| `assets/entity-database/mle-lexicon.md` | MLE (Multicultural London English) vocabulary | Parse drill lyrics and community language |
| `assets/geo-database/gang-information.csv` | 5,083 territory polygons in WKT format | Territory queries via geopandas |
| `assets/geo-database/gang-deaths.csv` | 2,432 death/incident points | Incident mapping |
| `assets/geo-database/gang-music-videos.csv` | 343 music video filming locations | Cross-reference filming against territories |
