# Scan Methodology

Signal discovery patterns for UK drill crime investigation. Load this file during SCAN phase before exercising MCP tools.

---

## Story-Worthiness Filter

Every lead MUST pass this filter before promotion to INVESTIGATE. A lead that fails all four criteria is discarded. A lead that passes 1-2 criteria goes on MONITOR. A lead that passes 3-4 criteria is promoted to INVESTIGATE.

### Criterion 1: Narrative Architecture
Does this case have the structural elements of a story?
- **Identifiable characters**: Named individuals with ages, backgrounds, relationships — not just anonymous "youths"
- **A sequence of events**: A chain of cause and effect, not an isolated incident
- **A turning point**: A moment where the story pivots — a decision, an escalation, a failure of intervention
- **Consequences**: Court proceedings, community impact, policy change, ongoing fallout

### Criterion 2: Systemic Illumination
Does this case reveal something beyond itself?
- Postcode war dynamics and territorial logic
- County lines pipeline mechanics
- The drill-to-violence feedback loop (lyrics encoding real events, social media escalation)
- Youth centre / safe space vulnerability
- Policing strategy failures or successes
- Sentencing patterns and judicial response
- School exclusion → gang recruitment pipeline
- Community resilience and intervention attempts

### Criterion 3: Public Record Sufficiency
Is there enough verifiable material to sustain a full episode (7,000-12,000 words)?
- Crown Court proceedings with sentencing remarks available
- CPS press releases or charging documents
- Court reporting from at least 2 independent outlets
- Police statements or press releases
- Local news coverage with community response
- Drill music references that can be identified and contextualised

Minimum threshold: At least ONE institutional source (court, CPS, police) confirming the basic facts. Episodes built entirely on community knowledge and social media are FORBIDDEN.

### Criterion 4: Thematic Argument Availability
Can this case support a thesis — not just "this happened" but "this happened and here is what it means"?
- The case illustrates a pattern (escalation cycle, retaliatory chain, geographic confinement)
- The case contains a symbolic element (bulletproof glass door on a youth centre, stabbing at a children's football session, arrest at an airport)
- The case raises a question the episode can explore without simplifying (why did intervention fail? what does the sentence mean? what happened to the community after?)

---

## Signal Taxonomy by Platform

### Reddit (r/ukdrill)

**High-value signal types:**
- **Court sentencing threads**: Highest value. These surface cases with full public record. Look for threads with high engagement (300+ upvotes) discussing specific court outcomes.
- **Incident aftermath threads**: Posts discussing a recent stabbing, shooting, or arrest. Valuable for timeline construction and community context. Cross-reference against news coverage immediately.
- **RIP/memorial threads**: Community response to a death. Useful for: victim identification, gang affiliation confirmation, emotional context, associated drill tracks.
- **Beef escalation posts**: Discussions about escalating tensions between specific gangs. Lower immediate value but useful for monitoring.
- **"What happened to..." threads**: Retrospective discussions about older cases. Useful for finding cases with sufficient temporal distance for comprehensive coverage.

**Low-value signal types (skip unless corroborated):**
- Speculation threads without named individuals
- Rumour-only posts ("I heard...")
- Score-keeping posts (body counts, comparison threads)
- Troll or bait posts

### Twitter/X

**High-value signal types:**
- **Incident-time posts**: Tweets from the minutes/hours during and after an incident. Valuable for: establishing timeline, capturing initial community response, identifying witnesses.
- **Court attendance posts**: People tweeting from outside or about court proceedings. Valuable for: confirming hearing dates, capturing reactions to verdicts.
- **Artist beef exchanges**: Direct exchanges between drill artists. Valuable for: mapping feuds, identifying escalation points, capturing lyrics that reference real events.
- **Memorial activity**: Posts marking anniversaries, birthdays, or deaths. Valuable for: confirming dates, identifying community connections.
- **Location drops**: Posts or check-ins revealing where individuals were at specific times.

**Archival priority: HIGH.** Tweets are deleted frequently. Screenshot and archive any tweet relevant to the investigation within the same session it is discovered.

### Instagram

**High-value signal types:**
- **Story activity around incident dates**: Artist stories from the day of an incident. Valuable for: establishing presence/absence, mood, location.
- **Location tags**: Geotagged posts confirming someone's presence at a specific location.
- **Memorial posts**: Posts memorialising victims. Valuable for: confirming relationships, gang affiliations, community connections.
- **Affiliation signals**: Group photos, hand signs, colour coordination, estate backgrounds. Useful for: confirming gang membership claims.

**Archival priority: CRITICAL.** Instagram stories disappear after 24 hours. If a story is relevant, capture it immediately.

### YouTube

**High-value signal types:**
- **Drill tracks referencing specific incidents**: Lyrics that encode real events. Cross-reference lyrical references against known incidents. Valuable for: narrative intelligence, gang perspective, cultural context.
- **Music video locations**: Identifiable estates, streets, and landmarks in music videos. Valuable for: confirming territorial claims.
- **Comment sections**: Occasionally contain firsthand accounts or specific details not found elsewhere. Low reliability but high potential value when they surface genuine information.
- **Channel activity patterns**: Sudden activity after a period of silence, or sudden removal of videos, can signal relevant events.

### Google (Web Search)

**Priority search targets:**
1. Crown Court sentencing remarks (judiciary.uk)
2. CPS press releases (cps.gov.uk)
3. Met Police news (met.police.uk/news)
4. BBC court reporting
5. PA Media/Press Association wire copy
6. Evening Standard, Brixton Buzz, South London Press
7. Academic research on the specific gang, postcode, or incident
8. Inquest reports

---

## Dork Query Construction

See references/dork-templates.md for platform-specific query generation patterns.

---

## Lead Triage

After scanning, categorise every lead:

| Category | Criteria | Action |
|---|---|---|
| **PROMOTE** | 3-4 story-worthiness criteria met. At least 1 institutional source identified. | Advance to INVESTIGATE immediately. |
| **HOLD** | 2 criteria met. Institutional sources not yet confirmed but likely exist. | Verify institutional source availability before promoting. |
| **MONITOR** | 1 criterion met. Interesting but insufficient for investigation. | Add to watchlist. Re-evaluate in 2 weeks or upon new developments. |
| **DISCARD** | 0 criteria met. Rumour, speculation, or insufficient substance. | Log reason for discard. Do not pursue. |

All triage decisions MUST be logged in Notion with the rationale for the categorisation.
