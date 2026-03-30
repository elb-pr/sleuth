# OSINT Methodology

Open-source intelligence collection adapted for UK drill crime investigation. Load during INVESTIGATE phase.

---

## Entity Profiling

For every individual, gang, and significant location in the case, build a structured profile.

### Individual Profile Requirements
- Full legal name (if available from court documents)
- Road name / street name / alias
- Age at time of incident
- Gang affiliation (with confidence level)
- Postcode / estate
- Associated drill artist name (if applicable)
- Prior known incidents (with dates and sources)
- Court history (charges, convictions, sentences)
- Family connections relevant to the case
- School / youth centre / community associations
- Social media handles (if publicly identifiable from court documents or news)

### Gang Profile Requirements
- Gang name and variants (e.g., 150 / GBG / Get Back Gang)
- Territory (estate, postcode, borough)
- Alliances (current and historical)
- Rivalries (current and historical, with precipitating events)
- Associated drill artists
- Known incidents attributed to the gang
- Estimated size and generational structure (olders, youngers)
- Affiliated sub-sets (e.g., AD from Angell Town under 150)

### Location Profile Requirements
- Full address or estate name
- Postcode
- Borough
- Physical description (type of estate, notable features, access points)
- Gang territorial significance
- History of incidents at this location
- Nearest landmarks for orientation
- Transport links (for understanding movement patterns)

---

## Timeline Construction

Build a chronological reconstruction of events with evidence citations.

**For each entry:**
- Date (exact or best estimate with confidence: CONFIRMED date / ESTIMATED date / APPROXIMATE period)
- Time (if available)
- Location (specific as possible)
- Event description
- Participants involved
- Source citation(s)
- GRADE certainty rating
- Relationship to other timeline entries (precursor, consequence, parallel)

**Timeline structure:**
1. The precipitating event (what started the chain — often a prior killing, a diss track, a territorial incursion)
2. Escalation events (retaliatory actions, social media provocations, drill track releases)
3. The central incident (the case's primary event)
4. Immediate aftermath (arrests, flight, community response)
5. Legal proceedings (charges, trial, verdict, sentencing)
6. Long-term consequences (community impact, policy response, ongoing feuds)

---

## Network Mapping

Map relationships between all entities in the case.

**Relationship types:**
- Gang membership (individual → gang)
- Alliance (gang ↔ gang)
- Rivalry / beef (gang ↔ gang, with precipitating event)
- Family tie (individual ↔ individual, specify: sibling, parent, cousin)
- Geographic proximity (entity → location)
- Musical connection (artist → artist: featuring, dissing, same label)
- Co-defendant (individual ↔ individual, in specific case)
- Victim-perpetrator (individual → individual, in specific incident)

**For each relationship:**
- Type
- Direction (if applicable)
- Confidence level (CONFIRMED / ASSESSED / REPORTED / UNVERIFIED)
- Source citation
- Temporal scope (current, historical, dissolved)

---

## Evidence Collection Standards

### Chain of Custody
For every piece of evidence:
1. Record source URL at time of collection
2. Record collection date and time
3. Record extraction method (web search, MCP tool, manual)
4. Generate content hash for integrity verification where possible
5. Note any paywalled or access-restricted content

### Archival Priority
- **CRITICAL**: Instagram stories (24hr expiry), tweets from accounts that delete frequently, YouTube videos that may be taken down
- **HIGH**: Reddit threads during active discussion, news articles during first 48 hours
- **MODERATE**: Court documents on judiciary.uk (generally persistent), CPS press releases
- **LOW**: Gang knowledge databases (generally persistent, updated periodically)

### Storage
- **Notion**: Structured data (entity profiles, evidence metadata, timeline entries, relationship maps)
- **Google Docs**: Long-form content (full articles, court transcripts, social media thread archives, case narrative documents)
