# GRADE for Drill Journalism

Evidence evaluation framework adapted from the GRADE (Grading of Recommendations, Assessment, Development and Evaluations) system for investigative drill journalism. Load this file when operating in VERIFY phase or when rating any individual claim or source.

---

## Evidence Type Hierarchy

Starting certainty level by source type. Each source enters at this baseline, then undergoes five-domain evaluation.

| Source Type | Starting Certainty | Rationale |
|---|---|---|
| Crown Court judgments / sentencing remarks | HIGH | Judicial findings of fact. Beyond reasonable doubt standard. Named individuals, specific charges, exact sentences. |
| Coroner's inquest findings | HIGH | Formal fact-finding body. Sworn testimony. Medical evidence. |
| CPS charging documents / press releases | HIGH | Prosecutorial assessment based on evidential and public interest tests. |
| CCTV / body-worn camera footage (described in court) | HIGH | Direct observation. Timestamped. Referenced in judicial proceedings. |
| Police press releases / Met statements | MODERATE-HIGH | Official institutional source. Selective — may omit context, emphasise threat narrative, use strategic ambiguity. |
| Court reporting — national press (BBC, PA, Guardian, Times) | MODERATE-HIGH | Professional reporters present in courtroom. Editorial standards. Institutional accountability. Prosecution framing tends to dominate. |
| Court reporting — local press (Evening Standard, Brixton Buzz, local papers) | MODERATE | Editorial standards apply but resources thinner. May rely on PA wire copy. Local knowledge compensates for institutional weight. |
| Local news reporting (non-court) | MODERATE | Editorial standards but secondary sourcing common. Accuracy variable. Good for community impact, weaker on procedural detail. |
| Drill lyrics referencing incidents | CONTEXTUAL | Lyrics are NOT evidence of events. They ARE evidence of: narrative framing, gang affiliations, feuds, emotional processing, cultural response. Claims encoded in lyrics REQUIRE independent corroboration. Treat as intelligence, not evidence. |
| r/ukdrill community knowledge | LOW-MODERATE | Collective intelligence aggregated over time. Generally accurate on gang territories, alliances, and well-known incidents. Vulnerable to: rumour propagation, factional bias, speculation presented as fact, deliberate misinformation. Accuracy degrades for recent or contested events. |
| Twitter/X drill accounts | LOW | Real-time signal source. Valuable for: timing, emotional response, immediate reactions. Unreliable for: factual claims, named individuals, specific details. Clout-driven. Deliberate misinformation common. Ephemeral — content deleted frequently. |
| Instagram posts/stories | LOW | Performative platform. Useful for: establishing presence, location tagging, affiliation signals, memorial activity. Unreliable for: factual claims. Stories disappear after 24 hours — archive immediately. |
| Gang knowledge databases (wiki-style aggregations) | MODERATE | Community-maintained. Generally accurate on alliances, territories, and established gang identities. Can lag behind recent changes. Useful as cross-reference, unreliable as sole source. |
| YouTube comments / community posts | VERY LOW | Unmoderated. Frequently wrong. Occasionally surfaces firsthand accounts that later prove accurate, but ratio is unfavourable. Treat as signal for further investigation only. |

---

## The Five GRADE Domains (Adapted)

Every claim MUST be evaluated across all five domains. Each domain assessment includes a rating (HIGH, MODERATE, LOW, VERY LOW) and a brief evidence statement.

### Domain 1: Source Credibility

Replaces GRADE's "Risk of Bias."

**What it measures:** The institutional, editorial, or legal standard that governs this source's output. The incentive structure that shapes what the source reveals and conceals.

**Assessment questions:**
- Who produced this information?
- What accountability mechanism exists? (editorial board, judicial review, professional standards body, none)
- What is the source's relationship to the case? (independent observer, party to proceedings, interested community member, anonymous)
- Does the source have institutional motivation to distort? (Met Police → threat narrative, defence solicitor → mitigation, prosecution → conviction narrative, community → factional loyalty)

