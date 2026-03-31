# Analytical Infrastructure in Investigative Methodology: A Cross-Disciplinary Architecture Report
DOMAIN 1: Entity Databases & Structured Profiles
Standards & Methodology
The standardisation of entity databases within investigative contexts is deeply fragmented across professional communities, reflecting differing operational priorities regarding data rigidity and schema evolution. Rather than a single unified doctrine, the domain is governed by a patchwork of structural ontologies and data exchange frameworks. The National Information Exchange Model (NIEM) 5.2 represents an ESTABLISHED architectural standard heavily utilised in United States and allied government contexts. This framework dictates meticulous properties and schemas for exchanging information across justice, military operations, and cyber domains, providing a common vocabulary for entities such as persons, organisations, and assets. Conversely, open-source intelligence (OSINT) and commercial intelligence largely rely on vendor-defined ontologies that have become de facto industry standards. Most notable are the IBM i2 iBase schema, which utilises strict semantic typing to ensure consistency across intelligence deployments , and the Palantir Gotham ontology, which maps physical and digital assets into a dynamic "digital twin" of the operational environment. The intelligence community utilises semantic typing to categorise data hierarchically, allowing disparate systems to interpret whether a node represents a specific "Victim," a "Witness," or a generic "Male" under a broader "Person" semantic umbrella.
The critical methodological component underpinning all entity databases is entity resolution (ER)—the process of determining when fragmented or inconsistent data records refer to the same real-world entity. The theoretical foundation for entity resolution remains the Fellegi-Sunter framework, an ESTABLISHED statistical model introduced in 1969. This framework provides a principled, unsupervised mathematical model for record linkage that operates without requiring training data, relying instead on frequency distributions of agreed field values among matches and non-matches. Modern implementations of ER diverge into two primary methodologies. Deterministic entity resolution relies on exact, predefined rules and identifiers (such as matching national identification numbers or precise email addresses) to link records. Probabilistic entity resolution, extending the Fellegi-Sunter principles, utilises statistical inference and machine learning models to estimate the likelihood of a match when data is messy, incomplete, or slightly inconsistent.
Standard Structure & Components
The canonical structure of an entity database record requires the explicit definition of object types, properties, and relationship links, ensuring that every piece of data is semantically categorised for downstream analysis.
| Component Category | Description and Standard Fields | Professional Context |
|---|---|---|
| Core Entity Types | Standard ontologies classify the world into discrete objects: Person, Organisation, Location, Vehicle, Account, Communication Device, Event, and Document. | Universal across all intelligence and law enforcement platforms. |
| Person Schema | Fields include givenName, familyName, additionalName (aliases), birthDate, birthPlace, affiliation, and unique external identifiers such as the Global Location Number (GLN). | Schema.org provides the foundational web standard, adapted heavily by corporate intelligence. |
| Organisation Schema | Fields include legalName, address, duns (Dun & Bradstreet number), department, alumni, and companyRegistration. | Corporate due diligence and financial investigation standard. |
| Metadata Standards | Every record must contain strict provenance metadata to maintain the chain of custody. Key fields include Create Date, Create User, and specific confidence scoring metrics for probabilistic matches. | Mandatory in law enforcement (CJIS compliance) and formal intelligence databases. |
| Link Types | Relationships must be typed and directional, defining the precise semantics (e.g., "Owned By," "Communicated With," "Employed By") between a source entity and a target entity. | Foundational for downstream network and link analysis. |
Construction Methodology
During an active investigation, the entity database is populated iteratively, functioning as the central nervous system of the analytical effort. Analysts and system architects begin by mapping available data sources to the established ontology, ensuring that fields from structured databases, scraped open-source tables, and unstructured document extractions align correctly. In ecosystems like Palantir Gotham, this initial mapping process translates raw datasources into the semantic elements of the ontology (objects, properties, and links) while applying granular security and governance controls to all changes. As new unstructured data is parsed and ingested, the extracted entities are subjected to the entity resolution pipeline.
The resolution process typically begins with deterministic matching, executing merges based on high-confidence unique keys. When dealing with noisy OSINT data, probabilistic matching algorithms take over, evaluating variations in names, transposed birth dates, or similar addresses. These algorithms assign confidence weights based on the rarity of the shared attributes—for example, a match on a highly unusual surname carries a greater probabilistic weight than a match on a common one, mirroring the mathematical principles of the Fellegi-Sunter model. Once potential matches cross a predefined confidence threshold, the system presents "candidate matches" to an analyst for manual review or, in highly scaled corporate environments, executes autonomous algorithmic merging. The system must maintain strict data lineage throughout this process so that any erroneously merged entity can be separated back into its constituent raw records.
Quality Criteria & Validation
Entity database quality is assessed through the accuracy of its entity resolution engine and the strictness of its schema adherence. The primary validation metric in investigative environments is the minimisation of two opposing errors: false positives (erroneously conflating two distinct entities into one record) and false negatives (failing to link fragmented records that refer to the same real-world entity). Quality frameworks demand that all probabilistic merges remain fully auditable. A database is considered analytically rigorous only if an investigator can trace a merged entity profile back to its original, disparate source documents to verify the matching logic.
Professional Community Variation
| Professional Community | Entity Resolution Methodology | Schema Rigidity & Application | Dominant Tools & Approaches |
|---|---|---|---|
| Law Enforcement | Deterministic priority. Requires high confidence to prevent evidentiary contamination. | High rigidity. Must comply with standards like NIEM 5.2 and strict criminal justice information protocols. | i2 iBase, Kaseware, custom relational databases. |
| Intelligence | Hybrid. Uses deterministic for known targets and probabilistic for signal intelligence. | High rigidity but dynamically extensible (e.g., Palantir Gotham ontologies). | Palantir Gotham, IBM i2. |
| Journalism / NGOs | Deterministic / Manual. Relies heavily on human-in-the-loop verification. | Low to Moderate. Ad-hoc structuring tailored to specific data leaks or investigations. | Neo4j, OpenRefine, Linkurious, custom spreadsheets. |
| Corporate Due Diligence | Probabilistic priority. Favours broad reach and scale over absolute precision. | Moderate. Adapts commercial standards like Schema.org or Salesforce configurations. | Quantexa, Senzing, DataWalk. |
Key Tools & Platforms
 * IBM i2 iBase (ibm.com): ESTABLISHED relational database application and modelling tool designed specifically for intelligence teams, utilising strict entity and link semantic types.
 * Palantir Gotham (palantir.com): ESTABLISHED enterprise intelligence platform leveraging a dynamic ontology of objects, properties, and links to power decision-making.
 * DataWalk (datawalk.com): EMERGING unified graph platform focusing on probabilistic entity resolution, offering flexibility for ad-hoc investigative workflows.
 * Senzing (senzing.com): EMERGING purpose-built, real-time entity resolution engine designed to handle autonomous record matching across massive, messy datasets.
 * OpenRefine (openrefine.org): ESTABLISHED open-source data wrangling tool heavily utilised in data journalism for text standardisation and manual entity clustering.
