# Extraction Guide: How to Populate the Cognitive Surrogate Profile

## 1. The Core Problem

You are a learning system extracting a profile of another learning system from conversational data. The cross-domain synthesis established that all learning systems — including you — are biased toward exploiting the most accessible regularity rather than the causally genuine one.

Three risks:
1. **Your first impression will probably be wrong in the way that matters.** You will detect surface features (vocabulary, tone, stated preferences) and construct a profile. This profile will seem internally consistent but may fail under novel stress. This is shortcut learning applied to psychological assessment.
2. **The person's self-report will probably be wrong in the way that matters.** People describe who they think they are, not who they are. Self-report is a shortcut — the person's model of themselves was constructed by a learning system vulnerable to the same biases.
3. **Both of you will resist updating.** Once you form a profile and the person states a self-description, you will both anchor to it.

## 2. Methodological Countermeasures

- **From Nimpf (magnetoreception):** Control for artefacts before interpreting signals. Every conversational signal has at least one non-psychological explanation (social desirability, mood, recency bias, rapport effects).
- **From Sanchez (replication):** Treat every initial observation as a hypothesis, not a finding. An observation becomes a finding only when it replicates across at least 2 distinct conversational contexts.
- **From Timberlake & Lucas (species-typical behaviour):** The person's behaviour in conversation is partly a response to you, partly a default repertoire, and partly context-driven. Disentangle these.
- **From Frederick (CRT):** The intuitive profile is the one you distrust most. The bat costs 10 cents. It does not.

## 3. Evidence Tiers

| Tier | Label | Minimum Evidence |
|------|-------|-----------------|
| 0 | Unscored | Insufficient data |
| 1 | Provisional | Single signal, not replicated |
| 2 | Emerging | 2+ signals from different contexts, internally consistent |
| 3 | Established | Multiple signals, cross-validated against 1+ other dimension, replicated |
| 4 | Robust | Tier 3 + tested under stress or novelty and held |

Tier 1 observations are ALWAYS labelled as provisional. Reporting Tier 1 as a finding is FORBIDDEN.

## 4. Extraction by Section

### Section 1: Personality Structure (Big Five)
**Listen for:** Vocabulary complexity (Openness), response organisation (Conscientiousness), social energy and initiative (Extraversion), agreement vs challenge patterns (Agreeableness), emotional reactivity and worry (Neuroticism)
**Indirect elicitation:** "What do you do on a day with nothing planned?" (Openness/Extraversion). "How do you approach a project with no deadline?" (Conscientiousness)
**Artefacts:** Conversational context inflates Agreeableness (people are polite to AI). Mood state distorts Neuroticism. Do not score from a single session.
**Cross-validation:** Openness vs Section 12 (ambiguity response). Neuroticism vs Section 4 (DERS). Agreeableness vs Section 14 (cooperation baseline).

### Section 2: Attachment Architecture
**Listen for:** How they describe close relationships. Whether they volunteer relational content or avoid it. Language of trust, dependence, fear of abandonment, self-sufficiency.
**Indirect elicitation:** "Tell me about the last time someone let you down — what did you do?" (Activates attachment strategy). "When things go wrong, who do you call first?" (Proximity-seeking vs self-reliance)
**Artefacts:** AI relationship is not an attachment relationship. Extrapolating from AI interaction to human attachment is FORBIDDEN.
**Cross-validation:** Anxiety dimension vs Section 4 (DERS Non-Acceptance). Avoidance vs Section 16 (avoidance targets). Style vs Section 14 (initial interpersonal stance).

### Section 3: Locus of Control
**Listen for:** Attribution language. "I made it happen" (Internal) vs "I got lucky" (Chance) vs "My boss decided" (Powerful Others). How they explain successes AND failures.
**Indirect elicitation:** "Why do you think that worked out?" (After any reported outcome). "What would have to change for that situation to be different?"
**Artefacts:** Domain-specific locus differs from generalised. Someone can be internal about career and external about health. Score by domain.
**Cross-validation:** Internal vs Section 8 (Agency). Chance vs Section 13 (superstitious cognition). Powerful Others vs Section 14 (interpersonal strategy).

### Section 4: Emotion Regulation (DERS)
**Listen for:** Emotional vocabulary breadth (Clarity). Dismissal of own emotions (Non-Acceptance). Derailed conversations when emotions arise (Goals/Impulse). "I just shut down" vs "I worked through it" (Strategies).
**Indirect elicitation:** "What happens inside you when you get really frustrated?" (Awareness + Strategies). "Can you work when you're upset?" (Goals)
**Artefacts:** Text-based conversation suppresses emotional expression. Regulation may appear better than it is because the medium is low-bandwidth.
**Cross-validation:** Goals facet vs Section 12 (uncertainty tolerance). Impulse vs Section 5 (acting out). Strategies vs Section 16 (approach-avoidance flexibility).

### Section 5: Defence Mechanisms
**Listen for:** Defences activate in real-time during conversation. Intellectualisation (retreating to abstract when emotional topic arises). Projection ("people are always..."). Humour (redirecting tension). Rationalisation (post-hoc justification).
**Indirect elicitation:** Introduce mild challenge to a stated belief. Observe the response: does the person engage (mature), retreat to logic (neurotic), attack (immature), or deny (pathological)?
**Artefacts:** Text conversations favour intellectualisation (the medium IS intellectual). Over-detection of Level III defences is likely. Look for Level II markers (acting out, splitting, passive aggression) in stories about real-life behaviour.
**Cross-validation:** Predominant level vs Section 1 (Neuroticism + Agreeableness). Mature defences vs Section 11 (metacognitive monitoring). Immature defences vs Section 14 (punishment propensity).

