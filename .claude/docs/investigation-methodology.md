# OSINT Investigation Methodology Landscape Survey: Standard Frameworks, Source Hierarchies, and Template Architecture Across Eight Intelligence Domains

**Research Conducted:** March 2026  
**Research Type:** Landscape Survey + Methodology Design  
**Objective:** Map standard methodologies, source hierarchies, analytical frameworks, report structures, and quality criteria used across OSINT investigation domains to inform construction of reusable investigation prompt templates

***

## Executive Summary

This research maps the current state of Open-Source Intelligence (OSINT) investigation methodology across eight domains: People Investigation, Business Intelligence, Social Media Intelligence, Financial Intelligence, Digital Forensics, Geospatial Intelligence, Cryptocurrency Investigation, and Threat Intelligence. The objective is not to conduct OSINT investigations, but to research HOW such investigations are structured, documented, and reported — thereby enabling the construction of reusable investigation prompt templates.

**Key Findings:**

**Universal Methodological Elements**: All OSINT domains share a common foundational structure built on the intelligence cycle (Direction, Collection, Processing, Analysis, Dissemination), hierarchical source evaluation, quality criteria frameworks, and standard report structures. This provides a base template architecture that can be inherited across all domain templates.

**Domain-Specific Variations**: While sharing common foundations, each domain exhibits distinct source hierarchies, analytical frameworks, and quality standards. Geospatial intelligence prioritises satellite imagery and geolocation verification, cryptocurrency investigation emphasises blockchain analysis and wallet clustering, whilst threat intelligence centres on MITRE ATT&CK frameworks and indicator management.

**Professional Community Divergence**: Law enforcement, journalism, corporate due diligence, and academic research communities structure the same investigation types differently. Law enforcement prioritises evidentiary standards and chain of custody, journalism emphasises verification and source protection, corporate focuses on risk assessment and compliance, whilst academic research prioritises reproducibility and ethical review.

**Evidence Quality Spectrum**: Methodology maturity varies significantly. **STRONG evidence** exists for Threat Intelligence (MITRE ATT&CK framework), Geospatial Intelligence (NGA GEOINT Basic Doctrine), and Cryptocurrency Investigation (established blockchain analysis methodologies). **MODERATE evidence** characterises Social Media Intelligence, Digital Forensics, and Financial Intelligence domains. **EMERGING evidence** appears in People Investigation ethics frameworks and Business Intelligence standardisation.

**Template Architecture Requirements**: Based on cross-domain analysis, investigation templates require five universal components: (1) Research Context (role assignment, epistemic stance, domain framing), (2) Task Specification (research questions, search strategy, domain coverage), (3) Quality Criteria (source hierarchy, evidence standards, validation rules), (4) Analytical Framework (synthesis method, contradiction handling, gap identification), and (5) Output Specification (report structure, format, deliverables, metadata).

**Critical Gaps Identified**: Absence of standardised report structures for people investigation, limited published methodology for beneficial ownership investigation outside FATF guidance, sparse academic literature on SOCMINT analytical frameworks, and inconsistent quality criteria across financial intelligence practices.

***

## DOMAIN 1: People Investigation & Entity Research

### Investigation Methodology

People investigation and entity research represents one of the most ethically sensitive OSINT domains, yet exhibits **EMERGING** evidence quality with limited institutional standardisation. The Berkeley Protocol on Digital Open Source Investigations provides the most comprehensive ethical and methodological framework, establishing principles of safety, accuracy, dignity, responsibility, and proportionality. However, this framework addresses human rights investigations specifically and may not fully translate to commercial or law enforcement contexts.

The OSINT intelligence cycle applies universally: Direction (defining research objectives and scope), Collection (gathering information from prioritised sources), Processing (organising and structuring data), Analysis (evaluating reliability and synthesising findings), and Dissemination (producing reports tailored to stakeholder needs). Within people investigation, this cycle must incorporate additional ethical review at each stage to ensure proportionality, purpose limitation, and data minimisation consistent with privacy law.

Professional practice varies significantly by sector. Law enforcement people investigation prioritises evidentiary admissibility, chain of custody documentation, and compliance with investigative powers legislation. Journalistic background research emphasises verification through multiple independent sources, protection of subject dignity, and public interest justification. Corporate due diligence focuses on risk assessment, regulatory compliance (particularly sanctions screening and politically exposed persons identification), and commercial relevance. Academic research requires ethical review board approval, informed consent considerations, and methodology documentation for reproducibility.

### Source Hierarchy

People investigation source hierarchies exhibit professional community variation, but consensus emerges around core tiers:

**Tier 1 - Official Government Records** (highest reliability): Electoral registers, company director registrations, land registry records, professional licensing databases, court judgments, bankruptcy registers. These sources provide legally verified identity information with auditability.

**Tier 2 - Verified Commercial Databases**: Credit reference agency data, corporate registry aggregators (Companies House, OpenCorporates), professional networking platforms with verified credentials (LinkedIn with identity confirmation), news archives from established outlets. Reliability depends on verification protocols and update frequency.

**Tier 3 - Social Media and Self-Published Content**: Personal social media profiles, blogs, forum participation, online reviews. Requires cross-verification as content may be misleading, outdated, or deliberately false. Authentication crucial.

**Tier 4 - Secondary Commentary**: News aggregation sites, gossip columns, unverified user-generated content, anonymous forums. Lowest reliability; useful for hypothesis generation but requires corroboration before inclusion in findings.

**Tier 5 - Data Breach and Leaked Information**: Credential leaks, hacked databases, document dumps. Legal and ethical constraints apply; many jurisdictions prohibit use of unlawfully obtained information regardless of public availability. Commercial OSINT providers explicitly exclude such sources to maintain compliance.

Jurisdictional coverage varies significantly. UK investigators access comprehensive electoral registers and Companies House director information. US investigators utilise extensive court records and property registries but face more limited beneficial ownership transparency. EU investigators must navigate GDPR restrictions on personal data processing.

### Standard Report Structure

No universally adopted standard exists for people investigation reports, representing a **critical gap**. However, analysis of practitioner outputs and professional body guidance reveals common structural elements:

**Executive Summary** (1-2 paragraphs): Subject identity confirmation, investigation scope, key findings summary, significant risk indicators.

**Subject Profile**: Full name and known aliases, date and place of birth (if ascertainable), current and historical addresses, nationality and residency status, family relationships (where relevant to investigation purpose).

**Professional Background**: Employment history from verified sources, professional qualifications and licenses, company directorships and shareholdings, industry affiliations and memberships.

**Financial Indicators**: Property ownership, company ownership structures, known business interests, bankruptcy or insolvency history, sanctions screening results, politically exposed person status.

**Legal History**: Civil litigation (as claimant or defendant), criminal convictions (where legally accessible), regulatory enforcement actions, professional disciplinary proceedings.

**Digital Footprint**: Social media presence analysis, website ownership, domain registrations, online business activities, digital reputation assessment.

**Association Mapping**: Network visualisation showing relationships to other individuals, companies, and organisations. Link analysis showing nature of relationships (familial, commercial, professional).

**Source Registry**: Complete list of sources consulted with URLs, access dates, and reliability ratings. Critical for auditability and verification.

**Caveats and Limitations**: Explicit statement of information not found, sources not accessible, assumptions made, and confidence levels for key findings.

Report tone varies by professional context. Law enforcement reports emphasise factual, neutral language with careful distinction between established facts and inferences. Journalistic reports may incorporate narrative elements whilst maintaining verification standards. Corporate due diligence reports focus on risk assessment and may include recommendation sections.

### Analytical Framework

People investigation analysis centres on **relationship mapping**, **timeline construction**, and **risk assessment**. The lack of standardised analytical frameworks represents another gap, though practitioners converge on common approaches.

