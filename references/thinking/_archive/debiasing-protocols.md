# Debiasing Protocols: Evidence-Based Countermeasures for Organisational Decision-Making

## Protocol 1: Temporal Separation (Anti-Automation Bias)

**Evidence Base:** Agudo et al., 2024, published in *Cognitive Research: Principles and Implications*; consistent findings across multiple studies compiled in PubMed Central systematic review.

**Trigger Condition:** Any decision process where algorithmic or AI recommendations are presented to human decision-makers before they form independent judgments.

**Protocol:**
1. Decision-makers MUST record their independent assessment in writing BEFORE viewing any algorithmic recommendation
2. The pre-commitment record is timestamped and cannot be modified after algorithmic output is revealed
3. Disagreements between the human pre-commitment and the algorithmic recommendation trigger a structured reconciliation process (not automatic deference to either)
4. The reconciliation must produce a documented rationale for whichever position is adopted

**Effectiveness:** This is the single most consistently effective intervention against automation bias across studies. By forcing independent judgment formation before exposure to the algorithm, it prevents the anchoring mechanism that drives both complacency and commission errors.

**Expected Resistance:** Decision-makers will report the protocol as burdensome and unnecessary. This is predicted by Buçinca et al. (2021): the most effective interventions receive the worst subjective ratings. Resistance is not evidence of protocol failure; it is evidence of protocol necessity.

**Implementation Cost:** Moderate. Requires process redesign and IT system changes to control information sequencing. Does not require new technology.

---

## Protocol 2: Calibrated Friction (Anti-Automation Bias)

**Evidence Base:** Buçinca, Malaya & Gajos, 2021, Harvard University, tested cognitive forcing functions and found significant reduction in over-reliance.

**Trigger Condition:** Decision environments where the consequence of error varies dramatically across cases (e.g., loan approvals where amounts range from small to material).

**Protocol:**
1. Classify decisions into consequence tiers (e.g., Tier 1: routine, Tier 2: significant, Tier 3: material)
2. Friction scales with tier: Tier 1 may proceed with algorithmic recommendation and single-click confirmation; Tier 2 requires written justification for agreement; Tier 3 requires independent assessment by a second qualified decision-maker with no visibility of the first assessment or the algorithmic output
3. Tier classification is determined by objective criteria (e.g., financial threshold, affected population size), not by the decision-maker processing the case

**Effectiveness:** Reduces over-reliance on automation while maintaining workflow efficiency for routine cases. Addresses the severity-inversion problem by inserting proportionally greater oversight where errors are most consequential.

**Expected Resistance:** Tier 3 friction will be perceived as distrust. Frame as quality assurance, not performance monitoring. The Georgetown CSET (2024) Patriot-AEGIS comparison provides a compelling narrative: the Navy's redundant identification chains were not a sign of distrust but of operational discipline.

---

## Protocol 3: Failure Exposure Training (Anti-Automation Bias)

**Evidence Base:** Georgetown CSET report, 2024; US Navy AEGIS training doctrine; general finding across automation bias literature that exposure to system failure cases increases detection sensitivity.

**Trigger Condition:** Any organisation deploying AI or algorithmic systems where human overseers are expected to catch errors.

**Protocol:**
1. Curate a library of realistic cases where the specific system in use produced incorrect outputs (not hypothetical scenarios; actual historical failures or carefully constructed realistic simulations)
2. Present these cases to human overseers regularly (minimum monthly) as part of ongoing proficiency training
3. Provide immediate feedback: show the correct answer, explain why the system failed, quantify the consequence of the error
4. Track detection rates over time; declining detection rates trigger increased training frequency
5. Rotate case types to prevent pattern memorisation

**Effectiveness:** Directly counters the base rate problem in automation monitoring. When a system is correct 97% of the time, monitors develop complacency because failures are too rare to maintain vigilance. Failure exposure training artificially increases the experienced base rate of failure, keeping detection circuits active.

**Expected Resistance:** "The system is reliable; this training wastes time." Counter with aviation analogy: pilots train for engine failures they may never experience because the consequence of missing one is catastrophic.

---

## Protocol 4: Pre-Mortem Analysis (Anti-Overconfidence, Anti-Confirmation Bias)

**Evidence Base:** Gary Klein, 2007, "Performing a Project Premortem," *Harvard Business Review*. Supported by Kahneman's endorsement in *Thinking, Fast and Slow* as one of the few individual-level debiasing techniques with demonstrated effectiveness.

