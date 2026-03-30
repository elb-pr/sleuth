# Entity Research

How to build structured profiles for individuals, gangs, and locations. Every entity in a case gets a profile. Profiles are populated from evidence only - never from assumption or stereotype.

---

## Individual Profile

### Required Fields

- Full legal name (if available from court documents)
- Road name / street name / alias
- Age at time of incident
- Gang affiliation (with confidence level and source)
- Postcode / estate
- Associated drill artist name (if applicable)
- Prior known incidents (with dates and sources)
- Court history (charges, convictions, sentences)
- Family connections relevant to the case
- School / youth centre / community associations
- Social media handles (if publicly identifiable from court documents or news)

### Username Discovery

Use Sherlock (scripts/sherlock.py) to search a username across platforms. Use Maigret for deeper cross-platform profiling. See tooling.md for invocation patterns.

When a username is found on one platform, immediately check:
- Same username on other platforms (Sherlock)
- Linked accounts (Instagram bios often link YouTube, Twitter)
- Tagged/mentioned by other accounts
- Cross-reference against known associates

### Mapping to the Cognitive Surrogate Profile

When building an individual profile, consider which of the 16 PSSP sections can be populated from available evidence. Not all sections are equally accessible for investigation subjects.

**High accessibility (public evidence usually available):**
- S3 Locus of Control - attribution language in statements, interviews, lyrics
- S5 Defence Mechanisms - observable in interview transcripts, court behaviour
- S8 Existential Orientation - meaning-making visible in public statements, cultural output
- S12 Behavioural Defaults - observable in documented behaviour patterns
- S13 Contingency Sensitivity - causal claims in their own words
- S14 Interpersonal Strategy - cooperation/defection patterns visible in court records, co-defendant behaviour

**Medium accessibility (sometimes available):**
- S1 Personality - inferrable from multiple sources but never directly testable
- S2 Attachment - family structure often documented, but attachment quality requires closer sources
- S4 Emotion Regulation - visible in crisis moments documented in court/news
- S7 Cognitive Triad - inferrable from sustained patterns in communication

**Low accessibility (rarely available for third parties):**
- S6 Cognitive Distortions, S9 Contradiction Map, S10 Predictive Risk Map, S11 Cognitive Processing, S15 Signal Discrimination

Prioritise populating high-accessibility sections first. Use `assess` on the PSSP MCP to identify which gaps are most worth pursuing and get the full framework methodology for advancing each section.

### Investigation-Adapted Extraction

The PSSP extraction guide is conversational ("listen for X, ask Y"). For investigation subjects - people you may never speak to - each extraction method needs an investigative equivalent:

| Conversational Extraction | Investigation Equivalent |
|---|---|
| "Listen for vocabulary complexity" | Analyse written/recorded statements, drill lyrics, social media language |
| "Ask them about X" | Search for contexts where X was revealed - interviews, court testimony, memoir, community accounts |
| "Observe in real-time" | Analyse available behavioural evidence - witness accounts, social media activity patterns |
| "Cross-validate across 2 contexts" | Cross-validate across 2 independent source types (not 2 sources from the same type) |

### Evidence Tiers for Profile Population

| Tier | Label | Minimum Evidence |
|---|---|---|
| 0 | Unscored | Insufficient data |
| 1 | Provisional | Single signal, not replicated. ALWAYS labelled as provisional. |
| 2 | Emerging | 2+ signals from different contexts, internally consistent |
| 3 | Established | Multiple signals, cross-validated against 1+ other dimension, replicated |
| 4 | Robust | Tier 3 + tested under stress or novelty and held |

Reporting Tier 1 as a finding is forbidden. It is a hypothesis.

---

## Gang Profile

### Required Fields

- Gang name and variants (e.g., 150 / GBG / Get Back Gang)
- Territory (estate, postcode, borough)
- Alliances (current and historical)
- Rivalries (current and historical, with precipitating events)
- Associated drill artists
- Known incidents attributed to the gang
- Estimated size and generational structure (olders, youngers)
- Affiliated sub-sets (e.g., AD from Angell Town under 150)

### Sources

Cross-reference gang knowledge base (assets/entity-database/gang-knowledge-base.json) against:
- Court documents naming gang affiliations
- Reddit community knowledge (r/ukdrill gang wiki threads)
- Drill music collaborations and diss tracks
- Geo data: territory polygons (assets/geo-database/gang-information.csv), incident points (gang-deaths.csv), music video locations (gang-music-videos.csv)

### Territory Mapping

Use geopandas (see analysis/geopandas.md) with the geo CSV data to:
- Query "what territory does this location fall in?"
- Find "all incidents within 500m of this location"
- Overlay music video filming locations against territory boundaries
- Map co-defendant home postcodes against gang territories

---

## Location Profile

### Required Fields

- Full address or estate name
- Postcode
- Borough
- Physical description (type of estate, notable features, access points)
- Gang territorial significance
- History of incidents at this location
- Nearest landmarks for orientation
- Transport links (for understanding movement patterns)

### Sources

- Geo database for territorial classification
- Google Maps / Street View for physical description
- Local authority planning records for estate history
- News archives for incident history
- Reddit for community knowledge of estate dynamics

---

## Timeline Construction

Build a chronological reconstruction with evidence citations for each entry:

**Per entry:**
- Date (exact or estimate with confidence: CONFIRMED / ESTIMATED / APPROXIMATE)
- Time (if available)
- Location (specific as possible)
- Event description
- Participants involved
- Source citation(s)
- Epistemic marker
- Relationship to other entries (precursor, consequence, parallel)

**Standard timeline structure:**
1. The precipitating event (prior killing, diss track, territorial incursion)
2. Escalation events (retaliatory actions, social media provocations, drill releases)
3. The central incident
4. Immediate aftermath (arrests, flight, community response)
5. Legal proceedings (charges, trial, verdict, sentencing)
6. Long-term consequences (community impact, policy response, ongoing feuds)

---

## Network Mapping

Map relationships between all entities in the case.

**Relationship types:**
- Gang membership (individual to gang)
- Alliance (gang to gang)
- Rivalry / beef (gang to gang, with precipitating event)
- Family tie (individual to individual, specify: sibling, parent, cousin)
- Geographic proximity (entity to location)
- Musical connection (artist to artist: featuring, dissing, same label)
- Co-defendant (individual to individual, in specific case)
- Victim-perpetrator (individual to individual, in specific incident)

**Per relationship:**
- Type and direction (if applicable)
- Confidence level (CONFIRMED / ASSESSED / REPORTED / UNVERIFIED)
- Source citation
- Temporal scope (current, historical, dissolved)

Use NetworkX (see analysis/networkx.md) for graph construction and analysis. Centrality measures reveal who connects otherwise separate groups.

---

## The FAN Principle

When profiling any subject (individual, group, estate), investigate:

- **Family:** Family connections, where they grew up, who they are related to in the scene
- **Associates:** Who they are seen with, musical collaborations, co-defendants
- **Neighbours:** Who else is on the estate, local geography, what services exist/existed

Adapted from genealogical research methodology. The subject is rarely the most informative source about themselves. Their network reveals what they cannot or will not say.
