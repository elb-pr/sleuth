# Search and Collection

Platform-specific techniques for finding, collecting, and preserving evidence in UK drill investigations. Load this reference when planning searches, executing collection, or archiving evidence.

---

## Search Planning

### Open Sources First

From UNESCO SBI: "Most of what we call 'secrets' are simply facts that we haven't paid attention to." 90% of investigation evidence comes from publicly accessible sources. Exhaust open sources before requesting access to anything restricted.

### Search Order

1. **Registry and record searches FIRST** — court records, sentencing remarks, CPS press releases, local authority records, planning documents, FOI responses
2. **Domain-specific primary sources SECOND** — drill music, social media, community platforms
3. **News and general web LAST** — treat every news claim as a lead to verify in primary sources

Self-check: if more than a third of citations are news articles, go back to primary sources.

### The Confirmation Principle

From UNESCO SBI: "It is always easier to get someone to confirm something you already know than to get them to volunteer information you do not possess."

When posting on Reddit or engaging community sources: present specific claims for confirmation rather than asking open questions. "The court docs show X was a co-defendant with Y in 2019 — can anyone confirm whether they were affiliated before that?" produces better intelligence than "Does anyone know about X?"

---

## Platform-Specific Techniques

### Reddit (r/ukdrill, r/drillshitpost)

**What it provides:** Community knowledge, gang associations, beef timelines, artist connections, estate culture, reactions to incidents, corrections to media misreporting.

**Search techniques:**
- Search within subreddit: `site:reddit.com/r/ukdrill "[subject name]"`
- Search for specific beefs: `[gang1] [gang2] beef` within r/ukdrill
- Search for incident discussion: `[estate name] [incident type]` or `[postcode]`
- Sort by date to reconstruct how the community learned about events
- Check user posting history for consistent knowledge vs one-off claims
- Read the FULL thread — the corrections and arguments in replies are often more informative than the original post

**Reliability notes:**
- Highly variable. Some users demonstrate deep, consistent knowledge across many threads. Others repeat myths.
- Cross-reference any Reddit claim against at least one other source type before marking LIKELY.
- Reddit threads citing court documents or sentencing remarks are more reliable than those citing "trust me."
- Beware score-settling: some posts are designed to damage reputations, not inform.

**MCP tool:** Reddit search_across_subreddits, retrieve_reddit_post, retrieve_post_comments

### YouTube

**What it provides:** Drill music videos (location data from filming locations, lyric references to events, gang associations through collaborations), news coverage of incidents, court reporting, community commentary.

**Search techniques:**
- Search artist name + gang tag for tracks
- Search estate name for music videos filmed on location
- Cross-reference filming locations against gangs-map-music.csv geo data
- Check video descriptions for producer credits (reveals network connections)
- Read comments for community knowledge and corrections
- Check upload dates against incident timelines

**Reliability notes:**
- Music videos are primary sources for what was said and shown, not for what actually happened
- Filming location is evidence of physical presence at that estate
- Comments are secondary-aggregated tier — same reliability as Reddit

**MCP tool:** YouTube MCP

### Court and Judiciary Websites

**What it provides:** Sentencing remarks, case outcomes, co-defendant information, prosecution theories, judge's assessment of evidence.

**Search techniques:**
- judiciary.uk for sentencing remarks (search by defendant name, not case name)
- CPS press releases for prosecution summaries
- Local news court reporting for cases too minor for national coverage
- Search co-defendant names individually — they may appear in other cases revealing network connections

**Reliability notes:**
- Primary-high tier for factual claims within the document
- Sentencing remarks represent the JUDGE'S interpretation, which may differ from what actually happened
- Co-defendant lists are gold — they reveal operational connections that social media doesn't
- Note what the judge DIDN'T address — gaps in sentencing remarks are significant

### Instagram / Social Media

**What it provides:** Real-time activity, location posts, association evidence (who appears in whose photos/stories), lifestyle indicators, pre/post-incident behaviour.

