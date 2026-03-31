[title]:


[note]:
Operational Case Decision & Intelligence Collection Log Template

1. Preliminary Case Authorization and Strategic Framing

The preliminary framing stage is the primary safeguard against "scope creep" and represents the bedrock of evidentiary integrity. In high-stakes operations, investigative focus must remain strictly aligned with core intelligence requirements to ensure that resources are not dissipated on tangential leads. This section establishes a contemporaneous audit trail, defining the operational mandate and ensuring that the investigation is designed to withstand rigorous judicial or tribunal scrutiny. By setting clinical boundaries at the outset, the Intelligence Architect ensures that every subsequent vector is tactically necessary and legally defensible.

Case Summary Record

This record formalizes the investigation under Domain 2 standards (APP for Investigations).

Field	Record Detail
Case Reference	Unique alphanumeric identifier for cross-referencing and disclosure logs.
Lead Investigator	Senior officer or architect responsible for tactical direction.
Investigation Scope	Definitive boundary statement; specify exactly what is in scope vs. excluded.
Target Completion	Projected date for final intelligence product delivery.

Legal and Ethical Parameters (PLAN Framework)

All investigative vectors must be justified against the PLAN framework to mitigate privacy intrusions and ensure compliance with the UK National Decision Model (NDM) and the Berkeley Protocol.

* Proportionality: COMMAND: Justify how the intrusiveness of the proposed collection is commensurate with the gravity of the suspected activity and the anticipated intelligence gain.
* Legality: COMMAND: Certify the specific legal authority, statutory power, or corporate policy (e.g., CPIA, GDPR, or specific operational mandate) that authorizes this investigation.
* Accountability: COMMAND: Designate the Senior Responsible Officer (SRO) for oversight and specify the retention and disposal schedule for the material collected.
* Necessity: COMMAND: Certify that all non-intrusive avenues (Tiers 1–3 of the Source Hierarchy) have been exhausted or dismissed with specific rationale before proceeding to intrusive vectors.

These high-level strategic decisions provide the essential foundation for specific task assignments in the subsequent phases of the intelligence cycle.


--------------------------------------------------------------------------------


2. The Contemporary Decision Log (Policy File)

The Contemporary Decision Log serves as a living audit trail for investigative judgment. Unlike retrospective summaries, this contemporaneous log captures the clinical logic of the investigator at the moment of action, ensuring transparency for legal discovery or peer review. Every significant decision must be anchored in the National Decision Model (NDM).

The National Decision Model (NDM) Guide for Rationale

When recording the rationale for a decision, users must address the five stages of the NDM:

1. Gather Information/Intelligence: What was known at the time?
2. Assess Threat and Risk: What was the risk of action vs. inaction?
3. Consider Powers and Policy: What legal/policy framework dictated the choice?
4. Identify Options/Contingencies: What alternatives were dismissed and why?
5. Take Action and Review: What was the selected vector and its intended outcome?

Decision Log Table

Every investigative task generates a recorded outcome.

