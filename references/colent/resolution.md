Phase 3 of the investigative workflow, **Collation & Entity Resolution**, focuses on transforming the raw, vetted intelligence gathered in Phase 2 into a structured, relational database. This phase acts as the "central nervous system" of the analytical effort, where disparate data points are resolved into unique real-world entities to identify hidden connections and patterns.

### Step 6: Structured Extraction and Schema Mapping
The first step in collation is the transition from unstructured text or raw data files into a machine-readable format using the **Entity Extraction & Profiling Template**.

*   **Task 6.1: Implementing the POLE Schema.** Before extraction begins, the investigator must map available data to the established operational ontology. The standard framework used is the **POLE** model, which categorizes all intelligence into four canonical entities: **Person, Object, Location, and Event**.
*   **Task 6.2: Parsing Unstructured Text.** The template parses raw investigative notes, witness statements, or scraped web data into structured records based on predefined schema keys. For example, a "Person" record must include specific fields such as `givenName`, `familyName`, `birthDate`, and unique external identifiers like passport or Dun & Bradstreet (DUNS) numbers.
*   **Task 6.3: Deterministic matching for Unique Identifiers.** The system is instructed to enforce deterministic matching for high-stakes identifiers. If a passport number or national ID is found, the record is automatically linked to existing entries with the same identifier to prevent duplication.

### Step 7: Centralized Database Management and Entity Resolution
Once extracted, entities are ingested into the **Entity Register**, which serves as the primary repository for the entire investigation.

*   **Task 7.1: Executing the Entity Resolution (ER) Pipeline.** This is the critical methodological process of determining when fragmented or inconsistent records refer to the same real-world entity. The process follows the **Fellegi-Sunter framework**, a statistical model for record linkage that does not require training data.
*   **Task 7.2: Probabilistic Matching and Human Review.** When dealing with "messy" OSINT data where exact identifiers are missing, the investigator uses probabilistic resolution. This subtask involves evaluating variations in names, transposed birth dates, or similar addresses and assigning confidence weights based on the rarity of shared attributes. Matches that cross a predefined confidence threshold are presented to the analyst as "candidate matches" for manual verification.
*   **Task 7.3: Universal Metadata Tagging.** Every record in the register must maintain strict provenance. Mandatory metadata fields for every entry include:
    *   **Source Attribution:** Exactly which source provided the record.
    *   **Date Observed/Collected:** When the information was current.
    *   **Analyst Identity:** Who created or last modified the record.
    *   **Confidence Scoring:** The certainty of the attribution between the record and the real-world entity.

### Step 8: Consolidated Profiling and Specialized Deep Research
After entities are resolved, the investigator consolidates findings into high-level profiles to support decision-making.

*   **Task 8.1: Developing Subject & Corporate Profiles.** Using the **Subject & Corporate Profiles Template**, the investigator synthesizes data from the Entity Register into a narrative or tabular summary. 
    *   **Subject Profiles** focus on identity, employment history, and digital footprints. 
    *   **Corporate Profiles** map ownership chains, identify beneficial owners, and flag financial risks like circular ownership.
*   **Task 8.2: Invoking Specialized Research Templates.** If the investigation requires deeper contextual intelligence, specialized templates are used to enrich the profiles:
    *   **Genealogical & Family Network Research Template:** Used to map kinship structures and test relationship hypotheses using the Genealogical Proof Standard (GPS).
    *   **Cultural Context & Ethnographic Background Template:** Used to map power hierarchies and community norms, particularly when investigating entities in unfamiliar social or geographic environments.

### Phase 3 Quality and Integrity Checkpoints
To ensure the analytical rigour of the database, the following validation steps are mandatory:
*   **Duplicate Audit:** A systematic check for unresolved duplicates or fragmented records.
*   **Source Audit:** Verifying that no record has been "divorced" from its original source attribution.
*   **Stale Record Flagging:** Identifying and reviewing records that have not been verified within a specific timeframe to ensure the database remains current.
*   **Data Lineage Preservation:** Ensuring the system can trace any merged entity back to its original, disparate source documents to verify the matching logic.

Would you like to proceed to Phase 4 to see how these structured entities are processed into Chronological Matrices and Network Architecture edge-lists for pattern identification?
