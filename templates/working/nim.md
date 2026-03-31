# Strategic & Tactical Assessment (NIM) Template: Operational Intelligence Framework

1. Strategic Direction & Intelligence Mission

In high-stakes law enforcement environments, the transition from raw data to actionable intelligence is governed by the National Decision Model (NDM). Adherence to this Strategic & Tactical Assessment template is a mandatory requirement for all analysts to ensure that intelligence products are objective, rigorous, and capable of mitigating both immediate operational risks and emerging strategic threats. Intelligence that fails to drive a decision is merely noise; this framework provides the structured architecture necessary to turn noise into force-level direction.

The NIM Temporal Framework: Strategic vs. Tactical

The National Intelligence Model (NIM) dictates two distinct analytical trajectories:

* Strategic Assessments: Commanded for long-term intelligence requirements. These identify multi-year trends, systemic vulnerabilities, and force-level priorities to inform high-level resource allocation and prevention strategies.
* Tactical Assessments: Commanded for immediate operational tasking. These identify current-period threats (targets and crime series) and high-priority opportunities for disruption, driving the daily tasking and coordination of frontline resources.

Analytical Directive: The BLUF Convention

Under Intelligence Community Directive (ICD) 203, all assessments must utilize the "Bottom Line Up Front" (BLUF) reporting convention. Senior decision-makers operating under extreme time pressure require analytical judgments and their operational implications immediately. Narrative build-up is a liability in a crisis. The BLUF ensures that the most vital message is presented at the outset, facilitating rapid, evidence-based executive action.


--------------------------------------------------------------------------------


2. The Entity Intelligence Layer: POLE & Database Schema

Structured entity resolution is the bedrock of intelligence. Analysts are commanded to implement a standardized schema to prevent "identity confusion" and ensure a "single version of the truth." Failure to distinguish between semantic types and entity types is a documented failure mode in database interoperability.

POLE & Technical Entity Schema: Minimum Required Fields

The following table defines the mandatory data architecture based on the POLE model (Person, Object, Location, Event).

Semantic Category	Entity Type (Examples)	Minimum Required Fields	Standard Optional Fields (Source-Derived)
Person	Offender, Witness, Subscriber	Full name, DOB, Nationality, Gender	Aliases, Historical Addresses, Identification Docs, Social Media Handles
Object	Vehicle, Weapon, Asset	Registration/Identifier, Make, Model, Colour	VIN (for Vehicles), Owner History, Associated Addresses
Location	Residential, Commercial, Point	Address or Coordinates, Type	Grid Reference, Geospatial Polygon, Historical Names
Event	Offence, Meeting, Transaction	Event Type, Date/Time, Location Reference	Participants, Description, Associated Entities, Narrative Link
Account	Financial, Social, Email	Account Type, Identifier, Platform	Creation Date, Status, Linked Recovery Phone/Email
Communication	Call, Message, VoIP	Channel Type, From/To Identifiers, Timestamp	Duration, Content Hash, Content Summary, Metadata Availability

Universal Metadata: The Anti-Liability Shield

Metadata is not optional; its absence constitutes a breach of NIM tradecraft and an active operational liability. Every entity record must include:

* Source Attribution: Explicit identification of the primary source (e.g., HUMINT, SOCMINT, SQL-Query).
* Confidence Level: The degree of certainty regarding the entity’s resolution (e.g., High, Moderate, Low).
* Analyst Identity: The unique identifier of the individual who verified the record.
* Last Verified Date: Mandatory timestamp for currency audit. Records without a "last verified" date within the current review cycle must be flagged as "Stale."


--------------------------------------------------------------------------------


3. Network Dynamics & Relational Analysis

Link analysis is the process of mapping interactions to expose the command and control structures of criminal networks. It is a requirement that analysts move beyond simple association to define directional, evidenced relationships.

Visual Grammar & Typed Links

Investigative link charts must adhere to the following visual standards:

* Nodes: Rectangles (Persons), Ovals (Organisations), Diamonds (Events), Triangles (Locations).
* Links: Solid lines denote "Confirmed" relationships; dashed lines denote "Unconfirmed/Probable."
* Link Labels (Typed Links): All links must be typed (e.g., ASSOCIATED_WITH, OWNS, EMPLOYS, DIRECTOR_OF, COMMUNICATES_WITH).
* Directional Arrows: Must indicate the flow of influence, money, or command (e.g., Subject A \rightarrow Subject B indicates "A directs B").

Solving the "Hairball Problem" through SNA Metrics

Visual density often obscures insight (the "Hairball Problem"). To maintain analytical clarity, analysts are commanded to use Social Network Analysis (SNA) metrics rather than relying on visual intuition:

1. Centrality Measures: Use Degree Centrality to find highly connected hubs; Betweenness Centrality to identify "gatekeepers" or bridges between sub-networks; and Eigenvector Centrality to identify nodes connected to other influential nodes.
2. Segmentation: Break complex networks into focused sub-charts based on specific clusters or "Typed Links."
3. Temporal Charting: Use time-filters to display only links active during specific operational windows, exposing how a network evolved.


--------------------------------------------------------------------------------


4. Chronological Analysis & Temporal Certainty

Timeline construction must be the first step in any complex investigation. Raw chronology must precede narrative interpretation to avoid "temporal bias," where a premature theory dictates the interpretation of timing.

Standard Investigative Timeline Entry

Entries must be normalized to ensure sequence integrity:

* UTC Normalization: All timestamps must be normalized to UTC. Local conversion must be documented in a separate field.
* Temporal Certainty: Every entry must be labeled as "Exact," "Approximate," or "Conflicting."
* Event Type: Categorization (e.g., Movement, Financial, Digital Footprint).

Parallel Timelines & Gap Analysis

To expose coordination between suspects, analysts should employ Parallel Timelines or a Time-Person Grid (Time intervals in columns \times Individuals in rows). This format is mandatory for identifying simultaneous actions or alibi conflicts.

Gap Analysis Directive: Analysts must explicitly distinguish between:

* Evidential Absence: A period where the record confirms nothing happened (e.g., a "dark" period in phone logs).
* Investigative Gap: A period where data is missing or unrecovered (e.g., missing CCTV). These gaps are "Known Unknowns" and must be prioritised in the intelligence requirements.


--------------------------------------------------------------------------------


5. Contextual Intelligence: Deep Environmental Analysis

Deep context is critical for interpreting intent. Without it, POLE data is merely a list.

Place History & Economic Trajectories

* Map Regression: Mandatory use of historical mapping series to track physical changes to a site (e.g., repurposed warehouses, concealed entrances).
* Growth-Pole/Resilience Theory: Evaluate if a location is an economic "growth pole" (attracting activity) or a region of decline. Economic grievances often drive the recruitment patterns of criminal networks.

The Genealogical Proof Standard (GPS)

When investigating kinship-based control structures (e.g., organized crime families), analysts must apply the GPS. This requires the separation of evidence into three tiers:

1. Direct Evidence: Explicitly answers the research question (e.g., a birth certificate proving parentage).
2. Indirect Evidence: Requires combination with other facts to infer a relationship (e.g., shared addresses and common surnames).
3. Negative Evidence: A documented absence where a record should exist, potentially suggesting a deliberate attempt to obscure a relationship.


--------------------------------------------------------------------------------


6. Analytical Tradecraft & Confidence Frameworks

The integrity of an assessment depends on the separation of the Probability of an Event from the Quality of the Evidence.

Probability Language (ICD 203)

Analysts must use the standardized probability scale for all judgments:

* Almost Certainly (95-99%)
* Likely (55-80%)
* Unlikely (20-45%)
* Remote (1-5%)

Grading Systems: Admiralty (NATO 6x6) & 5x5x5

UK Law Enforcement analysts must integrate the Handling Code from the 5x5x5 system.

Reliability (Source)	Credibility (Information)	Handling Code (5x5x5)
A - Completely Reliable	1 - Confirmed	1 - Dissemination within the service only
B - Usually Reliable	2 - Probably True	2 - Dissemination within UK partner agencies
C - Fairly Reliable	3 - Possibly True	3 - Dissemination to non-UK LEA
D - Not Usually Reliable	4 - Doubtful	4 - Dissemination to local partners
E - Unreliable	5 - Improbable	5 - Dissemination to the public
F - Cannot be Judged	6 - Cannot be Judged	

Mitigating Failure Modes

* Circular Reporting: Identify if multiple sources are merely "echoes" of a single flawed source.
* Confidence Inflation: Avoid presenting findings as more certain than the evidence base allows.
* ACH Directive: Analysts are commanded to use Analysis of Competing Hypotheses (ACH)—testing multiple explanations for the same data to find the most robust conclusion.


--------------------------------------------------------------------------------


7. Operational Tasking & Gap Identification

An assessment is a failure if it does not drive investigative actions. Reports must follow a structured format:

1. Key Judgments (BLUF): Core findings with confidence levels.
2. Supporting Analysis: POLE and Relational evidence.
3. Intelligence Gaps: What we don't know and how it impacts the threat picture.
4. Recommendations: Specific operational tasks.

Quality Control (QC) Checkpoints

Lead Analysts must ensure the following mandatory checkpoints are cleared:

* Scope Review: Verify the investigation has not suffered from "Scope Creep" beyond the intelligence requirement.
* Decision Audit: Every investigative choice must be recorded in a contemporaneous Decision Log with its rationale.
* Evidence Integrity: All digital evidence must be captured with SHA-256 hashing and archived in WARC files to ensure legal admissibility.


--------------------------------------------------------------------------------


8. Technical Infrastructure & Resource Inventory

The strategic shift in modern investigations is the move toward the "AI-Assisted Toolkit" and Model Context Protocol (MCP) orchestration.

Essential AI-Orchestratable & OSINT Tools

Category	Tool	Function
Entity Research	Maigret / Sherlock	Deep username/profile metadata extraction (MCP available).
Email Discovery	Holehe	Checks email registration across 120+ platforms via reset-probing.
Infrastructure	crt.sh / SpiderFoot	Certificate transparency logs and modular recon.
Corporate Intel	SEC EDGAR / LittleSis	Financial filings and power-mapping (MCP available).
Evidence	Wayback Machine / yt-dlp	Historical archival and high-grade media downloading.

The Post-API Reality & Legal Architecture

Automated scraping is increasingly obstructed. Analysts must shift to passive observation and archived data access. Note the following strategic constraints:

* Cost of Access: X/Twitter API access now starts at $100/mo; Reddit data has fractured into repositories like Arctic Shift and PullPush.
* Legal Mandates: All activity must adhere to the Berkeley Protocol on Digital Open Source Investigations and the UK Data Protection Act.
* Case Law: The hiQ v. LinkedIn decision governs the boundaries of public data collection. Any collection for facial recognition databases is prohibited under emerging AI Acts.

Admissibility Directive: Every digital artefact must be hash-verified and supported by an audit trail. Failure to maintain these standards will result in the exclusion of evidence in legal proceedings.