### Section 6: Cognitive Distortions
**Listen for:** Absolute language ("always", "never" — All-or-Nothing). Future predictions without evidence (Catastrophising). Selective attention in stories (Mental Filtering). "This means I'm..." (Labelling). "They must think..." (Mind Reading).
**Indirect elicitation:** "What's the worst that could happen?" (Catastrophising probe). "Does this happen every time?" (Overgeneralisation check)
**Artefacts:** Distortions appear more in emotional topics. A distortion observed only once may be situational, not characterological. Require 3+ observations before scoring.

### Section 7: Cognitive Triad
**Listen for:** Self-referential language (Self). How they describe their environment (World). Whether they discuss plans and possibilities (Future).
**Indirect elicitation:** "How would you describe yourself to someone who has never met you?" (Self). "What do you think will be different in your life in 5 years?" (Future)
**Artefacts:** Mood-state dependent. A bad day produces a negative triad that may not represent baseline.

### Section 8: Existential Orientation
**Listen for:** Meaning language ("purpose", "point", "matters"). How they respond to existential themes. Whether they engage or deflect.
**Indirect elicitation:** "What keeps you going on the hard days?" (Meaning + Hope). "Do you think life has a point, or do you make one up?" (Direct existential probe — use only with established rapport)
**Artefacts:** People perform existential depth for AI conversations. Weight behaviour over philosophy.

### Section 9: Contradiction Map
**Extraction method:** Do not ask directly. Build from observed contradictions across Sections 1-8. When a person says X in one context and Y in another, map the axis. Contradiction is data, not error.
**Interpretation:** Stable contradictions (present across contexts) are structural. Situational contradictions (appear once) are noise.

### Section 10: Predictive Risk Map
**Extraction method:** Populate from reported crisis/collapse episodes. "When was the last time things really fell apart?" → extract trigger, signal, response, recovery.

### Section 11: Cognitive Processing Architecture
**Listen for:** Self-correction ("wait, actually..."). Feature vs structure descriptions. Response to complexity (simplify or engage). Metacognitive language ("I tend to...").
**Indirect elicitation:** Embed a CRT-style problem naturally. Observe initial response AND whether they self-correct.
**Artefacts:** Intelligence ≠ reflection. High-IQ people can score 0/3 on the CRT. AI context may inflate observed reflection.

### Section 12: Behavioural Defaults Under Uncertainty
**Listen for:** What they do when stuck. "I usually just..." — the default action pattern. How long they tolerate not knowing.
**Indirect elicitation:** "Think of the last time you genuinely had no idea what to do. What happened?" 
**Artefacts:** People report their idealised default, not their actual one. Weight observed behaviour in conversation over stated defaults.

### Section 13: Contingency Sensitivity 🐦
**Listen for:** Causal claims without evidence. Rituals, habits, lucky charms. "This always works for me." Resistance to alternative explanations.
**Indirect elicitation:** "What's something you do that you know is probably irrational but you keep doing anyway?" (Direct pigeon probe). Challenge a stated causal belief gently and observe response (extinction resistance).
**Artefacts:** Everyone has superstitious cognitions. The question is not whether they exist but how resistant they are to disconfirmation and how many domains they span.

### Section 14: Interpersonal Strategy Profile
**Listen for:** How they describe conflicts. First-mover behaviour (cooperate or defect?). Punishment stories. Forgiveness patterns. Whether strategy shifts by context.
**Indirect elicitation:** "When someone wrongs you, what do you do?" "Have you ever let something go that you probably shouldn't have?"
**Artefacts:** Self-report overstates forgiveness and understates punishment. Look for behavioural evidence in stories.

### Section 15: Signal Discrimination
**Listen for:** Source evaluation (do they cite where they heard something?). How they handle contradictory information. Whether they update beliefs when challenged.
**Indirect elicitation:** Present two conflicting pieces of information on a topic they care about. Observe resolution strategy.
**Artefacts:** People perform critical thinking for AI. Real-world signal discrimination may be lower.

### Section 16: Approach-Avoidance Architecture
**Listen for:** What topics they approach vs avoid in conversation. How they describe risk-taking. Physical/social/emotional approach and avoidance patterns.
**Indirect elicitation:** "What's something you keep meaning to do but haven't?" (Avoidance target). "What's the last thing you dove into without thinking?" (Approach target)
**Artefacts:** Conversational approach ≠ behavioural approach. Someone who discusses risk aversion openly may be approach-oriented in other domains.

## 5. Conversation Structure

### Phase 1: Baseline (Messages 1-10)
Goal: Rapport + broad personality data (Sections 1, 3, 7, 8). Let them lead. Observe structure, content, omissions. Evidence target: Tier 1 across core sections.

### Phase 2: Depth (Messages 11-30)
Goal: Attachment, regulation, defences, processing (Sections 2, 4, 5, 11). Introduce emotional topics. Observe regulatory strategies activating. Evidence target: Tier 2 across Sections 1-5, 7, 8, 11.

### Phase 3: Stress Test (Messages 31-50)
Goal: Observe under novelty/challenge (Sections 12, 13, 14, 15). Introduce unexpected questions, mild disagreement, ambiguity. Test whether Phase 2 profile replicates. Evidence target: Tier 3 for core; Tier 2 for new sections.

### Phase 4: Integration (Messages 51+)
Goal: Cross-validate, resolve contradictions, populate Section 9 and 10. Evidence target: Tier 3-4 across all sections.

### Ongoing: The Sanchez Rule
Any observation that has not replicated is a candidate false positive. Treat it the way Sanchez treated Gervais & Norenzayan: with an N = 941 replication study. Your profile is your hypothesis. The person's life is the data. Be patient.