**Rating guide:**
- HIGH: Judicial findings, CPS documents, professional court reporting with named journalist
- MODERATE-HIGH: Met Police official statements, national press reporting
- MODERATE: Local press, gang knowledge databases with track record
- LOW-MODERATE: r/ukdrill community consensus with multiple contributors
- LOW: Individual social media accounts, anonymous claims
- VERY LOW: YouTube comments, unattributed rumour

### Domain 2: Corroboration

Replaces GRADE's "Inconsistency."

**What it measures:** How many independent sources confirm this claim. Independence is the critical word — five Reddit threads citing the same Twitter post is ONE source, not five.

**Assessment questions:**
- How many independent sources confirm this specific claim?
- Are the sources genuinely independent? (Different institutional origins, not copying each other)
- Do corroborating sources agree on the specific details, or only the broad claim?
- Where sources disagree, is the disagreement on peripheral details (normal) or core facts (problematic)?

**Rating guide:**
- HIGH: 3+ independent sources at MODERATE+ credibility agreeing on specifics
- MODERATE: 2 independent sources, or multiple sources agreeing on broad claim with peripheral disagreements
- LOW: Single source, or multiple sources that trace to the same origin
- VERY LOW: No corroboration available

**Independence test:** Trace each source to its origin. If two sources cite the same primary document, interview, or social media post, they are ONE source. Court reporters citing the same prosecution opening are independent on their observations but not on the prosecution's claims — note the distinction.

### Domain 3: Directness

Maps cleanly from GRADE.

**What it measures:** How directly the evidence supports the specific claim being made. A court judgment naming the defendant is direct evidence of guilt. A drill track saying "we caught one of them on the main road" is indirect — it might reference the incident, or a different one, or be fiction.

**Assessment questions:**
- Does the evidence directly support this specific claim? Or does it require inference?
- Is there an interpretive gap between what the source says and what the claim asserts?
- For drill lyrics: is the lyrical reference clearly identifiable as this incident, or could it reference multiple events?
- For social media: is the post directly about this event, or is the connection inferred from timing/location?

**Rating guide:**
- HIGH: Direct evidence — court judgment naming individuals, CCTV footage described in proceedings, police identification
- MODERATE: Evidence requires minimal inference — court reporter's summary of proceedings, named witness statement
- LOW: Evidence requires significant inference — drill lyrics that appear to reference the incident, social media posts timed around the event
- VERY LOW: Connection is speculative — YouTube comments, r/ukdrill speculation, pattern-matching without specific evidence

### Domain 4: Specificity

Replaces GRADE's "Imprecision."

**What it measures:** How granular and verifiable the evidence is. "A teenager was stabbed in Brixton" is low specificity. "17-year-old [full name] was stabbed at 21:40 on [date] outside the Costcutter on Walworth Road and pronounced dead at King's College Hospital at 22:15" is high specificity.

**Assessment questions:**
- Are full names provided? (Not just nicknames or road names)
- Are exact dates and times available?
- Are specific locations named? (Estate, road, building — not just borough or postcode)
- Are ages provided?
- Are specific injuries or causes of death detailed?
- Are sentence lengths exact?

**Rating guide:**
- HIGH: Full names, exact dates/times, specific locations, ages, detailed injuries/charges/sentences
- MODERATE: Some specifics present — names and dates but not times, or locations at borough level but not estate level
- LOW: Vague — "a youth was stabbed in South London", approximate timeframes, nicknames only
- VERY LOW: No verifiable specifics — anonymous individuals, unnamed locations, unspecified timeframes

### Domain 5: Narrative Bias

Replaces GRADE's "Publication Bias."

**What it measures:** Every source in drill journalism operates through a narrative lens. This domain identifies which lens and flags when all available sources share the same bias direction.

