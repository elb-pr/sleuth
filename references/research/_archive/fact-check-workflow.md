# Fact-Check Workflow

Structured claim extraction and verification for drill journalism. Load during VERIFY phase alongside references/grade-drill-journalism.md.

---

## Step 1: Claim Extraction

Read the complete case file. Extract every factual claim — each statement that asserts something happened, exists, or is true.

**Claim categories:**
- **Identity claims**: "[Name] is a member of [gang]", "[Name] was [age] years old"
- **Event claims**: "[Name] was stabbed on [date] at [location]"
- **Causal claims**: "The attack was in retaliation for [previous event]"
- **Relationship claims**: "[Gang A] and [Gang B] are allied/rivals"
- **Attribution claims**: "[Name] is the artist known as [stage name]"
- **Contextual claims**: "The estate has a history of gang violence dating to [year]"

**For each claim, record:**
- The exact claim text
- The source(s) it originates from
- The claim category
- Whether it is stated as fact, attributed, or speculative in the source

---

## Step 2: Evidence Gathering

For each extracted claim, gather all available evidence:

1. **Primary sources**: Court documents, CPS statements, police press releases
2. **Secondary sources**: News reporting, court reporting
3. **Community sources**: Reddit, Twitter, Instagram, YouTube
4. **Contextual sources**: Gang knowledge databases, drill lyrics, academic research

Record each piece of evidence in the evidence log with full provenance.

---

## Step 3: Evaluate Each Claim

Apply the five GRADE-drill-journalism domains from references/grade-drill-journalism.md to each claim:
1. Source credibility
2. Corroboration
3. Directness
4. Specificity
5. Narrative bias

Assign the certainty rating: CONFIRMED, ASSESSED, REPORTED, or UNVERIFIED.

---

## Step 4: Contact/Consultation Check

Identify claims where additional sources would change the rating:
- Would obtaining sentencing remarks upgrade a claim from ASSESSED to CONFIRMED?
- Would finding the defence solicitor's statement balance a narrative bias flag?
- Would locating local press coverage provide missing community perspective?

List these as **verification actions** in the handoff brief.

---

## Step 5: Contradiction Register

For every instance where sources disagree:
- Record both positions with their evidence
- Note which source has higher credibility
- Note whether the disagreement is on core facts or peripheral details
- Preserve both positions for the handoff brief — premature resolution is FORBIDDEN

---

## Step 6: Gap Documentation

Record what is NOT known:
- Missing dates, times, or locations
- Unnamed individuals
- Absent perspectives (defence, family, community, police)
- Events referenced but not verified
- Timeline gaps between known events
- Weather, atmospheric, or environmental details needed for script scene-setting

---

## Claim Tracking Template

```
| # | Claim | Category | Source(s) | GRADE Rating | Verification Actions | Script Handling |
|---|-------|----------|-----------|--------------|---------------------|-----------------|
| 1 | [claim text] | [category] | [sources] | [rating] | [actions] | [instruction] |
```
