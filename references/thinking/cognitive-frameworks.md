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
-e 

---

# Hypothesis Generation Reference

Systematic framework for developing testable scientific hypotheses. Load this file when operating in Brainstorming mode.

---

## 8-Step Workflow

### 1. Understand the Phenomenon
- Identify core observation or pattern requiring explanation
- Define scope and boundaries
- Note constraints and specific contexts
- Clarify known vs uncertain
- Identify relevant scientific domain(s)

### 2. Literature Grounding
Search existing scientific literature using available tools (web search, Scholar Gateway MCP, Consensus MCP, Exa MCP).

**Search strategy:**
- Begin broad to understand landscape
- Narrow to specific mechanisms, pathways, theories
- Look for contradictory findings and unresolved debates
- Identify analogies from related systems or domains

### 3. Synthesize Existing Evidence
- Summarise current understanding
- Identify established mechanisms or theories that may apply
- Note conflicting evidence and alternative viewpoints
- Recognise gaps, limitations, unanswered questions
- Identify cross-domain analogies

### 4. Generate Competing Hypotheses (3-5)
Each hypothesis MUST:
- Provide a mechanistic explanation (how and why, not just what)
- Be distinguishable from other hypotheses
- Draw on evidence from literature synthesis
- Consider different levels of explanation (molecular, cellular, systemic, population)

**Generation strategies:**
- Apply known mechanisms from analogous systems
- Consider multiple causative pathways
- Explore different scales of explanation
- Question assumptions in existing explanations
- Combine mechanisms in novel ways

### 5. Evaluate Hypothesis Quality

| Criterion | Question | Score 1-5 |
|-----------|----------|-----------|
| Testability | Can it be empirically tested? | |
| Falsifiability | What observations would disprove it? | |
| Parsimony | Is it the simplest explanation fitting the evidence? | |
| Explanatory Power | How much of the phenomenon does it explain? | |
| Scope | What range of observations does it cover? | |
| Consistency | Does it align with established principles? | |
| Novelty | Does it offer new insights beyond existing explanations? | |

Explicitly note strengths and weaknesses of each hypothesis.

### 6. Design Experimental Tests
For each viable hypothesis, propose specific experiments:

**Design elements:**
- What would be measured or observed?
- What comparisons or controls are needed?
- What methods or techniques would be used?
- What sample sizes or statistical approaches are appropriate?
- What are potential confounds and how to address them?

**Multiple approaches to consider:**
- Laboratory experiments (in vitro, in vivo, computational)
- Observational studies (cross-sectional, longitudinal, case-control)
- Clinical trials (if applicable)
- Natural experiments or quasi-experimental designs

### 7. Formulate Testable Predictions
For each hypothesis:
- State what SHOULD be observed if correct
- Specify expected direction and magnitude when possible
- Identify conditions under which predictions hold
- Distinguish predictions BETWEEN competing hypotheses
- Note predictions that would FALSIFY the hypothesis

### 8. Identify Priority Experiment
Select the single highest-value experiment that discriminates between the most hypotheses simultaneously. This maximises information gain per experimental investment.

---

## Output Template

```
## Phenomenon Summary
[What needs explaining — 2-3 sentences]

## Hypothesis N: [Descriptive Title]
**Mechanism:** [How and why — 1-2 paragraphs]
**Supporting evidence:** [2-3 key citations with brief context]
**Core assumptions:** [1-2 critical assumptions]
**Testable predictions:**
  - If correct: [specific observable outcome with expected direction]
  - Falsified by: [specific counter-observation]
**Experimental approach:** [Brief design — measurement, controls, method]
**Quality assessment:** Testability: X/5 | Parsimony: X/5 | Novelty: X/5

## Critical Comparisons
[Table or narrative showing which predictions distinguish between hypotheses]

## Priority Experiment
[Single experiment maximising discrimination between hypotheses]
```

---

## Common Pitfalls in Hypothesis Generation

1. **Unfalsifiable hypotheses** — if no observation could disprove it, it's not scientific
2. **Post-hoc rationalisation** — fitting explanations to known data without novel predictions
3. **Scope creep** — hypotheses trying to explain everything explain nothing
4. **Confirmation anchoring** — generating only hypotheses consistent with preferred theory
5. **Mechanism-free descriptions** — "X causes Y" without explaining how
6. **Ignoring competing explanations** — presenting one hypothesis when multiple are viable
-e 