**Narrative lenses:**
- **Prosecution lens**: Emphasises premeditation, gang affiliation, threat to public. Maximises severity.
- **Defence lens**: Emphasises mitigation, youth, background deprivation, coercion. Minimises culpability.
- **Police lens**: Emphasises operational success, gang threat, community safety. Justifies policing approach.
- **Media lens**: Emphasises dramatic elements, victim impact, community fear. Optimises for readership/viewership.
- **Community lens**: Emphasises systemic failure, lost potential, environmental factors. Can be factionally aligned.
- **Drill music lens**: Mythologises violence, encodes revenge narratives, performs loyalty. Deliberately provocative.
- **Academic/NGO lens**: Emphasises structural causes, policy failure, data patterns. Can minimise individual agency.

**Assessment questions:**
- Which narrative lens(es) does this source operate through?
- Are all available sources operating through the same lens? (If all sources are prosecution-side, the defence perspective is a gap)
- Has any source's framing been adopted uncritically by subsequent sources?
- What perspective is absent from the available evidence?

**Rating guide:**
- HIGH (low bias risk): Multiple sources with different narrative lenses, balanced representation
- MODERATE: Sources from 2-3 lenses, but one dominates
- LOW (high bias risk): All sources share the same narrative lens
- VERY LOW: Single source with strong narrative motivation (e.g., drill lyrics from a direct participant)

---

## Certainty Rating Assignment

After evaluating all five domains, assign exactly one certainty rating:

| Rating | Criteria | Script Handling Instruction |
|---|---|---|
| **CONFIRMED** | Source credibility: MODERATE-HIGH+. Corroboration: 2+ independent sources. Directness: HIGH. Specificity: MODERATE+. No unresolved narrative bias flags. | State as fact in script. Declarative language. |
| **ASSESSED** | Source credibility: MODERATE+. Corroboration: 1 credible source OR multiple low-credibility sources. Directness: MODERATE+. Specificity: MODERATE. Minor narrative bias acceptable. | State with attribution. "The court heard...", "According to the prosecution...", "Police stated..." |
| **REPORTED** | Source credibility: LOW-MODERATE. Corroboration: limited or absent. Directness: LOW-MODERATE. OR: claim has narrative bias from all available sources. | State with distancing language. "It is reported that...", "Sources suggest...", "Community accounts indicate..." |
| **UNVERIFIED** | Community knowledge only. No institutional source. Low specificity. OR: single social media source. OR: drill lyrics without corroboration. | Context and atmosphere ONLY. Stating as fact is FORBIDDEN. Use for scene-setting, not for factual claims. |

---

## Upgrade and Downgrade Factors

### Upgrade factors (can raise certainty by one level):
- **Large corroboration**: 5+ independent sources across different institutional types
- **Judicial confirmation**: Court proceedings confirm a previously community-sourced claim
- **Physical evidence**: CCTV footage, forensic evidence, or physical artifacts referenced in proceedings

### Downgrade factors (can lower certainty by one level):
- **Single-lens bias**: All available sources share the same narrative motivation
- **Temporal distance**: Sources reporting on events long after they occurred, with possible memory distortion
- **Factional contamination**: Source has known gang affiliation or factional loyalty that could shape the account
- **Retraction or correction**: Source has subsequently corrected or retracted elements of the claim

---

## Output Template

```
## GRADE Assessment: [Claim Text]

| Domain | Rating | Evidence |
|---|---|---|
| Source Credibility | [rating] | [assessment] |
| Corroboration | [rating] | [assessment] |
| Directness | [rating] | [assessment] |
| Specificity | [rating] | [assessment] |
| Narrative Bias | [rating] | [assessment] |

**Certainty Rating: [CONFIRMED/ASSESSED/REPORTED/UNVERIFIED]**
**Script Handling: [instruction]**
**Upgrade/downgrade factors applied: [if any]**
**Verification actions required: [what would raise the rating]**
```
