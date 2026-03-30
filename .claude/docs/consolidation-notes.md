# Research Consolidation Notes

**Date:** 2026-03-30
**What happened:** 25 files in references/research/ consolidated into 6. Originals archived in references/research/_archive/.

## Files Written

| File | Lines | Sources synthesised from |
|---|---|---|
| methodology.md | 171 | ai-research-handbook-blueprint, research_process, research_subprocess, research-and-evidence (hypothesis/structure sections), scan-methodology (story-worthiness, lead triage) |
| collection.md | 256 | search-and-collection, scan-methodology (signal taxonomy), social-media-intelligence, platforms, content-extraction, web-scraping-cascade |
| entity-research.md | 191 | osint-methodology, profile, extraction-guide (PSSP sections adapted for investigation) |
| faf-research.md | 164 | family-friends-research (FAN Principle), research-strategies (network patterns) |
| evidence.md | 227 | research-and-evidence (evidence assessment, tiers, confidence, GRADE), evidence-evaluation (three classifications), gps-guidelines, citation-templates, fact-check-workflow, research-log-guidance, IQTS concepts |
| tooling.md | 123 | NEW (setup.py deps, MCPs, scripts, assets inventory) |

## Decisions and Uncertainties

### IQTS Templates
The 3 IQTS tool files (Evidence Log, Investigation Plan, Note to File) are from the UNESCO SBI methodology. Their content is mostly operational templates. I folded the concepts into evidence.md (chain of custody, evidence logging) but the actual template tables were not reproduced — those should live in templates/working/ which already has IQTS template files. The IQTS tool files are preserved in _archive if the templates need updating.

### Genealogy Content
The genealogy files (research-strategies, research-plan-guidance, evidence-evaluation, gps-guidelines, citation-templates) contained genuinely useful frameworks that map well to investigation:
- FAN Principle → directly used in faf-research.md
- GPS 5-element standard → adapted in evidence.md
- Source/Information/Evidence classification → adapted in evidence.md
- Citation format → simplified in evidence.md

The genealogy-specific language (ancestors, census records, family trees) was stripped. The methodological frameworks were preserved.

### sherlock-removed-sites.md
1,997 lines of site data. Too large to include anywhere meaningful. Referenced in tooling.md as existing in _archive. If Sherlock gives unreliable results on a platform, check that file.

### Files I'm Not Sure About
- **extraction-guide.md** — this is the PSSP cognitive surrogate profile extraction guide. I took the investigation-adapted extraction table and evidence tiers into entity-research.md. The full 16-section extraction detail (which is massive) was not reproduced because it belongs more with the Thinking Toolkit / diagnose_entity tool documentation. Ethan should confirm this is the right call.
- **research_process.md / research_subprocess.md** — these are generic agentic research system prompts from a Deep Research-style tool. I extracted only the OODA loop concept and the research budget concept into methodology.md. Everything else was too generic. Ethan may want to keep them for the research-groundwork skill rather than this project.
- **ai-research-handbook-blueprint.md** — I used the 4-tier structure and 8-part decision framework as inspiration for methodology.md's approach types table. The full 450-line document was not reproduced. The structural principles are embedded in how methodology.md is written rather than being explicitly cited.

### What Templates Should Be Created (Future)
Based on what the references now support, these domain templates should exist:
entity, gang, family, friend, location/territory, incident/event, music/media, timeline, psychology, socio-economics, cultural-background, historical-context

Each should be a lightweight card: name/subject, 4-5 research questions, which tools to run, output format.

---

## Open Questions (to discuss next session)

1. **extraction-guide.md** — RESOLVED: The PSSP is handled entirely via the diagnose_entity MCP tool. We just fill the profile and submit it. entity-research.md only needs to know what profile sections exist and what evidence is accessible for investigation subjects (so we know what to feed the MCP). The full extraction logic lives in the tool, not in our docs.

2. **research_process.md / research_subprocess.md** — only took OODA and budget concepts. Should these stay in _archive for reference by the research-groundwork skill, or are they done?

3. **ai-research-handbook-blueprint.md** — the 4-tier/8-part CLES framework is embedded in methodology.md structurally but not explicitly cited. Is that enough or do we want it more visible?

4. **The plan file needs rewriting** — it still has state machine language from the earlier drafts. Should be stripped back to match what we actually agreed: folders are organised knowledge, methodology.md is a structured guide, no formal transitions, no routing, investigation is conversational.

5. **SKILL.md itself** — needs to lean harder into Claude as an actual investigative journalist. Always questioning, always suspicious. Not just a research helper. This is a separate task but worth scoping.

6. **diagnose_entity integration** — how does entity-research.md's PSSP mapping connect to the new Thinking Toolkit diagnose_entity tool in practice? The tooling.md references it but the workflow between them needs thinking through.
