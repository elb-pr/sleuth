# Technical Manual: Entity Extraction and Profiling Template (POLE Standard)

1. Conceptual Framework: The Shift from Narrative to Structured Intelligence

In modern investigative systems architecture, the transition from narrative note-taking to structured, typed entity databases is a strategic imperative. Relying on unstructured text invariably produces the "hairball" problem—an incoherent tangle of data where critical nodes and edges are obscured by volume and lack of ontological normalization. By adopting a typed entity-and-link schema, specifically the POLE (Person, Object, Location, Event) framework utilized by UK Law Enforcement and IBM i2 iBase environments, investigators enable computational analysis and automated deduplication. This shift allows for complex network queries and the identification of non-obvious patterns that remain latent within narrative reports.

The POLE framework functions as the core data architecture, ensuring semantic interpretability across various investigative platforms.

Category	Definition (UK Law Enforcement Convention)	Semantic Type (System Interpretation)
Person	Natural individuals relevant to the inquiry (e.g., suspects, witnesses).	Person (Subtypes: Offender, Witness, Subscriber)
Object	Tangible or digital items, including vehicles, accounts, and hardware.	Object (Subtypes: Vehicle, Account, Communication)
Location	Physical sites, addresses, or precise geospatial coordinates.	Location (Subtypes: Place, Address, Point of Interest)
Event	Occurrences at a specific point in time (e.g., crimes, meetings, calls).	Event (Subtypes: Transaction, Communication, Action)

This structural foundation dictates the specific data fields required for individual records, ensuring that every node in the graph is analytically viable.

2. The POLE Entity Schema: Mandatory Data Fields

Schema rigidity is the primary safeguard for data integrity and cross-jurisdictional interoperability. Without standardized field vocabularies grounded in schema.org or NIEM (National Information Exchange Model) approaches, data becomes machine-unreadable and siloed. Adhering to a fixed schema from the project's inception is critical; as noted in IBM iBase Designer guidance, retrospective schema changes are prohibitively costly and risk damaging the existing data ontology.

The following represent the minimum required and standard optional fields for the core POLE entities and digital footprints:

* Person
  * Minimum Required: Full name, DOB, Nationality, Gender.
  * Standard Optional: Aliases, Historical addresses, Employment history, Identifiers (Passport/SSN), Social media handles.
* Organisation
  * Minimum Required: Legal name, Registration number, Country of incorporation, Entity type.
  * Standard Optional: Registered/Trading addresses, Directors, Beneficial owners, Parent/Subsidiary relationships.
* Location
  * Minimum Required: Address or Coordinates (Lat/Long), Type (Residential/Commercial/Other).
  * Standard Optional: Grid reference, Country, Historical names, Geospatial polygon/Shapefile.
* Vehicle
  * Minimum Required: Registration plate, Make, Model, Color.
  * Standard Optional: VIN (Vehicle Identification Number), Owner(s), Sighting history.
* Account
  * Minimum Required: Account type (Financial/Social/Email), Identifier/Account number.
  * Standard Optional: Platform, Owner reference, Creation date, Current status.
* Communication
  * Minimum Required: Channel type, From/To identifiers, Timestamp.
  * Standard Optional: Content summary, Duration, Metadata (IP logs/Cell tower ID).
* Document
  * Minimum Required: Document type, Title, Date.
  * Standard Optional: Author, Source, Cryptographic Hash value, Archive URL.

Universal Metadata Fields

Every record, regardless of entity type, must carry the following metadata to maintain system auditability and security:

* Source Attribution: The specific source(s) providing the record data.
* Date Observed/Collected: When the information was last verified as current.
* Confidence Level: Certainty of the attribution between the record and the real-world entity.
* Classification/Handling: Access control levels (e.g., Restricted, Confidential).
* Analyst Identity: The individual responsible for the record's creation/modification.
* Last Verified: Timestamp of the most recent confirmation of accuracy.

Establishing these definitions is the prerequisite for the dynamic extraction of entities from raw investigative text.

3. The Extraction Workflow: From Raw Text to Structured Records

The extraction process adheres to the "Intelligence Cycle" of Direction, Collection, and Processing. A recurring failure mode in investigative systems is attempting data entry before finalizing the ontology; the schema must be defined before extraction to avoid the systemic error of retrospective re-classification.

The Extraction Protocol

1. Entity Identification: Parsing unstructured text for mentions of POLE-compliant entities.
2. Attribute Harvesting: Distilling specific properties (e.g., extracting a Residential Address from a news clip or a VIN from a police report).
3. Source Linking: Applying field-level attribution. To prevent "source conflation," every individual data point must be linked back to its primary source rather than applying a single attribution to the entire record.

Five-Tier Source Hierarchy

Investigators must rank the reliability of extracted data using this synthesized 5-tier hierarchy:

* Tier 1: Official Statutory/Vital Records: Civil registration (Birth/Marriage/Death), Land Registry, Court Judgments, Electoral Registers.
* Tier 2: Verified Commercial/Aggregated Databases: Companies House, Orbis, Credit Agency data, GLEIF Legal Entity Identifiers.
* Tier 3: Contextual/Social Archives: Population registers, Census data, Mass Observation records.
* Tier 4: Self-Published/Social Content: Social media profiles, blogs, forum participation (requires account authentication).
* Tier 5: Leaks and Derivative Commentary: Investigative leaks (e.g., Panama Papers), news aggregation, secondary commentary.

Following extraction, the system must determine if these entities represent new individuals or duplicates of existing records.

4. Identity Resolution Logic: Deterministic vs. Probabilistic Matching

Identity resolution—the process of determining if two records refer to the same real-world entity—is the central quality challenge. Architects must aggressively mitigate the systemic risk of False Positive Entity Matching (merging two distinct people), which can compromise legal admissibility, while also preventing the proliferation of Duplicate Entities.

Matching Logic	Application and Examples
Deterministic (Unique Identifiers)	Achieves 1:1 matching through unique, high-integrity identifiers. Examples: Passport Numbers, Company Registration Numbers, Cryptographic Hashes, and VINs.
Probabilistic (Corroborative Matches)	Relies on the "Two-Identifier Rule" to trigger a merge. Requires a match of at least two independent fields (e.g., Name + DOB or Email + Physical Address).

Thresholds for Merging

1. High-Confidence Merge: Requires a match on at least one Deterministic identifier or two independently verified Probabilistic identifiers.
2. Manual Review Trigger: Matches based on a single Probabilistic identifier (e.g., Name only) must be held in a staging environment for human review.
3. Conflict Resolution: If identifiers conflict (e.g., identical names but conflicting DOBs), records must remain distinct and be flagged for "Identity Conflict Investigation."

Once records are resolved, they are integrated into a network of relationships.

5. Relationship Mapping and Link Analysis

Link analysis provides the "Visual Grammar" of the investigation. Relationship types should be kept "minimal and meaningful" to prevent visual clutter and maintain analytical clarity.

Standard Link Types:

* ASSOCIATED_WITH: General connection.
* OWNS: Property or asset ownership.
* EMPLOYS: Professional/corporate tie.
* COMMUNICATES_WITH: Digital/physical contact.
* FAMILY_OF: Kinship ties.
* DIRECTOR_OF: Corporate governance connection.
* LOCATED_AT: Presence at a location.
* PARTY_TO: Participation in an Event.

Visual Grammar and Metadata

To distinguish between different levels of certainty, link charts must use the following line styles:

* Solid Line: Confirmed relationship (verified by Tier 1 or multiple Tier 2 sources).
* Dashed Line: Probable/unconfirmed relationship.
* Dotted Line: Suspected/low-confidence relationship.

Every link (Edge) must include: Directionality (A -> B, represented as a Directed Acyclic Graph where possible), Date Range, Strength Indicator, and Source Attribution.

6. Quality Assurance and Validation Framework

System quality is assessed via the four dimensions of Completeness, Accuracy, Currency, and Integrity.

The Admiralty Code (NATO 6x6)

Sources and information must be evaluated and assigned independently to prevent bias.

Source Reliability (A-F)	Information Credibility (1-6)
A: Completely reliable	1: Confirmed by other sources
B: Usually reliable	2: Probably true
C: Fairly reliable	3: Possibly true
D: Not usually reliable	4: Doubtful
E: Unreliable	5: Improbable
F: Reliability cannot be judged	6: Truth cannot be judged

Validation Checklist for Investigative Leads

* Duplicate Audit: Systematic check for unresolved entities sharing identifiers.
* Stale Record Flagging: Identifying entities based on "Date Last Verified" to ensure currency.
* Source Audit: Ensuring no "Unsourced Claims" exist; every field must have a citation.
* Hash Verification Audit: Confirming document integrity for Tier 1 digital records.
* Timezone Normalization Check: Ensuring all timestamps for Events and Communications are normalized to UTC to prevent temporal sequence errors.

Failure Mode Mitigation: Analysts must prevent "Source Conflation" by citing at the field level. "Schema Rigidity" is mitigated by utilizing a generic "Notes" field for emerging data that does not yet fit the established ontology.

7. Output Specification: The ICD 203 Briefing Format

The synthesis of investigative data must culminate in a BLUF (Bottom Line Up Front) report, following ICD 203 standards to ensure findings are actionable for decision-makers.

Finished Profile Requirements

1. Executive Summary (BLUF): The primary analytical message presented immediately.
2. Separation of Findings from Conclusions: Facts (what is known) must be strictly separated from Analytical Conclusions (what it means).
3. Standardized Probability Language: Analysts must use the ICD 203 probability scale to express the likelihood of events:
  * Almost Certainly: 95–99%
  * Very Likely: 80–95%
  * Likely: 55–80%
  * Roughly Even Chance: 45–55%
  * Unlikely: 20–45%
  * Very Unlikely: 5–20%
  * Remote: 1–5%
4. Formatting Restrictions: All outputs must be in standard Markdown. Use bolding for emphasis and tables for data summaries. Interactive elements, graphs, and external visualizations are prohibited to ensure cross-platform accessibility and analytical focus.
