# Research and Evidence

Techniques for structuring investigations, constructing hypotheses, assessing evidence quality, and calibrating confidence. Load this reference when beginning an investigation, forming or testing hypotheses, or preparing the handoff brief.

---

## Hypothesis Construction

A subject is not a hypothesis. "Investigate Angell Town" is a subject. "The closure of youth services in Lambeth between 2010-2013 created a recruitment pipeline that the 150/GBG exploited, producing the 2015-2018 violence spike" is a hypothesis.

Adapted from UNESCO Story-Based Inquiry (Hunter et al., 2011) and the stimfueled-scholar eight-step workflow.

### Converting Subjects to Hypotheses

Every hypothesis MUST:
1. Contain a testable causal claim (X happened because of Y)
2. Be decomposable into verifiable terms (each word can be checked independently)
3. Fit in maximum 3 sentences
4. Generate specific questions that can be answered through search

### Decomposition Process

Take the hypothesis apart. Each term generates questions:

Example: "Youth service closures in Lambeth created a gang recruitment pipeline"
- "Youth service closures" — which services? When exactly? FOI data available?
- "Lambeth" — which wards specifically? Do boundaries match gang territories?
- "Created" — is there a mechanism? Direct (kids went from youth club to estate corner) or indirect (removal of alternatives)?
- "Gang recruitment pipeline" — measurable? Court data on age at first offence? Under-18 association data?
- "Pipeline" — implies deliberate recruitment. Is that true, or is it organic social clustering?

### The Wrong Hypothesis Is Valuable

From UNESCO SBI: "If your hypothesis is wrong, the process of testing it leads to the real story."

The Baby Doe case study: Started with "doctors are killing babies." That hypothesis was wrong. Testing it revealed a law forcing doctors to save extremely premature babies, creating a quarter-million severely disabled children whose social security was then cut. The wrong hypothesis led to a bigger story.

When evidence contradicts the hypothesis: accept the facts, make a new hypothesis. The difficulty is neither clinging too hard to a wrong hypothesis nor leaping at the first contrary fact.

### Competing Hypotheses

Generate 3-5 competing hypotheses for the same phenomenon. Each MUST:
- Provide a different mechanistic explanation
- Be distinguishable from the others through evidence
- Have at least one prediction that differs from the others

### Hypothesis Quality Scoring

| Criterion | Question | Application |
|-----------|----------|-------------|
| Testability | Can it be checked with available evidence? | If it can only be confirmed by sources we can't access, it's untestable for us. |
| Falsifiability | What evidence would disprove it? | If nothing could disprove it, it's not a hypothesis. |
| Parsimony | Is it the simplest explanation that fits? | Prefer the explanation requiring fewest assumptions. |
| Explanatory Power | How much of what we observe does it explain? | Good hypotheses explain multiple observations, not just one. |
| Specificity | Does it make precise predictions? | "Something bad will happen" is useless. "The next incident will involve these postcodes" is testable. |

---

## Evidence Assessment

### Source Reliability Tiers

Adapted from UNESCO SBI, OSINT methodology, and person-investigation credibility framework.

| Tier | Source Type | Reliability | Notes |
|------|-----------|-------------|-------|
| **Primary-High** | Court documents, sentencing remarks, CPS press releases, coroner reports | Highest factual reliability for what they contain | May reflect prosecution narrative, not full truth |
| **Primary-Medium** | Official records (council minutes, FOI responses, planning documents, police statistics) | High for what they measure | May exclude relevant context |
| **Primary-Direct** | First-person social media posts from subjects, drill lyrics by artists involved | High for what was said/shown | Intent and truth of content separate from existence of content |
| **Secondary-Verified** | Quality news reporting with named sources and specific claims | Medium-High | Check: is the journalist quoting primary sources, or other journalists? |
| **Secondary-Aggregated** | Reddit threads (r/ukdrill, r/drillshitpost), forum posts, wiki pages | Medium for consensus, Low for specific claims | Multiple accounts saying the same thing may all trace to one original source |
| **Tertiary** | News aggregators, content farms, unnamed "community sources" | Low | Often circular: news quotes Reddit, Reddit quotes news |

### Critical Assessment Rules

1. **Multiple sources saying the same thing is NOT independent corroboration if they share an upstream source.** Three news articles all citing the same police press release is one source, not three.

2. **Court documents are reliable for what happened in court.** They are the prosecution's theory of the case, which may differ from what actually happened. Sentencing remarks reveal what the judge believed, not necessarily ground truth.

3. **Community accounts on Reddit are valuable for questions court documents can't answer** (social dynamics, reputation, estate culture, who was respected, who was feared). But they are subject to mythologisation, score-settling, and clout-chasing.

4. **Drill lyrics are primary sources for what the artist chose to say.** They are NOT reliable accounts of what happened. Artists exaggerate, fabricate, and reference events they weren't present for. Lyrics confirm that a narrative exists, not that the narrative is true.

5. **Absence of evidence is evidence of absence ONLY when the source would be expected to contain the information.** No mention in sentencing remarks means the judge didn't address it, not that it didn't happen. No Reddit threads might mean nobody posted, not that nobody knows.

