[title]:
Investigative Entity Register: Master Template and Implementation Guide

[note]:
Investigative Entity Register: Master Template and Implementation Guide

1. Foundational Architecture and Standards Selection

In the high-stakes environment of modern intelligence, the transition from unstructured data to a machine-readable entity register is not merely a procedural preference; it is a strategic mandate. This guide establishes the mandatory technical architecture for ensuring interoperability and entity resolution across diverse investigative platforms. Adopting standardized models prevents the formation of data silos and enables the automated link analysis required to decompose complex networks.

Comparative Analysis: POLE vs. Schema.org

The selection of a data architecture dictates the logic of the entire investigation.

* POLE (Person, Object, Location, Event): This is the canonical data architecture convention utilized throughout the UK Law Enforcement and allied intelligence communities. While not a single published doctrinal document, it is the structural framework embedded in the National Intelligence Model (NIM) and systems like HOLMES2. Its heritage traces back to the UK National Criminal Intelligence Service (NCIS) and is designed specifically for operational intelligence where legal admissibility and strict categorization are paramount.
* Schema.org: Originating from an open-community standard (Google, Microsoft, Yandex), this approach is the de facto standard for Open-Source Intelligence (OSINT). It provides a flexible, platform-agnostic vocabulary that ensures data is machine-readable and easily transferable across web-based tools and AI-assisted analysis platforms.

Standards Selection Guide

Standard	Primary Community	Best Use Case	Semantic Interpretation
IBM i2 (iBase)	Intelligence / Corporate	High-end link analysis and multi-investigator teams.	Uses Semantic Types to define how applications interpret entities (e.g., "Offender" carries a "Person" semantic).
POLE	Law Enforcement	Criminal investigations and national security.	Rigid Categorical Architecture optimized for operational intelligence and legal chain of custody.
Schema.org	OSINT / Journalism	Web-based collection and automated data scraping.	Uses Vocabularies to ensure universal machine-readability across web platforms.

These foundational standards dictate the specific attributes required for each record. All investigators must adhere to the following definitions to maintain the integrity of the investigative database.


--------------------------------------------------------------------------------


2. Core Entity Definition Modules

Granular entity definition is the primary defense against the conflation of distinct real-world actors. Precise field requirements are mandatory to satisfy the threshold for "Entity Resolution"—the process of determining if two disparate records refer to the same individual or organization.

Core Entity Templates

Entity: Person

Field Name	Status	Standardized Vocabulary / Examples
Full Name	Required	Legal name as per official documentation.
Date of Birth	Required	ISO 8601 (YYYY-MM-DD).
Nationality	Required	ISO 3166-1 alpha-2 country codes.
Gender	Required	Male, Female, Non-Binary, Unknown.
Aliases	Optional	Known pseudonyms or social media handles.
ID Documents	Optional	Passport number, National ID, Social Security.
Employment	Optional	Current/Historical employer and role.

Entity: Organisation

Field Name	Status	Standardized Vocabulary / Examples
Legal Name	Required	Full registered name (e.g., "Example Ltd").
Reg. Number	Required	Official company house or tax ID.
Country	Required	Jurisdiction of incorporation.
Type	Required	LLC, NGO, State-Owned, Trust, Foundation.
Reg. Address	Required	Attribute: Street, City, Postcode (Legal seat).
Status	Optional	Active, Dissolved, Liquidated, Dormant.

Entity: Location

Field Name	Status	Standardized Vocabulary / Examples
Coordinates	Conditional	Decimal Degrees (Latitude, Longitude). Mandatory if Address is unavailable.
Full Address	Conditional	Street, City, Postcode, Country. Mandatory if Coordinates are unavailable.
Type	Required	Residential, Commercial, Industrial, Public.
Polygon	Optional	Geospatial boundary for larger sites or zones.

Technical Mandate: Registered Address vs. Location

Investigators must strictly distinguish between a Registered Address and a Location.

1. Registered Address is an Attribute of an Organisation entity. It represents a legal/administrative seat.
2. Location is a Discrete Entity. It represents a physical geospatial point on the earth.

These two must be connected via a LOCATED_AT relationship. This architectural separation is the only defense against "Virtual Office" errors, where analysts might otherwise mistake a commercial mailbox for the actual site of operational activity.


--------------------------------------------------------------------------------


3. Specialized and Supportive Entity Registers

Supportive entities transform a static repository into a dynamic map of activity. By registering communications, products, and events, the database captures the "how" and "when" of network operations.

Supporting Entity Requirements

* Communication: Mandatory for tracing interactions.
  * Fields: Channel Type (Email, VoIP, SMS), From Identifier, To Identifier, Timestamp (UTC), and Content Summary/Metadata.
* Vehicles: Essential for movement and pattern-of-life analysis.
  * Fields: Registration Plate, Make, Model, Colour, VIN, and Owner Reference.
* Accounts (Financial/Social): Critical for tracing fund flows and digital presence.
  * Fields: Account Type, Platform/Bank, Identifier (IBAN/Handle), and Creation Date.
