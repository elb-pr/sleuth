# Source & Credibility Grader: The Admiralty 6x6 Standard for Intelligence Integrity

1. The Strategic Mandate for Source Grading

In the professional intelligence cycle, the transition from raw collection to structured intelligence is a critical juncture where the integrity of the entire analytical workspace is established. Filtering raw data as it enters this cycle is a strategic mandate; it prevents the "poisoning" of the investigative environment by ensuring that speculative noise and disinformation are bifurcated from actionable leads. Without a rigorous grading mechanism, the analytical process risks saturation by unverified data, which inevitably leads to skewed conclusions, false attributions, and the degradation of investigative outcomes.

Adhering to a standardized grader maintains the core principles of the Berkeley Protocol on Digital Open Source Investigations: accuracy and transparency. By providing a clinical audit trail for every claim, investigators ensure that the final intelligence product meets the standards of professional and legal admissibility. This structured approach moves the investigation from "raw data" to "intelligence" by adding layers of context, reliability, and skepticism. To achieve this rigor, the global intelligence community utilizes a specific alphanumeric framework known as the Admiralty System.

2. The Core Framework: The Admiralty 6x6 Matrix

The Admiralty System (NATO 6x6) serves as the formal doctrinal standard for source and information evaluation. Codified in AJP-2.1 (Allied Joint Doctrine for Intelligence Procedures) and STANAG 2511, this matrix provides a universal language for analysts to communicate the weight of evidence. The system separates the evaluation into two independent dimensions: the historical reliability of the source (A–F) and the logical consistency of the specific information (1–6).

Source Reliability (A–F)

This scale evaluates the origin of the information based on authenticity, trustworthiness, and past performance.

Grade	Definition	Criteria for Assignment
A	Completely Reliable	No doubt about authenticity, trustworthiness, or competency; history of complete reliability.
B	Usually Reliable	Minor doubts; strong overall track record; most information has been valid in the past.
C	Fairly Reliable	Genuine doubt exists; however, some valid information has been provided in the past.
D	Not Usually Reliable	Significant doubt regarding authenticity or trustworthiness; only occasional valid information.
E	Unreliable	History of providing invalid information; lacks authenticity, trustworthiness, and competency.
F	Reliability Cannot Be Judged	No established track record; new source; insufficient basis for evaluation.

Information Credibility (1–6)

This scale evaluates the claim itself based on corroboration and logical consistency.

Grade	Definition	Criteria for Confirmation
1	Confirmed by Other Sources	Independently corroborated by other sources; logical and consistent with other info.
2	Probably True	Not independently confirmed; logically sound and consistent with other reporting.
3	Possibly True	Not confirmed; reasonably logical; partially consistent with other known info.
4	Doubtful	Possible but not logical; no other information exists to compare or corroborate.
5	Improbable	Not confirmed; illogical; actively contradicted by other reliable reporting.
6	Truth Cannot Be Judged	No basis for evaluation; information is entirely new or lacks context for comparison.

The "F6" Analytical Starting Point

In Open-Source Intelligence (OSINT), the F6 rating is the mandatory default for new or untested sources. It signifies a source whose reliability is unknown (F) providing a claim whose truth cannot yet be judged (6). Within this doctrinal framework, F6 is not a reason for dismissal; it is a clinical starting point. It signals to the investigative team that the data point is recorded for situational awareness but carries zero weight until further research or corroboration moves the grade toward the "A1" end of the spectrum. These alphanumeric grades are applied systematically across a hierarchy of tiered source types.

3. Source Hierarchy and Tiered Reliability Benchmarks

To maintain consistency, investigators must distinguish between "Statutory/Official" records and "Secondary/Unverified" streams. This hierarchy is further refined by the Genealogical Proof Standard, which distinguishes between Direct Evidence (answers a question on its face), Indirect Evidence (requires combination with other data), and Negative Evidence (arising from a well-documented absence where a record should exist).

The Five-Tier Source Hierarchy

* Tier 1: Official Government Records Statutory filings including Land Registry records, SEC EDGAR filings, and corporate registers. These provide high-quality, time-bound identity and relationship data. Typical Admiralty Grade: A/B (Reliability) and 1/2 (Credibility).
* Tier 2: Verified Commercial/Regulated Disclosures Stock exchange announcements, Bloomberg/Capital IQ data, and regulated corporate aggregators. These sources operate under strict regulatory oversight. Typical Admiralty Grade: B (Reliability) and 1/2 (Credibility).
* Tier 3: Authenticated Social Media/Self-Published Content Verified accounts or content with confirmed geolocation and timestamps. This requires the active authentication of the user's identity. Typical Admiralty Grade: C/D (Reliability) and 2/3 (Credibility).
* Tier 4: Secondary Commentary/News Aggregates Unverified user-generated content, news summaries, and secondary commentary. Useful for lead generation but lacking primary authority. Typical Admiralty Grade: D/E (Reliability) and 4 (Credibility).
* Tier 5: Data Breaches/Leaked Information ICIJ databases or credential leaks. While often forensic-grade, they carry significant legal and ethical constraints and lack official verification. Typical Admiralty Grade: E/F (Reliability) and 1/6 (Credibility).