Failure Modes & Mitigations
 * Invisible False Positives: Over-aggressive probabilistic matching merges distinct entities who share attributes (e.g., fathers and sons with similar names and identical addresses). Mitigation: Implementation of negative weighting and strict "must-not-match" rules in the resolution algorithm.
 * Schema Rigidity: The inability of legacy relational databases to capture novel OSINT data types (e.g., cryptocurrency wallet addresses or dark web monikers). Mitigation: Utilising extensible, graph-based ontologies that permit ad-hoc property addition during an investigation.
 * Orphaned Records: Failure to execute deduplication, leaving a fragmented investigative view where critical connections are missed. Mitigation: Deploying continuous, background entity resolution algorithms that re-evaluate the database as new data arrives.
 * Loss of Provenance: Merging records in a way that overwrites the original source citations, destroying evidentiary value. Mitigation: Maintaining strict data lineage and ensuring Create User and Create Date metadata is preserved at the atomic record level.
Template Design Notes
 * Research Context: Establish the operational ontology before extraction begins, defining exactly what constitutes an entity within the specific investigative domain.
 * Task Specification: The prompt must instruct the AI to extract entities strictly conforming to predefined schema keys (e.g., Person.birthDate, Organisation.duns).
 * Quality Criteria: Mandate deterministic matching for high-stakes, unique identifiers (like passport numbers); require the AI to flag probabilistic, inferred matches for human review.
 * Output Specification: Produce structured JSON or Markdown tables mapping directly to the predefined entity and link schemas, ensuring seamless ingestion into downstream graph tools.
Evidence Quality Assessment
MODERATE. While theoretical frameworks (such as Fellegi-Sunter) and data exchange formats (NIEM) are strongly documented, the practical, investigative implementation layer relies heavily on proprietary vendor methodologies and software documentation rather than universal institutional doctrine.
Key Sources
 * NIEM 5.2 Documentation: http://niem.github.io/niem-releases/5.2/
 * Palantir Gotham Ontology Guide: https://palantir.com/docs/foundry/ontology/overview/
 * Entity Resolution Methodologies (Senzing): https://senzing.com/what-is-entity-resolution/
 * Stanford Entity Resolution Framework (SERF): http://infolab.stanford.edu/serf/ 
DOMAIN 2: Case Tracking & Investigation Management
Standards & Methodology
Investigation management methodology is formally ESTABLISHED within law enforcement and government intelligence through rigorous doctrinal frameworks. The UK College of Policing's Authorised Professional Practice (APP) on Intelligence Management provides a definitive standard, structuring the investigative workflow around the "Intelligence Cycle": Direction, Collection, Collation, Evaluation, Analysis, and Dissemination. At the core of this methodology is the requirement that all investigative actions be proportionate, necessary, and meticulously recorded. To satisfy legal and public scrutiny, investigators employ the STEEPLES mnemonic (Social, Technical, Economic, Environmental, Political, Legal, Ethical, Safety) to assess the influencing factors of an operation, and the PLAN mnemonic (Proportionality, Legality, Accountability, Necessity) to evaluate choices before executing a decision.
In the realm of open-source intelligence (OSINT) and digital investigations, the paramount standard is the preservation of the digital chain of custody. Methodologies dictate that digital evidence must be cryptographically hashed, timestamped, and immutably archived to prevent tampering and ensure legal admissibility in court. While corporate and journalistic communities do not always face the same evidentiary burdens as criminal prosecutors, organisations like the Association of Certified Fraud Examiners (ACFE) and the Global Investigative Journalism Network (GIJN) provide parallel frameworks focusing on workflow management, collaborative data structuring, and rigorous documentation to withstand civil litigation or defamation claims.
Standard Structure & Components
A comprehensive investigation management system relies on a structured, auditable Case File or Case Decision Log (CDL). The standard components include:
| Case File Component | Purpose and Standard Formatting |
|---|---|
| Intelligence Requirements | Strategic and tactical parameters defining knowledge gaps, potential sources, and collection strategies derived from the overarching control strategy. |
| Intelligence Collection Plan | A dynamic document detailing the specific information required, deadlines, source contact logs, and justification for the proportionality of the collection methods. |
| Case Decision Log (CDL) | A matrix recording: Situation/Circumstances, Aims/Outcome, Influencing Factors (STEEPLES), Assessment of Choices (PLAN), Preferred Option, and Risk Management strategies. |
| Evidence Register | Standardised documentation of captured physical and digital evidence, including Capture Details Reports, Video Evidence Continuity Reports, and hash values. |
| Dissemination Log | An audit trail recording the identity of intelligence recipients, the specific material shared, authorisations, and restrictions placed on further dissemination. |
Construction Methodology
Case tracking is an active, contemporaneous process that dictates the cadence of the investigation. At the "Direction" phase, an investigator or intelligence lead scopes the operational strategy and drafts an Intelligence Collection Plan. This plan prioritises information needs and mandates the exploration of both open and closed sources. During the "Collection" phase, particularly when conducting Internet Intelligence Investigations (III), investigators must maintain detailed audit trails. This involves logging every URL visited, documenting the IP footprints left behind, and securely archiving web pages and screenshots.
Decisions made throughout the investigation—especially policy deviations, joint agency actions, or negative decisions (conscious choices not to pursue a specific line of inquiry)—must be entered into the CDL in real-time. The methodology demands that these justifications be based solely on the information available at the time the decision was made, preventing hindsight bias. Modern case management systems automatically timestamp and digitally sign these entries. If electronic access is impossible, standard procedure requires the use of pre-carbonised, sequentially numbered, bound paper books where blank spaces are struck through to prevent retroactive alteration.
Quality Criteria & Validation
The primary quality criterion for case management is absolute auditability. If an investigation is subjected to cross-examination in court, regulatory review, or public scrutiny, the case file must transparently demonstrate the logical progression of the inquiry and the unassailable integrity of the evidence. Digital evidence systems validate this integrity through automated user-action logging and continuous hash verification of stored files. Furthermore, high-quality case management requires strict adherence to disclosure rules; for example, the UK MG5 standard explicitly mandates that case summaries remain objective and balanced, ensuring that sensitive intelligence tactics are kept separate from the main defence disclosure to protect operational security.
Professional Community Variation
| Professional Community | Case Tracking Priority | Documentation Format | Evidence Standard |
|---|---|---|---|
| Law Enforcement | Legal admissibility, rigorous disclosure compliance, and prosecutorial success. | Standardised forms (e.g., UK MG Forms, USFWS ROIs) and highly structured decision logs. | Strict chain of custody, cryptographic hashing, and immutability. |
| Investigative Journalism | Source protection, narrative development, and secure collaborative workflows. | Project management tools, encrypted collaborative pads (e.g., Tor-hidden Etherpad instances). | Journalistic verification, archival caching, and public interest defence. |
| Corporate Investigation | Regulatory compliance, risk mitigation, and operational efficiency. | Commercial case management software, ticketing systems, and corporate governance documentation. | Internal audit standards and civil litigation readiness. |
Key Tools & Platforms
 * Kaseware (kaseware.com): ESTABLISHED law enforcement case management system built to ensure Criminal Justice Information Services (CJIS) compliance and secure chain of custody tracking.
 * Hunchly (hunch.ly): ESTABLISHED OSINT web capture tool that operates as a browser extension, automatically tracking URLs, timestamping, and hashing digital evidence during research sessions.
 * Forensic OSINT (forensicosint.com): EMERGING digital evidence tool capable of generating standard Capture Details and Video Evidence Continuity reports for disclosure.
 * Etherpad (etherpad.org): EMERGING open-source collaborative editing tool frequently used by investigative journalists requiring anonymous or Tor-hidden instance tracking to protect operational security.