**Trigger Condition:** Any significant strategic decision where the team has converged on a preferred option and is approaching commitment.

**Protocol:**
1. After a tentative decision is reached but BEFORE formal commitment, convene the decision team
2. Frame: "Imagine we are one year in the future. The decision we just made has failed spectacularly. Write down independently the reasons why it failed."
3. Each participant writes independently for 5-10 minutes (no discussion)
4. Go around the table: each person reads one reason, cycling until all reasons are exhausted
5. Categorise reasons into: (a) addressable risks we have not mitigated, (b) assumptions we have not tested, (c) information we are missing
6. Revise the decision or its implementation to address the highest-priority items

**Effectiveness:** Legitimises dissent by making it a structured exercise rather than an act of disloyalty. Directly counters groupthink (Janis, 1972) by creating social permission to voice concerns. Counters overconfidence by forcing explicit consideration of failure scenarios. Counters WYSIATI by asking "what are we not seeing?"

**Expected Resistance:** Low. The exercise is brief, non-threatening, and framed as prudent rather than pessimistic.

---

## Protocol 5: Reference Class Forecasting (Anti-Optimism Bias, Anti-Inside View)

**Evidence Base:** Bent Flyvbjerg, from *Megaprojects and Risk* (Cambridge University Press, 2003). Mandated by UK Treasury for large infrastructure projects. Kahneman & Lovallo, 1993, "Timid Choices and Bold Forecasts," *Management Science* 39(1), pp. 17-31.

**Trigger Condition:** Any project estimate (cost, timeline, return) that has been generated primarily through bottom-up analysis of the specific project's features (the "inside view").

**Protocol:**
1. Identify a reference class: a set of comparable past projects with known outcomes
2. Obtain the distribution of outcomes in the reference class (mean, standard deviation, range)
3. Position the current project's bottom-up estimate within the reference class distribution
4. If the bottom-up estimate falls above the 50th percentile of the reference class, require explicit justification for why this project is genuinely different from the base
5. Apply empirical uplift factors: UK Treasury mandates 15-32% uplifts for capital expenditure. Adjust for domain-specific evidence.

**Effectiveness:** Directly addresses the optimism bias that afflicts 90% of mega-projects (Flyvbjerg). Forces the outside view onto a process that naturally gravitates toward the inside view.

**Expected Resistance:** "Our project is different." This is itself the inside view bias. The protocol's power lies in requiring evidence for differentiation rather than assuming it.

---

## Protocol 6: Bayesian Shrinkage for Portfolio Decisions (Anti-Optimiser's Curse)

**Evidence Base:** Smith & Winkler, 2006, *Management Science* 52(3); Schuyler & Nieman, 2007, applied to petroleum exploration.

**Trigger Condition:** Selection of the "best" option from a set of estimated values, particularly when: (a) multiple options have similar estimated values, (b) estimation uncertainty is high, or (c) the number of options is large.

**Protocol:**
1. Calculate the grand mean of all option estimates
2. Estimate the ratio of estimation noise to genuine value variation (w)
3. Apply shrinkage: Adjusted Value = (1 - w) x Estimate + w x Grand Mean
4. Rank options by adjusted values, not raw estimates
5. For "close calls" (separation delta < 1.0), explicitly acknowledge that the probability of selecting the correct option is below 73% and expected disappointment exceeds 0.54 standard deviations (per Smith & Winkler correction table)
6. Consider diversifying across top options rather than concentrating on the single "winner"

**Effectiveness:** Petroleum portfolios: true value might be half forecast value without correction (Schuyler & Nieman, 2007). With 100 options (e.g., CVC screening startup pitches), overestimation reaches approximately 2.5 standard deviations.

**Expected Resistance:** "You're telling us to aim for mediocrity." Counter: shrinkage does not penalise genuinely superior options (high separation delta produces minimal adjustment). It penalises the statistical illusion of superiority created by estimation noise.

---

## Protocol 7: Noise Audit (Anti-Noise)

**Evidence Base:** Kahneman, Sibony & Sunstein, 2021, *Noise: A Flaw in Human Judgment*.

**Trigger Condition:** Any repetitive judgment process performed by multiple decision-makers (hiring, underwriting, sentencing, performance evaluation, credit approval, medical diagnosis).

