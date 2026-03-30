# Web Scraping Cascade

Content extraction strategies for drill journalism source material. Load during INVESTIGATE phase when extracting articles, court documents, and social media content.

---

## Extraction Strategy Selection

Choose strategy based on source type:

| Source Type | Primary Strategy | Fallback Strategy |
|---|---|---|
| News articles (BBC, Guardian, Standard) | Web fetch with markdown extraction | Google cache search |
| Court documents (judiciary.uk) | Direct PDF fetch | Google cache |
| CPS press releases | Web fetch | Web search for cached copy |
| Reddit threads | Reddit MCP tool | Web fetch of thread URL |
| Twitter threads | Twitter MCP tool | Web search for cached/archived copies |
| Instagram posts | Instagram MCP tool | Web search for news articles containing the post |
| YouTube content | YouTube MCP tool for metadata | Web fetch for transcript if available |
| Paywalled articles (FT, Times, Telegraph) | Web search for alternative coverage of same story | Google cache, archive services |
| Local press (Brixton Buzz, local papers) | Web fetch | Web search for republished content |

---

## Extraction Workflow

### Step 1: Identify Source URL
From the evidence log or scan results, identify the exact URL to extract.

### Step 2: Select Strategy
Match source type to strategy from the table above.

### Step 3: Extract Content
Execute the extraction. Record:
- Source URL
- Extraction date and time
- Extraction method used
- Whether extraction was complete or partial
- Any access restrictions encountered

### Step 4: Clean and Structure
- Strip navigation, advertising, and boilerplate
- Preserve article structure (headline, byline, date, body)
- Preserve exact quotes and attributed statements
- Note any embedded media (images, video) that cannot be extracted

### Step 5: Archive
- Push extracted content to Google Docs with full metadata header
- Log extraction in Notion evidence log
- Record content hash for integrity verification

---

## Metadata Header Template

Every archived document MUST include this header:

```
---
Source URL: [url]
Publication: [publication name]
Author: [if available]
Publication Date: [if available]
Extraction Date: [date]
Extraction Method: [method used]
Access Status: [open / paywalled / cached / archived]
Content Status: [complete / partial — note what is missing]
---
```

---

## Handling Paywalled Content

When primary source is paywalled:
1. Search for the same story covered by non-paywalled outlets
2. Check Google cache for the original article
3. Search for quoted excerpts in other coverage
4. Note in the evidence log that the primary source was paywalled and what alternative was used
5. If no alternative exists, note the paywall as a gap in the fact-check workflow

Paywalled content that cannot be accessed is a gap, not an excuse to fabricate the content. Record what is known from secondary sources and flag the primary source as unverified.

---

## Ephemeral Content Priority

Content at risk of deletion MUST be extracted within the same session it is discovered:

1. **Instagram stories**: 24-hour window. Extract text, note visual content, record account and timestamp.
2. **Tweets from volatile accounts**: Drill artists and gang-affiliated accounts delete frequently. Extract full tweet text, engagement metrics, timestamp.
3. **YouTube videos**: Tracks referencing violence are frequently taken down. Extract title, description, upload date, view count, key comments. Note lyrical content relevant to the case.
4. **Reddit posts during active moderation**: Posts discussing ongoing cases may be removed. Extract full post text and top-level comments.

For ephemeral content, speed of capture outweighs completeness of metadata. Get the content first, document provenance second.