### Failure Modes & Mitigations
 * Retroactive Logging: Documenting decisions days or weeks after they were made, thereby corrupting the audit trail and inviting legal challenges regarding the investigator's true state of mind. Mitigation: Mandatory use of auto-timestamped Case Decision Logs and strict supervisory review cycles.
 * Single-Source Reliance: Failing to corroborate open-source intelligence, leading to investigations based on disinformation or error. Mitigation: Institutional mandate for "parallel sourcing" within the intelligence collection plan.
 * Chain of Custody Breaks: Saving digital evidence loosely on local hard drives or unsecured servers where it can be altered. Mitigation: Utilising automated hashing tools and depositing files into read-only, access-logged evidence vaults.
 * Scope Creep: Expanding the investigation beyond the original legal or ethical mandate without proper re-authorisation. Mitigation: Regularly reviewing the Terms of Reference (ToR) and updating the Intelligence Collection Plan under supervisory oversight.
Template Design Notes
 * Task Specification: The prompt template must enforce the generation of an Intelligence Collection Plan before substantive research begins, defining the scope and required sources.
 * Quality Criteria: Mandate the integration of the PLAN framework (Proportionality, Legality, Accountability, Necessity) to justify all proposed investigative vectors and search strategies.
 * Analytical Framework: Include a structured Decision Log matrix to track hypotheses that are abandoned and explicitly record the rationale for abandoning them.
 * Output Specification: Ensure the final output includes a meta-log of all simulated "URLs visited" or "sources queried" to mimic digital chain-of-custody requirements.