The differentiator between Primary Sources (direct observation/original filing) and Secondary Sources (reportage) is a primary driver of the Credibility score. Secondary sources—which "echo" primary material—rarely exceed a "3" until the underlying primary evidence is retrieved and verified.

4. Advanced Evaluation: The 5x5x5 System and Handling Codes

UK Law Enforcement extends the Admiralty framework through the 5x5x5 System, as governed by the UK College of Policing APP for Intelligence Management. This adds a third dimension: Handling Codes, which dictate the dissemination parameters of the intelligence.

Handling Codes (1-5)

1. Permits dissemination within the agency and to trusted partners.
2. Permits dissemination to specific agencies with predefined conditions.
3. Permits dissemination to third parties (e.g., NGOs) with caveats.
4. Permits dissemination only within the originating unit/team.
5. Permits no dissemination; requires the highest level of authorization for any access.

The Protective Barrier

Combining Reliability, Credibility, and Handling into a three-digit rating (e.g., 2/3/2) creates a "protective barrier" for the investigative team. This composite score prevents the accidental use of high-risk or low-quality data in final reports, ensuring only "actionable" intelligence is shared with external stakeholders.

5. Procedural Implementation: The Grader Template

The "Admiralty Assessment Entry" is the mandatory workflow for every discrete claim entering the database. Analysts must normalize all temporal data and verify digital hashes to meet modern forensic standards.

Field	Analyst Input
Claim/Data Point	The specific fact being graded (e.g., "Subject X is a Director of Entity Y").
Source Identifier	URL, Document ID, or Entity reference.
Timezone Normalization	Timestamps normalized to UTC with local conversion documented.
Hash Verification	SHA-256 cryptographic hash of the digital file/evidence item.
Source Hierarchy Tier	Select Tier (1-5).
Admiralty Reliability	Select Grade (A-F).
Admiralty Credibility	Select Grade (1-6).
Handling Code	Select Code (1-5).
Verification Path	Steps taken to corroborate (e.g., "Reverse Image Search," "CT Log Check").
Analytical Rationale	Brief justification for the assigned grade.

Verification Confidence Framework

Consistent with the Berkeley Protocol, claims are classified into three confidence categories:

* Verified: Content authenticity confirmed through multiple independent methods (e.g., geolocation + shadows).
* Likely Authentic: Strong but not conclusive; supported by reliable sources but lacking primary documentation.
* Likely Manipulated: Evidence of editing, forensic inconsistencies, or active contradiction by primary sources.

6. Quality Assurance and Bias Mitigation Protocols

To ensure objectivity and prevent "Confidence Inflation," analysts must adhere to the Analytical Tradecraft Standards codified in ICD 203. These standards distinguish between underlying intelligence and analyst judgment.

The Nine Analytical Tradecraft Standards

1. Describe Quality and Credibility: Properly assess the underlying sources.
2. Express Uncertainty: Explain and quantify the levels of uncertainty.
3. Distinguish Facts from Assumptions: Clearly label underlying intelligence versus analyst judgments.
4. Incorporate Alternatives: Evaluate competing hypotheses (Analysis of Competing Hypotheses).
5. Demonstrate Customer Relevance: Address the implications for the decision-maker.
6. Logical Argumentation: Use clear and consistent reasoning.
7. Explain Change/Consistency: Account for changes in previous analytical judgments.
8. Make Accurate Assessments: Ensure assessments are supported by the evidence base.
9. Visual Information: Incorporate effective visual information where appropriate (e.g., link analysis).

Expression of Uncertainty: The Probability Scale

Analysts must use the following precise probability language and associated percentages to convey the likelihood of an event:

* Almost certainly: 95–99%
* Very likely: 80–95%
* Likely: 55–80%
* Roughly even chance: 45–55%
* Unlikely: 20–45%
* Very unlikely: 5–20%
* Remote: 1–5%
* Almost no chance: 1–5%

Mitigation of Circular Reporting

Circular Reporting ("echoes") occurs when multiple sources report the same underlying information, creating a false sense of corroboration. The grader must follow a strict command: Trace all claims back to the original primary source before assigning a final grade. If multiple outlets quote a single unverified social media post, they are a single source, not independent corroboration.

By adhering to these grading and tradecraft standards, the investigator ensures the legal and professional admissibility of the final intelligence product, transforming raw data into a credible evidence base for high-stakes decision-making.

[list]:


[createdAt]: Mar 31, 2026, 2:29 PM
[updatedAt]: Invalid Date
