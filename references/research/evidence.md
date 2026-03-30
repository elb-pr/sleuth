# Evidence

How to classify, assess, verify, log, and cite evidence. Every claim carries a confidence level. Every source has a reliability tier. Every contradiction is preserved.

---

## Source Reliability Tiers

| Tier | Source Type | Reliability | Notes |
|---|---|---|---|
| **Primary-High** | Court documents, sentencing remarks, CPS press releases, coroner reports | Highest factual reliability for what they contain | May reflect prosecution narrative, not full truth |
| **Primary-Medium** | Official records (council minutes, FOI responses, planning documents, police statistics) | High for what they measure | May exclude relevant context |
| **Primary-Direct** | First-person social media posts from subjects, drill lyrics by artists involved | High for what was said/shown | Intent and truth of content separate from existence of content |
| **Secondary-Verified** | Quality news reporting with named sources and specific claims | Medium-High | Check: is the journalist quoting primary sources, or other journalists? |
| **Secondary-Aggregated** | Reddit threads, forum posts, wiki pages | Medium for consensus, Low for specific claims | Multiple accounts saying the same thing may all trace to one original source |
| **Tertiary** | News aggregators, content farms, unnamed "community sources" | Low | Often circular: news quotes Reddit, Reddit quotes news |

---

## Three Key Classifications

Adapted from the genealogical evidence framework. These distinctions matter because they determine how much weight evidence carries.

### 1. Source Classification (What you consulted)

**Original Source** - first recording of information in original form, created at or near time of event. Court documents, original certificates, police reports.

**Derivative Source** - copy, extract, abstract, or transcription created later from original. News articles reporting court outcomes, database entries, Reddit summaries of proceedings.

**Authored Work** - compiled or analysed work with interpretation. Academic research, published gang analyses, community wiki pages.

**Why it matters:** Derivative sources introduce transcription errors. Authored works introduce interpretation. Always seek the original where possible.

### 2. Information Classification (When recorded)

**Primary Information** - recorded at or very near time of event by someone with direct knowledge. Birth date on birth certificate, arrest date in charging documents.

**Secondary Information** - recorded well after event occurred, often from memory or hearsay. Background details in sentencing remarks, ages in news articles.

**Critical distinction:** An ORIGINAL source can contain SECONDARY information. Sentencing remarks (original source) may contain claims about events years prior (secondary information).

### 3. Evidence Classification (How it answers your question)

**Direct Evidence** - explicitly states the fact needed. Court document naming someone as a gang member.

**Indirect Evidence** - implies the fact when combined with other sources. Social media photos consistently showing someone in a specific territory.

**Negative Evidence** - absence of expected information. Person missing from expected court proceedings, no mention in sentencing remarks of a factor you expected to find.

Absence of evidence is evidence of absence ONLY when the source would be expected to contain the information.

---

## Epistemic Markers

Every claim in an investigation carries exactly one marker:

| Marker | Definition | Evidence Required |
|---|---|---|
| **CONFIRMED** | Multiple independent sources agree. Mechanism identified. Cross-referenced against timeline and geography. | Minimum 3 independent sources from different tiers, OR primary-high documentation |
| **LIKELY** | Supported by evidence but with gaps. Consistent with other confirmed findings. | Minimum 2 sources, OR 1 primary source plus consistent circumstantial pattern |
| **SPECULATION** | Plausible inference from available evidence. Not yet tested. | Stated mechanism, stated assumptions, stated test |
| **GAP** | Information needed but not yet found. Known unknown. | Description of what is missing and where it might be found |
| **DOES NOT ADD UP** | Evidence contradicts established pattern or other confirmed findings. | Specific contradiction identified with sources on both sides |

---

## Critical Assessment Rules

1. **Multiple sources saying the same thing is NOT independent corroboration if they share an upstream source.** Three news articles all citing the same police press release is one source, not three.

2. **Court documents are reliable for what happened in court.** They are the prosecution's theory, which may differ from what actually happened.

3. **Community accounts on Reddit are valuable for questions court documents cannot answer** (social dynamics, reputation, estate culture). But they are subject to mythologisation, score-settling, and clout-chasing.

4. **Drill lyrics are primary sources for what the artist chose to say.** They are NOT reliable accounts of what happened. Lyrics confirm that a narrative exists, not that the narrative is true.

5. **Base rate neglect is the most common confidence error.** "He was seen in rival territory the week before the incident" feels significant. But how often do people from that postcode travel through rival territory for ordinary reasons? If the base rate is high, the observation is meaningless. Always ask: "How often does this happen without the outcome we are investigating?"

---

## Confidence Calibration

### Investigative Self-Awareness

Biases Claude is most susceptible to during investigation:

