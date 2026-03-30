# Thinking Tooling

MCPs and resources available for investigative reasoning.

---

## Thinking Toolkit MCP (Primary)

**Server:** `https://server.smithery.ai/elbpr/thinking-toolkit`

The primary tool for structured reasoning during investigation.

### diagnose
Describe what you are stuck on. The tool identifies the type of reasoning problem and routes you to the appropriate thinking technique.

**Use when:** Stuck on a reasoning direction, unsure how to evaluate a claim, or need a structured approach to a problem.

### diagnose_entity
Submit a partially populated cognitive surrogate profile (16-section PSSP). The tool reads the profile, identifies gaps and tensions, generates targeted investigative questions, and routes each to a specific thinking technique.

**Use when:** Building a psychological profile of an investigation subject and need to know what to investigate next and how to think about what you find.

**The loop:** Submit profile → get questions with technique routing → investigate to answer questions → update profile → submit again → deeper questions emerge.

### get_technique
Load the full methodology for a specific thinking technique by ID.

**Use when:** You already know which technique you need, or diagnose/diagnose_entity has routed you to one.

### list_techniques
List all 12 available thinking techniques with descriptions and trigger feelings.

**Use when:** Browsing what is available or checking whether a technique exists for a specific reasoning need.

---

## Technique-to-Investigation Mapping

Common investigation reasoning needs and which techniques address them:

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
| Background fact might be the real driver | Inversion Exercise | Challenge the assumption |
| Individual story vs systemic pattern | Scale Game | Does the pattern hold at population level? |

---

## Assets in This Folder

| Asset | Purpose |
|---|---|
| `mle-lexicon.md.txt` | Multicultural London English vocabulary for parsing drill lyrics and community language during reasoning work |
