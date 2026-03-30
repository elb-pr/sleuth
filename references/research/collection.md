# Collection

Platform-specific techniques for finding, collecting, and preserving evidence in UK drill investigations.

---

## Search Order

1. **Registry and records FIRST** - court records, sentencing remarks, CPS press releases, local authority records, planning documents, FOI responses
2. **Domain-specific primary sources SECOND** - drill music, social media, community platforms
3. **News and general web LAST** - treat every news claim as a lead to verify in primary sources

Self-check: if more than a third of citations are news articles, go back to primary sources.

## The Confirmation Principle

From UNESCO SBI: "It is always easier to get someone to confirm something you already know than to get them to volunteer information you do not possess."

When engaging community sources: present specific claims for confirmation rather than asking open questions. "The court docs show X was a co-defendant with Y in 2019 - can anyone confirm whether they were affiliated before that?" produces better intelligence than "Does anyone know about X?"

---

## Court and Institutional Sources

### Court and Judiciary Websites

**What it provides:** Sentencing remarks, case outcomes, co-defendant information, prosecution theories, judge's assessment of evidence.

**Search patterns:**
- judiciary.uk for sentencing remarks (search by defendant name, not case name)
- CPS press releases for prosecution summaries
- Local news court reporting for cases too minor for national coverage
- Search co-defendant names individually - they may appear in other cases revealing network connections

**Reliability:** Primary-High tier for factual claims within the document. Sentencing remarks represent the JUDGE'S interpretation, not necessarily ground truth. Co-defendant lists are gold - they reveal operational connections that social media does not. Note what the judge did NOT address - gaps in sentencing remarks are significant.

### Official Records

**Sources:** Council minutes, FOI responses, planning documents, police statistics, school exclusion data, youth service records, local authority budgets.

**Search patterns:**
- FOI directories for relevant local authority data
- What Do They Know (whatdotheyknow.com) for existing FOI responses
- Council meeting minutes for estate-related decisions
- Planning applications for understanding estate development and changes

**Reliability:** Primary-Medium tier. High for what they measure, but may exclude relevant context.

### News Archives

**Priority targets:**
1. BBC court reporting
2. PA Media/Press Association wire copy
3. Evening Standard, Brixton Buzz, South London Press (local)
4. Academic research on the specific gang, postcode, or incident
5. Inquest reports

**Search patterns:**
- Date-restricted searches for incident coverage
- Name searches for prior incidents involving same individuals
- Local papers for incidents too small for national coverage

**Reliability warning:** Circular sourcing is rampant. News quotes police, police cite news, Reddit cites news, news cites Reddit. Always trace the claim back to its PRIMARY source.

---

## Social Media Platforms

### Reddit (r/ukdrill, r/drillshitpost)

**What it provides:** Community knowledge, gang associations, beef timelines, artist connections, estate culture, reactions to incidents, corrections to media misreporting.

**Search patterns:**
- Within subreddit: `site:reddit.com/r/ukdrill "[subject name]"`
- Specific beefs: `[gang1] [gang2] beef` within r/ukdrill
- Incident discussion: `[estate name] [incident type]` or `[postcode]`
- Sort by date to reconstruct how the community learned about events
- Check user posting history for consistent knowledge vs one-off claims
- Read the FULL thread - corrections and arguments in replies are often more informative than the original post

**High-value signal types:**
- Court sentencing threads (300+ upvotes = significant cases)
- Incident aftermath threads (cross-reference against news immediately)
- RIP/memorial threads (victim ID, gang affiliation, associated tracks)
- "What happened to..." retrospective threads (older cases with temporal distance)
- Corrective comments (community members correcting misinformation - often contain accurate detail)

**Reliability:** Highly variable. Cross-reference any Reddit claim against at least one other source type before marking LIKELY. Threads citing court documents are more reliable than those citing "trust me." Beware score-settling.

**MCP:** Reddit search_across_subreddits, retrieve_reddit_post, retrieve_post_comments

### Twitter/X

**What it provides:** Real-time incident signals, court attendance reactions, artist beef exchanges, memorial activity, location drops.

**Value:** Speed. Twitter surfaces incidents within minutes. Drill artists and associates post reactions, threats, and provocations in real time.

**Monitoring patterns:**
- Sudden spikes in mentions of a gang name or postcode
- Artist accounts going silent after activity (may indicate arrest or hiding)
- Memorial hashtags appearing unexpectedly
- Court date mentions and verdict reactions
- Deleted tweets (if cached by third-party services)

**Archival priority: HIGH.** Tweets are deleted frequently. Archive within the same session.

**MCP:** Twitter MCP

### Instagram

**What it provides:** Visual confirmation, location tags, group photos, affiliation signals, pre/post-incident behaviour.

**Search patterns:**
- Use Instaloader (scripts/) for profile data collection
- Cross-platform username search via Sherlock (scripts/)
- Check tagged locations against geo data
- Monitor stories for estate-specific content