Evidence Quality Assessment
STRONG. This domain is backed by rigorous, publicly available law enforcement doctrine (such as the UK College of Policing guidelines and US Fish and Wildlife Service policies) as well as well-documented forensic digital evidence standards.
Key Sources
 * UK College of Policing Intelligence Cycle: https://www.college.police.uk/app/intelligence-management/intelligence-cycle
 * Home Office Case Decision Logs Guidance:(https://assets.publishing.service.gov.uk/media/5d01031640f0b609575c272a/Case_decision_logs_v4.0EXT_cleanarchived.pdf)
 * OSINT Digital Evidence Management: [https://www.osint.industries/post/handling-digital-evidence-our-ultimate-guide-to-forensic-osint](https://www.osint.industries/post/handling-digital-evidence-our-ultimate-guide-to-forensic-osint) 
DOMAIN 3: Briefing & Reporting Formats
Standards & Methodology
Investigative reporting formats are heavily dictated by professional doctrine, designed to ensure that complex findings are communicated with absolute clarity, objectivity, and appropriate nuance regarding uncertainty. In the United States Intelligence Community, reporting is strictly governed by the Office of the Director of National Intelligence (ODNI) through Intelligence Community Directive (ICD) 203 (Analytic Standards) and ICD 208 (Utility of Analytic Products). These ESTABLISHED frameworks mandate that all analytical products maintain independence from political consideration and enforce a clear, structural differentiation between underlying intelligence information (facts), suppositions used to frame arguments (assumptions), and the final analytical conclusions (judgements).
In law enforcement, specifically within the UK, the Manual of Guidance (MG) forms represent the ESTABLISHED standard. The MG5 (Police Report) standardises the presentation of case evidence for prosecutors and defence counsel, requiring an objective, balanced summary of events that aligns precisely with the legal points to prove. Corporate investigations operate under slightly more flexible guidelines. The Association of Certified Fraud Examiners (ACFE) standards explicitly state there is no single mandated report format for fraud examinations, provided that the final product is not misleading and meets the specific needs of the client or regulatory body.
Standard Structure & Components
The canonical intelligence product structure, adhering to ICD 203/208 conventions, requires specific narrative components designed for rapid executive consumption and rigorous peer review:
| Report Component | Purpose and Format Constraints |
|---|---|
| Bottom Line Up Front (BLUF) | Presents the main analytic message and core judgements immediately at the beginning of the document. |
| Sourcing Summary | A transparent description of the quality, credibility, and gaps in the underlying sources, explicitly noting which sources drive the key judgements. |
| Chronological / Thematic Summary | In law enforcement (e.g., MG5 forms), this is a factual chronological summary of the offence and evidence, avoiding investigative history or personal opinions. |
| Confidence & Likelihood Assessment | Standardised language expressing the probability of judgements, strictly adhering to established heuristic scales. |
| Analysis of Alternatives | An assessment of plausible alternative hypotheses, mandated especially when the analysis contends with significant complexity or uncertainty. |
| Tearlines | Portions of the report written at a lower classification level to facilitate broader dissemination without compromising sensitive sources or methods. |
Construction Methodology
Investigative reports are constructed by synthesising data, timelines, and matrices from the case management layer into a fluid narrative. Analysts begin the drafting process by explicitly defining and isolating the assumptions that bridge their information gaps. Writing must follow strict syntactical rules designed to prevent cognitive overload and misinterpretation. For instance, ICD 203 instructs analysts to actively avoid blending a "confidence level" (e.g., high confidence in the evidence) with a "degree of likelihood" (e.g., the event is unlikely) in the same sentence.
In law enforcement contexts, officers compile the MG5 report by outlining the specific legal elements required to prove an offence. They detail witness statements and summarise suspect interviews using a strict Question & Answer format. Crucially, the methodology requires investigators to deliberately strip out sensitive intelligence methods, personal opinions, or unverified intelligence from the main report, relegating sensitive material to separate, protected schedules (such as the MG6 form) to maintain legal privilege and operational security during court disclosure.
Quality Criteria & Validation
Under ICD 203, reports are continuously evaluated against specific analytic standards: clarity, logical argumentation, timeliness, and the explicit acknowledgement of significant contrary information. The intelligence community utilises an independent Analytic Ombuds to safeguard adherence to these standards and address concerns regarding bias or politicisation. In the corporate sector, the ACFE dictates that fraud reports must be fundamentally clear and accurate to prevent client deception, with quality validation occurring through peer review against the agreed-upon scope of the examination. Law enforcement supervisors provide validation by certifying that case summaries accurately reflect the available evidence without prejudice.
Professional Community Variation
| Professional Community | Reporting Standard / Framework | Key Focus | Language Protocol |
|---|---|---|---|
| Intelligence | ODNI ICD 203 & ICD 208 | Actionable strategic/tactical insight, threat anticipation. | Strict 7-tier probability language; distinct separation of facts vs. judgements. |
| Law Enforcement | UK MG5 / USFWS ROI | Evidentiary summary, legal elements, points to prove. | Objective, factual, chronological; entirely stripped of covert tactics. |
| Corporate/Due Diligence | ACFE Professional Standards | Commercial risk assessment, regulatory compliance. | Flexible, client-driven formatting; highly focused on financial liability. |
### Key Tools & Platforms
 * Standard Word Processors: Microsoft Word, Google Docs (ubiquitous across all disciplines for final drafting).
 * Palantir / i2 Reporting Modules: Integrated software modules that dynamically pull graph visualisations, entity profiles, and metadata into structured reporting templates, ensuring data consistency.
 * Kaseware Document Generation: Platform feature that auto-generates structured law enforcement reports and forms directly from underlying case and evidence data.
Failure Modes & Mitigations
 * Confidence/Likelihood Conflation: Writing confusing statements such as "We have high confidence it is highly likely that..." which obscures the analyst's true assessment. Mitigation: Strict adherence to ICD 203 vocabulary rules and editorial review.
 * Burying Caveats: Placing critical source limitations or data gaps at the end of a dense, multi-page report where policymakers may miss them. Mitigation: Mandating that Source Credibility statements appear up front, immediately following the BLUF.
 * Intelligence Leakage in Legal Reports: Inadvertently including covert tactics, surveillance methods, or unverified intelligence in discoverable court summaries. Mitigation: Utilising separated intelligence schedules (e.g., UK MG6 instead of MG5) to compartmentalise sensitive data.
 * Narrative Bias: Crafting a report that only presents evidence supporting the chosen conclusion. Mitigation: Mandating an "Analysis of Alternatives" section to formally address contrary data.
Template Design Notes
 * Output Specification: The template must enforce a BLUF (Bottom Line Up Front) structure, regardless of the overall length of the requested report.
 * Analytical Framework: The prompt must explicitly instruct the AI to separate Facts (data), Assumptions (suppositions), and Judgements (conclusions) in its output using distinct headers.
 * Quality Criteria: Force the AI to map any probabilistic claims to the standard ICD 203 7-tier scale (e.g., "Very unlikely", "Roughly even chance") and forbid improvised probability terminology.
 * Research Context: Assign the AI a clear epistemic stance (e.g., objective intelligence analyst) to prevent the adoption of an adversarial or advocacy tone.
Evidence Quality Assessment
STRONG. ICD 203 and the UK Manual of Guidance standards are public, foundational documents that are highly prescriptive regarding the structural and linguistic requirements of investigative reporting.
Key Sources
 * ODNI ICD 203 Analytic Standards:(https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
 * UK Police MG5 Completion Guide: https://www.judiciary.uk/wp-content/uploads/2015/09/bcm-mg5-how-to-complete.pdf
 * ACFE Code of Professional Standards:(https://www.acfe.com/~/-/media/9560BECA7A1441B5B3CD9A6E14CE7B89.ashx)
DOMAIN 4: Link Analysis & Network Visualisation
Standards & Methodology
Link analysis methodology provides the visual and mathematical framework for interpreting complex relationships. The standards governing this domain are ESTABLISHED through law enforcement and intelligence advisory bodies, notably the International Association of Law Enforcement Intelligence Analysts (IALEIA) and the Law Enforcement Intelligence Unit (LEIU). These bodies outline specific techniques for visualising criminal hierarchies, tracking commodity flows, and identifying network vulnerabilities.
Simultaneously, the academic foundations of this domain are deeply rooted in Social Network Analysis (SNA). Pioneered by sociologists and advanced by network scientists like Valdis Krebs, SNA provides the rigorous mathematical methodology to measure relationships, calculate node centrality, and assess network density. The visual grammar of link analysis—how these mathematical concepts are actually drawn—has been heavily standardised not by doctrine, but by commercial software dominance. IBM i2 Analyst's Notebook sets the de facto industry standard for node representation and edge styling, creating a visual language recognised universally by intelligence professionals.
Standard Structure & Components
Investigative network visualisations utilise standard matrices and charts to represent different facets of a dataset :
| Visualisation Type | Structural Description | Primary Application |
|---|---|---|
| Association Matrix / Chart | Nodes represent discrete entities (people, organisations); edges represent relationships (e.g., "Communicated With," "Owned By"). Often derived directly from telephone or financial record analysis. | Mapping conspiracy, identifying command hierarchies, and determining network breadth. |
| Commodity Flow Chart | Visualises the movement of physical goods, currency, or services. Nodes are entities; directional arrows indicate the flow, annotated externally with the specific commodity. | Tracking money laundering, narcotics distribution, or stolen asset movement. |
| Event Flow Analysis | Focuses on the sequence of events leading to an incident. Nodes represent actions or events connected by directional arrows. | Understanding modus operandi and identifying conflicting witness statements. |
| Visual Grammar (Styling) | Distinct semantic icons represent entity types (e.g., specific avatars for vehicles vs. banks). Line styles (solid, dashed, weighted) represent the confirmed status or intensity of the relationship. | Rapid cognitive processing of large, complex intelligence datasets. |
Construction Methodology
Experienced analysts rarely begin an investigation by immediately drawing a chart. The methodology requires building an underlying data matrix first. For Association Analysis, the analyst compiles fragmented data from multiple domains (e.g., telecommunications billing records, corporate registries, surveillance logs) into a structured grid. From this matrix, nodes and edges are systematically plotted.
In advanced SNA applications, the resulting network is quantitatively analysed before it is visually interpreted. Algorithms calculate various forms of "centrality" to identify the most connected nodes (Degree Centrality), bridge nodes that act as gatekeepers between isolated clusters (Betweenness Centrality), and nodes closest to all others in the network (Closeness Centrality). In complex, multi-faceted investigations, analysts employ two-mode analysis, mapping people (mode 1) to events, locations, or corporations (mode 2) to identify hidden co-occurrences and indirect affiliations that a simple person-to-person graph would obscure.
Quality Criteria & Validation
A high-quality link chart must overcome the infamous "hairball" effect—an unreadable, dense mass of overlapping connections that provides no analytical value. Validation requires that every single link on a chart is traceable back to a specific intelligence report, raw data file, or evidence artefact. Furthermore, charts must be properly legendised. This includes indicating the temporal scope of the data, the overall classification level, and the confidence level of unconfirmed links (traditionally denoted by dashed or dotted lines to separate them visually from proven associations).
Professional Community Variation
| Professional Community | Analytical Approach | Primary Focus | Key Output |
|---|---|---|---|
| Law Enforcement | Association / Commodity Flow Analysis. | Proving conspiracy, mapping criminal hierarchies, and supporting tactical interventions. | Link charts formatted for court presentation or immediate tactical action. |
| Academic / Data Science | Social Network Analysis (SNA). | Mathematical centrality, graph theory, and diffusion modelling. | Sociograms, statistical network metrics, and academic papers. |
| Corporate Intelligence | Beneficial Ownership Mapping. | Tracing the Ultimate Beneficial Owner (UBO) through shell companies to ensure regulatory compliance. | Corporate structure charts and risk assessment matrices. |
Key Tools & Platforms
 * IBM i2 Analyst's Notebook (ibm.com): ESTABLISHED industry standard for manual and semi-automated link charting, featuring deep semantic icon libraries and robust temporal analysis views.
 * Maltego (maltego.com): ESTABLISHED OSINT graph visualization tool focusing heavily on automated data enrichment via API integrations (transforms).
 * Gephi (gephi.org): ESTABLISHED open-source visualization and exploration software used for large-scale algorithmic Social Network Analysis.
 * Palantir Gotham (palantir.com): ESTABLISHED platform integrating link analysis directly with its dynamic enterprise ontology.
Failure Modes & Mitigations
 * Association Fallacy: Treating a minor edge (e.g., two individuals appearing in the background of the same photograph) as definitive evidence of criminal conspiracy. Mitigation: Explicitly typing and weighting edges based on the nature and intensity of the association.
 * The "Hairball" Problem: Overloading a graph with raw, unfiltered data, rendering it visually and analytically useless. Mitigation: Applying SNA clustering algorithms, filtering by link weight, or utilizing two-mode analysis to separate data layers.
 * Source Conflation: Plotting links derived from a highly reliable intelligence intercept identically to links derived from an unverified anonymous tip. Mitigation: Employing strict visual grammar rules (e.g., using dashed lines for unverified links) to visually represent epistemic doubt.
Template Design Notes
 * Inputs: The prompt template requires structured edge-list data from the user (Source Node, Target Node, Relationship Type, Evidence Citation).
 * Output Specification: If generating text-based prompts designed for downstream graph rendering (e.g., Mermaid.js syntax), the AI must ensure strict adherence to syntax, node grouping, and line-style rules based on confidence levels.
 * Task Specification: Mandate the analytical identification of "Central Hubs" (high degree centrality) and "Bridge Nodes" (high betweenness centrality) within the provided data to simulate basic SNA.
Evidence Quality Assessment
STRONG. IALEIA and LEIU standards provide clear, tactical methodologies for law enforcement, while decades of academic research in Social Network Analysis provide an unshakeable mathematical rigour to the domain.
Key Sources
 * IALEIA Successful Law Enforcement Using Analytic Methods:(https://www.ialeia.org/docs/Successful_Law_Enforcement_Using_Analytic_Methods.pdf)
 * Social Network Analysis (Valdis Krebs):(http://www.orgnet.com/Beautiful_Visualization_Chapter_7_Krebs.pdf)
 * IBM i2 Analyst's Notebook Documentation:(https://www.ibm.com/docs/en/SSJSV9_9.2.4/pdf/analysts_notebook_pdf.pdf) 
DOMAIN 5: Timeline Construction & Chronological Analysis
Standards & Methodology
Chronological analysis forms the temporal backbone of all investigative work, functioning as the primary mechanism for establishing causality and resolving conflicting narratives. Formal standards exist prominently within digital forensics, such as ASTM E2713 (standard guidance for forensic engineering and investigation methodologies). In the realm of open-source investigations and human rights journalism, the Bellingcat verification methodology provides an EMERGING, highly respected standard for temporal and spatial verification. Their methodology focuses on four rigorous pillars: searching, preservation, verification, and analysis, specifically engineered to elevate OSINT to an evidentiary standard suitable for international courts. In cybersecurity incident response, timeline analysis relies heavily on the systematic aggregation of system logs, Master File Table ($MFT) extraction, and the correlation of disparate digital artifacts to trace threat actor movements.
Standard Structure & Components
A rigorous investigative timeline is structured not as a simple list, but as a dense chronological matrix or array designed to highlight patterns and gaps. Required fields include:
| Timeline Field | Description and Standard Requirements |
|---|---|
| Timestamp | The exact date and time of the event, requiring precise timezone normalisation (universally converted to UTC to prevent sequencing errors). |
| Event Description | A purely objective statement of the occurrence, devoid of analytical assumptions or unproven causal links. |
| Entity Involvement | The specific actors, computer systems, physical assets, or accounts involved in the event. |
| Source / Provenance | A direct citation of the digital evidence, witness statement, or OSINT artifact proving the event occurred. |
| Uncertainty Marker | Explicit indicators of temporal ambiguity (e.g., noting that an event occurred sometime between 14:00 and 16:00, rather than assigning an arbitrary precise time). |
Construction Methodology
Timeline construction is a meticulous, multi-step aggregation process that varies by domain but shares core principles. In digital forensics, automated tools extract raw timestamps from low-level file systems (e.g., using MFTECmd.exe for Windows NTFS volumes) and sort them into a unified, human-readable view (e.g., using mactime from The Sleuth Kit). In general OSINT and criminal investigations, analysts manually construct Event Flow Charts (boxes arranged chronologically with directional arrows) or linear master timelines.
A critical component of this methodology is the handling of uncertainty. Analysts systematically document their "unknowns" by placing empty markers or placeholder squares on the timeline (e.g., "Victim activity unknown between 14:00 and 16:00"). This practice highlights intelligence gaps, prevents the mind from jumping to false conclusions, and directs future resource collection. In complex visual investigations, tools like Google Street View, shadow analysis, and metadata extraction are used to verify the exact timing and location of user-generated content before it is permitted to be plotted on the master timeline.
Quality Criteria & Validation
Timelines are validated by their ability to identify and resolve temporal contradictions. Correlation of evidence across multiple streams is crucial; if two sources claim an entity was in different locations at the exact same time, the analyst must score the reliability of the sources to resolve the conflict or flag the anomaly for further investigation. Furthermore, high-quality timelines address technical backward compatibility issues and rigorously normalise formatting across disparate system logs or international calendar date formats to ensure the sequence of events is mathematically sound.
Professional Community Variation
| Professional Community | Timeline Focus | Handling of Uncertainty | Key Tools |
|---|---|---|---|
| Digital Forensics / IR | Millisecond precision, system events, file modifications. | Rigid. Based on immutable cryptographic timestamps and log parsing. | TSK (mactime), MFTECmd, Log2Timeline. |
| Journalism / Human Rights | Narrative flow, public accountability, war crime documentation. | Addressed via transparent, open verification (e.g., Bellingcat methods). | TimeLineJS, custom interactive mapping. |
| Law Enforcement | Event Flow Analysis, establishing Modus Operandi (MO). | Clearly separating known facts from suspected actions using visual markers. | i2 Analyst's Notebook (Temporal views). |
Key Tools & Platforms
*   The Sleuth Kit (TSK) / mactime: ESTABLISHED open-source digital forensics toolset used for deep timeline generation from raw disk images.
 * IBM i2 Analyst's Notebook: ESTABLISHED analytical tool capable of visualising complex chronological and event-flow data natively alongside traditional relationship links.
 * TimeLineJS: EMERGING open-source tool heavily utilised in data journalism to publish interactive, visually rich timelines derived from spreadsheet data.
 * Eric Zimmerman's Tools (MFTECmd): ESTABLISHED suite of forensic parsing tools essential for extracting accurate temporal data from Windows file systems.
Failure Modes & Mitigations
 * Timezone Conflation: Mixing UTC, local time, and system time within the same matrix, causing critical events to appear out of chronological sequence. Mitigation: Strict, mandatory normalisation of all timestamps to UTC in the master timeline matrix prior to analysis.
 * Correlation vs. Causation: Assuming Event B was caused by Event A simply because it followed it chronologically. Mitigation: Utilizing Hypothesis Tracking methodologies (like ACH) to rigorously test causal links rather than relying on visual proximity.
 * Data Overload: Flooding the timeline with routine, non-diagnostic events (e.g., millions of routine system logs), burying the critical anomaly. Mitigation: Applying strict filtering heuristics and creating modular sub-timelines for specific entities or event types.
Template Design Notes
 * Inputs: The user provides unstructured chronological narrative data or multiple timestamped system logs.
 * Analytical Framework: The prompt must instruct the AI to standardise all dates/times (requesting clarification if timezones are ambiguous) and automatically sort the data chronologically.
 * Output Specification: Enforce a strict tabular format (Date/Time, Event, Entities, Source, Uncertainty Notes). Require the AI to explicitly flag any temporal overlaps, gaps, or logical impossibilities.
Evidence Quality Assessment
MODERATE. While digital forensic timelines possess highly rigorous technical standards, OSINT and human-centric timeline methodologies rely heavily on evolving practitioner consensus and non-governmental organisations rather than formal institutional doctrine.
Key Sources
 * DFRWS Timeline-based Event Reconstruction:(https://dfrws.org/wp-content/uploads/2025/05/SoK-Timeline-based-event-reconstruction-for-digital-forensics-Terminology-methodology-and-current-challenges.pdf)
 * Bellingcat Methodological Standards:(https://eprints.ncrm.ac.uk/id/eprint/4545/1/Bellingcat%E2%80%99s%20Yemen%20Project.pdf)
 * SANS Incident Timeline Analysis: https://isc.sans.edu/diary/13537
DOMAIN 6: Source Evaluation & Confidence Frameworks
Standards & Methodology
Source evaluation serves as the epistemic foundation of all intelligence work; an investigation is only as robust as the framework used to vet its underlying data. The predominant standard in military and traditional intelligence is the Admiralty System (often referred to as the NATO System 6x6, formally defined in NATO Allied Joint Publication AJP-2). This ESTABLISHED framework distinctly separates the evaluation of the source's historical reliability from the evaluation of the specific information's current credibility. Concurrently, the United States Intelligence Community enforces ODNI ICD 203, which mandates a specific, standardised 7-tier probabilistic language scale for expressing analytical confidence and likelihood in final assessments.
Standard Structure & Components
Source evaluation frameworks rely on rigid matrices and controlled vocabularies to eliminate subjective interpretation:
The Admiralty 6x6 Matrix :
 * Source Reliability (A-F): Evaluates the historical trustworthiness of the provider.
   * A (Completely Reliable), B (Usually Reliable), C (Fairly Reliable), D (Not Usually Reliable), E (Unreliable), F (Cannot Be Judged).
 * Information Credibility (1-6): Evaluates the logic and external corroboration of the data itself.
   * 1 (Confirmed), 2 (Probably True), 3 (Possibly True), 4 (Doubtfully True), 5 (Improbable), 6 (Cannot Be Judged).
 * Output: An alphanumeric grade appended to the intelligence report (e.g., "B2" indicates a Usually Reliable source providing Probably True information).
The ICD 203 Likelihood Scale :
When expressing the probability of an event or judgement, analysts must use one of the following tiers:
 * 01–05%: Almost no chance / Remote
 * 05–20%: Very unlikely / Highly improbable
 * 20–45%: Unlikely / Improbable
 * 45–55%: Roughly even chance / Roughly even odds
 * 55–80%: Likely / Probable
 * 80–95%: Very likely / Highly probable
 * 95–99%: Almost certain / Nearly certain
Construction Methodology
When a new piece of information enters the intelligence cycle during the Evaluation phase, it must be graded via an Intelligence Report (IR). The methodology requires the analyst to first assess the historical trustworthiness of the source (A-F) completely independent of the current data. Subsequently, they assess the internal logic and external corroboration of the current data (1-6). This bipartite system prevents plausible lies from highly unreliable sources from polluting the database.
When analysts synthesise this data to write their final assessments, they apply the ICD 203 standards, assigning a likelihood percentage to their overarching judgements based on the aggregate quality of the underlying A1-to-F6 evaluated data. In modern open-source contexts, however, a methodological friction occurs. Determining the "historical reliability" of a newly discovered, anonymous social media account (which would default to 'F') is often impossible. Consequently, OSINT methodologies pivot heavily toward data validity—relying on technical verification, metadata analysis, and geolocation—rather than traditional human-source vetting.
Quality Criteria & Validation
A high-quality evaluation strictly avoids cognitive conflation. An analyst must not rate a source as "A" simply because the information seems highly plausible, nor rate information as "1" simply because it originates from a historically reliable source. The framework forces independent, isolated validation of both vectors. ICD 203 further validates analytical quality by mandating that analysts explicitly explain the basis for their uncertainties. They are explicitly forbidden from mixing terms from different probability tiers without a clarifying disclaimer to prevent reader confusion.
Professional Community Variation
| Professional Community | Epistemic Framework | Core Metric | Handling of OSINT |
|---|---|---|---|
| Military/Intelligence | Admiralty 6x6 / ICD 203. | Historical reliability combined with corroboration. | Often struggles with one-off digital sources, defaulting them to low reliability. |
| Journalism (e.g., Bellingcat) | Digital Verification. | Technical corroboration (Geolocation, Chronolocation, Metadata). | High focus on data validity over source history; the data proves itself. |
| Academic | CRAAP Test / Peer Review. | Reproducibility, transparency, and peer consensus. | Methodological rigour and literature review. |
Key Tools & Platforms
 * Intelligence Management Systems (e.g., Palantir, iBase): Generally feature built-in, mandatory metadata fields to tag objects with Admiralty grading upon ingestion.
 * Bellingcat Verification Toolkit: A suite of open-source methodologies (reverse image search, shadow analysis, metadata extraction) acting as the OSINT equivalent to traditional source vetting.
Failure Modes & Mitigations
 * Circular Reporting: Multiple sources report the exact same fact, artificially inflating its credibility (e.g., rating it '1'), but all sources secretly derive from a single, hidden primary source. Mitigation: Meticulously mapping information lineage and applying Structured Analytic Techniques to uncover the root source.
 * Source Laundering: Hiding a low-reliability source behind a high-reliability intermediary to bypass grading filters. Mitigation: Strict adherence to source-of-origin documentation rules, ensuring the original collector is evaluated.
 * The OSINT Mismatch: Rating a verified, mathematically geolocated video found on an anonymous burner account as "F" (unreliable source), thereby downgrading its intelligence value despite undeniable physical proof. Mitigation: Modifying doctrinal matrices in digital units to prioritize technical verification over human-source history.
Template Design Notes
 * Task Specification: Require the AI to process provided intelligence snippets and assign an Admiralty code (A-F, 1-6) to each discrete claim, providing justification for both axes.
 * Quality Criteria: Force the AI to use exact ICD 203 terminology when delivering final analytical judgements. Explicitly reject non-standard terms like "might happen," "good chance," or "could be."
 * Output Specification: Append a structured source evaluation matrix as an appendix to the final output, ensuring epistemic transparency.
Evidence Quality Assessment
STRONG. The Admiralty system and ODNI ICD 203 are among the most heavily documented, public-facing, and universally applied doctrines in the global intelligence profession.
Key Sources
 * Admiralty System / NATO AJP-2 Guidelines:(https://conservationcriminology.com/wp-content/uploads/2019/09/6x6-Admiralty-System.pdf)
 * ODNI ICD 203 Analytic Standards:(https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
DOMAIN 7: Hypothesis Tracking & Analytical Reasoning
Standards & Methodology
Hypothesis tracking represents the highest cognitive layer of investigative infrastructure, designed specifically to combat cognitive biases—primarily confirmation bias and premature closure. The ESTABLISHED gold standard in the intelligence community is the Analysis of Competing Hypotheses (ACH), pioneered by Richards J. Heuer Jr. at the CIA's Center for the Study of Intelligence. ACH operates on the scientific principle of refutation rather than confirmation. Instead of seeking evidence to prove a favoured theory, it asserts that the most likely hypothesis is the one with the least evidence against it—a concept known as the Inconsistency Principle.
Standard Structure & Components
The ACH methodology relies on a highly structured matrix to externalise the analyst's thought process :
| Matrix Component | Structural Description |
|---|---|
| Y-Axis (Evidence) | A comprehensive list of all significant evidence, facts, and assumptions. Advanced automated ACH systems expand this axis to include metadata such as source reliability, credibility, and temporal relevance. |
| X-Axis (Hypotheses) | A mutually exclusive, collectively exhaustive set of possible explanations for the investigative problem. |
| Matrix Cells (Diagnosticity) | Ratings indicating how consistent an item of evidence is with a specific hypothesis. Typically scored as: C (Consistent), CC (Very Consistent), I (Inconsistent), II (Very Inconsistent), or N/A. |
| Inconsistency Score | The calculated total of 'I' and 'II' ratings for each hypothesis, used to mathematically rank the viability of explanations. |
Construction Methodology
The ACH process strictly follows an 8-step methodology (often condensed in modern practice to 7 steps) to ensure analytical rigour :
 * Identify Hypotheses: Brainstorm all possible explanations, avoiding any premature filtering or judgement.
 * Make Evidence List: Assemble all collected evidence and, crucially, identify critical underlying assumptions.
 * Prepare Matrix: Plot the evidence against the hypotheses in the grid.
 * Refine Matrix (Diagnosticity): Evaluate the "diagnosticity" of each piece of evidence. This is the critical step: the analyst must ask, "If this hypothesis is true, how likely is it that I would see this evidence?" If a piece of evidence is consistent with all hypotheses, it has no diagnostic value and should be removed from the matrix.
 * Draw Conclusions: Evaluate the hypotheses based on their inconsistency scores. The hypothesis with the lowest inconsistency score is generally the most likely.
 * Sensitivity Analysis: Test how dependent the final conclusion is on a few critical pieces of evidence. The analyst asks: What if those specific items are wrong, deceptive, or misinterpreted?.
 * Report Conclusions: Draft the final analytical report, explicitly detailing why alternative hypotheses were rejected based on the matrix.
Quality Criteria & Validation
A high-quality ACH matrix does not guarantee the correct answer; rather, it guarantees an appropriate process that minimises human error. Validation involves auditing the matrix to check whether the analyst actively sought disconfirming evidence rather than cherry-picking confirming data. Advanced variants, such as Bayesian ACH, apply complex mathematical probability algorithms to evidence evaluation, though practitioners note this often sacrifices the intuitive, collaborative usability of the manual matrix.
Professional Community Variation
| Professional Community | Hypothesis Management Approach | Bias Mitigation Strategy |
|---|---|---|
| Intelligence | Formal ACH Matrix. | Institutionalised Structured Analytic Techniques (SATs), Red Teaming, Devil's Advocacy. |
| Law Enforcement | Investigative Strategy / CDL. | Documenting within the Case Decision Log exactly why alternative lines of enquiry were closed to satisfy disclosure rules. |
| Journalism / Academia | Peer Review / Fact-Checking. | Editorial oversight, reproducible methodologies, and public transparency. |
Key Tools & Platforms
 * PARC ACH (Palo Alto Research Center): ESTABLISHED legacy software specifically built to run the classic ACH matrix methodology.
 * Pherson ACH Software: EMERGING automated tools providing "analyst shoebox" capabilities to sort evidence by date, type, and weight, calculating complex inconsistency scores.
 * Spreadsheets (Excel/Google Sheets): The most common ad-hoc tool used by practitioners to build manual ACH matrices due to extreme flexibility.
Failure Modes & Mitigations
 * Satisficing: Stopping the investigation at the very first hypothesis that seems to fit the data adequately. Mitigation: The core ACH requirement to brainstorm and evaluate all viable hypotheses simultaneously before drawing any conclusions.
 * Non-Diagnostic Evidence Overload: Filling an ACH matrix with generic facts that are consistent with every hypothesis, skewing the visual perception of the data. Mitigation: Rigorous Step 4 pruning (Refining the Matrix) to isolate and retain only highly diagnostic evidence.
 * Anchoring Bias: Refusing to significantly update hypothesis probabilities when new, contradictory evidence arrives. Mitigation: Implementing iterative re-evaluation triggers or utilising Bayesian updating models.
Template Design Notes
 * Research Context: Adopt a refutational, objective epistemic stance, instructing the AI to actively try to disprove theories.
 * Analytical Framework: The prompt must instruct the AI to build an ACH matrix (via Markdown table) assessing the provided evidence against a minimum of 3 distinct hypotheses.
 * Quality Criteria: Force the AI to calculate an "Inconsistency Score" and explicitly state which pieces of evidence possess the highest diagnosticity.
 * Output Specification: The narrative conclusion must be derived logically from the hypothesis with the fewest inconsistencies, not the most confirmations.
Evidence Quality Assessment
STRONG. Richards Heuer’s foundational work and subsequent intelligence community doctrine on Structured Analytic Techniques represent the absolute bedrock of modern analytical reasoning methodology.
Key Sources
 * Analysis of Competing Hypotheses (Pherson / Heuer):(https://pherson.org/wp-content/uploads/2013/06/06.-How-Does-ACH-Improve-Analysis_FINAL.pdf)
 * Step-by-Step ACH Guide: [https://strukturierteanalysedeutschland.de/2023/03/14/the-structured-analytic-technique-analysis-of-competing-hypotheses-ach/](https://strukturierteanalysedeutschland.de/2023/03/14/the-structured-analytic-technique-analysis-of-competing-hypotheses-ach/)
## META-INSTRUCTIONS: SYNTHESIS & ARCHITECTURE GUIDELINES
1. Cross-Cutting Synthesis: The Quality Backbone
Across all seven domains of analytical infrastructure, a universal "quality backbone" emerges, dictating the non-negotiable elements of professional investigative work. Regardless of whether the investigator is a police detective, a national security intelligence analyst, or an OSINT journalist, three principles remain absolute and must be coded into any AI-assisted investigation template:
 * Strict Provenance and Lineage: Data must never be divorced from its origin. In entity databases, this manifests as Create Date and Create User metadata. In case tracking, it requires cryptographic hashing of digital evidence. In reporting, it demands upfront source summaries. An AI template must never generate a fact without a contiguous semantic link to its source.
 * Epistemic Transparency (Confidence vs. Likelihood): Every professional tool forces the analyst to separate what the evidence says from how much they trust it. The Admiralty system handles the trust of the source, while ICD 203 handles the likelihood of the output. AI templates must structurally separate data ingestion validation from analytical output probability.
 * Auditable Logic: Investigations are defined by their transparency of process. Whether via Case Decision Logs (utilising PLAN/STEEPLES frameworks) or the ACH matrix, the infrastructure is designed not just to record the final answer, but to immutably record the discarded alternatives. This is what distinguishes a formal investigation from mere search engine usage; an AI prompt must force the documentation of negative decisions and rejected hypotheses.
2. Tool Dependency Map
The analytical tools operate in a sequential, highly interdependent graph. Constructing tools out of order leads to analytical failure.
| Sequence | Tool Category | Dependency Role | Feeds Into |
|---|---|---|---|
| 1 (Foundation) | Case Tracking & Management | Defines the scope (Intelligence Requirements), justifies proportionality, and establishes evidence vaults. | All subsequent tools. |
| 2 (Filter) | Source Evaluation | As raw data enters, it passes through an epistemic filter (e.g., Admiralty 6x6) to prevent database poisoning. | Entity Databases. |
| 3 (Repository) | Entity Databases | Evaluated data is parsed into nodes and edges via entity resolution. | Link Analysis, Timelines. |
| 4 (Processing) | Link Analysis & Timelines | Structured entities are mapped relationally (Link Charts) and chronologically (Timelines) to identify patterns and gaps. | Hypothesis Tracking. |
| 5 (Reasoning) | Hypothesis Tracking | The outputs of timelines and link charts serve as the "Evidence" row in the ACH matrix, rigorously testing theoretical explanations. | Briefing Formats. |
| 6 (Delivery) | Briefing Formats | The surviving hypothesis, appended with ICD 203 confidence language and source summaries, is generated as the final output. | Client / Decision Maker. |
3. Standardisation Spectrum
| Tool Category | Standardisation Level | Dominant Standard | Template Feasibility |
|---|---|---|---|
| Source Evaluation | HIGH | Admiralty 6x6 Matrix | High. Templates can strictly enforce matrix logic. |
| Briefing Formats | HIGH | ODNI ICD 203 / UK MG5  | High. Templates can enforce BLUF and 7-tier language. |
| Hypothesis Tracking | HIGH | ACH Methodology | High. Templates can generate markdown matrices. |
| Link Analysis | MODERATE | IALEIA / SNA Centrality  | Moderate. Text-based AI struggles with visual drawing but can output edge-lists. |
| Case Tracking | MODERATE | College of Policing CDL | Moderate. Requires adaptation for specific jurisdictions. |
| Entity Databases | WEAK | Fragmented (NIEM vs Vendor) | Low/Custom. Requires building a bespoke prompt ontology. |
| Timelines | WEAK | Fragmented (DFIR vs OSINT) | Moderate. Requires strict UTC normalisation prompts. |
4. Community Convergence Map
All professional communities converge on the fundamental necessity of objective analysis, verifiable sourcing, and mitigation of cognitive bias. However, they diverge irreconcilably on the handling of intelligence collection and entity resolution. Law enforcement demands strict digital chain-of-custody and deterministic entity resolution for legal prosecution. Corporate intelligence tolerates probabilistic matching to scale massive datasets quickly. Journalism prioritises digital verification over human source history to protect whistleblowers.
Recommendation for AI Templates: The Intelligence Community (IC) approach serves as the best default architecture. It bridges the gap by employing rigorous analytical logic (ACH, ICD 203) while remaining flexible enough to ingest the unstructured OSINT data that rigid law enforcement systems often reject due to evidentiary concerns.
5. Gap Register
 * OSINT Source Evaluation Gap: The Admiralty 6x6 system fails when applied to anonymous digital OSINT (e.g., an unverified account posting a real, geolocatable video). Design Requirement: A modified evaluation template blending Admiralty grading for human sources with Bellingcat's digital verification metrics for data.
 * Uncertainty Visualisation Gap: Text-based AI models struggle to generate visual link charts or timelines with nuanced uncertainty markers (like dashed lines). Design Requirement: Templates must output strict, pre-formatted Markdown tables or Mermaid.js syntax that explicitly codes for "Unconfirmed" edges to preserve doubt visually.
 * Schema Extensibility Gap: Rigid databases fail when new tech emerges (e.g., crypto). Design Requirement: Entity templates must allow for ad-hoc property creation.
6. Recommended Template Set
 * Entity Extraction & Profiling Template: Inputs raw text; Outputs NIEM-inspired JSON/Markdown tables categorising entities. Enforces deterministic matching keys.
 * Case Decision & Collection Log Template: Inputs user goals; Outputs an Intelligence Collection Plan and STEEPLES/PLAN decision log.
 * Analytical Briefing Generator Template: Inputs raw findings; Outputs an ICD 203 compliant BLUF report using strict 7-tier probability language.
 * Network Architecture (Edge List) Template: Inputs entity relationships; Outputs structured tabular data identifying Central Hubs and Bridge Nodes suitable for SNA import.
 * Chronological Matrix Template: Inputs disjointed events; Outputs a UTC-normalised timeline highlighting gaps and resolving timezone conflations.
 * Source & Credibility Grader Template: Inputs URLs/documents; Outputs an Admiralty 6x6 score and OSINT verification status.
 * Analysis of Competing Hypotheses (ACH) Template: Inputs evidence and theories; Outputs a fully calculated ACH matrix identifying the most diagnostic evidence and the lowest inconsistency score.
7. Investigation Toolkit Model
A fully equipped investigation workspace requires an orchestration layer. The Minimum Viable Toolkit begins with the Case Log (to define the scope and legal proportionality) and the Source Grader (to filter garbage data at the gate). As collection proceeds, the Entity Extractor and Chronological Matrix operate in parallel to populate the analytical workspace with structured nodes and temporal events. Finally, before any conclusions are drawn, the ACH Template acts as a mandatory cognitive checkpoint to destroy confirmation bias. The surviving hypothesis is seamlessly fed into the Briefing Generator, ensuring that the final output is defensible, objective, and meticulously sourced.
