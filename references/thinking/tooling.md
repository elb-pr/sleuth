# Thinking Tooling

MCPs and resources available for investigative reasoning.

---

## Thinking Toolkit MCP

**Server:** `https://server.smithery.ai/elbpr/thinking-toolkit`

Structured reasoning for when you are stuck on a problem.

### diagnose
Describe what you are stuck on. The tool identifies the type of reasoning problem and routes you to the appropriate thinking technique.

### get_technique
Load the full methodology for a specific thinking technique by ID.

### list_techniques
List all 12 available thinking techniques with descriptions and trigger feelings.

---

## Pigeon Superstition Superposition MCP (PSSP)

**Server:** `https://server.smithery.ai/elbpr/pigeon-superstition-superposition`

Psychological profiling toolkit for constructing Cognitive Surrogate Profiles from documentary evidence. 16 frameworks covering personality, attachment, cognition, emotion regulation, defence mechanisms, interpersonal strategy, and risk prediction.

### list_frameworks
List all 16 profiling frameworks with descriptions and trigger profile signals. Use first to understand what is available.

### assess
Describe the current profile state, available evidence, and what sections need advancing. The tool assesses the profile gap and returns the recommended framework with full methodology. Include: which sections are populated, evidence types available, current tier status, any cross-section contradictions.

**This is the primary investigation progression tool.** Submit your profile state, get back targeted guidance on which framework to apply next and how.

### get_framework
Load the full methodology for a specific framework by ID. Framework IDs: big-five, attachment-architecture, locus-of-control, emotion-regulation, defence-mechanisms, cognitive-distortions, cognitive-triad, existential-orientation, contradiction-map, predictive-risk-map, cognitive-processing, behavioural-defaults, pigeon-superstition-superposition, interpersonal-strategy, signal-discrimination, approach-avoidance.

### get_profiling_toolkit
Load the master Profiling Toolkit — the orchestration router with the full dispatch table, evidence tier system, profile state assessment decision tree, framework combinations, and methodological countermeasures.

---

## How The Two MCPs Work Together

| Need | Which MCP | Which Tool |
|---|---|---|
| Stuck on an investigative reasoning problem | Thinking Toolkit | diagnose |
| Need to evaluate a causal claim | Thinking Toolkit | get_technique("cause-effect-confusion") |
| Need to hold a contradiction productively | Thinking Toolkit | get_technique("contradiction-holding") |
| Building a psychological profile of a subject | PSSP | assess |
| Need to populate a specific profile section | PSSP | get_framework("[section-id]") |
| Want to understand the full profiling system | PSSP | get_profiling_toolkit |
| Profile section produces a cross-section contradiction | Both — PSSP to identify it, Thinking Toolkit to reason about it |

---

## Technique-to-Investigation Mapping (Thinking Toolkit)

| Investigation Need | Likely Technique | Why |
|---|---|---|
| Causal claim from community source | Cause-Effect Confusion | Score across 6 pigeon dimensions |
| Two sources contradict | Contradiction Holding | Hold both poles, extract what the collision reveals |
| Timeline sequence assumed but unverified | Temporal Blindness | Check whether the order is load-bearing |
| Everyone describes subject the same way | Inversion Exercise | Unanimous accounts are suspicious |
| Behaviour seems irrational | Perspective Mapping | Model their internal logic from their position |
| Same pattern across multiple cases | Meta-Pattern Recognition | Is this structural or coincidental? |
| Self-reinforcing dynamic identified | Feedback Loop Mapping | Where does intervention break it? |
| Multiple explanations, each partial | Simplification Cascades | What single insight makes it all click? |

---

## Assets in This Folder

| Asset | Purpose |
|---|---|
| `mle-lexicon.md` | Multicultural London English vocabulary for parsing drill lyrics and community language during reasoning work |