Dec #	Date/Time	Information Available	Decision Taken	Rationale (Risk-Benefit & NDM Alignment)	Evidence Ref / Outcome
001	YYYY-MM-DD	Initial seed data...	Initiate Tier 1 audit.	Detail the tactical options considered. Explain why this vector was selected based on a risk-benefit analysis per NDM Stage 4.	[Ref #]

The decisions documented here dictate the specific knowledge gaps identified in the subsequent STEEPLES analysis.


--------------------------------------------------------------------------------


3. Knowledge Gap Analysis: STEEPLES Framework

The STEEPLES framework categorizes "knowns" against "unknowns," ensuring a holistic scan of the environment. Investigators must distinguish between Semantic Types (e.g., Person, Organization) and Entity Types (e.g., Target, Witness) when populating this matrix.

Domain	Baseline Status (Current Data)	Intelligence Requirement (Knowledge Gap)
Social	Documented social network dynamics.	SYNTHESIZE community gatekeepers and familial trust structures.
Technical	Known digital footprint/IP data.	EVALUATE infrastructure reuse, SSL/TLS certificates, and domain resolutions.
Economic	Known beneficial ownership data.	DECONSTRUCT asset concealment methods and value extraction flows.
Environmental	Known geospatial/site data.	DETERMINE significance of physical sites via map regression.
Political	Documented PEP status/connections.	ASSESS influence of patronage networks on subject activity.
Legal	Known litigation/regulatory history.	AUDIT pending enforcement actions or undisclosed civil disputes.
Ethical	Identified privacy/safety constraints.	CERTIFY compliance with the Berkeley Protocol and "Do No Harm" mandates.
Safety	Known physical/operational risks.	EVALUATE threat level posed to the investigation team or sources.

Identified gaps serve as the direct inputs for the prioritized Intelligence Collection Plan.


--------------------------------------------------------------------------------


4. The Intelligence Collection Plan (ICP) and Source Hierarchy

A tiered strategy ensures the most authoritative sources are targeted first to maximize resource efficiency. All incoming intelligence must be graded using the Admiralty System (STANAG 2511).

Source Prioritization Table

Tier	Category	Assigned Task	Required Tool/Platform
1	Statutory Filings	Verify legal identity/ownership.	GLEIF LEI API, SEC EDGAR, Companies House
2	Regulated Disclosures	Analyze listed company filings.	Stock Exchange Portals, OpenSanctions
3	Financial Databases	Peer/Industry comparison.	Bloomberg, USASpending, JudyRecords
4	Verified Media	Identify adverse media context.	Reuters, FT, ICIJ Offshore Leaks
5	Company Comms	Review subject's self-narrative.	Corporate Sites, Wayback Machine APIs
6	Social Signals	Map informal leads/networks.	twscrape, Maigret, Holehe
7	Technical Infrastructure	Map digital assets.	crt.sh, Shodan InternetDB, Censys
8	Self-Published Info	Assess reputation/footprint.	WhatsMyName, Archive.today

Admiralty System (6x6) Evaluation Guide

Reliability (Source) and Credibility (Information) must be assigned independently. Note: F6 is the default grading for new OSINT sources.

Source Reliability (A-F):

* A: Completely Reliable (No doubt of authenticity/trustworthiness).
* B: Usually Reliable (Minor doubts).
* C: Fairly Reliable (Some doubt, some valid info in past).
* D: Not Usually Reliable (Significant doubt).
* E: Unreliable (History of invalid information).
* F: Reliability Cannot be Judged (New/Untested source).

Information Credibility (1-6):

* 1: Confirmed by other sources (Independently corroborated).
* 2: Probably True (Logically sound, consistent with reporting).
* 3: Possibly True (Reasonably logical, partially consistent).
* 4: Doubtful (Possible but not logical; no comparison available).
* 5: Improbable (Actively contradicted by other reporting).
* 6: Truth Cannot be Judged (Insufficient basis for evaluation).


--------------------------------------------------------------------------------


5. Operational Entity Schema and Link Analysis Prep

Defining the POLE (Person, Object, Location, Event) schema prevents data conflation and facilitates automated link analysis. All records require universal metadata for legal defensibility.

Entity Schema & Universal Metadata

Universal Metadata Fields (Required for all types):

1. Source Attribution: Which specific source provided this record?
2. Date Observed: When was this information current?
3. Confidence Level: Analyst's certainty in the record-to-entity match.
4. Analyst ID: Who created/last modified this record?
5. Last Verified: Timestamp of the most recent confirmation.

Entity Type	Minimum Required Fields
Person	Full Name, DOB, Nationality, Identifiers (Passport/ID).
Object (Vehicle)	Registration Plate, VIN, Make/Model, Owner Reference.
Object (Account)	Platform, Account Type (Financial/Social), Identifier, Creation Date.
Location	Address or Coordinates, Type (Residential/Commercial), Grid Ref.
Event	Type, Date/Time, Participants, Description, Location Ref.

Link Analysis & Parsimony

Relationships must be recorded as typed links. Warning on Link Parsimony: Investigators must keep link types minimal and meaningful to prevent the "hairball problem" and ensure network structure remains analytically clear.

* OWNS / DIRECTOR_OF: Legal control (Statutory source required).
* ASSOCIATED_WITH: Evidenced connection between entities.
* COMMUNICATES_WITH: Evidenced contact via technical/social channels.
* PARTY_TO: Entity involvement in a specific event.

Requirement: Every link must cite the source and the Confidence Level (High/Moderate/Low) based on the quality of the corroborating evidence.


--------------------------------------------------------------------------------


This template transforms raw investigative intent into a structured, defensible, and high-value intelligence operation, ensuring that findings are resilient to challenge.

[list]:


[createdAt]: Mar 31, 2026, 2:30 PM
[updatedAt]: Invalid Date