**High-value signals:**
- Story activity around incident dates (presence/absence, mood, location)
- Location tags placing individuals at specific estates
- Group photos confirming affiliations (hand signs, colour coordination, estate backgrounds)
- Deletion patterns (what was taken down and when tells its own story)

**Archival priority: CRITICAL.** Stories disappear after 24 hours. Capture immediately.

**MCP:** Instagram MCP. Also: Instaloader script, Sherlock script.

### YouTube

**What it provides:** Drill music videos (location data, lyric references, gang associations through collaborations), news coverage, court reporting, community commentary.

**Search patterns:**
- Artist name + gang tag for tracks
- Estate name for music videos filmed on location
- Cross-reference filming locations against gangs-map-music.csv geo data
- Check video descriptions for producer credits (network connections)
- Check upload dates against incident timelines

**High-value signals:**
- Tracks referencing specific incidents (released within days/weeks of events)
- Track removal (often indicates legal proceedings or police pressure)
- Comment sections with specific claims about referenced events
- Feature collaborations indicating alliance shifts

**Reliability:** Music videos are primary sources for what was said and shown, not for what actually happened. Filming location is evidence of physical presence. Lyrics confirm a narrative exists, not that it is true.

**MCP:** YouTube MCP

### LinkedIn

**What it provides:** Career history, professional connections, relocation history, organisational affiliations.

**Search patterns:**
- `site:linkedin.com "First Last" company`
- URL patterns: /in/firstnamelastname, /in/firstname-lastname

**Key signals:** Gaps between positions (career breaks), location changes (relocation history), short tenures (<1yr), title inflation patterns.

**Reliability:** Self-presented professional identity. People curate LinkedIn more carefully than other platforms.

---

## Content Extraction

When you discover a content platform (YouTube channel, podcast appearances, blog, conference talks) - extract immediately. Do not bookmark for later. Later equals never.

A person talking for 20 minutes on camera reveals more than 100 social media posts. Content platforms are the richest source for understanding how someone thinks and presents themselves.

**YouTube transcript extraction (3-5 most viewed or recent videos):**
- Topics they discuss = what they care about
- Speaking style = formal/casual, speed, filler words, humour
- Vocabulary = jargon level, code-switching
- Recurring themes across videos
- Guest interactions

**Podcast appearances:**
- Hosts ask personal questions - origin stories, failures, mentors
- Cross-reference claims in podcasts vs other platforms (people exaggerate differently in different contexts)

---

## Evidence Preservation

### Archive Before It Disappears

Drill content gets deleted constantly - videos taken down after arrests, profiles wiped, posts removed, articles paywalled. Archive FIRST, analyse SECOND.

### Preservation Methods

| Content Type | Preservation Method |
|---|---|
| Web page | Wayback Machine submission + local PDF save |
| YouTube video | Note URL, title, upload date, description, comment highlights |
| Reddit thread | Archive.today + full text copy including replies |
| Instagram post | Instaloader + screenshot with timestamp |
| Court document | PDF download + SHA-256 checksum |
| News article | Archive.today + local text copy with URL and access date |

### Archival Priority

1. Instagram stories (24hr window) - CRITICAL
2. Tweets from accounts known to delete - capture immediately
3. YouTube videos with low views or controversial content (takedown risk)
4. Reddit posts during active moderation periods (removal risk)
5. News articles behind soft paywalls (access may expire)

### Evidence Metadata

Every piece of evidence MUST be recorded with:
- **Source URL** (original location)
- **Archive URL** (preserved copy location)
- **Access date** (when accessed)
- **Source tier** (from evidence.md credibility tiers)
- **Epistemic marker** (CONFIRMED / LIKELY / SPECULATION / GAP / DOES NOT ADD UP)
- **Brief description** (what this evidence shows and for which hypothesis)

---

## Source Mapping

From UNESCO SBI: when one source is blocked, use the source map to find someone adjacent who can see past the obstacle.

For any investigation, draw the relationships between all potential sources:

```
                [SUBJECT/INCIDENT]
                /        |        \
      [Family]     [Associates]    [Estate residents]
       /    \        /      \         /         \
[School   [Social   [Co-     [Music    [Youth     [Local
 records]  workers]  defendants] collabs] workers]   business]
```

The map reveals: gaps (who should we be asking but are not?), clusters (which sources share the same biases?), bridges (who connects two separate groups?), absent voices (who is affected but not represented?).

---

## Coordinated Activity Detection

Watch for patterns suggesting coordinated social media campaigns:
- Multiple accounts posting similar content within a short timeframe
- Accounts with similar creation dates or naming patterns
- Cross-platform posting of identical or near-identical content
- Brigading of court sentencing discussions with one-sided commentary

Coordinated activity is a narrative bias flag. It does not invalidate the underlying claim but it downgrades the corroboration assessment (multiple coordinated posts = one source, not many).

---

## Ethical Boundaries

- Use only publicly available information
- Identify individuals only when named in court proceedings, news coverage, or self-identifying public social media
- Archive content for investigative purposes only
- Exercise particular caution with content involving minors - do not profile individuals under 18 unless named in court proceedings as defendants