**Link Analysis**: Mapping connections between individuals, organisations, and events using network visualisation tools (Maltego, i2 Analyst's Notebook). Analysis identifies direct relationships (family, employment, partnership) and indirect relationships (shared addresses, common associates, overlapping company networks). Clustering techniques reveal hidden networks and potential collusion.

**Timeline Analysis**: Constructing chronological sequences of events, appointments, transactions, and movements. Temporal analysis identifies patterns, contradictions, and critical periods requiring deeper investigation. Cross-referencing timelines from multiple sources reveals inconsistencies requiring resolution.

**Source Triangulation**: Applying the three-source rule where possible — independent corroboration of key facts from three distinct sources before treating as established. When corroboration unavailable, explicit confidence qualifiers applied (e.g., "single source, unverified", "corroborated by two independent sources").

**Contradiction Resolution**: When sources disagree, investigators assess source reliability, recency, and position relative to the fact in question. Primary sources (direct observation) outweigh secondary sources (reportage). Recent sources generally outweigh historical sources unless documenting past states. Explicit notation of unresolved contradictions required rather than arbitrary selection.

**Risk Scoring**: Corporate due diligence commonly applies risk rating frameworks assessing reputational risk, regulatory risk, sanctions risk, and association risk. Scoring remains largely proprietary with limited published methodology. Academic research into risk scoring sparse.

### Key Databases & Tools

**People Search Platforms**: Pipl, Spokeo, PeopleFinders (US-focused), 192.com (UK). Aggregate public records, social media, and commercial data. Reliability variable; verification essential.

**Social Media Intelligence Tools**: Social-Searcher, Hootsuite, Brand24 for monitoring and archival. Maltego Social Transforms for relationship mapping. Platform-native search (Twitter/X Advanced Search, Facebook Graph Search where available).

**Company Registry Services**: OpenCorporates (global aggregator, 200+ million companies), Companies House (UK), SEC EDGAR (US), national registries (variable access).

**Court Records**: PACER (US federal courts), National Archives (historical records), Courtlistener (US case law), BAILII (British and Irish case law), national court websites.

**Professional Licensing Databases**: General Medical Council (UK doctors), Solicitors Regulation Authority (UK solicitors), state bar associations (US lawyers), professional body membership directories.

**Property and Land Registries**: Land Registry (England/Wales), Registers of Scotland, various US county registries, Zoopla/Rightmove for UK property transaction history.

**Sanctions and PEP Screening**: OpenSanctions (consolidates 245 global sources), OFAC SDN List, EU Sanctions List, UN Security Council Sanctions List, World-Check (commercial).

**Archival Tools**: Wayback Machine (Internet Archive), Archive.today, Hunchly (browser extension for evidence collection and chain of custody).

### Quality Criteria & Verification

Quality standards for people investigation remain largely practitioner-driven rather than institutionally codified. The Berkeley Protocol provides the most authoritative framework, establishing six core principles:

**Safety**: Investigations must not place subjects, investigators, or sources at risk of harm. Operational security (OPSEC) protocols protect investigator identity when researching hostile actors. Source protection protocols prevent exposure of confidential informants.

**Accuracy**: Claims require evidential support. Distinguish between established facts, reasonable inferences, and speculation. Apply appropriate confidence qualifiers (confirmed, probable, possible, unconfirmed).

**Dignity**: Subjects retain human rights regardless of alleged wrongdoing. Avoid unnecessary intrusion into private life unrelated to legitimate investigation purpose. Proportionality assessment required: information gathering must be proportionate to investigation objective.

**Responsibility**: Investigators accountable for methodology, findings, and potential harms. Document decision-making process. Maintain audit trail enabling independent verification.

**Transparency**: Methodology must be documentable and reproducible. Sources must be citeable (whilst protecting confidential informants). Limitations and gaps explicitly stated.

**Purpose Limitation**: Data collection limited to information relevant to defined investigation purpose. Function creep (expanding investigation beyond original scope) requires explicit justification.

**Source Reliability Assessment** employs various frameworks. The NATO Admiralty Code rates sources (A = completely reliable to F = unreliable) and information (1 = confirmed to 6 = cannot be judged). The similar 5x5 matrix appears in law enforcement contexts. However, application remains inconsistent across practitioners.

**Verification Protocols** vary by claim type. Identity verification requires government-issued identification cross-referenced with electoral register or similar. Employment claims verified through company confirmation, LinkedIn verification, or professional body membership. Property ownership verified through land registry. Association claims require multiple independent confirmations or documentary evidence (company filings showing shared directorships).

### Failure Modes & Mitigations

**Common Failure Modes**:

1. **Identity Confusion**: Confusing subjects with similar names. **Mitigation**: Require multiple confirming identifiers (date of birth, address, unique reference numbers).

2. **Outdated Information**: Presenting historical information as current. **Mitigation**: Date-stamp all information, explicitly note currency, prioritise recent sources.

3. **Circular Reporting**: Multiple sources reporting the same underlying original source, creating false corroboration. **Mitigation**: Trace claims to primary sources, identify unique sources vs echoes.

4. **Confirmation Bias**: Seeking information confirming pre-existing hypothesis whilst ignoring contradictory evidence. **Mitigation**: Actively seek disconfirming evidence, document contradictions, apply devil's advocate analysis.

5. **Scope Creep**: Investigating beyond proportionate necessity. **Mitigation**: Maintain clear purpose limitation statement, require justification for scope expansion, periodic relevance review.

6. **Privacy Violations**: Collecting personal data without lawful basis. **Mitigation**: GDPR compliance review, purpose limitation enforcement, data minimisation, legal basis documentation.

7. **Source Reliability Failures**: Treating unreliable sources as authoritative. **Mitigation**: Mandatory source rating, three-source rule for critical claims, explicit reliability qualifiers.

8. **Inadequate Documentation**: Insufficient audit trail preventing verification. **Mitigation**: Real-time evidence collection (Hunchly), source registry maintenance, screenshot archival with metadata.

### Template Design Notes

People investigation templates must incorporate:

- **Mandatory ethical review checkpoint** before investigation commencement assessing proportionality, purpose limitation, and legal basis under privacy law.
- **Source hierarchy hardcoded** with Tier 1-5 structure and reliability ratings.
- **Verification protocols** specifying minimum corroboration requirements for different claim types (identity, employment, associations, property).
- **Output structure** with mandatory sections: Subject Profile, Professional Background, Financial Indicators, Legal History, Association Mapping, Source Registry, Caveats.
- **Quality checklist** ensuring Berkeley Protocol principles addressed: safety, accuracy, dignity, responsibility, transparency, purpose limitation.
- **Customisable elements**: Investigation scope (personal vs professional focus), depth of association mapping (1-degree vs 2-degree connections), jurisdiction (determines accessible records).

### Evidence Quality Assessment

**EMERGING** — Limited institutional standardisation. Berkeley Protocol provides ethical framework but lacks detailed methodological specification. UK College of Policing guidance needed but not found. ACFE standards focus on fraud investigation specifically. Gap in comprehensive people investigation methodology guidance. Practitioner-driven approaches dominant but lack formal validation.

### Key Sources

1. Berkeley Protocol on Digital Open Source Investigations
2. OSINT Framework (methodology overview)
3. Commercial due diligence OSINT practices
4. GDPR compliance in OSINT investigations

***

## DOMAIN 2: Business Intelligence & Corporate Investigation

### Investigation Methodology

Corporate investigation methodology exhibits **MODERATE** evidence quality with stronger institutional frameworks than people investigation, particularly regarding beneficial ownership transparency. The Financial Action Task Force (FATF) Recommendation 24 and its Interpretive Note establish global standards requiring countries to prevent misuse of legal persons for money laundering or terrorist financing, ensuring adequate, accurate, and up-to-date beneficial ownership information.

Practitioner frameworks divide corporate OSINT into distinct investigation types: **competitive intelligence** (market positioning, strategy, capabilities assessment), **due diligence** (risk assessment prior to transactions or partnerships), **corporate transparency** (beneficial ownership, control structures, governance), and **supply chain mapping** (upstream and downstream relationships, dependencies, vulnerabilities).

The OSINT intelligence cycle applies with domain-specific adaptations. **Direction** phase defines whether investigation focuses on reputational risk, financial stability, sanctions exposure, beneficial ownership, competitive positioning, or supply chain resilience. **Collection** prioritises official company registries, financial filings, and beneficial ownership databases over less reliable sources. **Processing** structures data into corporate hierarchy visualisations, ownership chains, and financial trend analysis. **Analysis** applies red flag detection, peer comparison, and network analysis. **Dissemination** tailors outputs to stakeholder needs (investment committee, compliance team, investigative journalist).

Corporate intelligence professionals distinguish between **competitive intelligence** (ethical, using only public sources) and **industrial espionage** (illegal, involving unauthorised access). Professional bodies including Strategic and Competitive Intelligence Professionals (SCIP) maintain ethical codes prohibiting misrepresentation, unauthorised system access, and breach of confidentiality.

### Source Hierarchy

Corporate investigation source hierarchies exhibit stronger consensus than people investigation:

**Tier 1 - Statutory Filings and Official Registers** (highest reliability): Company formation documents, annual financial statements, beneficial ownership registers, charges and mortgages registers, insolvency records. Legally mandated with penalties for false filing. Examples: Companies House (UK), SEC EDGAR (US), national company registries globally.

**Tier 2 - Regulated Disclosures**: Stock exchange announcements (for listed companies), prospectuses, takeover documentation, major shareholding notifications. Regulatory oversight ensures accuracy. False statements carry criminal liability.

**Tier 3 - Financial Databases and News Services**: Bloomberg, Capital IQ, Orbis (Bureau van Dijk), PitchBook, Crunchbase. Aggregate and standardise regulatory filings. Add value through analytics and peer comparison. Reliability high but dependent on underlying regulatory data quality.

**Tier 4 - Verified Media and Industry Publications**: Established financial press (Financial Times, Wall Street Journal, Reuters), trade publications, analyst reports. Editorial standards provide reliability safeguard. Requires verification of factual claims through primary sources.

**Tier 5 - Company Communications**: Corporate websites, press releases, marketing materials, social media. Inherently promotional. Useful for understanding company narrative but requires critical evaluation and independent verification.

**Tier 6 - Social Signals and Unverified Commentary**: Anonymous forums, review sites, social media commentary, gossip. Lowest reliability. May indicate areas requiring further investigation but never cited as authoritative evidence.

**Specialised Tier - Leak Databases**: ICIJ Offshore Leaks, Panama Papers, Paradise Papers, Pandora Papers. Legally complex. Journalistic organisations treat as authentic following forensic verification. Commercial investigators often prohibited from using leaked data. Legal risk varies by jurisdiction.

Jurisdictional transparency varies dramatically. UK Companies House provides comprehensive, freely accessible company information including director details, shareholdings, and financial accounts for most companies. US SEC filings cover public companies extensively but private company information sparse. EU beneficial ownership registers exhibit variable implementation of 5th Anti-Money Laundering Directive requirements. Offshore jurisdictions (BVI, Cayman Islands, Panama) historically opaque but improving under international pressure.

### Standard Report Structure

Corporate investigation reports exhibit more standardisation than people investigation, particularly in due diligence context:

**Executive Summary**: Company identity and jurisdiction, investigation scope and methodology, key findings summary (risk rating where applicable), significant red flags or concerns, recommendation (where appropriate: proceed, proceed with caution, do not proceed).

**Company Overview**: Full legal name and registration number, jurisdiction of incorporation, date of incorporation, registered office address, business activities and industry classification, corporate group structure (parent/subsidiaries if applicable), key personnel (directors, officers, significant shareholders).

**Ownership and Control**: Shareholding structure with percentages, beneficial owners meeting materiality thresholds (typically 25%+ in EU, 10%+ in some jurisdictions), nominee arrangements and their disclosed principals, complex ownership structures (trusts, foundations, bearer shares where still permitted), ultimate beneficial ownership (natural persons at the end of ownership chains), changes in ownership and control over time.

**Financial Analysis**: Summary financial statements (revenue, EBITDA, profit, assets, liabilities, equity) with multi-year trends, key financial ratios (profitability, liquidity, leverage, efficiency), peer comparison against industry benchmarks, going concern indicators, audit opinion and auditor identity, notable transactions or balance sheet items requiring explanation.

**Legal and Regulatory**: Litigation history (civil claims, regulatory enforcement), insolvency proceedings (current or historical), regulatory licenses and compliance status, sanctions screening (company and related parties), politically exposed person connections, adverse media (corruption allegations, financial crime, reputational issues).

**Network Analysis**: Relationships with other companies (suppliers, customers, joint ventures), shared directors or shareholders with other entities, registered office sharing (potential virtual office or nominee arrangement), common advisors (lawyers, accountants) suggesting coordination.

**Red Flag Assessment**: Shell company indicators (no substantive operations, minimal or no employees, registered office at commercial formation agent, frequent changes of officers/address), circular ownership (entities ultimately owning themselves through complex chains), high-risk jurisdictions in ownership chain, inconsistencies between stated business and financial profiles, use of bearer shares or nominee arrangements without disclosure.

**Source Documentation**: Complete source list with access dates and URLs, methodology explanation, limitations and information gaps, confidence levels for key findings.

Corporate transparency investigations (journalistic) may adopt alternative structures focusing on narrative reconstruction of complex corporate networks, whereas competitive intelligence briefs emphasise strategic capabilities and market positioning over ownership structures.

### Analytical Framework

Corporate investigation analysis employs several established frameworks:

**Corporate Structure Mapping**: Visualising corporate groups, subsidiaries, affiliates, and special purpose vehicles. Identifying control chains from ultimate beneficial owners through intermediate holding companies to operating entities. Tools: Orbis, OpenCorporates API, LittleSis for politically connected entities.

**Beneficial Ownership Tracing**: Following ownership chains through nominee shareholders, trusts, foundations, and offshore vehicles to identify natural persons exercising ultimate control. Particular focus on circular ownership, bearer shares, and jurisdictions with limited transparency. FATF Recommendation 24 compliance assessment.

**Financial Trend Analysis**: Multi-year revenue, profitability, and leverage trends. Peer comparison using industry-specific metrics. Going concern assessment examining liquidity, debt covenants, and auditor opinions. Red flag detection: unexplained volatility, inconsistent margins, related party transactions at non-market terms.

**Red Flag Detection Frameworks**: Multiple proprietary and institutional frameworks exist. Common indicators include: (1) Corporate structure red flags: excessive use of shell companies, offshore vehicles without business rationale, circular ownership, bearer shares, frequent changes of structure; (2) Financial red flags: unexplained cash movements, related party transactions, inconsistent revenue/employee ratios, losses inconsistent with stated business success; (3) Officer/director red flags: convicted directors, disqualified directors, directors of multiple unrelated companies, nominee directors; (4) Jurisdictional red flags: incorporation in secrecy jurisdictions without operational justification, migration between jurisdictions, use of countries with weak anti-money laundering frameworks.

**Network Analysis**: Identifying clusters of related entities through shared officers, shareholders, addresses, or service providers. Detecting potential nominee arrangements when same individuals appear as directors/shareholders of numerous unconnected companies. Mapping supply chains to identify dependencies and vulnerabilities.

### Key Databases & Tools

**Company Registry Aggregators**: OpenCorporates (200+ million companies across 140+ jurisdictions, API access for automation), Orbis/Amadeus (Bureau van Dijk, 400+ million companies, financial data, ownership), Dun & Bradstreet (business intelligence, credit ratings), GlobalDatabase (international company data).

**National Registers**: Companies House (UK, free access, extensive data), SEC EDGAR (US public companies, comprehensive filings), Bundesanzeiger (Germany), INPI (France), national equivalents. Variable access costs and data completeness.

**Beneficial Ownership Registers**: UK Persons of Significant Control (PSC) Register (freely accessible), EU national registers (5AMLD implementation variable), OpenOwnership (aggregates and standardises beneficial ownership data globally, currently 20+ million records).

**Financial Data Platforms**: Bloomberg Terminal (institutional, comprehensive but expensive), FactSet, Refinitiv, Capital IQ (S&P), PitchBook (private equity/venture capital focus), Crunchbase (startup funding data).

**Sanctions and PEP Screening**: World-Check (Refinitiv, comprehensive, expensive, 5+ million profiles), OpenSanctions (open source, 245 source consolidation), Dow Jones Risk & Compliance, ComplyAdvantage.

**Leak Databases**: ICIJ Offshore Leaks Database (searchable, 810,000 offshore entities from multiple leaks), OpenCorporates Officers interface (links individuals to companies globally), DocumentCloud (investigative journalism document repository).

**Court Records**: Commercial court databases, insolvency registers, land registries (for corporate property ownership), procurement databases (government contract awards).

**Network Visualisation**: Maltego (link analysis, transforms for company data), Linkurious (graph database visualisation), i2 Analyst's Notebook (law enforcement standard), Gephi (open source, academic).

### Quality Criteria & Verification

Corporate investigation quality standards derive from multiple sources:

**FATF Standards**: Recommendation 24 requires adequate, accurate, and up-to-date beneficial ownership information. Countries must ensure competent authorities can access such information timely. Verification requirements: companies must obtain and hold beneficial ownership information, competent authorities must verify accuracy.

**Due Diligence Standards**: No single universal standard, but convergence around core elements. Enhanced due diligence applies to high-risk jurisdictions, politically exposed persons, and complex ownership structures. Standard due diligence sufficient for lower-risk scenarios. Risk-based approach codified in various regulatory frameworks (UK Bribery Act, US Foreign Corrupt Practices Act, EU Anti-Money Laundering Directives).

**Source Verification Protocols**: Primary sources (statutory filings) require minimal additional verification beyond authenticity confirmation. Secondary sources (news reports, databases) require triangulation against primary sources for material claims. Ownership chains verified through multiple jurisdictions to ensure consistency. Discrepancies between sources documented and investigated.

**Confidence Levels**: Commonly applied framework:
- **Confirmed**: Verified through statutory filing or multiple independent authoritative sources
- **Probable**: Supported by reliable sources but not independently verified through primary documentation  
- **Possible**: Single source or indirect evidence suggesting but not confirming
- **Unconfirmed**: Reported but unable to verify through available sources
- **Disputed**: Contradictory information from sources of similar reliability

**Red Flag Severity Assessment**: **High severity**: Sanctioned individuals/entities in ownership chain, convicted directors, active law enforcement investigations, insolvency proceedings, regulatory enforcement actions. **Medium severity**: Politically exposed persons without disclosed conflict management, high-risk jurisdiction incorporation without clear business rationale, complex ownership obscuring ultimate beneficial owners, adverse media allegations requiring investigation. **Low severity**: Administrative non-compliance (late filings), minor litigation typical for business type, common directorship in unrelated companies.

### Failure Modes & Mitigations

**Common Failure Modes**:

1. **Stopping at Nominee Level**: Identifying nominee directors/shareholders as ultimate beneficial owners without tracing further. **Mitigation**: Mandatory beneficial ownership analysis to natural persons, red flag nominee indicators (multiple directorships, nominee company names, professional nominee services).

2. **Jurisdictional Gaps**: Missing entities in ownership chain registered in jurisdictions not covered by investigation. **Mitigation**: Comprehensive jurisdiction coverage, use of OpenCorporates for broad search, assumption that unexplained gaps indicate higher risk.

3. **Outdated Information**: Presenting historical ownership/financial data as current, particularly problematic when entities restructure frequently. **Mitigation**: Date-stamp all information, prioritise most recent filings, note filing date alongside data points.

4. **Missing Related Party Transactions**: Failing to identify related party transactions that may indicate conflicts of interest or value extraction. **Mitigation**: Detailed notes to financial statements review, network analysis to identify potentially related entities, comparison of transaction terms against market norms.

5. **Confirmation Bias in Red Flag Assessment**: Over-weighting red flags confirming pre-existing suspicion whilst dismissing contradictory evidence. **Mitigation**: Structured red flag framework with severity ratings, active search for exculpatory evidence, peer review of high-risk assessments.

6. **Circular Reporting**: Multiple databases reporting the same underlying primary source, creating false sense of corroboration. **Mitigation**: Trace secondary sources to underlying primary filings, explicitly note when multiple sources derive from single original.

7. **Language Barriers**: Failing to properly translate/interpret corporate documents in foreign languages, particularly in non-Latin alphabets. **Mitigation**: Professional translation for material documents, native-speaker verification for complex legal terms.

8. **Jurisdictional Legal Violations**: Inadvertently violating data protection or privacy laws when accessing corporate information across jurisdictions. **Mitigation**: Legal compliance review for cross-border investigations, adherence to each jurisdiction's access restrictions.

### Template Design Notes

Corporate investigation templates must incorporate:

- **Investigation type selection** (competitive intelligence vs due diligence vs beneficial ownership vs supply chain) determining scope and depth.
- **Jurisdiction specification** hardcoding appropriate national registries and data sources.
- **Risk-based approach** with enhanced due diligence criteria (PEPs, high-risk jurisdictions, complex structures) triggering additional requirements.
- **Red flag framework** with severity ratings and investigation triggers.
- **Beneficial ownership tracing protocol** specifying when investigation stops vs traces further through nominees.
- **Output structure** varying by investigation type: due diligence emphasises risk assessment and recommendation, competitive intelligence emphasises capabilities and market position, transparency investigations emphasise ownership chains and control.
- **Quality checklist**: verified beneficial ownership to natural persons, sanctions screening conducted, financial statements analysed, litigation searched, source documentation complete, confidence levels assigned.

### Evidence Quality Assessment

**MODERATE** — Institutional frameworks exist (FATF Recommendation 24, various national AML regulations) providing standards for beneficial ownership transparency. Practitioner methodologies well-developed in due diligence context. However, limited published methodology from professional bodies. SCIP provides competitive intelligence ethics guidance but minimal methodological specification. Gap in comprehensive corporate investigation methodology comparable to academic research methodology standards. Practice outpaces published standards.

### Key Sources

1. FATF Recommendation 24 on Beneficial Ownership
2. Corporate investigation OSINT checklists
3. OpenCorporates and corporate registry methodologies
4. Commercial due diligence OSINT practices

***

## DOMAIN 3: Social Media Intelligence (SOCMINT)

### Investigation Methodology

Social Media Intelligence (SOCMINT) represents a subset of OSINT focused specifically on intelligence gathering from social media platforms. Evidence quality is **MODERATE**, with strong practitioner methodologies (particularly from Bellingcat and verification organisations) but limited formal institutional standardisation.

The JAPAN principle provides a practitioner framework for SOCMINT classification: **Judicious** (ethical use respecting platform terms of service), **Analytical** (applying structured analysis rather than confirmation bias), **Passive** (observation without interaction reducing detection risk), **Actionable** (producing usable intelligence), and **Notable** (documenting significant findings).

Verification and authentication represent the defining characteristic distinguishing professional SOCMINT from casual social media observation. The Verification Handbook (multiple editions, available in various languages) provides detailed methodologies for authenticating social media content, verifying user accounts, and geolocating media. Bellingcat's extensive resources section includes numerous guides on social media verification techniques, platform-specific search methods, and content authentication.

Professional SOCMINT divides into several investigation types: **identity investigation** (attributing social media accounts to real individuals), **content verification** (authenticating photos, videos, and claims), **network analysis** (mapping relationships and influence patterns), **sentiment analysis** (measuring opinion and emotion), **event monitoring** (tracking real-time developments), and **disinformation research** (identifying coordinated inauthentic behaviour, bot networks, and manipulation campaigns).

Platform evolution creates methodology instability. Features disappear (Twitter/X API access restrictions), privacy settings change, search capabilities decline. SOCMINT methodologies require continuous updating. Professional practitioners maintain updated tool lists and workarounds.

### Source Hierarchy

SOCMINT source hierarchies differ from other OSINT domains due to verification centrality:

**Tier 1 - Verified Accounts with Corroborated Content**: Accounts with platform verification (blue checkmark historically, now more complex), content corroborated through multiple independent sources, posting history consistent with claimed identity, verifiable connection to real-world identity through crossposting or official attribution. Examples: official government accounts, verified news organisations, confirmed public figures.

**Tier 2 - Unverified but Authenticated Accounts**: Accounts without platform verification but authenticated through investigation: consistent posting history over time, content demonstrating specialised knowledge or access, corroboration with known facts, network connections supporting claimed identity. Requires explicit confidence statement.

**Tier 3 - Anonymous Accounts with Verifiable Content**: Account identity unknown but posted content independently verifiable. Examples: eyewitness videos with confirmed geolocation, leaked documents authenticated through forensic analysis, crowdsourced information corroborated by multiple independent sources. Source assessment focuses on content rather than identity.

**Tier 4 - Unverified Anonymous Accounts**: Neither account identity nor content independently verified. Lowest reliability. May serve as investigative leads or hypothesis generators but never cited as authoritative evidence without verification.

**Platform Reliability Considerations**: Some platforms implement stronger identity verification than others. LinkedIn encourages but doesn't require identity verification. Facebook historically had higher barriers to fake accounts than Twitter/X (pre-2022). Platform policy changes affect source reliability over time.

**Archived vs Live Content**: Archived content (via Wayback Machine, Hunchly, screenshots with metadata) more reliable than live content which may be deleted or edited. Best practice: archive content immediately upon discovery with full metadata preservation.

### Standard Report Structure

SOCMINT reports vary significantly by investigation type. **Account attribution reports**, **content verification reports**, and **network analysis reports** require distinct structures:

**Account Attribution Report**:
- Executive Summary: Account identification, attribution confidence level, key evidence summary
- Account Profile: Username/handle, display name, profile information, account creation date, follower/following counts, posting frequency
- Attribution Evidence: Cross-platform account matching, unique identifiers (email, phone number patterns), distinctive content or language patterns, network connections supporting identity claim, real-world verification (employment, location confirmation)
- Content Analysis: Topics, language, geographic focus, temporal patterns
- Confidence Assessment: Confirmed/probable/possible/uncertain attribution
- Source Documentation: Evidence sources, archival URLs, methodology

**Content Verification Report**:
- Executive Summary: Content summary, verification conclusion, confidence level
- Content Description: Original post details, metadata (date, time, location claims), technical characteristics (resolution, format, embedded data)
- Verification Methodology: Reverse image search results, geolocation verification, temporal verification (shadows, weather, historical imagery), source chain analysis
- Findings: Authentic/manipulated/misattributed/indeterminate
- Supporting Evidence: Matching imagery, maps with pinned locations, weather records, corroborating sources
- Confidence Assessment and Caveats

**Network Analysis Report**:
- Executive Summary: Network composition, key influencers, significant patterns
- Methodology: Data collection approach, time period, platforms covered, analysis tools used
- Network Visualisation: Graphs showing connections, influence metrics, clusters
- Key Actors: Central nodes, amplifiers, bridge accounts
- Patterns: Coordination indicators, bot activity, inauthenicity signals
- Narrative Analysis: Dominant themes, hashtag campaigns, amplification mechanisms

Reports for disinformation research incorporate attribution of coordinated inauthentic behaviour, bot detection results, and narrative manipulation techniques identified.

### Analytical Framework

SOCMINT analysis employs several established frameworks:

**Verification Methodology** (as codified by Bellingcat, First Draft/IREX, Verification Handbook):

1. **Source Analysis**: Who posted? Account history? Previous reliability? Claimed expertise? Potential biases or motivations?
2. **Provenance Research**: Original source of content? Chain of transmission? Previous appearances? Watermarks or attribution?
3. **Reverse Image/Video Search**: Google Image Search, TinEye, Yandex, InVID/WeVerify. Identifies earlier appearances, original context, manipulations.
4. **Geolocation Verification**: Identifying precise location through visual cues (buildings, landmarks, signage, terrain), confirming through satellite imagery (Google Earth, Sentinel Hub), cross-referencing historical imagery for temporal consistency.
5. **Chronolocation**: Determining when content created through: shadows (SunCalc for solar position), weather (historical weather data), vegetation (seasonal indicators), temporal landmarks (construction progress, historical satellite imagery comparisons).
6. **Metadata Analysis**: EXIF data (camera, location, date/time if not stripped), platform metadata, edit history where accessible.
7. **Forensic Analysis**: Reverse engineering edits, detecting deepfakes or manipulated content, identifying compression artifacts inconsistent with claimed history.
8. **Corroboration**: Multiple independent sources confirming same event, cross-platform verification, official statements or records.

**Social Network Analysis**: Applying graph theory to map relationships, identify influencers, detect communities, and reveal coordination patterns. Metrics include centrality (identifying key influencers), clustering coefficient (community detection), betweenness (bridge accounts connecting subnetworks). Tools: Gephi, NodeXL, Maltego social transforms.

**Sentiment Analysis**: Computational and manual assessment of emotional tone, opinion distribution, and narrative framing. Distinguishes grassroots sentiment from coordinated campaigns. Machine learning models trained on platform-specific language patterns.

**Coordinated Inauthentic Behaviour (CIB) Detection**: Identifying bot networks, troll farms, and sock puppet accounts through: identical or near-identical content posting, temporal synchronisation (posting at same time), network structure anomalies (artificially inflated follower counts, reciprocal following patterns), content fingerprints (identical hashtag sequences, coordination on engagement).

**Temporal Analysis**: Tracking narrative evolution over time, identifying amplification events, detecting rapid mobilisation patterns suggesting coordination rather than organic spread.

### Key Databases & Tools

**Platform-Native Search**:
- Twitter/X Advanced Search (filtered by date, location, engagement, account type)
- Facebook Graph Search (limited following privacy changes)
- Instagram hashtag and location search
- LinkedIn Boolean search for professional targeting
- TikTok hashtag and sound discovery
- Reddit Boolean search, pushshift.io archives (historical content)
- Telegram channel search and monitoring

**Verification and Analysis Tools**:
- InVID/WeVerify (video verification plugin with reverse search, metadata extraction, forensic filters)
- RevEye (reverse image search across multiple engines)
- TinEye (oldest reverse image search, detects modifications)
- Google Lens (visual matching, text extraction)
- FotoForensics (error level analysis detecting manipulation)
- SunCalc (shadow analysis for temporal and geographic verification)
- Bellingcat's OpenStreetMap Search, Overpass Turbo (geolocation support)

**Social Network Analysis**:
- Gephi (open-source network visualisation)
- NodeXL (Excel-based, Twitter/X focused)
- Maltego (commercial, extensive transforms including social media)
- Brand24, Hootsuite, Social-Searcher (monitoring and analytics)

**Archival and Documentation**:
- Wayback Machine (Internet Archive, historical social media captures)
- Archive.today (on-demand archiving)
- Hunchly (browser extension for evidence collection, maintains chain of custody)
- DownThemAll, youtube-dl (content download for forensic analysis)

**Bot and Automation Detection**:
- Botometer (Indiana University, Twitter bot scoring)
- Hoaxy (Indiana University, tracks claim spread and fact-checking)
- Trends24 (Twitter trending topics by location and time)

### Quality Criteria & Verification

Quality standards for SOCMINT derive primarily from journalistic verification practices and academic integrity guidelines:

**Verification Confidence Levels** (adapted from Berkeley Protocol):
- **Verified**: Content authenticity confirmed through multiple independent methods (geolocation confirmed via satellite imagery, chronology confirmed through shadows/weather, source authenticated through cross-platform verification)
- **Likely Authentic**: Strong but not conclusive verification (single-method geolocation confirmed, source authenticated but content partially verifiable)
- **Cannot Verify**: Insufficient information for verification (indistinct location, no temporal markers, unverifiable source)
- **Likely Manipulated**: Evidence of manipulation (forensic analysis detects edits, content matches earlier context inconsistent with claim, geolocation contradicts claim)
- **Confirmed Manipulated**: Definitive evidence of manipulation (original unedited version found, forensic analysis proves alteration, official debunking)

**Source Reliability Ratings**:
- **Authenticated**: Real-world identity confirmed through multiple methods
- **Corroborated**: Claims consistent with known facts and other reliable sources
- **Unverified**: Insufficient information to authenticate or corroborate
- **Contradicted**: Claims inconsistent with verified information
- **Known Unreliable**: History of false claims or demonstrated manipulation

**Platform Terms of Service Compliance**: Ethical SOCMINT respects platform ToS. Prohibited: creating fake accounts to gain unauthorised access, scraping at scale violating API terms, interacting with subjects to elicit responses (active vs passive intelligence). Legal risk varies by jurisdiction — some platform ToS violations constitute computer misuse offences.

**Privacy and Ethical Considerations**: GDPR applies to personal data from social media. Even publicly accessible personal data requires legal basis for processing. Purpose limitation and data minimisation principles apply. Research ethics review required for academic SOCMINT. Journalistic exemptions may apply for public interest investigations. Corporate SOCMINT must demonstrate legitimate interest.

**Documentation Standards**: Screenshots insufficient — full URL archival with date stamps required. Hunchly or similar tools provide chain of custody documentation defensible in legal proceedings. Methodology documentation enables reproducibility.

### Failure Modes & Mitigations

**Common Failure Modes**:

1. **Attribution Without Verification**: Assuming social media account represents claimed identity without authentication. **Mitigation**: Cross-platform verification, network analysis confirming connections, content analysis for consistency, real-world corroboration where possible.

2. **Context Stripping**: Treating content as representing events claimed without verifying context. **Mitigation**: Reverse image/video search for original context, geolocation and chronolocation verification, corroboration with independent sources.

3. **Circular Verification**: Multiple social media sources reporting the same underlying (unverified) original source, creating false corroboration. **Mitigation**: Trace all sources to original, identify unique vs echo sources, weight only independent confirmations.

4. **Platform Bias**: Over-relying on Twitter/X or English-language platforms whilst missing critical activity on other platforms or languages. **Mitigation**: Multi-platform search strategy, language-specific platform inclusion (VK for Russian language, Weibo for Chinese), translation where necessary.

5. **Temporal Errors**: Applying historical content to current events (old photos misrepresented as recent). **Mitigation**: Reverse image search for earliest appearance, forensic dating through metadata/environmental clues, explicit date attribution in reports.

6. **Bot Misidentification**: Treating bot-generated or coordinated content as organic grassroots activity. **Mitigation**: Apply bot detection tools (Botometer), analyse temporal patterns for coordination, examine network structure for anomalies, content fingerprinting for identical/near-identical posts.

7. **Deepfake/AI-Generated Content**: Treating synthetic media as authentic recording. **Mitigation**: Forensic analysis (FotoForensics, deepfake detection tools), biological implausibility detection (unnatural movements, lighting inconsistencies), corroboration with independent sources.

8. **OPSEC Failures**: Investigator accounts identified and blocked, investigations compromised. **Mitigation**: Sock puppet account management, separate browser profiles, VPN usage, no engagement with subjects, passive observation only.

9. **Terms of Service Violations**: Violating platform ToS creating legal risk. **Mitigation**: Review ToS for each platform, avoid prohibited scraping/automation, obtain legal advice for grey areas, document access methods.

### Template Design Notes

SOCMINT templates must incorporate:

- **Investigation type selection** (identity attribution vs content verification vs network analysis vs sentiment analysis vs disinformation research) determining methodology and output structure.
- **Platform specification** hardcoding relevant search tools and verification methods for each platform.
- **Verification protocol** with multi-step methodology: reverse search, geolocation, chronolocation, metadata analysis, corroboration.
- **Confidence framework** with explicit ratings for source reliability and content authenticity.
- **OPSEC requirements**: sock puppet guidance, passive observation protocols, platform ToS compliance.
- **Output structure** varying by type: attribution reports emphasise identity evidence, verification reports emphasise authentication methodology, network analysis reports emphasise visualisations and influence metrics.
- **Quality checklist**: verification methodology applied, confidence levels assigned, sources archived, OPSEC maintained, ToS compliance verified, privacy law compliance documented.

### Evidence Quality Assessment

**MODERATE** — Strong practitioner methodologies from Bellingcat, verification organisations (First Draft/IREX, Verification Handbook), and Stanford Internet Observatory. EU DisinfoLab and DFRLab provide analytical frameworks for disinformation research. However, limited formal institutional standards. Academic SOCMINT methodology developing but not yet consolidated. Professional body standards (equivalent to ACFE for fraud examination) absent. Practice-driven with strong community knowledge sharing but limited codification.

### Key Sources

1. Bellingcat SOCMINT methodology guides
2. OSINT Framework social media intelligence section
3. JAPAN principle and SOCMINT classification
4. Verification Handbook (multiple editions)

***

## DOMAIN 4: Financial Intelligence & Asset Investigation

### Investigation Methodology

Financial intelligence and asset investigation using open sources exhibits **MODERATE** evidence quality with strong institutional frameworks from Financial Action Task Force (FATF), particularly regarding asset recovery, but variable implementation across jurisdictions.

FATF's 2025 Asset Recovery Guidance and Best Practices provides the most comprehensive methodology framework, covering modern financial investigations, swiftly securing assets, safeguarding rights, and compensating victims with recovered funds. The guidance includes 85+ real-world case examples and recovery techniques from experts across the FATF Global Network.

Financial OSINT investigation types include: **asset tracing** (identifying and locating assets for recovery), **money laundering investigation** (detecting illicit fund flows and identifying beneficial ownership), **sanctions screening** (identifying entities subject to financial sanctions), **suspicious activity analysis** (detecting indicators of financial crime), **due diligence** (pre-transaction risk assessment), and **financial network mapping** (understanding complex corporate and trust structures).

The intelligence cycle applies with domain-specific modifications. **Direction** defines whether investigation focuses on asset recovery, beneficial ownership transparency, sanctions compliance, money laundering detection, or fraud prevention. **Collection** prioritises company registries, land registries, financial regulatory filings, beneficial ownership databases, sanctions lists, and investigative journalism leak databases (ICIJ). **Processing** structures data into ownership chains, transaction flows, and network visualisations. **Analysis** applies red flag detection, network analysis, and financial pattern recognition. **Dissemination** produces reports meeting evidentiary standards for civil litigation, criminal prosecution, or regulatory enforcement.

Professional communities apply different standards. **Law enforcement** prioritises legally admissible evidence, chain of custody, and coordination with financial intelligence units. **Journalism** (ICIJ, OCCRP model) emphasises verification, public interest, and source protection. **Compliance** focuses on regulatory requirements, sanctions screening automation, and risk-based assessments. **Asset recovery practitioners** (civil litigation, insolvency) prioritise locating executable assets and establishing beneficial ownership for enforcement.

### Source Hierarchy

Financial intelligence source hierarchies prioritise official registries and regulatory filings:

**Tier 1 - Official Financial Regulatory Filings**: Securities commission filings (SEC, FCA), banking regulatory submissions, insurance disclosures, pension fund reports. Legally mandated with criminal penalties for false statements. Highest reliability for financial data.

**Tier 2 - Statutory Company and Land Records**: Company formation documents, annual accounts, charges registers (secured lending), land registry records (property ownership), insolvency registers. Legally verified identity and ownership information. Examples: Companies House (UK), Land Registry (England/Wales), SEC EDGAR (US), cadastral registries.

**Tier 3 - Beneficial Ownership Registers and Sanctions Lists**: National beneficial ownership registers (UK PSC, EU registers), FATF-aligned databases, sanctions lists (OFAC SDN, EU Sanctions, UN Security Council), PEP databases (World-Check, OpenSanctions). Quality varies by jurisdiction and verification requirements. OpenSanctions consolidates 245 global sources providing de-duplicated dataset.

**Tier 4 - Investigative Journalism Leak Databases**: ICIJ Offshore Leaks Database (Panama Papers, Paradise Papers, Pandora Papers — 810,000+ offshore entities), OpenLux (Luxembourg beneficial ownership leak), OpenCorporates (aggregates corporate data globally). Authenticity verified by journalism organisations but legal constraints apply to use.

**Tier 5 - Court Records and Legal Proceedings**: Civil litigation records, criminal proceedings, bankruptcy filings, arbitration awards. Reveal asset ownership through disclosure, financial disputes, and enforcement proceedings. Jurisdictional variation in accessibility.

**Tier 6 - Procurement and Contract Databases**: Government contract awards, public procurement records, concession agreements. Reveal revenue sources, business relationships, and potential conflicts of interest. Transparency varies by jurisdiction.

**Tier 7 - Financial Press and Analyst Reports**: Financial Times, Wall Street Journal, Bloomberg, specialist financial press. Useful for context and leads but requires verification through primary sources before treating as established facts.

**Tier 8 - Self-Published Financial Information**: Company websites, press releases, investment prospectuses (for private placements), financial presentations. Inherently promotional. Useful for understanding narrative but requires critical evaluation and independent verification.

Data quality and accessibility varies dramatically by jurisdiction. Switzerland's asset recovery includes blockchain analysis helping trace illicit transactions admitted as reliable evidence in court and confiscation of over CHF 313 million funding population benefits. Conversely, secrecy jurisdictions intentionally limit information availability.

### Standard Report Structure

Financial intelligence report structures vary by investigation purpose:

**Asset Tracing Report**:
- Executive Summary: Subject identity, investigation scope, total assets identified (with confidence levels), significant concealment methods, recommendation for recovery action
- Subject Profile: Full identity details, known aliases, relationships to relevant entities
- Asset Register: Comprehensive list with: asset type (property, bank accounts, securities, business interests, intellectual property), jurisdiction, legal owner, beneficial owner (if different), estimated value, encumbrances, liquidity assessment
- Ownership Structures: Corporate vehicles, trusts, foundations, nominee arrangements, visualised ownership chains from beneficial owner to assets
- Transaction Analysis: Significant transactions, fund flows between related entities, value extraction mechanisms, timing relative to enforcement risk
- Concealment Mechanisms: Offshore vehicles, bearer shares, nominee arrangements, circular ownership, jurisdictional complexity
- Recovery Opportunities: Executable assets by jurisdiction, estimated recovery value, legal obstacles, recommended recovery strategy
- Evidence Documentation: Source list, confidence levels, methodology, audit trail

**Suspicious Activity Analysis Report**:
- Executive Summary: Activity summary, suspicion indicators, risk rating, recommended action
- Activity Description: Transactions, parties involved, amounts, timeframes, business rationale (claimed vs assessed)
- Red Flag Analysis: Structured assessment against financial crime typologies (money laundering, terrorist financing, sanctions evasion, fraud), indicator severity ratings
- Network Analysis: Related parties, beneficial ownership, connection to higher-risk entities
- Source Documentation and Confidence Assessment

**Beneficial Ownership Investigation Report**:
- Executive Summary: Entity identity, ultimate beneficial owners identified (confidence levels), ownership complexity, red flags
- Corporate Structure: Legal entity hierarchy, jurisdictions, formation dates, registered agents
- Ownership Chain: Complete chain from entity to natural persons, percentages at each level, nominee identification, trust beneficiaries
- Control Analysis: Voting rights, veto powers, board composition, actual vs legal control divergence
- Red Flag Assessment: Circular ownership, bearer shares, high-risk jurisdictions, PEP connections, sanctions proximity
- Source Documentation

**Sanctions Screening Report**:
- Executive Summary: Screening results, matches identified, risk assessment, recommendation
- Methodology: Datasets searched, matching parameters, date ranges
- Match Details: Entity screened, matching sanctioned entity, confidence level, designation details (designating authority, date, sanctions measures)
- Risk Assessment: Direct hit vs indirect exposure (ownership, transactions), severity based on sanctions regime
- Mitigation Recommendations

All financial intelligence reports must maintain evidentiary standards if intended for legal proceedings: chain of custody documentation, source authentication, methodology transparency, peer review for complex analyses.

### Analytical Framework

Financial intelligence analysis employs multiple established frameworks:

**FATF Asset Recovery Framework**: Modern financial investigations emphasising: (1) Early asset securing (restraint, freezing, seizure), (2) Comprehensive asset identification (beyond traditional banking to crypto, luxury goods, intellectual property), (3) International cooperation (mutual legal assistance, asset sharing agreements), (4) Victim compensation (returning recovered assets to affected populations).

**Beneficial Ownership Analysis** (FATF Recommendation 24 implementation): Tracing ownership through multiple layers: legal ownership (registered), beneficial ownership (ultimate control), nominee identification (professional nominees, family members), trust structures (settlors, trustees, beneficiaries), foundations and other vehicles. Analysis identifies concealment techniques: circular ownership (entities ultimately owning themselves), bearer shares (untraceable ownership), nominee shareholders obscuring beneficial owners, offshore layering (multiple jurisdictions complicating investigation).

**Red Flag Detection Frameworks** for financial crime indicators:

*Money Laundering Indicators*: Transactions inconsistent with known business, round-sum transactions, structuring (breaking large transactions into smaller amounts below reporting thresholds), rapid movement through multiple jurisdictions, use of high-risk jurisdictions, transactions with no apparent economic purpose, related party transactions at non-market terms.

*Terrorist Financing Indicators*: Small transactions to jurisdictions with terrorism risk, transactions structured to avoid detection, use of charitable organisations as conduits, hawala or informal value transfer systems, currency exchange patterns.

*Sanctions Evasion Indicators*: Use of non-sanctioned subsidiaries or related entities, transactions through jurisdictions with weak sanctions enforcement, complex corporate structures obscuring beneficial ownership, front companies, use of alternative payment systems bypassing correspondent banking.

**Financial Network Analysis**: Mapping relationships between individuals, companies, and financial transactions. Identifying: value extraction (funds flowing from legitimate businesses through related entities to beneficial owners), circular transactions (funds flowing between related entities without economic substance), layering (multiple transactions obscuring original source), integration (illicit funds entering legitimate economy).

**Timeline Analysis**: Constructing chronological sequences of transactions, corporate formations, ownership changes, and related events. Temporal patterns reveal: anticipatory restructuring (asset transfers before enforcement action), coordination (simultaneous actions across multiple entities), response to regulatory scrutiny (sudden changes following inquiries).

**Comparative Analysis**: Benchmarking financial profiles against peer companies or individuals. Unexplained wealth (lifestyle inconsistent with known income), asset accumulation inconsistent with revenue, financial ratios diverging from industry norms.

### Key Databases & Tools

**Company and Ownership Databases**:
- OpenCorporates (200+ million companies, 140+ jurisdictions, API access)
- Orbis (Bureau van Dijk, 400+ million companies, beneficial ownership where available)
- OpenOwnership (beneficial ownership consolidation, 20+ million records)
- National company registries (Companies House UK, SEC EDGAR US, etc.)

**Land and Property Registries**:
- Land Registry (England/Wales), Registers of Scotland
- US county property records (variable digitisation)
- European cadastral registries (variable access)
- Zoopla/Rightmove (UK property transaction prices)

**Sanctions and PEP Screening**:
- OpenSanctions (open source, 245 source consolidation, regularly updated)
- OFAC SDN List (US sanctions)
- EU Consolidated Sanctions List
- UN Security Council Sanctions List
- World-Check (Refinitiv, commercial, comprehensive)
- Dow Jones Risk & Compliance
- ComplyAdvantage

**Leak Databases**:
- ICIJ Offshore Leaks Database (searchable, multiple leak integration)
- OpenLux (Luxembourg beneficial ownership leak)
- FinCEN Files
- Pandora Papers

**Court and Legal Records**:
- PACER (US federal courts)
- Courtlistener (US case law)
- BAILII (British and Irish case law)
- National insolvency registers
- Commercial court databases

**Financial Regulatory Databases**:
- SEC EDGAR (US securities filings)
- Companies House accounts (UK)
- National securities regulators
- Banking regulatory disclosures

**Analytical and Visualisation Tools**:
- Maltego (network analysis, corporate transforms)
- i2 Analyst's Notebook (law enforcement standard, link analysis)
- Palantir (advanced analytics, law enforcement/intelligence use)
- OpenSanctions tooling (matching algorithms, entity resolution)
- Neo4j (graph database for complex relationships)

**Cryptocurrency Tools** (overlaps with Domain 7):
- Blockchain explorers (Blockchain.com, Etherscan)
- Chainalysis (commercial, law enforcement use, transaction tracing)
- Crystal Blockchain, Elliptic (commercial alternatives)
- Breadcrumbs (investigative visualisation)

### Quality Criteria & Verification

**FATF Standards** provide the institutional framework. Countries must implement measures ensuring:
- **Adequate beneficial ownership information**: Companies must obtain and hold accurate, up-to-date information on beneficial owners (natural persons ultimately owning/controlling ≥25% or exercising control through other means)
- **Timely access**: Competent authorities (law enforcement, financial intelligence units, supervisors) must access beneficial ownership information without delay
- **Verification requirements**: Countries must ensure beneficial ownership information is verified (either by companies or competent authorities) to ensure accuracy
- **Sanctions and penalties**: Effective, proportionate, and dissuasive sanctions for companies failing to maintain accurate information

**Evidence Standards for Asset Recovery** (from FATF 2025 guidance):
- **Chain of custody**: Document evidence collection, handling, and analysis. Critical for civil forfeiture and criminal proceedings
- **Blockchain analysis admissibility**: Multiple jurisdictions now accept blockchain analysis as reliable evidence when properly documented. US cases demonstrate tracing over USD 400 million in illicit transactions admitted in court
- **Multi-source corroboration**: Material ownership claims require verification through multiple independent sources (company registries, land registries, court records, sanctions lists)
- **Expert witness standards**: Financial analysis may require expert testimony. Analyst qualifications, methodology transparency, and peer review enhance admissibility

**Source Reliability Assessment**:
- **Statutory filings**: Highest reliability due to criminal liability for false statements. Verification focuses on authenticity (genuine filing vs forgery)
- **Beneficial ownership registers**: Reliability varies by jurisdiction and verification requirements. UK PSC Register relies on self-certification by companies (weakness). Some jurisdictions require notarisation or regulatory verification (stronger)
- **Leak databases**: Authenticity verified by journalism organisations (ICIJ) through forensic document analysis, but legal constraints on use vary by jurisdiction
- **Court records**: High reliability for facts established through adversarial process. Lower reliability for unproven allegations in pleadings

**Confidence Levels**:
- **Confirmed**: Verified through statutory filing or multiple independent authoritative sources, consistent across sources
- **Probable**: Supported by reliable sources (beneficial ownership register, leak database) but not independently verified through statutory filing
- **Possible**: Single source or indirect evidence (corporate structure suggesting beneficial ownership without confirmation)
- **Unconfirmed**: Reported in media or alleged in legal proceedings but unable to verify
- **Contradicted**: Evidence exists contradicting claim

**Red Flag Severity** in financial intelligence:
- **Critical**: Designated sanctions target (direct hit), active law enforcement investigation, confirmed financial crime conviction, unexplained wealth orders
- **High**: Sanctions proximity (ownership/transaction with sanctioned entity), PEP involvement without controls, high-risk jurisdiction incorporation without business rationale, significant unexplained wealth
- **Medium**: Complex ownership obscuring beneficial owners, related party transactions at non-market terms, minor regulatory violations, adverse media requiring investigation
- **Low**: Administrative non-compliance, typical litigation for business type

### Failure Modes & Mitigations

**Common Failure Modes**:

1. **Stopping at Offshore Layer**: Identifying offshore company as owner without tracing to ultimate beneficial owner. **Mitigation**: Mandatory beneficial ownership tracing to natural persons, use of leak databases (Panama Papers, etc.), assumption that untraceable ownership indicates concealment warranting enhanced scrutiny.

2. **Missing Value Extraction**: Failing to identify mechanisms extracting value from legitimate businesses (management fees, related party transactions, intellectual property licensing to offshore entities). **Mitigation**: Transaction analysis, comparison of terms against market norms, identification of related parties through ownership/director overlap.

3. **Jurisdictional Gaps**: Missing assets or entities in jurisdictions not covered by investigation. **Mitigation**: Global company registry search (OpenCorporates), land registry searches in likely jurisdictions (lifestyle analysis suggesting property locations), leaked data providing leads.

4. **Nominee Misidentification**: Treating nominee as beneficial owner. **Mitigation**: Red flag indicators (professional nominee services, multiple unrelated directorships, family members of wealthy individuals), investigation of nominee's background revealing nominee status.

5. **Sanctions Screening Gaps**: Missing sanctions matches due to name variations, transliteration differences, or indirect exposure through ownership. **Mitigation**: Fuzzy matching algorithms, multiple name variant searches, ownership chain screening (not just direct counterparty).

6. **Outdated Information**: Treating historical beneficial ownership or asset ownership as current, particularly problematic when structures deliberately changed to obscure assets. **Mitigation**: Date-stamp all information, prioritise most recent filings, timeline analysis revealing restructuring before enforcement.

7. **Circular Reporting**: Multiple leak databases containing same underlying source document, creating false sense of corroboration. **Mitigation**: Identify primary source document, note when leaks derive from same underlying dataset (e.g., multiple leaks from Mossack Fonseca).

8. **Legal Access Violations**: Accessing information unlawfully or violating data protection law. **Mitigation**: Legal compliance review, use only legally accessible sources, document legal basis for processing, respect jurisdictional access restrictions.

### Template Design Notes

Financial intelligence templates must incorporate:

- **Investigation type selection** (asset tracing vs beneficial ownership vs sanctions screening vs money laundering investigation) determining scope and methodology.
- **Jurisdiction specification** hardcoding appropriate registries, legal frameworks, and sanctions lists.
- **FATF compliance framework** embedding Recommendation 24 beneficial ownership standards and asset recovery best practices.
- **Red flag detection framework** with severity ratings and investigation triggers.
- **Mandatory beneficial ownership tracing** with stopping criteria (traced to natural persons or documented barriers preventing further investigation).
- **Multi-source verification protocol** specifying minimum corroboration requirements for material ownership/asset claims.
- **Output structure** varying by type: asset tracing emphasises asset register and recovery opportunities, beneficial ownership emphasises ownership chains and control analysis, sanctions screening emphasises match analysis and risk assessment.
- **Evidence standards** with chain of custody documentation if intended for legal proceedings.
- **Quality checklist**: beneficial ownership traced to natural persons, sanctions screening conducted, red flags assessed, multi-source verification applied, confidence levels assigned, evidence chain documented.

### Evidence Quality Assessment

**MODERATE** — Strong institutional frameworks from FATF providing global standards for beneficial ownership, asset recovery, and anti-money laundering. FATF 2025 Asset Recovery Guidance represents comprehensive methodology with 85+ case examples. However, implementation varies dramatically by jurisdiction. ICIJ and OCCRP provide investigative journalism methodologies but limited formal standards. Academic literature sparse compared to practice. Professional certifications exist (ACAMS) but methodology guidance limited compared to practice sophistication. Gap between institutional standards and detailed operational methodology.

### Key Sources

1. FATF Asset Recovery Guidance and Best Practices (2025)
2. FATF Recommendation 24 on Beneficial Ownership
3. OpenSanctions methodology and data consolidation
4. Financial investigation OSINT practices

***

## DOMAIN 5: Digital Forensics & Technical Intelligence

### Investigation Methodology

Digital forensics and technical infrastructure investigation using OSINT exhibits **MODERATE** evidence quality with strong technical practitioner methodologies but limited institutional standardisation outside specialised cybersecurity frameworks.

The MITRE ATT&CK framework provides the most comprehensive methodological structure, particularly for reconnaissance tactics (T1590-T1599 in Enterprise matrix). Reconnaissance tactics include: Active Scanning (T1595), Search Open Websites/Domains (T1593), Search Open Technical Databases (T1596), Phishing for Information (T1598 — but outside pure OSINT scope), and Search Victim-Owned Websites (T1594).

Technical OSINT investigation types include: **domain analysis** (investigating domain ownership, history, relationships), **infrastructure mapping** (identifying servers, networks, services, relationships), **certificate analysis** (using certificate transparency logs to find related domains), **attribution** (linking infrastructure to threat actors or organisations), **reconnaissance analysis** (understanding adversary information gathering), and **exposure assessment** (identifying vulnerable or misconfigured systems).

The intelligence cycle applies with technical-specific adaptations. **Direction** defines whether investigation focuses on threat actor attribution, security posture assessment, digital supply chain analysis, or infrastructure mapping. **Collection** uses passive DNS, certificate transparency logs, WHOIS records, port scanning engines (Shodan, Censys), BGP data, and web archives. **Processing** structures data into infrastructure graphs, timeline reconstructions, and change detection. **Analysis** applies clustering (related infrastructure), anomaly detection (unusual configurations), and pattern recognition (infrastructure reuse revealing attribution). **Dissemination** produces technical reports, indicator lists, or threat intelligence feeds.

Professional community variation appears less pronounced than in other domains. Cybersecurity researchers, threat intelligence analysts, law enforcement digital investigators, and penetration testers share substantially overlapping methodologies. Divergence appears mainly in operational constraints (active vs passive techniques, legal authority) rather than fundamental methodology.

### Source Hierarchy

Technical OSINT source hierarchies prioritise technical authoritative sources:

**Tier 1 - DNS and Network Infrastructure Registries**: Authoritative DNS records (queried directly from name servers), WHOIS data from registry operators (not third-party aggregators), Regional Internet Registries (RIPE, ARIN, APNIC, LACNIC, AFRINIC) for IP allocation data, BGP routing data from RouteViews or RIPE RIS. Highest technical reliability.

**Tier 2 - Certificate Transparency Logs**: Public logs of all SSL/TLS certificates (crt.sh, Censys, Certificate Transparency project). Cryptographically authenticated, cannot be retroactively removed. Reveals domain relationships through Subject Alternative Names (SANs).

**Tier 3 - Passive DNS and Historical Data**: SecurityTrails, PassiveTotal, RiskIQ. Aggregates historical DNS resolutions revealing infrastructure changes over time. Reliability depends on data collection coverage and temporal granularity.

**Tier 4 - Internet-Wide Scanning Services**: Shodan (internet-connected device search), Censys (certificate and host data), BinaryEdge (attack surface monitoring), ZoomEye (cyberspace search). Active scanning of public IP space. Reliability high for current state but requires ongoing updates to track changes.

**Tier 5 - Web Archives**: Wayback Machine (Internet Archive), Archive.today. Historical website content, structure, and linked resources. Reliability for content accurate but may miss dynamically loaded content or ephemeral resources.

**Tier 6 - Code Repositories and Paste Sites**: GitHub, GitLab, Bitbucket for code, configuration files, exposed credentials. Pastebin and similar for leaked credentials or configurations. Requires verification — may contain false information or honeypots.

**Tier 7 - Threat Intelligence Sharing Platforms**: VirusTotal (malware and URL scanning), AlienVault OTX (open threat exchange), MISP (malware information sharing), Hybrid Analysis (malware sandbox). Community-contributed intelligence with variable quality. Higher-reputation contributors more reliable.

**Tier 8 - Public Vulnerability Databases**: CVE (Common Vulnerabilities and Exposures), NVD (National Vulnerability Database), vendor security advisories. Authoritative for vulnerability information but identification in wild infrastructure requires scanning or passive observation.

Data recency critical in technical OSINT. Infrastructure changes rapidly (domain reassignment, service reconfigurations, certificate renewals). Date-stamping essential. Historical data valuable for attribution (infrastructure reuse patterns) but current state requires fresh collection.

### Standard Report Structure

Technical OSINT report structures vary by investigation type:

**Domain Analysis Report**:
- Executive Summary: Domain identity, investigation scope, key findings, attribution confidence, risk assessment
- Domain Profile: Domain name, registrar, registration date, expiration date, update history, WHOIS data (registrant if accessible, privacy service if used), name servers, DNS records (A, AAAA, MX, TXT, NS, CNAME)
- Infrastructure: IP addresses (current and historical), hosting provider, ASN, geolocation, reverse DNS, shared hosting neighbours (other domains on same IP)
- Certificate Analysis: Current SSL/TLS certificate, issuer, validity period, Subject Alternative Names (related domains), historical certificates, self-signed vs CA-issued
- Website Analysis: Technology stack (web server, CMS, frameworks, JavaScript libraries identified via Wappalyzer or BuiltWith), content analysis, external resources (CDNs, analytics, third-party scripts), historical changes (Wayback Machine)
- Email Infrastructure: MX records, SPF/DKIM/DMARC policies, email security posture
- Related Infrastructure: Domains sharing IP, certificates, name servers, or registrant, infrastructure clusters suggesting common ownership
- Risk Assessment: Malicious indicators (malware hosting, phishing, C2 infrastructure), vulnerability exposure, misconfiguration detection
- Timeline: Key infrastructure changes, registration events, content modifications
- Attribution Assessment: Infrastructure patterns consistent with known actors, unique identifiers, confidence level
- Source Documentation: Tools used, query timestamps, methodology

**Infrastructure Attribution Report**:
- Executive Summary: Infrastructure summary, attributed actor/organisation, confidence assessment, supporting evidence summary
- Infrastructure Inventory: Domains, IP addresses, certificates, ASNs, hosting providers
- Attribution Evidence: Infrastructure reuse (domains/IPs previously attributed to same actor), unique fingerprints (unusual configurations, custom certificates, distinctive web server responses), temporal patterns (operational times, update schedules), resource overlap (shared name servers, registrars, hosting), linguistic/cultural indicators (language in code comments, time zone patterns)
- Alternative Hypotheses: Other potential attributions considered, evidence for/against each
- Confidence Assessment: High (multiple unique indicators, no contradictory evidence), Moderate (pattern consistent but not unique, some ambiguity), Low (limited evidence, significant ambiguity)
- Recommendations: Monitoring strategy, indicator list for detection
- Source Documentation

**Exposure Assessment Report** (security posture):
- Executive Summary: Organisation assessed, exposure summary, critical findings, risk rating
- Methodology: Tools used, scope (domains/IP ranges assessed), date of assessment
- Domain Inventory: Legitimate domains, subdomain enumeration results, abandoned/forgotten subdomains
- Service Exposure: Open ports and services identified (via Shodan/Censys), service versions, known vulnerabilities
- Certificate Issues: Expired certificates, self-signed certificates on production, weak cryptography
- DNS Misconfigurations: Missing SPF/DMARC, wildcard DNS, dangling DNS (domains pointing to uncontrolled infrastructure)
- Leaked Credentials: Findings from breach databases, paste site monitoring
- Cloud Exposure: Misconfigured S3 buckets, exposed cloud databases, cloud infrastructure enumeration
- Risk Prioritisation: Critical (immediate exploitation risk), High (significant risk, needs patching), Medium (moderate risk), Low (minor issues)
- Recommendations: Remediation priorities, monitoring suggestions

All technical reports must clearly distinguish between current state and historical observations, explicitly date all findings, and note limitations (tools used, scope, access constraints).

### Analytical Framework

Technical OSINT analysis employs several frameworks:

**Infrastructure Clustering**: Grouping related infrastructure through shared characteristics: **IP clustering** (domains resolving to same IP or IP range), **certificate clustering** (domains sharing certificates or appearing in SANs together), **name server clustering** (domains sharing authoritative name servers), **registrar/registrant clustering** (domains registered through same service or entity), **ASN clustering** (resources within same autonomous system), **hosting provider clustering** (domains/IPs with same hosting provider). Clustering reveals infrastructure under common control even when ownership obscured.

**Temporal Analysis**: Examining infrastructure changes over time: **registration patterns** (bulk domain registrations suggesting campaigns), **DNS changes** (infrastructure rotation, failover configurations), **certificate lifecycle** (renewal patterns, expiration suggesting abandonment), **content modifications** (website changes tracked via Wayback Machine), **operational time patterns** (update times suggesting operator time zones). Temporal patterns aid attribution and campaign tracking.

**Technology Fingerprinting**: Identifying software, versions, and configurations: **web server identification** (Apache, nginx, IIS) and version, **CMS detection** (WordPress, Joomla, Drupal), **framework identification** (React, Angular, Django), **analytical and tracking services** (Google Analytics, Facebook Pixel), **CDN usage** (Cloudflare, Akamai), **hosting provider indicators**. Technology stack reveals operational capabilities, potential vulnerabilities, and sometimes attribution clues.

**Attribution Analysis** (from MITRE ATT&CK and threat intelligence practice): Building attribution through: **infrastructure reuse** (threat actors reusing domains/IPs across campaigns), **operational security failures** (exposed emails, usernames, real names in certificates or WHOIS), **timing patterns** (operational hours suggesting geography), **linguistic indicators** (language in error messages, code comments), **victimology** (target selection patterns), **TTP consistency** (techniques, tactics, procedures matching known actors), **resource overlap** (shared infrastructure with previously attributed operations). Attribution confidence must be explicit and qualified.

**Adversary Reconnaissance Reconstruction**: Analysing attacker information gathering through logs, honeypots, and passive observation. MITRE ATT&CK reconnaissance tactics framework: Active Scanning (port scans, vulnerability scans), Search Open Websites/Domains (target website reconnaissance), Search Open Technical Databases (DNS, WHOIS, certificate databases), Gather Victim Identity Information (employee names, email formats). Understanding adversary reconnaissance informs defensive priorities.

**Certificate Transparency Analysis**: Leveraging CT logs for: **subdomain discovery** (finding all subdomains for a target domain through historical and current certificates), **infrastructure mapping** (identifying related domains through SAN analysis), **phishing detection** (domains mimicking legitimate brands with similar names), **timeline reconstruction** (certificate issuance dates revealing infrastructure provisioning).

### Key Databases & Tools

**DNS and WHOIS**:
- dig, nslookup (command-line DNS queries)
- WhoisXML API, who.is (WHOIS lookups)
- SecurityTrails (historical DNS and WHOIS)
- PassiveTotal, RiskIQ (passive DNS)
- DNSDumpster (domain reconnaissance)
- Reverse WHOIS (finding related domains)

**Internet Scanning Platforms**:
- Shodan (internet-connected device search, 400+ ports)
- Censys (certificate and host database, research-focused)
- BinaryEdge (attack surface monitoring)
- ZoomEye (cyberspace search engine)
- Criminal IP (infrastructure scanner)

**Certificate Transparency**:
- crt.sh (certificate search, comprehensive CT log coverage)
- Censys Certificates
- SSLMate (CT monitoring and alerting)
- Facebook CT monitoring

**IP and ASN Analysis**:
- bgp.he.net (BGP routing and ASN lookup)
- IPinfo.io, ip-api (IP geolocation and ASN)
- RIPE Stat (RIPE region IP/ASN analysis)
- GreyNoise (identifying internet scanners)

**Web Analysis**:
- Wayback Machine (Internet Archive, historical websites)
- BuiltWith, Wappalyzer (technology identification)
- Netcraft (web server analysis, site reports)
- URLscan.io (URL analysis and screenshots)
- PhishTank (phishing URL database)

**Subdomain Enumeration**:
- Sublist3r (subdomain discovery)
- Amass (OWASP, comprehensive subdomain enumeration)
- Certificate transparency logs (via crt.sh)
- DNS brute-forcing (dnsenum, fierce)

**Threat Intelligence Platforms**:
- VirusTotal (malware and URL scanning)
- AlienVault OTX (open threat exchange)
- Hybrid Analysis (malware sandbox)
- AbuseIPDB (IP reputation)
- URLhaus (malware URL database)

**Network Analysis**:
- Maltego (relationship mapping, extensive transforms)
- SpiderFoot (automated OSINT collection)
- Recon-ng (reconnaissance framework)
- theHarvester (email, subdomain, name gathering)

### Quality Criteria & Verification

Quality standards for technical OSINT derive primarily from cybersecurity research practices and threat intelligence frameworks:

**Data Currency**: Technical infrastructure changes frequently. All findings must be date-stamped. Historical data valuable for attribution but current state requires fresh queries. Currency requirements vary by data type: DNS records (query within 24 hours for current state), WHOIS (changes infrequent but note registration/update dates), certificates (note validity period), web content (archive historical, note access date).

**Source Authentication**: Verify queries return data from authoritative sources: DNS queries from authoritative name servers (not cached/recursive), WHOIS from registry operators (not third-party aggregators where possible), certificate data from CT logs (cryptographically verifiable), BGP data from RouteViews/RIPE RIS (authoritative routing data).

**Passive vs Active Techniques**: Distinguish between passive (querying existing databases, CT logs, passive DNS) and active techniques (port scanning, web requests to target). Passive techniques leave no traces on target infrastructure. Active techniques potentially detectable and may constitute unauthorised access in some jurisdictions. Legal and ethical implications require explicit consideration. Threat intelligence and security research commonly use passive techniques exclusively.

**Attribution Confidence Framework** (adapted from threat intelligence practice):
- **High Confidence**: Multiple unique technical fingerprints, infrastructure reuse with previously confirmed attribution, operational security failure exposing actor identity, multiple independent indicators consistent with single actor
- **Moderate Confidence**: Technical patterns consistent with known actor but not unique, timing patterns consistent with suspected actor, some infrastructure overlap with previous operations, plausible alternative explanations exist
- **Low Confidence**: Limited technical indicators, patterns common across multiple actors, significant ambiguity, insufficient evidence for firm conclusion
- **No Assessment**: Insufficient evidence to attribute

**Indicator Quality Ratings** (for threat intelligence):
- **High Quality**: Indicator directly linked to malicious activity, low false positive rate, specific to particular threat actor/campaign
- **Medium Quality**: Indicator associated with malicious activity but may appear in legitimate contexts, moderate false positive rate, distinguishes between limited set of actors
- **Low Quality**: Indicator appears in both malicious and legitimate contexts, high false positive rate, generic infrastructure used by many actors

**Documentation Standards**: Reproducible methodology essential. Document: exact queries used, tools and versions, query timestamps, source databases accessed, any API keys or access methods. Enable peer verification. Screenshot evidence for ephemeral resources. Wayback Machine or archive.today for web content preservation.

### Failure Modes & Mitigations

**Common Failure Modes**:

1. **Stale Data**: Treating historical infrastructure data as current state. **Mitigation**: Fresh queries for current state, explicit date stamping, comparison of historical and current data to detect changes.

2. **Shared Infrastructure Misattribution**: Attributing all domains on shared hosting (shared IP, shared certificate) to single actor when multiple unrelated entities share infrastructure. **Mitigation**: Additional clustering signals beyond IP/certificate sharing, verification of shared ownership through WHOIS or content analysis, explicit confidence qualifiers.

3. **CDN/Proxy Masking**: Identifying CDN edge server (Cloudflare, Akamai) as origin server, missing actual origin infrastructure. **Mitigation**: Historical DNS data from before CDN adoption, certificate analysis revealing origin server, scanning non-HTTP ports, subdomain enumeration finding non-CDN-protected resources.

4. **Privacy Service Opacity**: WHOIS privacy services (Domains by Proxy, WhoisGuard) obscuring registrant information. **Mitigation**: Historical WHOIS before privacy adoption, related domain analysis revealing registrant patterns, certificate email addresses (sometimes), leak databases for registrant information.

5. **Certificate Misinterpretation**: Misunderstanding certificate meaning, particularly treating "example.com" in certificate as confirming legitimacy when certificate may be self-signed, expired, or obtained fraudulently. **Mitigation**: Certificate validation (issuer trustworthiness, validity period, chain verification), comparison with legitimate certificates for same organisation, CT log analysis for anomalous certificates.

6. **Attribution Overconfidence**: Treating circumstantial evidence as definitive attribution. **Mitigation**: Explicit confidence framework, consideration of alternative hypotheses, peer review for attribution claims, avoiding attribution based on single indicator.

7. **Legal Boundary Violations**: Active scanning crossing into unauthorised access, particularly when scanning systems without clear public exposure. **Mitigation**: Limit to passive techniques or use scanning services (Shodan, Censys) aggregating legally obtained data, legal review for grey areas, explicit scope limitations.

8. **Tool Over-Reliance**: Treating automated tool output as complete without manual verification. **Mitigation**: Manual verification of critical findings, understanding tool methodologies and limitations, cross-tool verification for material claims.

### Template Design Notes

Technical OSINT templates must incorporate:

- **Investigation type selection** (domain analysis vs infrastructure attribution vs exposure assessment vs threat actor reconnaissance reconstruction) determining scope and tools.
- **Passive-first requirement** defaulting to passive techniques (CT logs, passive DNS, WHOIS, Shodan/Censys) unless active scanning explicitly justified and legally authorised.
- **Clustering methodology** hardcoding infrastructure relationship analysis (IP, certificate, name server, ASN, registrar clustering).
- **Attribution framework** with explicit confidence levels (high/moderate/low/no assessment) and alternative hypothesis consideration.
- **Currency protocols** specifying maximum data age for different resource types (DNS, WHOIS, certificates, content).
- **Output structure** varying by type: domain analysis emphasises comprehensive domain profile, attribution reports emphasise evidence synthesis and confidence assessment, exposure assessments emphasise risk prioritisation.
- **Quality checklist**: data currency verified, source authenticity confirmed, passive/active techniques distinguished, attribution confidence explicit, alternative hypotheses considered, legal constraints respected, methodology documented.
- **MITRE ATT&CK mapping** for reconnaissance techniques observed or employed.

### Evidence Quality Assessment

**MODERATE** — Strong technical practitioner methodologies from cybersecurity research community. MITRE ATT&CK provides comprehensive framework for reconnaissance tactics. SANS training materials (SEC487, SEC497, SEC587) codify practitioner knowledge. However, limited formal institutional standards outside specialised cybersecurity frameworks. Academic literature on OSINT infrastructure investigation less developed than technical security research. Professional certifications (GIAC GOSI) emerging but not yet universal. Gap between sophisticated practice and published standards. Technical community knowledge sharing strong but informal.

### Key Sources

1. MITRE ATT&CK reconnaissance tactics framework
2. Technical OSINT tools and methodologies
3. SANS OSINT technical infrastructure training
4. Domain analysis and network reconnaissance techniques

***

## DOMAIN 6: Geospatial Intelligence (GEOINT)

### Investigation Methodology

Geospatial Intelligence (GEOINT) using open sources exhibits **STRONG** evidence quality with comprehensive institutional frameworks, particularly from the National Geospatial-Intelligence Agency (NGA) and practitioner methodologies from Bellingcat.

The NGA GEOINT Basic Doctrine Publication 1.0 provides the authoritative framework defining GEOINT as "the exploitation and analysis of imagery and geospatial information to describe, assess, and visually depict physical features and geographically referenced activities on the earth". GEOINT consists of three components: (1) **Imagery** (likenesses of natural or man-made features from satellites, aircraft, UAVs, or handheld devices with positional data), (2) **Imagery Intelligence** (technical, geographic, and intelligence information derived through interpretation), and (3) **Geospatial Information** (information identifying geographic location and characteristics of features, including statistical data, remote sensing, mapping, surveying, geodetic data).

The **Geospatial Preparation of the Environment (GPE)** provides the standard analytical methodology:
1. **Define the Environment**: Establish exact location of mission/area of interest through coordinates, boundaries (physical, political, ethnic), grid systems
2. **Describe Influences of the Environment**: Identify natural conditions, infrastructure, and cultural factors affecting operations
3. **Evaluate the Environment**: Assess how environmental factors enable or constrain activities
4. **Update Continuously**: Maintain current understanding through ongoing monitoring

OSINT geospatial investigation types include: **geolocation** (determining precise location of imagery or events), **chronolocation** (determining when imagery captured through environmental clues), **site monitoring** (tracking changes at specific locations over time), **movement tracking** (following individuals/vehicles across time and space), **verification** (confirming or refuting location claims), and **environmental analysis** (understanding terrain, infrastructure, and their implications).

Bellingcat has developed extensive practitioner methodologies for open-source geolocation, emphasising systematic verification through multiple independent signals rather than single identifying features. The Berkeley Protocol on Digital Open Source Investigations provides ethical guidelines for geospatial investigations in human rights contexts.

### Source Hierarchy

Geospatial source hierarchies prioritise technical quality, resolution, and temporal currency:

**Tier 1 - High-Resolution Commercial Satellite Imagery** (sub-1 meter resolution): Maxar/DigitalGlobe, Planet Labs (PlanetScope, SkySat), Airbus Defence & Space. Commercial providers offering near-daily global coverage at 0.3-1m resolution. Highest quality for detailed analysis. Cost-prohibitive for individual researchers but increasingly accessible through partnerships, Planet's Education and Research programme, or Sentinel Hub commercial access.

**Tier 2 - Free High-Resolution Satellite Imagery**: Google Earth (integrates multiple commercial sources, historical imagery back to 1980s in some locations), Bing Maps (comparable to Google Earth), USGS Earth Explorer (Landsat, Sentinel, ASTER). Google Earth provides highest-quality freely accessible imagery with extensive historical archive. Sentinel-2 (10m optical) and Sentinel-1 (SAR) provide regular, recent coverage.

**Tier 3 - Moderate-Resolution Satellite Imagery**: Sentinel-2 (10-20m optical, 5-day revisit), Landsat 8/9 (15-30m, 16-day revisit), MODIS (250m-1km, daily). Sufficient for large-feature identification (buildings, roads, land use) but insufficient for detailed analysis. Value in multi-spectral analysis (vegetation health, thermal, etc.) and temporal frequency.

**Tier 4 - Street-Level Imagery**: Google Street View (most comprehensive, though coverage variable), Mapillary (crowdsourced, growing coverage), Apple Look Around (limited cities), Yandex Panoramas (strong in Russia/CIS). Essential for ground-truth verification of satellite analysis. Dates vary — must verify currency.

**Tier 5 - User-Generated Georeferenced Content**: Social media photos/videos with geotags, Flickr/Instagram with location data, YouTube videos claiming locations, crowdsourced imagery. Requires verification through reverse image search and geolocation techniques. May provide unique perspectives unavailable from commercial imagery.

**Tier 6 - Synthetic Aperture Radar (SAR)**: Sentinel-1 (free, regular coverage), commercial SAR (Capella Space, ICEYE). Advantage: cloud-penetrating, day/night operation. Disadvantage: interpretation complexity, lower resolution than optical. Specialised use cases (ice monitoring, flood mapping, ship detection).

**Tier 7 - Topographic and Thematic Maps**: OpenStreetMap (crowdsourced, highly detailed in many areas), official topographic maps (Ordnance Survey GB, USGS), nautical charts, aviation charts. Provides feature identification, naming, and context. Quality varies by region and contributor activity.

**Tier 8 - Geocoded Databases**: Geonames (place names, coordinates), Natural Earth (country/region boundaries), GADM (administrative boundaries). Essential for location identification and context. Generally high quality but requires verification for disputed territories or recent changes.

Resolution and temporal currency critical. Satellite imagery from years ago may show demolished buildings or prior land use. Date verification essential for any time-sensitive analysis. Multi-source corroboration (satellite + street-level + user-generated content) provides strongest verification.

### Standard Report Structure

Geospatial investigation reports vary by investigation type:

**Geolocation Verification Report**:
- Executive Summary: Content summary, claimed location, verified location (coordinates), confidence level, methodology summary
- Content Description: Original source, content details (what is shown), claimed location and date, technical characteristics (resolution, quality, metadata)
- Methodology: Verification approach (satellite imagery, street view, crowdsourced imagery), tools used, search strategy
- Geolocation Evidence: Visual matches identified (buildings, terrain, infrastructure, vegetation, signage), satellite imagery showing matches (with coordinates, date of imagery), street-level imagery corroboration (with dates), unique identifying features
- Location Confirmation: Precise coordinates, confidence boundary (margin of error), map showing verified location, comparison of content with reference imagery
- Chronolocation Assessment: Date/time determination if possible (shadows, vegetation, weather, temporal landmarks), confidence level
- Confidence Assessment: Confirmed (multiple unique features, unambiguous match), Probable (strong match but some ambiguity), Possible (limited features but consistent), Unverifiable (insufficient distinctive features)
- Caveats and Limitations: Features obscured in reference imagery, temporal gaps in available imagery, assumptions made
- Source Documentation: All reference imagery sources with dates and URLs, tool list, methodology reproducibility statement

**Site Monitoring Report**:
- Executive Summary: Site identity, monitoring period, key changes detected, significance assessment
- Site Profile: Location (coordinates, address), site type (military installation, industrial facility, infrastructure), initial baseline description
- Monitoring Methodology: Imagery sources used, temporal frequency, change detection approach
- Observed Changes: Chronological listing of detected changes with: date first observed, description of change, imagery evidence, interpretation of significance, comparison imagery (before/after)
- Activity Assessment: Patterns in activity, construction/demolition, vehicle presence, environmental changes
- Interpretation: What changes indicate about site use, ownership, activity levels
- Future Monitoring Recommendations
- Source Documentation

**Movement Tracking Report**:
- Executive Summary: Subject identity (individual, vehicle, vessel), tracking period, route summary, key locations identified
- Subject Description: Identifying characteristics, known associations, background context
- Methodology: Sources used (social media geotags, satellite imagery, automatic identification systems for ships, flight tracking)
- Timeline and Route: Chronological sequence of confirmed locations with dates, times, coordinates, movement map, travel method
- Location Analysis: Significant locations visited, duration at each location, associations with other individuals/entities
- Verification Evidence: For each location: source material, geolocation verification, temporal verification
- Intelligence Assessment: What movement pattern reveals about activities, intentions, associations
- Source Documentation

All geospatial reports must include maps with verified locations marked, comparison imagery demonstrating matches, and explicit statements of confidence and methodology limitations.

### Analytical Framework

Geospatial intelligence analysis employs several established frameworks:

**Geolocation Verification Methodology** (Bellingcat standard approach):

1. **Initial Assessment**: Examine content for distinctive features (buildings, landmarks, terrain, vegetation, signage, street furniture), assess whether sufficient detail exists for geolocation
2. **Macro-Level Identification**: Identify country/region through: linguistic clues (language on signage, number plates), architectural styles, vegetation types, infrastructure styles (roads, power lines), cultural indicators
3. **Meso-Level Narrowing**: Narrow to city/district through: distinctive landmarks (identifiable buildings, monuments), topography (hills, water bodies, skyline), infrastructure networks (road layouts, rail lines)
4. **Micro-Level Pinpointing**: Determine precise location through: unique feature combinations, spatial relationships between elements, viewing angles and perspectives, matching every visible element
5. **Verification**: Confirm through: satellite imagery showing all visible features in correct spatial relationship, street-level imagery matching ground perspective, multiple independent sources corroborating location
6. **Confidence Assessment**: Rate confidence based on uniqueness of features, number of matching elements, potential for alternative explanations

**Chronolocation Techniques**:

1. **Shadow Analysis**: Using SunCalc or similar tools, determine solar position for claimed date/time/location. Compare shadows in content against calculated shadows. Mismatches indicate incorrect date, time, or location. Requires sufficient shadow visibility and known location
2. **Vegetation Analysis**: Seasonal vegetation states (deciduous trees leafless/in leaf, crops at different growth stages, grass colour). Compare content against historical satellite imagery showing vegetation at different times. Agricultural calendars for crop types
3. **Weather Verification**: Historical weather data for location and claimed date. Match weather conditions (precipitation, cloud cover, temperature effects like snow) visible in content against weather records
4. **Temporal Landmarks**: Construction progress visible in content compared against historical satellite imagery showing construction timeline, seasonal decorations, advertised events with known dates
5. **Astronomical Events**: Moon phases, planetary positions (rarely usable but occasionally determinative), star positions for night imagery

**Multi-Spectral Analysis**: Using satellite imagery beyond visible spectrum: **Near-Infrared (NIR)** for vegetation health assessment, crop type identification, and camouflage detection. **Short-Wave Infrared (SWIR)** for geology, moisture content, and fire detection. **Thermal Infrared** for heat signatures, building insulation, and industrial activity. Multi-spectral analysis requires specialised training and typically uses Sentinel Hub, Landsat, or commercial providers.

**Temporal Analysis**: Examining location changes over time through historical satellite imagery. Detecting: construction/demolition, land use changes, environmental changes (deforestation, desertification), seasonal patterns, military buildups, infrastructure development. Tools: Google Earth historical imagery (slider showing imagery from different dates), Sentinel Hub time-lapse, Planet Labs temporal comparison.

**Spatial Pattern Recognition**: Identifying patterns across multiple locations: identifying installations through similar layouts/features, tracking movement patterns, analysing spatial clustering (density of particular features), measuring distances/areas for capacity assessment.

### Key Databases & Tools

**Satellite Imagery Platforms**:
- Google Earth Pro (desktop, most comprehensive free imagery, extensive historical archive)
- Sentinel Hub (Copernicus Sentinel data, free tier, powerful EO Browser, custom scripts for analysis)
- Planet Explorer (commercial, free Education and Research programme, daily global coverage at 3-5m)
- USGS Earth Explorer (Landsat, Sentinel, ASTER, MODIS, free)
- NASA Worldview (near-real-time satellite imagery, multiple sensors)

**Street-Level Imagery**:
- Google Street View (most comprehensive coverage)
- Mapillary (crowdsourced, API
