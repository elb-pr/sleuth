# Theoretical Foundation: Spurious Regularities Across Learning Systems

## Core Finding

All learning systems — biological, artificial, and institutional — reliably detect regularities in their environment but have no intrinsic mechanism to distinguish genuine causal structure from spurious correlation. Errors arise when the system's solution exploits a feature that covaries with the outcome in the training environment but fails to generalise.

## Source Papers and Key Contributions

| Paper | Domain | Key Finding | Evidence Level |
|-------|--------|-------------|---------------|
| Skinner (1948) | Animal behaviour | Noncontingent reinforcement produces stable "superstitious" behaviour | Very Low |
| Justice & Looney (1990) | Animal behaviour | Partial replication — diverse behaviours, stable within subjects, but different from Skinner's observations | Low |
| Timberlake & Lucas (1985) | Animal behaviour | "Superstitious" behaviour is species-typical appetitive behaviour, not adventitious reinforcement | Low-Moderate |
| Ingvarsson & Fernandez (2023) | Applied behaviour analysis | Noncontingent reinforcement effects are primarily nonoperant | Review |
| Fernandez (2020) | Applied animal behaviour | FT schedules elicit approach in avoidant sheep — same mechanism, different species | Low |
| Geirhos et al. (2020) | Machine learning | DNNs exploit spurious features (shortcut learning) — identical pattern to pigeon superstition | Perspective |
| Balbuena et al. (2026) | Game theory | High-psychopathy individuals use context-dependent mixed strategies, not fixed defection | Very Low-Low |
| Frederick (2005) | Cognitive science | CRT predicts patience, risk tolerance, decision quality — measures ability to override shortcuts | Moderate |
| Nimpf et al. (2019) | Neuroscience | Pigeon magnetoreception via inner ear — decades of chasing artefacts illustrate signal/noise problem | Low-Moderate |
| Sanchez et al. (2017) | Replication science | Analytic thinking reducing religious belief did not replicate (d = 0.07 vs original d = -0.59) | High (for null) |

## Convergence Map

The same structural pattern appears across all domains:
- **Superstitious behaviour in pigeons:** temporal contiguity mistaken for contingency
- **Species-typical appetitive behaviour:** phylogenetic priors override contingency learning
- **Shortcut learning in DNNs:** dataset biases mistaken for causal features
- **Cognitive shortcuts in humans:** intuitive answers accepted without reflection
- **False positive findings in science:** underpowered studies produce spurious effects
- **Context-sensitive defection in psychopathy:** apparent irrationality is adaptive strategy selection
- **Artefact-prone results in magnetoreception:** genuine mechanisms obscured by methodological noise

## Divergence Map: Error Correction Mechanisms

The key divergence is how each system corrects errors:
- **Animal behaviour:** Theoretical reanalysis across decades (Skinner → Staddon → Timberlake → Justice)
- **Machine learning:** Architectural intervention (adversarial training, data augmentation)
- **Human cognition:** Effortful override via cognitive reflection (Frederick's CRT)
- **Science:** Replication with adequate power (Sanchez)
- **Psychopathy:** No correction — the "error" may be adaptive

## Four Testable Hypotheses

### H1: Temporal Contiguity Bias as Domain-General Shortcut Heuristic
All learning systems are biased toward detecting temporal contiguity over genuine contingency because contiguity detection is computationally cheaper. Systems override this bias only when explicit error signals force re-evaluation.

### H2: Phylogenetic Priors as Biological Inductive Bias
What Timberlake called "species-typical appetitive behaviour" is the biological equivalent of architectural inductive bias in DNNs. The organism brings pre-existing behavioural modules to the learning environment. These modules constrain which regularities are detected.

### H3: Cognitive Reflection as Learned Distribution-Shift Detection
Frederick's CRT measures not intelligence but the ability to detect that the intuitive answer fails under closer inspection — the human equivalent of out-of-distribution testing. This capacity is learnable and domain-specific.

### H4: Stochastic Environments Preserve Shortcut Strategies
Variable reinforcement schedules (which produce maximum extinction resistance in pigeons) should also produce maximum shortcut persistence in DNNs and maximum superstitious cognition persistence in humans. The noisier the environment, the harder it is to detect that your strategy is coincidental.

## Application to PSSP

The PSSP skill applies this framework to individual humans:
1. The person's beliefs and habits are regularities extracted from their life experience
2. Their learning system (brain) has no intrinsic mechanism to distinguish causal from spurious
3. PSSP maps where they are causally grounded versus where they are pigeon
4. Extinction tests are the human equivalent of out-of-distribution testing
5. The AI performing the profiling is ALSO a learning system vulnerable to shortcuts — the methodology must be adversarial toward its own first impressions