---

# First Principles Thinking

## Core Concept

Strip away assumptions and conventions to reach fundamental truths, then rebuild understanding from the ground up.

## Three-Step Process

### Step 1: Identify Assumptions

**Ask:** "What do we assume to be true about this?"

List all implicit and explicit assumptions in the content:
- Unstated premises
- Inherited wisdom ("everyone knows...")
- Industry conventions
- Historical precedents treated as universal laws

**Example from business:**
- Assumption: "We need a physical store to sell products"
- Question: Is this fundamentally true or historically convenient?

### Step 2: Break Down to Fundamentals

**Ask:** "What is definitely, provably true?"

Reduce to indisputable facts:
- Physical laws (if applicable)
- Mathematical truths
- Core human needs/behaviors
- Cause-effect relationships you can verify

**Sorting Framework:**
```
Claim → Ask: "How do I know this is true?"
    ↓
├─ "It just is" → Probably an assumption, dig deeper
├─ "That's how it's always done" → Convention, not fundamental
├─ "X happens, then Y happens" → Potential fundamental (verify causation)
└─ "Mathematically/physically must be true" → Fundamental
```

### Step 3: Rebuild from Scratch

**Ask:** "Starting from fundamentals only, what logically follows?"

Reconstruct without importing old assumptions:
1. Begin with verified fundamentals
2. Each step must logically follow from previous
3. Note where you make new assumptions (be explicit)
4. Compare new construction to original concept

## Application Template

```markdown
## Original Concept/Argument
[What the author claims]

## Hidden Assumptions
- Assumption 1: [Something taken as given]
- Assumption 2: [...]

## Verified Fundamentals
- Fundamental 1: [Provably true core fact]
- Fundamental 2: [...]

## Rebuilt Understanding
Starting from fundamentals only:
Step 1: [First logical derivation]
Step 2: [Second logical derivation]
...
Conclusion: [What actually follows]

## Comparison
Original vs. Rebuilt:
- What survived: [Fundamentally sound ideas]
- What doesn't hold: [Based on questionable assumptions]
- New insights: [What rebuilding revealed]
```

## Common First Principles in Different Domains

### Business/Economics
- People act in self-interest (with caveats)
- Supply and demand affect price
- Value = willingness to pay
- Scarcity creates value

### Psychology/Human Behavior
- Humans seek pleasure, avoid pain
- Social status matters to humans
- Cognitive biases exist (not "people are rational")
- Habits form through repetition

### Technology
- Information can be copied at near-zero cost
- Network effects: value ∝ n² (Metcalfe's law)
- Moore's law (transistor density doubles ~every 2 years)
- Computation has energy cost

### Physics/Reality
- Energy is conserved
- Entropy increases
- Speed of light is constant
- Cause precedes effect

## Red Flags: Pseudo-First Principles

Watch for claims disguised as fundamentals:
- "People always prefer X" (overgeneralization)
- "This is just human nature" (often cultural)
- "Economics proves..." (many schools of economics)
- "Science says..." (which study? replicated?)

**Test:** Can you point to specific evidence/mechanism, or is it folk wisdom?

## Powerful Questions

- "Why is this true?" (repeat 5 times - "5 Whys")
- "What must be true for this to work?"
- "If I couldn't do it this way, what's another path?"
- "What would an alien with no context think?"
- "What if the opposite were true?"

## Example: Deconstructing "Need for College Education"

**Assumptions:**
- Need degree to get good job
- Learning requires formal institution
- 18-22 is the right age
- Four years is optimal duration

**Fundamentals:**
- Employers want skilled workers
- Skills can be demonstrated
- Learning requires time + practice
- Knowledge can be transmitted

**Rebuilt:**
→ Employers want proof of skill
→ Proof can be: degree OR portfolio OR test OR track record
→ Therefore, degree is one option, not necessity
→ Insight: Focus on skill + proof, not credential alone

## Practical Use in Reading

When analyzing content:
1. **Identify claims** that seem absolute
2. **Challenge foundations:** "Does this HAVE to be true?"
3. **Verify causation:** "Does A truly cause B, or just correlate?"
4. **Rebuild the argument** from indisputable facts only
5. **Compare** what survives vs. what was assumption

This exposes weak arguments and strengthens valid ones.
