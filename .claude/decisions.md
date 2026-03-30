
The methodology.md in each folder isn't a "master reference file" — it's a skill file without the YAML header. Identity, constraints, methodology, reference routing, examples, constraints reminder. The main SKILL.md is the router/kernel dispatching into these sub-skills based on investigation state.
So the folder structure is literally:
references/research/
├── methodology.md      ← the Research "skill file"
├── collection.md       ← reference doc (like a skill's reference/)
├── entity-research.md  ← reference doc
├── faf-research.md     ← reference doc
├── evidence.md         ← reference doc
└── tooling.md          ← reference doc (deps, MCPs, scripts)
And methodology.md says: "You are in the RESEARCH state. Here's who you are in this state, here's what you can and can't do, here's your workflow, here's which reference files to load and when, here's examples of good research behaviour." Exactly like a skill, just loaded by the parent SKILL.md instead of triggered by a description match.
That means the plan structure is right but the framing of methodology.md needs updating — it's not a workflow document, it's a sub-skill definition. And that also means the SAVVY methodology applies to writing each one.