| Bias | Mechanism | Countermeasure |
|---|---|---|
| Confirmation bias | Finding what fits and stopping | Active counter-evidence search |
| Narrative bias | Constructing coherent stories from sparse data | Flag when the narrative is smoother than the evidence supports |
| Anchoring | First hypothesis dominates despite contrary evidence | Generate competing hypotheses early |
| Gap-filling | Bridging evidence gaps with unverified inference | Use the GAP marker. "I do not know" is always available. |
| Authority bias | Trusting court documents over community accounts unconditionally | Court documents reflect the prosecution's theory, not truth |
| Circular sourcing | Treating derivative sources as independent | Always trace claims upstream to their origin |
| Sunk cost | Continuing a hypothesis because of time invested | Kill hypotheses early and cheaply |

### Counter-Evidence Protocol

After building a case for the hypothesis, actively search for evidence against it:
1. Formulate the opposing hypothesis and search for evidence supporting THAT
2. Ask: "What would I expect to see if this hypothesis were WRONG?"
3. If counter-evidence search produces nothing, upgrade confidence
4. If it produces credible dispute, downgrade and note

---

## Fact-Check Workflow

### Step 1: Claim Extraction
Read the complete case file. Extract every factual claim:
- **Identity claims:** "[Name] is a member of [gang]"
- **Event claims:** "[Name] was stabbed on [date] at [location]"
- **Causal claims:** "The attack was in retaliation for [previous event]"
- **Relationship claims:** "[Gang A] and [Gang B] are rivals"
- **Attribution claims:** "[Name] is the artist known as [stage name]"

### Step 2: Evidence Gathering
For each claim, gather all available evidence from primary, secondary, community, and contextual sources.

### Step 3: Evaluate
Apply source tiers and epistemic markers to each claim.

### Step 4: Contradiction Register
For every instance where sources disagree:
- Record both positions with their evidence
- Note which source has higher credibility
- Note whether the disagreement is on core facts or peripheral details
- Preserve both positions. Premature resolution is forbidden.

### Step 5: Gap Documentation
Record what is NOT known: missing dates, unnamed individuals, absent perspectives, events referenced but not verified, timeline gaps.

---

## GRADE for Handoff

Applied ONLY during handoff brief construction, never during active investigation.

### Starting Level

| Evidence Type | Starting Level |
|---|---|
| Multiple primary-high sources corroborating | HIGH |
| Primary-high + secondary-verified corroboration | MODERATE |
| Secondary-verified sources only | LOW |
| Community accounts, single sources, inference | VERY LOW |

### Downgrade Factors (each reduces by 1-2 steps)
- **Inconsistency:** Sources disagree on key details
- **Indirectness:** Evidence is about a similar case, not this case
- **Imprecision:** Claims lack specific dates, names, locations, or mechanisms
- **Source bias:** Source has a stake in the narrative
- **Circular sourcing:** Multiple sources trace to a single origin

### Upgrade Factors
- **Large convergence:** 4+ truly independent sources reach the same conclusion
- **Specificity of detail:** Claims include verifiable specifics that check out
- **Against interest:** Source makes a claim that works against their own position

### Handoff Ratings
- **HIGH:** Confident this finding will hold. Production can build a scene around it.
- **MODERATE:** Probably right. Production should present with appropriate framing.
- **LOW:** May be right. Production should present as one account among several.
- **VERY LOW:** Speculative. Production should either verify independently or omit.

---

## Evidence Logging

### Per-Item Record

Every piece of evidence MUST be logged with:
- Evidence ID (unique, sequential: E-001, E-002)
- Source URL (original location)
- Archive URL (preserved copy)
- Access date
- Source type (from tiers above)
- Source tier
- Epistemic marker
- Description (what this evidence shows)
- Relevant hypothesis (which claim does this support or contradict)
- Collector (Claude or user)

### Chain of Custody

For evidence that may be referenced in the handoff:
1. Record source URL at time of collection
2. Record collection date and time
3. Record extraction method (web search, MCP tool, manual)
4. Generate content hash for integrity verification where possible
5. Note any paywalled or access-restricted content

---

## Citation Format

### For Investigation Notes (Working Format)

Keep citations brief but traceable during active investigation:

```
[Source type] [Identifier]: [Key claim] ([Access date])
Court: R v [Name] [Year] - sentencing remarks, judiciary.uk (accessed 2026-03-30)
Reddit: u/[username], r/ukdrill, "[thread title]" (accessed 2026-03-30)
News: [Outlet], "[Headline]", [Date published] (accessed 2026-03-30)
```

### For Handoff Brief (Full Format)

Full provenance with archive links:

```
[Source tier]. [Full citation]. Original: [URL]. Archived: [archive URL]. Accessed: [date]. Epistemic marker: [marker].
```

### The GPS Framework Adapted

Five elements that MUST be satisfied before a conclusion is presented as established:

1. **Reasonably exhaustive research** - all accessible standard sources searched, multiple source types consulted, FAN principle applied
2. **Complete and accurate source citations** - every claim traceable to its source
3. **Analysis and correlation** - evidence from different sources compared and integrated
4. **Resolution of conflicting evidence** - contradictions addressed (not ignored or prematurely collapsed)
5. **Soundly reasoned conclusion** - logic transparent, assumptions stated, confidence calibrated

A finding that has not passed all five elements is a working hypothesis, not a conclusion.
