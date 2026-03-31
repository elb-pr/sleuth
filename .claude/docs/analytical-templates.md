# Analytical Infrastructure of Investigative Work: A Comprehensive Methodology Survey

**Research Conducted:** March 2026
**Scope:** Seven analytical infrastructure domains — Entity Databases, Case Tracking, Briefing Formats, Link Analysis, Timelines, Source Evaluation, Hypothesis Tracking
**Purpose:** Map standard formats, construction methodologies, quality frameworks, and professional standards to support construction of seven reusable analytical infrastructure prompt templates

***

## DOMAIN 1: Entity Databases & Structured Profiles

### Standards & Methodology

No single universal standard governs entity databases across investigative disciplines. The closest to a formal standard is **IBM i2 iBase**, which implements a typed entity-and-link schema architecture used by law enforcement, intelligence agencies, and corporate investigators worldwide. IBM's i2 Enterprise Insight Analysis Data Model White Paper (publicly available at `ibm.com/docs`) defines the schema architecture: entity types and link types each carry property types, semantic types, identifiers, and display names. Semantic types (such as `Person`, `Organisation`, `Location`, `Vehicle`) define how applications interpret entities categorically, while entity types are investigator-defined subcategories within those semantics (e.g., `Offender`, `Witness`, `Subscriber` all carry the `Person` semantic type). [ibm](https://www.ibm.com/docs/en/SSXVTH_4.3.3/com.ibm.i2.understand.data.doc/platform_datamodel_whitepaper_pdf.pdf)

