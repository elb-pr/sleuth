"""
claude-sleuth :: investigation scripts

Core investigation toolkit for the DI Claudian skill.
All scripts are designed to work independently via CLI or as importable modules.

Scripts:
    setup.py                - Dependency installer with module selection
    evidence_preservation.py - SHA-256 hashing, WARC archiving, chain-of-custody
    corporate_intel.py      - Cross-jurisdictional company research (CH/EDGAR/GLEIF/ICIJ)
    domain_intel.py         - DNS, RDAP, crt.sh, Shodan InternetDB pipeline
    sanctions_screen.py     - OFAC/UN/EU/UK fuzzy matching
    geolocation.py          - Sun position, EXIF, weather, reverse geocoding
    financial_analysis.py   - SEC EDGAR anomaly detection, Benford's Law, Z-Score
    network_graph.py        - NetworkX + pyvis POLE entity graph
    entity_resolver.py      - Deterministic + probabilistic record linkage
    chronological_matrix.py - UTC timeline with gap/conflict detection
    source_grader.py        - Admiralty 6x6 Matrix scoring
    username_enum.py        - Maigret/Sherlock/WhatsMyName wrapper
    content_archiver.py     - yt-dlp + gallery-dl + Playwright capture
    report_generator.py     - ICD 203 briefings and findings memos
    database_manager.py     - Entity database CRUD and integrity
    task_runner.py          - Sequential 56-task workflow runner
    template_builder.py     - Dynamic workspace assembler from templates
"""

__version__ = "1.0.0"
