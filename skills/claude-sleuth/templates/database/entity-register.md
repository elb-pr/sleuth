# Entity Register

## Administrative Metadata

| Field | Entry |
|---|---|
| Case ID | [...] |
| Register Version | [...] |
| Lead Analyst | [...] |
| Date Created (UTC) | [YYYY-MM-DDTHH:MM:SSZ] |
| Last Audit (UTC) | [...] |
| Classification | [...] |

---

## Section 1 — Master Entity Table

| Entity ID | POLE Type | Entity Sub-Type | Full Name / Label | Aliases | Key Identifiers | Country / Jurisdiction | Source Reference | Observation Date (UTC) | Analyst ID | Admiralty Grade | Confidence Level | Handling Code |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ENT-001 | Person | Subject / Witness / Associate | [...] | [...] | DOB, Passport #, Email | [...] | [...] | [...] | [...] | [...] | High / Moderate / Low | [...] |
| ENT-002 | Organisation | Corporate / NGO / Gov | [...] | [...] | Reg #, LEI, Domain | [...] | [...] | [...] | [...] | [...] | [...] | [...] |
| ENT-003 | Location | Residential / Commercial | [...] | [...] | Address, Coordinates | [...] | [...] | [...] | [...] | [...] | [...] | [...] |
| ENT-004 | Event | [...] | [...] | [...] | Date/Time, Location | [...] | [...] | [...] | [...] | [...] | [...] | [...] |

---

## Section 2 — Typed Link Register

| Link ID | Source Entity ID | Relationship Type | Target Entity ID | Date Range | Strength | Evidence Reference | Admiralty Grade |
|---|---|---|---|---|---|---|---|
| LNK-001 | [...] | ASSOCIATED_WITH / OWNS / EMPLOYS / DIRECTOR_OF / COMMUNICATES_WITH / FAMILY_OF | [...] | [...] | High / Moderate / Low | [...] | [...] |

---

## Section 3 — Entity Resolution Log

| Candidate A | Candidate B | Shared Identifiers | Resolution Decision | Rationale | Analyst | Date (UTC) |
|---|---|---|---|---|---|---|
| ENT-001 | [...] | [...] | Merge / Defer / Reject | [...] | [...] | [...] |

---

## Section 4 — Stale / Currency Review

| Entity ID | Last Verified (UTC) | Review Due (UTC) | Status | Action |
|---|---|---|---|---|
| ENT-001 | [...] | [...] | Current / Stale | Update / Flag / Remove |
