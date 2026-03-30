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