* Product: Documents physical or digital assets involved in the investigation.
  * Fields: Product Name, Type, Unique Identifier (Serial No/SKU).
* Documents: Provides the evidentiary trail.
  * Fields: Document Type, Title, Date, Author, and Hash Value (SHA-256 for digital integrity).

The "Event" Entity

The Event entity is the central node for timeline analysis. Every Event record must include an Event Type (e.g., Financial Transaction, Movement, Meeting), a Location Reference, and a list of Participants. This structure allows for the reconstruction of chronologies and the identification of non-obvious clusters of cooperation.


--------------------------------------------------------------------------------


4. The Universal Metadata and Provenance Protocol

An entity record without source attribution is an analytical liability. To mitigate "Source Conflation," this protocol mandates field-level attribution. Each specific attribute (e.g., a specific Date of Birth or a Phone Number) must carry its own source tag, rather than attributing the entire entity record to a single source.

Universal Metadata Checklist

The following six fields MUST be applied to every record and updated at the field level where information originates from disparate sources:

1. Source Attribution: The specific document, URL, or database providing the data.
2. Date Observed: When the information was confirmed current by the source.
3. Confidence Level: The degree of certainty using the Admiralty Scale.
4. Classification/Handling: Access restrictions (e.g., Official, Secret, RBAC-restricted).
5. Analyst Identity: The individual responsible for the entry or last modification.
6. Last Verified: The date the information was last audited for currency.

Confidence Level Reference (Admiralty Scale)

Source Reliability (A–F) and Information Credibility (1–6) must be judged independently.

* Reliability: A (Completely reliable) to E (Unreliable). F indicates reliability cannot be judged.
* Credibility: 1 (Confirmed by other sources) to 5 (Improbable). 6 indicates truth cannot be judged.

Technical Note on F6 Ratings: In OSINT investigations, the F6 rating is the most common starting point for new data. It must not be used as a reason to discard data but rather as a trigger for further corroboration.


--------------------------------------------------------------------------------


5. Relationship Taxonomy and Link Typology

Typed links reveal the internal logic of a network. Standardized relationships are the primary defense against the "Hairball Problem"—the visual clutter caused by undifferentiated connections. Links must be kept minimal and meaningful; over-proliferation of link types degrades analytical clarity.

Master Link Taxonomy

Relationships must be categorized using the following standardized typology:

* ASSOCIATED_WITH: General connection; used only when specific nature is unknown.
* OWNS: Indicates asset ownership or majority shareholding.
* EMPLOYS: A formal professional or contractual relationship.
* DIRECTOR_OF: A legal governance role within an organization.
* COMMUNICATES_WITH: Based on phone, email, or social media logs.
* LOCATED_AT: Connects an entity (Person/Org) to a physical Location entity.
* WITNESSED_BY: Connects an Event to an observer or participant.
* PARTY_TO: Participation in a specific Event or Transaction.
* FAMILY_OF: Known kinship or domestic relationships.

Link Metadata

Each link must carry:

* Directional Properties: (e.g., Entity A controls Entity B).
* Date Range: Period during which the relationship was active.
* Strength/Confidence: The weight of evidence supporting the connection.


--------------------------------------------------------------------------------


6. Quality Control, Validation, and Entity Resolution

The integrity of a register decays over time. Without regular audits, "stale records" and "false positive matches" will compromise the investigation.

Data Integrity Protocol

* Duplicate Audits: Systematic checks using Record Linkage Libraries and manual i2 matching functions. Phonetic indexing (Metaphone/Soundex) should be used to catch name variations.
* Dead Record Reviews: Archiving entities with no investigative relevance or those whose data has been superseded.
* Source Audits: Verifying that no record has become "unsourced" during data merging or migration.

Entity Resolution Methodology

Records may only be merged when they meet a specific confidence threshold. The professional standard requires two or more independent verified identifiers.

* Independent: A Name and Date of Birth from a government registry are independent. A Name and a Social Media Handle are often not independent, as the handle may be self-certified based on the name.
* Threshold: High-confidence mergers require Name + DOB or Email + Physical Address corroboration.

Failure Mode Mitigation

Common Error	Mitigation Strategy
Schema Rigidity	Reserve generic "Notes" fields and utilize semantic types for mid-investigation variation.
Source Conflation	Attribute at the field level. Never merge disparate source citations into a single note.
No Access Control	Implement Role-Based Access Control (RBAC) and field-level classification.
Stale Records	Mandatory "Date Observed" fields and scheduled 30/90/120-day currency reviews.
Over-collection	Ensure all entities link directly to specific Intelligence Requirements (IRs).

The Investigative Entity Register is a living architecture. As the investigation progresses, analysts must iteratively review the schema to accommodate new entity types and relationship complexities as they emerge.

[list]:


[createdAt]: Mar 31, 2026, 3:08 PM
[updatedAt]: Mar 31, 2026, 3:08 PM
