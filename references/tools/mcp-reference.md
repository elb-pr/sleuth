# MCP Server Quick Reference

All MCP servers available to Detective Inspector Claude during investigation. Organised by investigation phase.

---

## Research Phase

### Reddit
**URL:** `https://server.smithery.ai/reddit`
**Phase:** Collection, verification
**Tools:** `search_across_subreddits`, `retrieve_reddit_post`, `retrieve_post_comments`
**Targets:** r/ukdrill, r/drillshitpost, r/policeuk, r/london, r/unitedkingdom
**Yields:** Community knowledge on gang associations, incident context, sentencing discussions, artist backgrounds, territory disputes. Reddit threads often surface connections before news or courts do.

### Twitter / X
**URL:** `https://server.smithery.ai/twitter`
**Phase:** Collection, real-time monitoring
**Yields:** Incident signals within minutes. Court attendance reactions, artist beef exchanges, memorial activity, location check-ins. High volume, low reliability without corroboration.

### Instagram
**URL:** `https://server.smithery.ai/instagram`
**Phase:** Collection, entity profiling
**Yields:** Profile data, post content, tagged locations, story captures. Complements Instaloader for metadata extraction. Location tags are high-value for territory confirmation.

### YouTube
**URL:** `https://server.smithery.ai/youtube`
**Phase:** Collection, media analysis
**Yields:** Drill tracks, video metadata, upload dates, filming locations (cross-reference against geo data), channel associations, comment sentiment. Music videos are primary evidence for gang associations and territory claims.

### Parallel Search
**URL:** `https://server.smithery.ai/parallel/search`
**Phase:** Collection, broad scanning
**Yields:** Web search results across multiple engines. Court documents, news articles, academic research, government publications, FOI responses.

---

## Analysis & Thinking Phase

### Thinking Toolkit
**URL:** `https://server.smithery.ai/elbpr/thinking-toolkit`
**Phase:** Reasoning, analysis, decision-making
**Tools:** `diagnose`, `get_technique`, `list_techniques`, `get_thinking_toolkit`
**12 techniques including:** cause-effect-confusion, contradiction-holding, temporal-blindness, inversion-exercise, perspective-mapping, meta-pattern-recognition, feedback-loop-mapping, simplification-cascades
**Use:** When stuck on investigative reasoning. Causal claims from unreliable sources, contradictory evidence, timeline assumptions, unanimous accounts (suspicious), irrational-seeming behaviour, recurring patterns.

### Pigeon Superstition Superposition (PSSP)
**URL:** `https://server.smithery.ai/elbpr/pigeon-superstition-superposition`
**Phase:** Entity profiling, psychological assessment
**Tools:** `assess`, `get_framework`, `list_frameworks`, `get_profiling_toolkit`
**16 frameworks:** big-five, attachment-architecture, locus-of-control, emotion-regulation, defence-mechanisms, cognitive-distortions, cognitive-triad, existential-orientation, contradiction-map, predictive-risk-map, cognitive-processing, behavioural-defaults, pigeon-superstition-superposition, interpersonal-strategy, signal-discrimination, approach-avoidance
**Use:** Building cognitive surrogate profiles of investigation subjects from documentary evidence. The `assess` tool reads profile state and routes to the next framework to advance. Primary tool for understanding why subjects behave the way they do.

---

## Workspace & Output

### Notion
**URL:** `https://mcp.notion.com/mcp`
**Phase:** All phases (output, organisation)
**Use:** Push structured investigation data to the workspace. Entity profiles, evidence logs, timeline entries, relationship maps, case briefs, handoff documents. Templates in `templates/notion/` define the expected Notion page structures.

---

## Source Reliability Notes

| Server | Default Admiralty Grade | Notes |
|---|---|---|
| Reddit | F3 (untested/possibly true) | Community knowledge, often accurate but unverified. Multiple corroborating threads increase to C2. |
| Twitter / X | F4 (untested/doubtful) | Real-time but high noise. Useful for temporal signals, unreliable for facts. |
| Instagram | E3 (unreliable/possibly true) | Self-published by subjects. Location tags valuable. Content may be performative. |
| YouTube | D2 (not usually reliable/probably true) | Music videos are primary sources for association claims. Metadata is factual. Lyrical content requires MLE translation. |
| Parallel Search | Varies by result | Grade each source individually. Government/court sources: A1-B2. News: C2-D3. Forums: F6. |
| Notion | N/A | Output tool, not a source. |
| Thinking Toolkit | N/A | Reasoning tool, not a source. |
| PSSP | N/A | Assessment tool, not a source. Profiles are analytical products, not evidence. |