---

## Confidence Calibration

Every claim in an investigation carries a confidence level. Confidence MUST be calibrated against evidence, not against how strongly the claim feels true.

### The Epistemic Markers

| Marker | Definition | Evidence Required |
|--------|-----------|-------------------|
| **CONFIRMED** | Multiple independent sources agree. Mechanism identified. Cross-referenced against timeline and geography. | Minimum 3 independent sources from different tiers, OR primary-high documentation |
| **LIKELY** | Supported by evidence but with gaps. Consistent with other confirmed findings. | Minimum 2 sources, OR 1 primary source plus consistent circumstantial pattern |
| **SPECULATION** | Plausible inference from available evidence. Not yet tested. | Stated mechanism, stated assumptions, stated test |
| **GAP** | Information needed but not yet found. Known unknown. | Description of what's missing and where it might be found |
| **DOESN'T ADD UP** | Evidence contradicts established pattern or other confirmed findings. | Specific contradiction identified with sources on both sides |

### Base Rate Neglect

The most common confidence error: treating a striking finding as significant without checking how common it is.

Example: "He was seen in rival territory the week before the incident" feels significant. But how often do people from that postcode travel through rival territory for ordinary reasons (work, family, shopping)? If the base rate is high, the observation is meaningless.

Always ask: "How often does this happen without the outcome we're investigating?" If the answer is "frequently," the observation doesn't support the hypothesis.

### Confirmation Bias in Investigation

Claude's primary failure mode: finding evidence that fits the hypothesis and stopping. The evidence that DISCONFIRMS is more valuable than the evidence that confirms.

Countermeasures:
1. After building a case for the hypothesis, actively search for evidence against it
2. Formulate the opposing hypothesis and search for evidence supporting THAT
3. Ask: "What would I expect to see if this hypothesis were WRONG?"
4. If counter-evidence search produces nothing, upgrade confidence. If it produces credible dispute, downgrade and note.

### Investigative Self-Awareness

Biases Claude is most susceptible to during investigation:

| Bias | Mechanism | Countermeasure |
|------|-----------|----------------|
| Confirmation bias | Finding what fits and stopping | Active counter-evidence search |
| Narrative bias | Constructing coherent stories from sparse data | Flag when the narrative is smoother than the evidence supports |
| Anchoring | First hypothesis dominates despite contrary evidence | Generate competing hypotheses early |
| Gap-filling | Bridging evidence gaps with unverified inference | Use the GAP marker. "I don't know" is always available. |
| Authority bias | Trusting court documents over community accounts | Court documents reflect the prosecution's theory, not truth |
| Recency bias | Overweighting the most recently found evidence | Check: would this change my assessment if I'd found it first? |
| Sunk cost | Continuing a hypothesis because of time invested | Kill hypotheses early and cheaply |

---

## GRADE for Handoff

Applied ONLY during handoff brief construction, never during active investigation.

### Starting Level

| Evidence Type | Starting Level |
|--------------|---------------|
| Multiple primary-high sources (court docs, official records) corroborating | HIGH |
| Primary-high + secondary-verified corroboration | MODERATE |
| Secondary-verified sources only | LOW |
| Community accounts, single sources, inference | VERY LOW |

### Downgrade Factors

Each factor can reduce the level by 1-2 steps:

- **Inconsistency:** Sources disagree on key details without explanation
- **Indirectness:** Evidence is about a similar case, not this case specifically
- **Imprecision:** Claims lack specific dates, names, locations, or mechanisms
- **Source bias:** Source has a stake in the narrative (score-settling, self-promotion, legal defence)
- **Circular sourcing:** Multiple sources trace back to a single origin

### Upgrade Factors

- **Large convergence:** 4+ truly independent sources reach the same conclusion through different evidence
- **Specificity of detail:** Claims include verifiable specifics (dates, locations, names) that check out
- **Against interest:** Source makes a claim that works against their own position

### Handoff Ratings

- **HIGH:** Confident this finding will hold. Production can build a scene around it.
- **MODERATE:** Probably right. Production should present with appropriate framing.
- **LOW:** May be right. Production should present as one account among several.
- **VERY LOW:** Speculative. Production should either verify independently or omit.

---

## Investigation Structure

### Discovery Questions

Before starting, answer:

1. What specific question are we trying to answer? (Not "investigate X" but "did X happen because of Y?")
2. Is this exploratory (we don't know the story yet) or confirmatory (we have a hypothesis to test)?
3. What evidence would confirm or deny the hypothesis?
4. What sources are available to us? What's behind access walls?
5. What does failure look like? (What would make this investigation produce nothing useful?)
6. What's the handoff format? (What does claudian-of-the-yard need from us?)

### The FAN Principle

When profiling a subject (individual, group, estate), investigate:

- **Family:** Family connections, where they grew up, who they're related to in the scene
- **Associates:** Who they're seen with, who they collaborate with musically, co-defendants
- **Neighbours:** Who else is on the estate, what's the local geography, what services exist/existed

Adapted from genealogical research methodology. The subject is rarely the most informative source about themselves. Their network reveals what they can't or won't say.