**Search techniques:**
- Use Instaloader (bundled in scripts/) for profile data collection
- Search by username across platforms using Sherlock (bundled in scripts/)
- Check tagged locations against geo data
- Monitor stories for estate-specific content
- Screenshot everything — content gets deleted

**Reliability notes:**
- Social media posts are primary-direct sources — high reliability for WHAT WAS POSTED
- Extremely low reliability for claims made within posts (bragging, fabrication, misdirection)
- Deletion patterns are evidence: what was taken down and when tells its own story

**MCP tool:** Instaloader script, Sherlock script

### Web Archives

**What it provides:** Deleted content, historical snapshots of social media profiles, old news articles, removed YouTube videos.

**Search techniques:**
- Wayback Machine: `web.archive.org/web/*/[URL]`
- Google cache: `cache:[URL]`
- Archive.today for recent snapshots
- Search with date-restricted queries: `before:YYYY-MM-DD` in Google

**Reliability notes:**
- Archived content has the same reliability tier as the original source
- The act of archiving provides a timestamp — useful for proving something existed at a specific date
- Always archive evidence yourself before it can be deleted: save URLs to Wayback Machine, screenshot, save page as PDF

### News Archives

**What it provides:** Incident reporting, police statements, community reactions, local council responses, historical context.

**Search techniques:**
- Local papers (South London Press, Hackney Gazette, etc.) for incidents too small for nationals
- Date-restricted searches for incident coverage
- Name searches for prior incidents involving the same individuals
- FOI directories for relevant local authority data

**Reliability notes:**
- Quality varies enormously. Local papers with named court reporters are secondary-verified tier. National tabloids rewriting press releases are tertiary.
- Circular sourcing is rampant: news quotes police, police cite news, Reddit cites news, news cites Reddit
- Always trace the claim back to its PRIMARY source

---

## Evidence Preservation

### Archive Before It Disappears

Drill content gets deleted constantly — videos taken down after arrests, social media profiles wiped, Reddit posts removed, news articles paywalled. Archive FIRST, analyse SECOND.

### Preservation Methods

| Content Type | Preservation Method |
|-------------|-------------------|
| Web page | Wayback Machine submission + local PDF save |
| YouTube video | Note URL, title, upload date, description, and comment highlights |
| Reddit thread | Archive.today + full text copy including replies |
| Instagram post | Instaloader + screenshot with timestamp |
| Court document | PDF download + SHA-256 checksum |
| News article | Archive.today + local text copy with full URL and access date |

### Evidence Metadata

Every piece of evidence MUST be recorded with:
- **Source URL** (original location)
- **Archive URL** (preserved copy location)
- **Access date** (when Claude or user accessed it)
- **Source tier** (from the evidence credibility reference)
- **Epistemic marker** (CONFIRMED / LIKELY / SPECULATION / GAP / DOESN'T ADD UP)
- **Brief description** (what this evidence shows and for which hypothesis)

---

## Source Mapping

From UNESCO SBI: When one source is blocked, use the source map to find someone adjacent who can see past the obstacle.

### Building the Map

For any investigation, draw the relationships between all potential sources:

```
                    [SUBJECT/INCIDENT]
                    /        |        \
          [Family]     [Associates]    [Estate residents]
           /    \        /      \         /         \
    [School]  [Social   [Co-     [Music    [Youth     [Local
     records]  workers]  defendants] collabs] workers]   business]
```

### Source Map as Investigation Tool

The map reveals:
1. **Gaps:** Who should we be asking but aren't?
2. **Clusters:** Which sources cluster together? (They may share the same biases)
3. **Bridges:** Who connects two otherwise separate groups?
4. **Absent voices:** Who is affected but not represented in any source we've found?
5. **New leads:** Following connections to adjacent nodes often reveals more than returning to the same sources

---

## Search Splitting

Claude handles digital searches. The user handles:
- Content behind logins (Instagram accounts, private groups)
- CAPTCHAs and rate-limited services
- Physical location visits and photography
- Messaging contacts and community members
- FOI requests to local authorities
- Court document access requiring physical presence

After every search round, BOTH share what they found. Compare notes. Discuss. Then plan the next round together.