The UK law enforcement and allied intelligence communities have converged on a data model based on **POLE** — **Person, Object, Location, Event** — as the four canonical entity categories for criminal intelligence databases. The POLE model underpins the Police National Computer, the HOLMES2 major incident management system, and related systems across England and Wales. POLE is not a published doctrinal document but a data architecture convention embedded in law enforcement systems and training. It is the closest thing to a formal standard for entity categorisation in operational law enforcement contexts. [i2group](https://i2group.com/articles/what-is-link-analysis-and-link-visualization)

For OSINT practitioners without access to i2 or enterprise platforms, **OSINT Combine** has published a collection schema (2023) grounded in **schema.org** vocabularies — the open community standard co-founded by Google, Microsoft, Yahoo, and Yandex — covering entity types: Person, Place, Organisation, Event, Action, and Product. The schema.org approach provides machine-readable, platform-compatible entity definitions with defined field vocabularies, offering a de facto interoperability standard for OSINT collection databases.  For Maltego users, entity types map to nodes in the graph environment, with standard entity types including `Person`, `Company`, `Email`, `Domain`, `IP Address`, `Phone`, `Website`, `Location`, and `Phrase` — each with defined properties and transform paths. [osintcombine](https://www.osintcombine.com/post/osint-collection-schema)

**Evidence Quality: MODERATE.** POLE and i2 schema architecture are established operational standards in law enforcement and intelligence. Schema.org-based OSINT schemas are emerging practitioner standards without institutional endorsement.

***

### Standard Structure & Components

#### Core Entity Types (across systems)

| Entity Type | Minimum Required Fields | Standard Optional Fields |
|---|---|---|
| **Person** | Full name, DOB, nationality, gender | Aliases, addresses (historical), employment, telephone numbers, email addresses, social media handles, physical description, identification documents |
| **Organisation** | Name, registration number, country, type | Registered address, trading addresses, directors, beneficial owners, parent/subsidiary relationships, incorporation date, dissolution date |
| **Location** | Address or coordinates, type (residential/commercial/other) | Grid reference, country, historical names, geospatial polygon |
| **Vehicle** | Registration plate, make, model, colour | VIN, owner(s), associated addresses, sighting history |
| **Account** | Account type (financial/social/email), identifier | Platform, owner reference, creation date, status |
| **Communication** | Channel type, from/to identifiers, timestamp | Content summary, duration (calls), metadata available |
| **Document** | Document type, title, date | Author, source, hash value, archive URL |
| **Event** | Event type, date/time, location reference | Participants, description, associated entities |

#### Universal Metadata Fields (all entity types)

All entity records across professional communities require:
- **Source attribution**: Which source(s) provided this record?
- **Date observed/collected**: When was this information current?
- **Confidence level**: How certain is the attribution between record and real-world entity?
- **Classification/handling**: Who may access this record?
- **Analyst identity**: Who created/last modified the record?
- **Last verified**: When was this information last confirmed as current?

 [i2group.github](https://i2group.github.io/analyze-connect/content/walkthrough/1-schema-design-guide.html)

***

### Construction Methodology

Entity databases are constructed iteratively throughout an investigation. The standard process begins with **schema design** — defining entity and link types appropriate to the investigation domain — before data entry begins. IBM's iBase Designer guidance explicitly warns against beginning data entry without a finalised schema, as retrospective schema changes are costly. The OSINT Combine schema approach mirrors this: define your entity types and their fields before collection begins, derived from your intelligence requirements. [youtube](https://www.youtube.com/watch?v=Oc0Ckt8v0rU&list=PL_MdWkeY52FH398nceJeJz4pCLEu7Av2D&index=9)

**Entity resolution** — the process of determining whether two records refer to the same real-world entity — is the central quality challenge in entity database management. No formal published standard governs entity resolution methodology in OSINT contexts. In practice, investigators apply informal confidence thresholds: records sharing two or more independently verified identifiers (e.g., name + DOB, or email + address) are merged with high confidence; single-identifier matches require corroboration before merging. IBM i2's Analyst's Notebook supports manual entity resolution through its entity matching functions; automated resolution requires additional tooling such as record linkage libraries or purpose-built deduplication platforms.

Relationships between entities are recorded as **typed links** with directional properties and qualifying metadata. i2 iBase's Designer guidance specifies that link types should be kept minimal and meaningful — over-creating link types is a documented failure mode. Standard link types in law enforcement contexts include: `ASSOCIATED_WITH`, `OWNS`, `EMPLOYS`, `COMMUNICATES_WITH`, `FAMILY_OF`, `DIRECTOR_OF`, `LOCATED_AT`, `PARTY_TO` (events), `WITNESSED_BY`. Each link should carry source attribution, date range, strength/confidence indicator, and analyst notes. [i2group.github](https://i2group.github.io/analyze-connect/content/walkthrough/1-schema-design-guide.html)

***

### Quality Criteria & Validation

Quality in entity databases is assessed across four dimensions: **completeness** (are all known entities recorded?), **accuracy** (do records correctly represent real-world entities?), **currency** (are records up to date?), and **integrity** (are entity resolutions correct and duplicate-free?). The UK College of Policing's intelligence management guidance emphasises that intelligence records must be sourced, graded, and reviewed regularly — stale records are an active liability in operational contexts.

Validation requires periodic **dead record review** (removing entities with no investigative relevance or outdated information), **duplicate audit** (systematic check for unresolved duplicates), and **source audit** (verifying that all records have source attribution). In major investigations using HOLMES2, dedicated indexers perform entity extraction and resolution as a specialised role distinct from the investigative team.

***

### Professional Community Variation

| Community | Approach | Schema Standard | Key Distinction |
|---|---|---|---|
| **Law enforcement (UK)** | POLE-based, system-embedded (HOLMES2, iBase) | POLE / i2 | Strict source attribution; legal admissibility requirements |
| **Intelligence community** | Classified ontologies; i2 iBase widely used | Classified + i2 | Entity types classified; handling controls mandatory |
| **Investigative journalism** | Spreadsheet-based, Maltego, Airtable | Informal / schema.org | Minimal schema; verification notes more important than field completeness |
| **Corporate/due diligence** | Proprietary CRM systems, Relativity, bespoke | Vendor-dependent | Regulatory compliance fields (PEP status, sanctions screening) |
| **OSINT practitioners** | Maltego, Hunchly, Obsidian, spreadsheets | Schema.org / informal | Collection-schema focus; transformation paths as relationship discovery |

The **OSINT/journalism approach** is most transferable to AI-assisted investigation because it is schema-explicit, uses open standards (schema.org), and does not depend on proprietary software. [docs.i2group](https://docs.i2group.com/anb/10.0.2/)

***

### Key Tools & Platforms

- **IBM i2 iBase** (`i2group.com`) — Purpose-built investigative relational database. Typed entity/link schema, integration with Analyst's Notebook. Strengths: mature, law enforcement standard. Limitations: expensive, Windows-only, requires schema design expertise. [docs.i2group](https://docs.i2group.com/ibase/10.0.0/designing_a_database.html)
- **IBM i2 Analyst's Notebook** (`i2group.com`) — Visual analysis front-end for iBase and other sources. Strengths: industry standard for link analysis. Limitations: cost, proprietary. [dataexpert](https://dataexpert.eu/products/analytics-link-analysis-visualisation-i2-group/i2-analysts-notebook)
- **Maltego** (`maltego.com`) — Graph-based OSINT platform with entity transforms. Strengths: automated data enrichment, broad integration. Limitations: subscription cost; graph not a structured database.
- **OCCRP Aleph** (`aleph.occrp.org`) — Open-source investigative data platform used by OCCRP journalists. Document and entity management with cross-referencing. Strengths: open source, journalism-grade, free tier. Limitations: requires hosting for full deployment.
- **OSINT Combine Schema** (`osintcombine.com`) — Schema.org-based entity templates for OSINT collection. Strengths: free, platform-agnostic, machine-readable. Limitations: manual; no database engine. [osintcombine](https://www.osintcombine.com/post/osint-collection-schema)
- **Neo4j** (`neo4j.com`) — Open-source graph database used by advanced practitioners for entity/relationship storage. Strengths: powerful querying (Cypher), open source. Limitations: requires technical setup.
- **Hunchly** (`hunch.ly`) — OSINT case management with automatic page capture. Entity tracking limited but source capture strong.
- **Obsidian / Notion** — Note-based knowledge management adapted by OSINT practitioners. Strengths: flexible, free. Limitations: no formal entity schema enforcement.

***

### Failure Modes & Mitigations

- **Duplicate entities**: Two records created for the same person under different name spellings. *Mitigation*: Entity resolution review at regular intervals; unique identifier fields made mandatory (e.g., date of birth, company registration number).
- **Stale records**: Information recorded as current that has since changed (addresses, phone numbers, relationships). *Mitigation*: Date-observed fields mandatory; periodic currency review scheduled.
- **Source conflation**: Multiple sources merged into a single attribution, obscuring which source supported which field. *Mitigation*: Source attribution at field level, not record level; never merge source citations.
- **False positive entity matching**: Two different real-world entities merged into one record due to shared identifiers. *Mitigation*: Require minimum two independent identifiers for confident resolution; flag uncertain resolutions.
- **Schema rigidity**: Pre-defined schema cannot accommodate entity types that emerge mid-investigation. *Mitigation*: Reserve a generic `Notes` field; plan schema with anticipated entity diversity; use semantic types to accommodate variation.
- **Over-collection**: Recording entities with no analytical relevance, degrading database usefulness. *Mitigation*: Collection driven by intelligence requirements; entities recorded only when linked to investigation focus.
- **No access control**: Sensitive entities accessible to all team members. *Mitigation*: Field-level and record-level classification; role-based access control in enterprise systems.

***

### Template Design Notes

- **Deliverable**: A structured entity register with typed records for all persons, organisations, locations, accounts, and events identified during the investigation, with source attribution, confidence levels, and relationship links.
- **Required inputs**: Investigation scope, seed entities, intelligence requirements, preferred schema standard (POLE/schema.org/custom).
- **Standards to enforce**: Entity type from POLE taxonomy; source attribution per field; confidence level per record; date observed; relationship typing.
- **Quality checks**: Duplicate audit; stale record flagging; source citation completeness; mandatory identifier fields.
- **Failure modes to prevent**: Unsourced entity creation; duplicate entities; entity records without dates.

***

### Key Sources

- IBM i2 Enterprise Insight Analysis Data Model White Paper: `ibm.com/docs/en/SSXVTH_4.3.3/com.ibm.i2.understand.data.doc/platform_datamodel_whitepaper_pdf.pdf` [ibm](https://www.ibm.com/docs/en/SSXVTH_4.3.3/com.ibm.i2.understand.data.doc/platform_datamodel_whitepaper_pdf.pdf)
- i2 Group documentation — Entities: `docs.i2group.com/anb/10.0.2/about_entities.html` [docs.i2group](https://docs.i2group.com/anb/10.0.2/about_entities.html)
- i2 iBase Designer Guide: `docs.i2group.com/ibase/10.0.0/designing_a_database.html` [docs.i2group](https://docs.i2group.com/ibase/10.0.0/designing_a_database.html)
- OSINT Combine Collection Schema: `osintcombine.com/post/osint-collection-schema` [osintcombine](https://www.osintcombine.com/post/osint-collection-schema)
- Schema.org entity vocabularies: `schema.org/Person`, `schema.org/Organization`, `schema.org/Event`
- i2 Group: What is Link Analysis: `i2group.com/articles/what-is-link-analysis-and-link-visualization` [i2group](https://i2group.com/articles/what-is-link-analysis-and-link-visualization)
- inet-investigation.com OSINT Report Building: `inet-investigation.com/osint/how-to-build-an-osint-report/` [inet-investigation](https://www.inet-investigation.com/osint/how-to-build-an-osint-report/)

***

## DOMAIN 2: Case Tracking & Investigation Management

### Standards & Methodology

The most comprehensive published standard for criminal investigation management in the UK is the **College of Policing Authorised Professional Practice (APP) for Investigation**, available at `college.police.uk/app/investigation`. APP is the mandatory guidance framework for police investigations in England and Wales, setting out standards for investigative strategy, reasonable lines of enquiry, evidence management, and case supervision. APP draws on the **Criminal Procedure and Investigations Act 1996 (CPIA) Code of Practice**, which requires investigators to: pursue all reasonable lines of enquiry whether pointing towards or away from a suspect; record and retain all material obtained; and maintain a disclosure schedule. [cps.gov](https://www.cps.gov.uk/prosecution-guidance/disclosure-manual-chapter-3-roles-and-responsibilities)

The **HOLMES2** (Home Office Large Major Enquiry System) platform operationalises major investigation management for serious and complex crimes in the UK, implementing structured case file management including: action logs, policy files, decision logs, message registers, document registers, and index of subjects/vehicles/locations. The **NPCC Major Crime Investigation Manual** (not fully public but referenced in College of Policing guidance) extends APP into serious crime investigation management. The College of Policing also maintains guidance on investigative strategies and decision-making through the **National Decision Model (NDM)**, which frames investigative decisions within a structured ethical framework. [college.police](https://www.college.police.uk/support-forces/practices/crime-management-framework)

For OSINT-specific case management, no equivalent institutional standard exists. The **Hunchly** platform provides a practitioner-level framework through its methodology documentation, centring on automatic URL capture, timestamped page archiving, and case note attachment. The **Berkeley Protocol on Digital Open Source Investigations** (OHCHR/UC Berkeley, 2022) provides the most comprehensive public framework for OSINT investigation management in human rights contexts, with guidance on documentation, chain of custody, team coordination, and evidence archival. It is not a universal standard but is the closest formal guidance available for non-law-enforcement OSINT case management.

**Evidence Quality: MODERATE.** Law enforcement case management is strongly standardised (APP, CPIA, HOLMES2). OSINT/journalism case management is primarily practitioner-driven with limited institutional standards.

***

### Standard Structure & Components

A complete investigation case file, synthesised across professional standards, contains:

**1. Case Summary Record**
- Case reference number, title, classification
- Investigation type and scope statement
- Lead investigator and team composition
- Date opened, current status, target completion
- Brief summary (one paragraph) of investigation purpose

**2. Investigation Plan / Strategy Document**
- Intelligence requirements (what questions must be answered?)
- Collection strategy (what sources will be used, in what sequence?)
- Priority lines of enquiry (ranked)
- Resource allocation and task assignments
- Ethical and legal parameters (proportionality, privacy considerations)
- Review and escalation triggers

**3. Task Log / Actions Register**
- Task number, description, assigned to, date assigned
- Priority level, deadline
- Status (open/in progress/complete/deferred)
- Outcome and findings (when complete)
- Date completed

**4. Decision Log (Policy File in UK policing)**
- Decision number, date/time
- Decision taken
- Rationale (why this decision, what alternatives were considered?)
- Decision-maker identity
- Information available at time of decision
- Review date

**5. Evidence / Material Register**
- Item reference, description, type
- Source (URL, database, contact, etc.)
- Date collected, collected by
- Storage location (file path, archive URL, hash)
- Admissibility/handling notes
- Confidence level

**6. Source Register**
- Source identifier, source type (open/human/technical)
- Source description
- Reliability rating (Admiralty letter)
- Date first used, last used
- Access method
- Handling restrictions

**7. Chronological Case Log / Running Log**
- Date/time of each investigation activity
- Activity description
- Investigator
- Outcome/finding

**8. Entity Index** (cross-reference to Entity Database)

**9. Interim and Final Reports** (cross-reference to Domain 3)

 [judiciary](https://www.judiciary.uk/wp-content/uploads/2022/01/2022-0017-Response-from-NPCC-and-College-of-Policing_Published-1.pdf)

***

### Construction Methodology

Investigation management begins before collection. The standard approach across professional communities is to produce a written **investigation plan** before active enquiries commence. In UK policing, APP requires that an initial investigation plan be completed by the officer in command by the end of day for priority offences. The plan defines scope, legal authority, intelligence requirements, and initial lines of enquiry. This plan is reviewed by a supervisor within 24–96 hours depending on crime category. [college.police](https://www.college.police.uk/support-forces/practices/crime-management-framework)

Task management is continuous throughout. Each enquiry is recorded as a discrete action/task, assigned, tracked, and closed with documented outcomes. In HOLMES2 major investigations, actions are managed by an Incident Room Manager and tracked through a formal action board. In smaller investigations, equivalent discipline is achieved through structured spreadsheets or tools such as Notion, Trello, or Hunchly. The critical principle is that **every task generates a recorded outcome**, not merely a status update — even negative enquiries (nothing found) must be documented to demonstrate reasonable lines of enquiry were pursued.

The **decision log** is the audit trail for investigative judgment. UK College of Policing guidance and the NPCC Major Crime Investigation Manual both emphasise that decisions should be recorded contemporaneously with the reasoning behind them, not retrospectively. This requirement serves both quality control (reviewers can assess decision-making quality) and legal protection (prosecutors can demonstrate the investigation was conducted fairly). In journalism, equivalent documentation is the **editorial decision log** — recording why a story was published, what was verified, what claims were not included and why. [judiciary](https://www.judiciary.uk/wp-content/uploads/2022/01/2022-0017-Response-from-NPCC-and-College-of-Policing_Published-1.pdf)

***

### Quality Criteria & Validation

Quality assurance in investigation management involves structured review at three levels: **task-level review** (each task outcome reviewed by a supervisor before closure), **investigation-level review** (periodic strategic review of investigation plan against actual progress), and **case-level review** (independent review of the completed investigation file, typically before prosecution or publication). In UK policing, APP mandates inspector review every 30 days, chief inspector every 90 days, superintendent every 120 days for active investigations. [college.police](https://www.college.police.uk/support-forces/practices/crime-management-framework)

Digital evidence quality requires four additional standards: **URL archiving** (all web pages captured with archival timestamp, e.g., via archive.org or Hunchly); **hash verification** (cryptographic hash of digital files at time of collection); **screenshot methodology** (full-page screenshots with visible URL and timestamp); and **metadata preservation** (EXIF data preserved on image files). The CPIA Code of Practice requires that all retained material be scheduled and identified in a way that facilitates disclosure to the defence in criminal proceedings. [onlinelibrary.wiley](https://onlinelibrary.wiley.com/doi/10.1111/1556-4029.15655)

***

### Professional Community Variation

| Community | Framework | Key Document | Audit Requirement |
|---|---|---|---|
| **UK law enforcement** | APP + CPIA Code of Practice | Policy file, action log, MG forms | CPIA disclosure schedule; IPCC-auditable |
| **US law enforcement** | FBI case management policy (not public), ACFE guidelines | Case file, chain of custody | Federal Rules of Evidence compliance |
| **Intelligence community** | Classified; general: tasking and collection management | RFI logs, collection plans, reports registry | Internal QA; no external audit |
| **Investigative journalism** | GIJN/Bellingcat best practice; no formal standard | Story development log, editorial decisions, verification notes | Editorial review; legal review before publication |
| **Corporate due diligence** | ACFE investigation standards; ISO 37001 guidance | Investigation brief, findings log, legal hold notices | Client reporting; regulatory compliance |
| **Academic OSINT** | IRB/Ethics committee protocols | Data management plan, consent records | Ethics board review |

The **journalism approach** (structured verification logs, editorial decision documentation, pre-publication legal review) is most transferable to AI-assisted OSINT because it is domain-agnostic, privacy-aware, and does not require proprietary systems.

***

### Key Tools & Platforms

- **HOLMES2** (UK police, gov-access only) — Major incident case management. Standard for UK serious crime. Not publicly available.
- **Hunchly** (`hunch.ly`) — OSINT case management with automatic URL capture, case notes, evidence export. Strengths: purpose-built for OSINT, automatic archiving. Limitations: single-user focus.
- **CaseFile** (`casefile.com`) — Mind-mapping/case management tool used by some investigators. Strengths: visual. Limitations: limited structured case management features.
- **Notion** — General project management adapted for case tracking. Strengths: flexible databases, templates, free tier. Limitations: no OSINT-specific features; security considerations for sensitive investigations.
- **Airtable** — Structured database approach to case management. Strengths: relational fields, customisable views. Limitations: data residency concerns.
- **Custom spreadsheets (Google Sheets / Excel)** — Widespread across journalism and corporate. Strengths: universal, free, adaptable. Limitations: no audit trail, version control issues.
- **OCCRP Aleph** (`aleph.occrp.org`) — Document-centred investigation management for journalism. Strengths: entity cross-referencing, open source. Limitations: requires deployment.

***

### Failure Modes & Mitigations

- **Scope creep**: Investigation expands beyond original intelligence requirements, wasting resources and degrading focus. *Mitigation*: Explicit scope statement in investigation plan; scope changes require documented decision and re-prioritisation.
- **Lost evidence chains**: Digital evidence collected without archiving; URLs go dead; screenshots lack timestamps. *Mitigation*: Archive-on-capture policy (Hunchly/Wayback Machine); hash all evidence files at time of collection.
- **Undocumented decisions**: Investigative decisions made verbally or informally, not recorded. *Mitigation*: Decision log maintained throughout; rule that no operational decision is valid until recorded.
- **Duplicate effort across teams**: Multiple investigators unknowingly pursuing the same enquiry. *Mitigation*: Centralised task log with assignment visibility; daily brief in multi-person investigations.
- **Premature closure**: Investigation closed before all reasonable lines of enquiry are exhausted. *Mitigation*: Closure criteria defined in investigation plan; independent review before closure.
- **Task outcomes not recorded**: Tasks marked complete without documenting what was found (including negative results). *Mitigation*: Task log requires outcome field; negative results explicitly recorded.

***

### Template Design Notes

- **Deliverable**: A complete investigation management file including case summary, investigation plan, task log, decision log, evidence register, and source register.
- **Required inputs**: Case reference, investigation question, scope boundaries, team composition, legal/ethical parameters, evidence collected to date.
- **Standards to enforce**: College of Policing APP structure; CPIA-aligned evidence management; decision log with rationale; all evidence hash-verified and archived.
- **Quality checks**: Review schedule compliance; task log completeness; evidence archive integrity; decision log currency.
- **Failure modes to prevent**: Undocumented decisions; evidence without chain of custody; tasks without outcomes.

***

### Key Sources

- UK College of Policing APP — Investigation: `college.police.uk/app/investigation` [college.police](https://www.college.police.uk/app/investigation)
- College of Policing Crime Management Framework: `college.police.uk/support-forces/practices/crime-management-framework` [college.police](https://www.college.police.uk/support-forces/practices/crime-management-framework)
- CPS Disclosure Manual Chapter 3: `cps.gov.uk/prosecution-guidance/disclosure-manual-chapter-3-roles-and-responsibilities` [cps.gov](https://www.cps.gov.uk/prosecution-guidance/disclosure-manual-chapter-3-roles-and-responsibilities)
- NPCC/College of Policing Major Crime Investigation Manual guidance: `judiciary.uk/wp-content/uploads/2022/01/2022-0017-Response-from-NPCC-and-College-of-Policing_Published-1.pdf` [judiciary](https://www.judiciary.uk/wp-content/uploads/2022/01/2022-0017-Response-from-NPCC-and-College-of-Policing_Published-1.pdf)
- GAMEPLANS digital evidence strategy framework: `onlinelibrary.wiley.com/doi/10.1111/1556-4029.15655` [onlinelibrary.wiley](https://onlinelibrary.wiley.com/doi/10.1111/1556-4029.15655)
- inet-investigation.com OSINT Report Building: `inet-investigation.com/osint/how-to-build-an-osint-report/` [inet-investigation](https://www.inet-investigation.com/osint/how-to-build-an-osint-report/)

***

## DOMAIN 3: Briefing & Reporting Formats

### Standards & Methodology

The most authoritative published standard for intelligence analytical reporting is **Intelligence Community Directive 203 (ICD 203): Analytic Standards**, issued by the Office of the Director of National Intelligence (ODNI), effective 2 January 2015, technically amended 21 January 2022. ICD 203 governs the production and evaluation of all IC analytic products and is publicly available at `dni.gov/files/documents/ICD/ICD-203.pdf`. ICD 203 articulates five Analytic Standards: **Objective** (free from assumptions and bias); **Independent of political consideration**; **Timely**; **Based on all available sources**; and **Implements and exhibits nine Analytic Tradecraft Standards**. [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

The nine Analytic Tradecraft Standards under ICD 203 are: (1) properly describe quality and credibility of underlying sources; (2) properly express and explain uncertainties; (3) properly distinguish between underlying intelligence and analysts' assumptions and judgments; (4) incorporate analysis of alternatives; (5) demonstrate customer relevance; (6) use clear and logical argumentation; (7) explain change to or consistency of analytic judgments; (8) make accurate judgments and assessments; (9) incorporate effective visual information where appropriate. These nine standards function as the quality checklist for every IC analytic product. [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

Complementary to ICD 203 is **ICD 206: Sourcing Requirements for Disseminated Analytic Products**, which governs how sources are described in analytic products, including source summary statements providing holistic assessments of the source base. Together, ICD 203 and ICD 206 constitute the primary documentary standard for intelligence community reporting. The UK equivalent is the **Joint Intelligence Committee (JIC)** standardised assessment format, including the use of the UK probability language framework (described under Domain 6 below). The JIC format is not publicly published in detail, but its probability language is partially documented in academic intelligence studies literature. [bmbs](https://www.bmbs.org/salamanca/readings/ODNI_ICDs_203-206-208.pdf)

For law enforcement analytical products, the **UK College of Policing** publishes analytical product guidance under APP, distinguishing between strategic assessments, tactical assessments, target profiles, problem profiles, and subject profiles — each with defined purpose, structure, and review cycle under the **National Intelligence Model (NIM)**. The NIM was introduced in England and Wales in 2004 following the National Criminal Intelligence Service model, and was examined in peer-reviewed literature as the foundational framework for crime analysis integration into policing. [tandfonline](https://www.tandfonline.com/doi/pdf/10.1080/10439463.2016.1262364?needAccess=true)

**Evidence Quality: STRONG** for intelligence community (ICD 203 is formal doctrine). **MODERATE** for law enforcement (NIM/APP-embedded) and journalism (practitioner-driven, no formal standard).

***

### Standard Structure & Components

#### Intelligence Community Standard Brief (BLUF Format, per ICD 203 conventions)

```
[CLASSIFICATION LINE]
[PRODUCT TITLE]
[DATE / DISSEMINATION CONTROL]

BOTTOM LINE UP FRONT (BLUF)
  [1–3 sentences: main analytic judgment, confidence level, key implication]

KEY JUDGMENTS
  [Numbered list of principal findings, each with:
   - Likelihood expression (per ICD 203 probability scale)
   - Confidence level (High / Moderate / Low)
   - Basis distinction: intelligence vs. assumption vs. judgment]

SUPPORTING ANALYSIS
  [Structured exposition supporting each key judgment]
  [Source descriptions per ICD 206]
  [Alternative hypotheses addressed]

INFORMATION GAPS
  [Named gaps affecting confidence; indicators that would alter judgments]

SOURCE SUMMARY STATEMENT
  [Holistic assessment of source base quality per ICD 206]

[CLASSIFICATION LINE]
```



#### Law Enforcement Analytical Product (NIM Framework, UK College of Policing)

The NIM defines five core analytical product types:
1. **Strategic Assessment** — Longer-term intelligence picture; informs force-level strategy
2. **Tactical Assessment** — Current-period threats and opportunities; drives operational tasking
3. **Target Profile** — Intelligence picture on a specific subject of interest
4. **Problem Profile** — Intelligence picture on a crime series, problem, or issue
5. **Subject Profile** — Detailed profile of an individual or organisation

Each follows a common structure: executive summary, key findings, supporting evidence, confidence assessment, gaps, recommendations, appendices. [tandfonline](https://www.tandfonline.com/doi/pdf/10.1080/10439463.2016.1262364?needAccess=true)

#### OSINT/Journalism Format (practitioner standard, per inet-investigation.com)

Four standard formats identified by OSINT practitioners: [inet-investigation](https://www.inet-investigation.com/osint/how-to-build-an-osint-report/)
1. **Subject Profile** — Identity, address history, employment, public record, adverse findings, online presence
2. **Timeline** — Chronological findings with source and confidence per entry
3. **Findings Memo** — Confirmed findings / corroborated findings / unverified leads / negative results / scope limitations / conclusions and assessment / source index
4. **Adverse Findings Summary** — Risk-focused output for due diligence contexts

***

### Construction Methodology

Analytical reports are assembled from the working documents that precede them — entity databases, timelines, link charts, and hypothesis trackers feed the report. The BLUF structure mandates that the main analytical message appears first, not buried at the end as in academic writing. This is not a stylistic preference but a functional standard: intelligence consumers are senior decision-makers reading under time pressure, for whom narrative build-up is a liability. ICD 203 Tradecraft Standard 6 states explicitly: "Analytic products should present a clear main analytic message up front." [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

Confidence expression in IC products must follow ICD 203's probability language precisely. Likelihood of events is expressed using one of two standardised scales (row-consistent terms required): `almost certainly` / `very likely` / `likely` / `roughly even chance` / `unlikely` / `very unlikely` / `remote`. Probability percentages map to these terms (55–80% = `likely`; 80–95% = `very likely`; 95–99% = `almost certainly`). Confidence levels (`High`, `Moderate`, `Low`) are distinct from likelihood expressions and must not appear in the same sentence as a likelihood expression to avoid confusion. This distinction — between *probability of an event* (likelihood) and *quality of the evidence base* (confidence) — is one of the most frequently violated standards in analytical writing. [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

***

### Quality Criteria & Validation

ICD 203 requires IC elements to maintain formal product evaluation programmes using the nine Tradecraft Standards as assessment criteria, with annual status reporting to the Deputy Director for Mission Integration. Each IC element designates a reviewer responsible for checking products against the standards before dissemination. The ODNI Analytic Ombuds serves as an independent oversight role for objectivity concerns. This constitutes the most formalised quality assurance system for analytical reporting in any professional community. [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

For non-IC contexts, quality criteria from OSINT practitioners converge on: separation of findings from conclusions (clearly labelled); negative results documented alongside positive findings; confidence level assigned to every finding; scope limitations stated; source index complete. The most common quality failure identified in practitioner literature is conflating confirmed findings with analytical conclusions — mixing what was found with what it means — without clear labelling. [inet-investigation](https://www.inet-investigation.com/osint/how-to-build-an-osint-report/)

***

### Professional Community Variation

| Community | Primary Standard | Report Format | Key Distinguishing Feature |
|---|---|---|---|
| **US Intelligence Community** | ICD 203 / ICD 206 | BLUF brief; National Intelligence Estimate; finished intelligence products | Mandatory confidence levels; formal source summary statement; political independence requirement |
| **UK Intelligence Community** | JIC assessment format; JDP 2-00 | JIC Assessment structure | UK probability language; JIC-coordinated assessment process |
| **UK Law Enforcement** | NIM / College of Policing APP | Five NIM product types | Tied to intelligence cycle and tactical/strategic tasking |
| **Investigative Journalism** | No formal standard; GIJN/Bellingcat practice | Story-led narrative with sourcing transparency | Verification-first; public interest justification; publication-ready |
| **Corporate Due Diligence** | ACFE; no universal standard | Executive summary + findings + recommendations | Risk-rating focus; regulatory compliance language; client-actionable |
| **Academic Intelligence Studies** | Peer review conventions | Case study / analytical article | Methodology transparency; reproducibility; literature review |

The **IC format (ICD 203)** is most transferable to AI-assisted investigation because its standards are explicit, enumerated, and structured — making them directly encodable in prompt instructions. [intelligence](https://www.intelligence.gov/mission/our-values/objectivity)

***

### Failure Modes & Mitigations

- **Confidence inflation**: Findings presented with higher certainty than the evidence supports. *Mitigation*: Mandatory confidence level per finding; ICD 203 probability language enforced.
- **Buried caveats**: Limitations and gaps mentioned only in footnotes or appendices. *Mitigation*: Information gaps section required at main body level, not in appendix.
- **Unsourced claims**: Findings presented without citation of the source(s) that generated them. *Mitigation*: Source citation mandatory per finding; source index as appendix.
- **Findings-conclusion conflation**: What was found presented as if it were what it means. *Mitigation*: Separate labelled sections for Findings and Assessment/Conclusions.
- **Narrative bias**: Report constructed to support a conclusion already reached. *Mitigation*: Competing hypotheses section required; alternative explanations for findings documented.
- **Information overload**: Report provides too much raw material without synthesis. *Mitigation*: Executive summary / BLUF required; report length disciplined to audience need.
- **Actionability gap**: Report provides findings but no clear implication for decisions. *Mitigation*: ICD 203 Tradecraft Standard 5: demonstrate customer relevance and address implications.

***

### Template Design Notes

- **Deliverable**: A structured analytical report following ICD 203 conventions — BLUF, key judgments with confidence/likelihood, supporting analysis, gaps, source summary.
- **Required inputs**: Investigation findings, entity list, timeline, hypothesis assessment, source register, intended audience.
- **Standards to enforce**: ICD 203 nine Tradecraft Standards; probability language from ICD 203 scale; confidence levels distinct from likelihood; findings/conclusions separated.
- **Quality checks**: Tradecraft Standard compliance check (all nine); source index completeness; negative results documented; gaps section present.
- **Failure modes to prevent**: Confidence inflation; unsourced claims; missing gaps section; findings-conclusion conflation.

***

### Key Sources

- ODNI ICD 203: `dni.gov/files/documents/ICD/ICD-203.pdf` [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
- ICD 203/206/208 combined: `bmbs.org/salamanca/readings/ODNI_ICDs_203-206-208.pdf` [bmbs](https://www.bmbs.org/salamanca/readings/ODNI_ICDs_203-206-208.pdf)
- Intelligence.gov on ICD 203: `intelligence.gov/mission/our-values/objectivity` [intelligence](https://www.intelligence.gov/mission/our-values/objectivity)
- inet-investigation.com OSINT Report Building: `inet-investigation.com/osint/how-to-build-an-osint-report/` [inet-investigation](https://www.inet-investigation.com/osint/how-to-build-an-osint-report/)
- UK College of Policing APP Investigation: `college.police.uk/app/investigation` [college.police](https://www.college.police.uk/app/investigation)

***

## DOMAIN 4: Link Analysis & Network Visualisation

### Standards & Methodology

Link analysis in investigative contexts has no single published doctrinal standard equivalent to ICD 203 or the CPIA Code of Practice. The dominant methodology is **embedded in tool ecosystems** — principally IBM i2 Analyst's Notebook — rather than published as freestanding doctrine. IBM's i2 Group publishes methodology articles on link analysis, defining it as examining and visualising relationships between entities categorised as **People, Objects, Locations, and Events (POLE)**, with applications in clustering, pathway discovery, social network analysis (SNA), and temporal analysis. [i2group](https://i2group.com/articles/what-is-link-analysis-and-link-visualization)

The **IALEIA (International Association of Law Enforcement Intelligence Analysts)** publishes guidance on analytical products including link charts, but its detailed methodology standards are available to members. IALEIA defines link analysis as a core law enforcement analytical product type. The UK College of Policing's APP includes link charts as an analytical product within the NIM framework. No publicly available doctrinal text precisely specifies the visual grammar of law enforcement link charts with the same authority as, say, ICD 203 specifies confidence language.

Social network analysis (SNA) methodology from academic literature provides a more rigorous analytical framework. The standard academic references are **Wasserman and Faust's *Social Network Analysis: Methods and Applications*** (1994, Cambridge University Press) and **Borgatti, Everett, and Johnson's *Analyzing Social Networks*** (SAGE, 2013). These texts define centrality measures (degree, betweenness, closeness, eigenvector centrality), clustering algorithms, bridge identification, and community detection — the analytical vocabulary used in investigative network analysis. For law enforcement and intelligence practitioners, these concepts are applied operationally through Analyst's Notebook's SNA functions and Gephi's analytical modules.

**Evidence Quality: MODERATE.** Tool documentation and academic SNA methodology are well-developed. Formal law enforcement/IC doctrinal standards for link chart construction methodology are limited in publicly available form.

***

### Standard Structure & Components

#### Visual Grammar of Investigative Link Charts (synthesised from i2 Analyst's Notebook conventions and IALEIA practitioner standards)

**Node types (entity representations):**
- Each entity type is represented by a distinct shape and/or colour
- Standard shapes: rectangle (person), oval/circle (organisation), diamond (event), triangle (location), parallelogram (vehicle/object), hexagon (account/document)
- Colour coding: typically user-defined per schema but should be consistent throughout a chart and include a legend

**Link types (relationship representations):**
- Directed links: arrow indicates direction of relationship (A → B = "A directs B")
- Undirected links: line without arrowhead (mutual or unspecified relationship)
- Line style: solid (confirmed relationship), dashed (probable/unconfirmed), dotted (suspected/low confidence)
- Line weight: heavier lines indicate stronger/higher-frequency relationships
- Link labels: relationship type (e.g., `EMPLOYS`, `COMMUNICATES_WITH`), date range, confidence grade

**Metadata on nodes and links:**
- Source attribution (which source established this entity/relationship?)
- Date range (when was this relationship active?)
- Confidence indicator (Admiralty credibility rating or equivalent)
- Analyst notes

**Chart-level documentation:**
- Title, analyst name, date created/modified
- Classification
- Legend (all entity types, link types, confidence indicators)
- Data sources listed
- Method notes (how was the chart constructed? What data fed it?)

 [thesignaturebrand.co](https://thesignaturebrand.co.uk/training/analyst-training/i2-analysts-notebook-training/)

***

### Construction Methodology

Link chart construction follows a defined sequence. First, entity extraction from the source material (case notes, communications data, financial records, OSINT collection) — each entity recorded in the entity database before being represented on the chart. Second, relationship identification from source material — each relationship typed, sourced, and dated. Third, initial chart layout using automatic layout algorithms (hierarchical, circular, force-directed) to expose network structure, followed by manual adjustment for analytical clarity. Fourth, analytical operations: centrality analysis to identify key nodes (high betweenness centrality = bridge/gatekeeper), clustering analysis to identify sub-groups, pathway analysis to find non-obvious connections between entities. Fifth, annotation with confidence indicators and source labels.

The **POLE model** drives entity extraction: for every document or communication reviewed, analysts ask: what People, Objects, Locations, and Events does this reference? This structured extraction approach ensures completeness across entity types. In Analyst's Notebook, entity records can be fed from iBase (the database back-end) ensuring that every node on the chart has a corresponding database record with full source attribution. [dataexpert](https://dataexpert.eu/products/analytics-link-analysis-visualisation-i2-group/i2-analysts-notebook)

***

### Quality Criteria & Validation

Quality in link charts is assessed against: **source attribution** (every link has a named source); **confidence grading** (every link has an Admiralty or equivalent credibility rating); **completeness** (are all known entities and relationships represented?); **accuracy** (do links correctly represent the relationships evidenced in source material?); and **interpretive rigour** (are analytical conclusions drawn from network structure — centrality, clustering — supported by the underlying data?).

The primary quality problem is the **hairball** — charts that become so dense with nodes and links that no analytical insight is possible. Quality practice requires segmenting complex networks into sub-charts by entity cluster, time period, or relationship type, and using graduated visual encoding (weight, colour intensity) to expose the most analytically significant relationships without eliminating the full dataset.

***

### Professional Community Variation

| Community | Approach | Primary Tool | Key Standard |
|---|---|---|---|
| **Law enforcement** | POLE-based; operational focus; evidential annotation | i2 Analyst's Notebook, HOLMES2 | Source + confidence on every link; admissibility |
| **Intelligence community** | Similar to law enforcement; classified schemas | i2 Analyst's Notebook, Palantir Gotham | Classified; handling controls on charts |
| **Investigative journalism** | Less formal; relationship-mapping for story structure | Maltego, OCCRP Aleph vis, draw.io | Verification-focused; publication-ready |
| **Corporate investigation** | Financial flow focus; boardroom-presentable | i2 Analyst's Notebook, Maltego, PowerPoint | Executive-readable; risk-rated |
| **Academic SNA** | Rigorous centrality metrics; algorithmic methods | Gephi, NodeXL, R (igraph), Python (NetworkX) | Reproducibility; statistical method documentation |

***

### Key Tools & Platforms

- **IBM i2 Analyst's Notebook** (`i2group.com`) — Industry standard for law enforcement/IC link analysis. Strengths: entity-link charting, temporal views, SNA metrics, iBase integration. Limitations: cost, proprietary.
- **Maltego** (`maltego.com`) — OSINT-focused graph analysis. Strengths: automated transforms for entity enrichment. Limitations: not primarily a charting tool; graph becomes complex quickly.
- **Gephi** (`gephi.org`) — Open-source SNA platform. Strengths: free, powerful centrality/community algorithms. Limitations: no investigative-specific features; requires data preparation.
- **NodeXL** (`nodexl.codeplex.com`) — Excel-based SNA for social media networks. Strengths: accessible. Limitations: limited to social media; older platform.
- **OCCRP Aleph / vis.occrp.org** — Open-source investigative visualisation. Strengths: free, journalism-oriented. Limitations: limited analytical functions.
- **yEd Graph Editor** (`yworks.com/products/yed`) — Free diagramming with automatic layouts. Strengths: free, flexible. Limitations: no investigative-specific features.
- **Palantir Gotham** (`palantir.com`) — Enterprise-grade intelligence analysis. Strengths: powerful ontology. Limitations: government/enterprise only; very high cost.

***

### Failure Modes & Mitigations

- **Hairball problem**: Network too dense to extract analytical insight. *Mitigation*: Segment by sub-group, time period, relationship type; use link weight and colour to encode significance; produce multiple focused sub-charts from one master network.
- **False positive links**: Relationships included without adequate evidential basis. *Mitigation*: Every link must have source attribution and confidence rating; links below minimum confidence excluded from operational charts.
- **Temporal conflation**: Relationships from different time periods shown as simultaneous. *Mitigation*: Date ranges on all links; temporal chart view for time-sensitive networks.
- **Missing nodes**: Key entities not in the chart because they weren't in the analyst's data sources. *Mitigation*: Structured POLE extraction; gap analysis as explicit chart review step.
- **Treating association as causation**: Co-occurrence on a chart interpreted as implying direction or causation. *Mitigation*: Analytical notes distinguish between `associated with` and directional relationship types; interpretive text required alongside chart.
- **No legend**: Chart unintelligible to any analyst other than the creator. *Mitigation*: Legend mandatory on every exported chart; all entity types, link types, confidence indicators defined.

***

### Template Design Notes

- **Deliverable**: An annotated link chart with entity-type legend, relationship legend, confidence indicators, source attribution, and accompanying analytical narrative interpreting network structure (centrality, clusters, key nodes, gaps).
- **Required inputs**: Entity register, relationship evidence, date ranges, source attributions, confidence ratings, analytical questions to be answered.
- **Standards to enforce**: POLE entity typing; source/confidence on every link; temporal dating; legend on every chart.
- **Quality checks**: No unsourced links; hairball prevention (max nodes for main chart?); legend present; accompanying analytical narrative.
- **Failure modes to prevent**: Undated links; unsourced links; missing legend; association-causation conflation in narrative.

***

### Key Sources

- i2 Group: What is Link Analysis: `i2group.com/articles/what-is-link-analysis-and-link-visualization` [i2group](https://i2group.com/articles/what-is-link-analysis-and-link-visualization)
- i2 Analyst's Notebook Documentation: `docs.i2group.com/anb/10.0.2/` [docs.i2group](https://docs.i2group.com/anb/10.0.2/)
- i2 Analyst's Notebook Training (Signature Brand): `thesignaturebrand.co.uk/training/analyst-training/i2-analysts-notebook-training/` [thesignaturebrand.co](https://thesignaturebrand.co.uk/training/analyst-training/i2-analysts-notebook-training/)
- DataExpert i2 Analyst's Notebook: `dataexpert.eu/products/analytics-link-analysis-visualisation-i2-group/i2-analysts-notebook` [dataexpert](https://dataexpert.eu/products/analytics-link-analysis-visualisation-i2-group/i2-analysts-notebook)
- OSINT Combine Collection Schema (Venn diagram/relationship model): `osintcombine.com/post/osint-collection-schema` [osintcombine](https://www.osintcombine.com/post/osint-collection-schema)

***

## DOMAIN 5: Timeline Construction & Chronological Analysis

### Standards & Methodology

No single doctrinal standard governs investigative timeline construction across professional communities. Timeline methodology is documented in three distinct traditions that converge on similar practice without referencing each other: **digital forensics timeline analysis**, **criminal investigation chronology construction**, and **historical/archival methodology**.

In **digital forensics**, the SoK (Systematisation of Knowledge) paper "Timeline based event reconstruction for digital forensics" (ScienceDirect, 2025) surveys timeline analysis methodology, identifying data collection, event normalisation, ordering and correlation, and visualisation as the standard construction sequence. Digital forensics timelines require event normalisation (standardising data formats across log sources) and timezone management as specific technical disciplines not required in other timeline types. [sciencedirect](https://www.sciencedirect.com/science/article/pii/S266628172500071X)

In **criminal investigation**, the UK College of Policing's Major Crime Investigation Manual and equivalent guidance reference several timeline types: **Narrative Chronology** (prose account of events in date order); **Tabular Timeline** (table with events, dates, sources, confidence levels); and **Time-Person Grid** (matrix showing what each individual was doing at defined time intervals). These are described as analytical techniques for root cause analysis and major incident investigation rather than prescribed templates with mandatory fields. [unaettie](https://unaettie.com/en-us/aq/rca_timeline.php)

For OSINT-specific timelines, practitioner methodology documented at `inet-investigation.com` identifies the timeline as one of four standard OSINT report formats and specifies that every entry must carry a source and confidence level — medium/low confidence entries should be visually distinct from high-confidence entries. [inet-investigation](https://www.inet-investigation.com/osint/how-to-build-an-osint-report/)

The ACFE's *Fraud Examination Manual* treats timeline construction as a core investigative technique for financial fraud, with emphasis on transaction sequencing and the evidentiary significance of timing gaps between related events — the technique of identifying what *should* have happened between two confirmed events and investigating the gap.

**Evidence Quality: MODERATE.** Digital forensics methodology is formally documented. Criminal investigation timeline practice is documented in operational guidance. OSINT timeline methodology is practitioner-level without institutional standards.

***

### Standard Structure & Components

#### Standard Investigative Timeline Entry (synthesised across communities)

| Field | Description | Required? |
|---|---|---|
| **Date/Time** | As precise as evidence allows; date range if uncertain | Mandatory |
| **Timezone** | UTC + local conversion documented | Mandatory for multi-jurisdiction |
| **Event Description** | Factual description of the event; no analytical interpretation | Mandatory |
| **Event Type** | Category (financial transaction / communication / movement / document creation / etc.) | Recommended |
| **Entity References** | Which entities (from entity database) are involved? | Mandatory |
| **Source Reference** | Which source(s) document this event? | Mandatory |
| **Source Confidence** | Admiralty 1–6 rating of information credibility | Mandatory |
| **Evidence Reference** | Link to supporting document/screenshot/evidence item | Recommended |
| **Temporal Certainty** | Exact / approximate / estimated / conflicting (with explanation) | Mandatory |
| **Analyst Notes** | Analytical observations about the event's significance | Optional |
| **Status** | Confirmed / Corroborated / Unverified / Disputed | Recommended |

#### Timeline Types by Investigative Purpose

- **Master chronology**: All events, all entities, all sources — the complete documentary base
- **Subject-specific timeline**: Events involving a specific entity only — used for subject profiles and prosecution files
- **Financial transaction timeline**: Movements of funds; sequenced with legal events (incorporation, litigation, insolvency)
- **Communication timeline**: Calls, messages, emails in sequence — exposes contact pattern and relationship evolution
- **Parallel/comparative timeline**: Two subjects or two event streams on the same timeline — reveals coordination, meetings, simultaneous actions
- **Time-person grid**: Matrix format; time intervals (columns) × individuals (rows); shows simultaneous actions and alibis

 [studysmarter.co](https://www.studysmarter.co.uk/explanations/law/forensic-science/timeline-analysis/)

***

### Construction Methodology

Timeline construction is iterative. The first pass — the **raw chronology** — places every dated event from source material in chronological order without interpretation. This raw material reveals the true sequence before narrative has been imposed. The second pass — **gap analysis** — explicitly identifies periods with no evidential record and assesses whether the gap is an evidential absence (nothing happened, nothing was recorded) or an investigative gap (something may have happened that has not yet been found). Distinguishing these two types of gap is analytically critical: evidential absences sometimes have their own significance (fraud investigations routinely turn on what *didn't* happen at a particular time).

Temporal uncertainty must be managed explicitly. The standard approach: record the date as given by the source, record the source's confidence/reliability, and note the uncertainty in the temporal certainty field. When multiple sources give conflicting dates for the same event, record all dates with their respective sources and flag as `Disputed` — resolving the conflict becomes an investigative task in the task log. Do not arbitrarily select one date over another. [unaettie](https://unaettie.com/en-us/aq/rca_timeline.php)

***

### Quality Criteria & Validation

Every entry requires a source. Entries without source citations are analytical assertions, not findings. Confidence levels must be applied: a timeline entry based on a confirmed official document (court filing, company registration) carries different evidential weight than one based on a single social media post. Gap analysis must be explicit and documented. Timezone documentation is mandatory for any international investigation or any investigation involving digital evidence (log timestamps default to server timezone, which may differ from local time). [studysmarter.co](https://www.studysmarter.co.uk/explanations/law/forensic-science/timeline-analysis/)

***

### Failure Modes & Mitigations

- **Temporal bias toward documented events**: Timeline reflects only events that left a documentary trace, producing a distorted picture. *Mitigation*: Gap analysis as explicit step; hypothesised events (what should have happened?) noted as investigative questions.
- **Timezone errors**: Events timestamped in wrong timezone, corrupting sequence. *Mitigation*: All timestamps normalised to UTC with local conversion documented; source timezone recorded.
- **Cherry-picking events to fit narrative**: Events selected that support existing hypothesis; contradicting events omitted. *Mitigation*: Raw chronology created before analytical narrative; all source events included in master timeline.
- **Correlation-sequence conflation**: Event A precedes event B, therefore A caused B. *Mitigation*: Analytical notes distinguish sequence from causation; competing hypotheses documented.
- **Unsourced entries**: Events added from memory or unrecorded sources. *Mitigation*: Source citation mandatory for every entry; entries without sources deleted or flagged as unverified leads.
- **Missing gap analysis**: Timeline presented as complete when large periods are undocumented. *Mitigation*: Gap analysis section required; gaps explicitly labelled with their evidential status.

***

### Template Design Notes

- **Deliverable**: A master chronological table (all events, all entities, sourced and confidence-rated) with a gap analysis section identifying periods of no evidential record, plus optional sub-timelines by entity or theme.
- **Required inputs**: Evidence register, entity list, source register, date range for investigation, known key events.
- **Standards to enforce**: Source citation per entry; confidence rating per entry; temporal certainty field; gap analysis section.
- **Quality checks**: No unsourced entries; timezone normalisation; gap periods identified and status assessed; competing dates for same event flagged.
- **Failure modes to prevent**: Timezone errors; cherry-picked entries; missing gap analysis; sequence-causation conflation.

***

### Key Sources

- StudySmarter Timeline Analysis: `studysmarter.co.uk/explanations/law/forensic-science/timeline-analysis/` [studysmarter.co](https://www.studysmarter.co.uk/explanations/law/forensic-science/timeline-analysis/)
- SoK: Timeline based event reconstruction for digital forensics: `sciencedirect.com/science/article/pii/S266628172500071X` [sciencedirect](https://www.sciencedirect.com/science/article/pii/S266628172500071X)
- Root Cause Analysis tabular timeline methodology: `unaettie.com/en-us/aq/rca_timeline.php` [unaettie](https://unaettie.com/en-us/aq/rca_timeline.php)
- inet-investigation.com OSINT Report Building: `inet-investigation.com/osint/how-to-build-an-osint-report/` [inet-investigation](https://www.inet-investigation.com/osint/how-to-build-an-osint-report/)

***

## DOMAIN 6: Source Evaluation & Confidence Frameworks

### Standards & Methodology

This is the most formally standardised of the seven domains, with multiple named, institutionally-endorsed frameworks in active use.

**The Admiralty System (NATO 6×6)** — formally the **NATO Intelligence Grading System**, codified in **AJP-2.1 (Allied Joint Doctrine for Intelligence Procedures), Edition B (2016)** under **STANAG 2511 (2003)** — is the dominant source evaluation framework across Western intelligence, law enforcement, and an increasing number of corporate intelligence contexts. The system uses a two-part alphanumeric rating: a letter (A–F) for source reliability and a number (1–6) for information credibility. The two ratings are assigned independently and should remain independent. [arxiv](https://arxiv.org/abs/2405.19968)

**Source Reliability (A–F):**
- **A — Completely reliable**: No doubt about the source's authenticity, trustworthiness, or competency; history of complete reliability (AJP-2.1)
- **B — Usually reliable**: Minor doubts; strong overall track record
- **C — Fairly reliable**: Genuine doubt exists; some valid information provided in the past
- **D — Not usually reliable**: Significant doubt; occasional valid information
- **E — Unreliable**: History of providing invalid information; lacks authenticity, trustworthiness, competency
- **F — Reliability cannot be judged**: No established track record; default for new sources

**Information Credibility (1–6):**
- **1 — Confirmed by other sources**: Independently corroborated; logical; consistent with other information
- **2 — Probably true**: Not independently confirmed; logically sound; consistent with other reporting
- **3 — Possibly true**: Not confirmed; reasonably logical; partially consistent
- **4 — Doubtful**: Possible but not logical; no other information to compare
- **5 — Improbable**: Not confirmed; illogical; actively contradicted by other reporting
- **6 — Truth cannot be judged**: Insufficient basis for evaluation

F6 is the most common rating in OSINT work — an untested source providing unverifiable information. It is a starting point for analysis, not a reason to discard the information. [pangearesearch.substack](https://pangearesearch.substack.com/p/the-admiralty-code-nato-6x6-system)

**ICD 203 Confidence Levels** provide a complementary framework for expressing analyst confidence in an assessment (as distinct from the probability of an event occurring). ICD 203 uses **High**, **Moderate**, and **Low** confidence levels. High confidence is based on high-quality information and sound analytical reasoning; Moderate confidence reflects information that is credible but not sufficiently corroborated; Low confidence reflects significant information gaps, questionable reliability, or fragile assumptions. ICD 203 explicitly requires that confidence levels and likelihood expressions not appear in the same sentence, to prevent reader confusion between the two dimensions. [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

**ICD 203 Probability Language** (for likelihood of events): `almost certainly` (95–99%), `very likely` (80–95%), `likely` (55–80%), `roughly even chance` (45–55%), `unlikely` (20–45%), `very unlikely` (5–20%), `remote` (1–5%), `almost no chance` (1–5%). Analysts must use terms from a single row and must not mix terms from different rows without a disclaimer. [dni](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)

**UK JIC/Defence Intelligence Probability Language**: The UK uses a similar framework documented in **Joint Doctrine Publication 2-00 (JDP 2-00): Understanding and Intelligence Support to Joint Operations** and referenced in academic intelligence studies. UK probability terms include: `Almost certain`, `Highly likely`, `Likely`, `Realistic possibility`, `Unlikely`, `Highly unlikely`, `Remote chance`. These map approximately (not exactly) to ICD 203 terms but the frameworks are distinct and should not be interchanged. [pangearesearch.substack](https://pangearesearch.substack.com/p/the-admiralty-code-nato-6x6-system)

**The UK Law Enforcement 5×5×5 System** is a three-dimensional extension of the Admiralty system used in UK policing. It adds a third dimension: **handling code** (specifying who may receive the information and what they may do with it), coded 1–5. The system thus produces three-digit ratings (e.g., 2/3/2) covering source reliability, intelligence reliability, and handling restriction simultaneously. The 5×5×5 system is documented in UK College of Policing intelligence handling guidance and is mandatory for intelligence recorded on police systems in England and Wales. [linkedin](https://www.linkedin.com/posts/jessicastutzman_osint-opensourceintelligence-intelligenceanalysis-activity-7432120971609714688-IopK)

**Evidence Quality: STRONG.** The Admiralty System is formally codified in NATO doctrine. ICD 203 is formal US IC directive. JDP 2-00 provides UK doctrine. These are among the most formally standardised frameworks across all seven domains.

***

### Standard Structure & Components

#### Source Evaluation Record (per entry in Source Register)

```
Source Identifier: [unique ID]
Source Type: [human / technical / open / liaison]
Source Description: [without identifying information if sensitive]
Reliability Rating: [A / B / C / D / E / F] with justification
Track Record Summary: [brief history of source's reporting accuracy]
Potential Motivation: [what does the source gain from providing this information?]
Access Assessment: [can the source plausibly know what they claim to know?]
Handling Code (5x5x5): [1-5 if UK policing context]
Date First Assessed: [date]
Last Reviewed: [date]
Reviewing Analyst: [ID]
```

#### Information Credibility Assessment (per intelligence item)

```
Information Item Reference: [links to Evidence Register]
Source Reference: [links to Source Record]
Credibility Rating: [1-6] with justification
Corroboration Status: [confirmed / corroborated / single source / unverified]
Logical Consistency: [consistent with / inconsistent with / no other information]
Temporal Currency: [date information was current]
Analyst Confidence: [High / Moderate / Low per ICD 203]
Likelihood Expression: [ICD 203 or JDP 2-00 probability language if applicable]
```

***

### Structured Analytical Techniques for Bias Reduction

**Analysis of Competing Hypotheses (ACH)** — developed by Richards Heuer (CIA, documented in *