**Protocol:**
1. Select 15-20 representative cases that span the range of typical decisions
2. Have each case independently evaluated by a minimum of 5 qualified decision-makers
3. No discussion or calibration between evaluators during the exercise
4. Calculate between-evaluator variability for each case (standard deviation, coefficient of variation)
5. If median coefficient of variation exceeds 25-30% of the decision scale, noise is a primary error source
6. Implement structured decision guidelines: explicit criteria, defined scales, sequenced evaluation (evaluate each criterion independently before integrating into an overall judgment)

**Effectiveness:** Structured decision protocols typically reduce noise by 30-50% without eliminating appropriate variability. The key is distinguishing desirable variation (different cases warrant different decisions) from undesirable variation (same case, different judge, different outcome).

**Expected Resistance:** "You're replacing professional judgment with checklists." Counter: the audit quantifies how much "professional judgment" is actually noise. Present the insurance underwriting data: median ratio of highest to lowest quote for identical risk = 1.55x. Ask whether that variation reflects expertise or randomness.

---

## Protocol 8: Structured Dissent (Anti-Groupthink)

**Evidence Base:** Janis, 1972, *Victims of Groupthink* (Houghton Mifflin); Charlan Nemeth, 2018, *In Defense of Troublemakers* (Basic Books); Red Team practices documented across military, intelligence, and corporate contexts.

**Trigger Condition:** Cohesive teams making high-stakes decisions, particularly when: (a) the team has a strong leader with a known preference, (b) the team has a history of consensus, (c) there is time pressure or external threat, (d) the team is homogeneous.

**Protocol Options:**

**Option A: Designated Devil's Advocate**
- Formally assign one team member to argue against the emerging consensus at each decision meeting
- Rotate the role to prevent identification with a "negative" position
- The advocate must present the strongest possible counter-case, not a token objection
- Limitation: Nemeth (2018) found that designated devil's advocates are less effective than authentic dissenters because the group discounts the argument as role-playing

**Option B: Red Team / Blue Team**
- Divide the decision team into two independent groups
- Blue Team develops and advocates the proposed course of action
- Red Team independently develops the strongest case against it and proposes alternatives
- Teams present to a decision authority who evaluates both cases
- More resource-intensive but more effective than devil's advocacy

**Option C: Anonymous Challenge Protocol**
- Before finalising any major decision, provide a channel for anonymous written challenges
- Challenges must be formally addressed and responded to before the decision is ratified
- Most effective when combined with a norm that generating challenges is expected behaviour, not disloyalty

**Effectiveness:** Red teaming is standard practice in US military planning and intelligence analysis. Corporate adoption is growing, particularly for M&A decisions, product launches, and strategic pivots.

**Expected Resistance:** "We don't have time for this." Counter: the cost of a structured dissent process is hours; the cost of a preventable strategic failure is years and millions. Bay of Pigs vs Cuban Missile Crisis: Kennedy added structured dissent after Bay of Pigs and achieved a radically better outcome during the missile crisis.

---

## Protocol 9: Algorithmic Fairness Documentation Protocol

**Evidence Base:** Kleinberg, Mullainathan & Raghavan, 2016; EU AI Act (Regulation 2024/1689); Green, 2022, *Philosophy & Technology*.

**Trigger Condition:** Deployment of any algorithmic or AI system that produces recommendations affecting individuals from populations with differing base rates (hiring, lending, healthcare triage, criminal justice, insurance underwriting).

**Protocol:**
1. Identify the outcome being predicted and its base rates across relevant demographic groups
2. If base rates differ, the Kleinberg impossibility theorem applies. Document this explicitly.
3. Choose which fairness definition governs:
   - **Calibration:** Same score means same probability, regardless of group. Appropriate when decision-makers need reliable risk estimates (clinical settings).
   - **Equal false positive rates:** Same proportion of false alarms across groups. Appropriate when the burden of false positives falls disproportionately on one group.
   - **Equal false negative rates:** Same proportion of missed cases across groups. Appropriate when failure to identify true positives disproportionately harms one group.
4. Document the choice, the rationale, and the trade-offs explicitly
5. Document what the chosen definition does NOT protect against
6. Review the choice annually and when base rates shift materially
7. Maintain an audit trail suitable for regulatory review under EU AI Act high-risk classification

**Effectiveness:** Does not eliminate the impossibility, but transforms an implicit default into an explicit, documented, defensible choice. The strategic value is converting a potential liability (undocumented algorithmic bias) into a governance asset (documented, deliberate fairness trade-off).

**Expected Resistance:** "This makes us look like we're admitting bias." Counter: the bias exists whether documented or not. Documentation demonstrates governance maturity, not fault. The EU AI Act requires it for high-risk systems regardless.
