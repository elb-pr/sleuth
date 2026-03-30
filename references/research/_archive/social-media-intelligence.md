# Social Media Intelligence

SOCMINT patterns for monitoring UK drill scene activity. Load during SCAN and INVESTIGATE phases.

---

## Platform-Specific Intelligence Value

### Twitter/X — Real-Time Signal
Primary value: Speed. Twitter surfaces incidents within minutes. Drill artists and associates post reactions, threats, and provocations in real time.

**Monitoring patterns:**
- Sudden spikes in mentions of a gang name or postcode
- Artist accounts going silent after a period of activity (may indicate arrest or hiding)
- Memorial hashtags appearing unexpectedly
- Court date mentions and verdict reactions
- Deleted tweets (if cached by third-party services)

### Instagram — Visual SOCMINT
Primary value: Visual confirmation. Location tags, group photos, affiliation signals.

**Monitoring patterns:**
- Story activity around known incident dates
- Location tags placing individuals at specific estates
- Group photos confirming gang affiliations
- Changes in profile (bio updates, removed posts)
- Memorial posts with relationship context
- Story replies and DM references visible in screenshots shared publicly

### Reddit (r/ukdrill) — Community Intelligence
Primary value: Aggregated knowledge. r/ukdrill functions as an informal intelligence database where community members collate, debate, and refine information about UK drill gangs.

**Monitoring patterns:**
- High-engagement sentencing threads (300+ upvotes typically indicate significant cases)
- Corrective comments (community members correcting misinformation — these often contain accurate detail)
- "Wiki-style" information posts that map gang territories and alliances
- Comparison with gang knowledge databases for consistency
- Moderator-verified information threads

### YouTube — Narrative Intelligence
Primary value: Cultural context. Drill lyrics encode real events, feuds, and emotional responses.

**Monitoring patterns:**
- New track releases referencing specific incidents (within days or weeks of an event)
- Track removal (often indicates legal proceedings or police pressure)
- Comment sections with specific claims about events referenced in lyrics
- Feature collaborations indicating alliance shifts
- View counts and engagement as proxy for community significance

---

## Content Archival Protocol

Ephemeral content MUST be archived within the session it is discovered. Priority order:

1. Instagram stories (24hr window)
2. Tweets from accounts known to delete (capture immediately)
3. YouTube videos with low view counts or controversial content (takedown risk)
4. Reddit posts during active moderation periods (removal risk)
5. News articles behind soft paywalls (access may expire)

**Archive format:** Full text extraction pushed to Google Docs. URL, timestamp, and source metadata logged in Notion evidence log.

---

## Coordinated Activity Detection

Watch for patterns suggesting coordinated social media campaigns:
- Multiple accounts posting similar content within a short timeframe
- Accounts with similar creation dates or naming patterns
- Cross-platform posting of identical or near-identical content
- Sudden appearance of accounts promoting a specific narrative
- Brigading of court sentencing discussions with one-sided commentary

Coordinated activity is a narrative bias flag — it does not invalidate the underlying claim but it downgrades the corroboration assessment (multiple coordinated posts = one source, not many).

---

## Ethical Boundaries

- Use only publicly available information
- Identify individuals only when they are named in court proceedings, news coverage, or self-identifying public social media
- Archive content for investigative purposes only
- Respect platform terms of service where practical
- Exercise particular caution with content involving minors — do not profile individuals under 18 unless they are named in court proceedings as defendants
