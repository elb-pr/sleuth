# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-04-07

### Added
- Initial release of Claude Sleuth — OSINT skill for journalists and investigators
- Core dependency stack: `requests`, `httpx`, `aiohttp`, `beautifulsoup4`, `pandas`, `rich`
- Optional dependency groups: `identity`, `social`, `network`, `corporate`, `sanctions`, `geo`, `nlp`, `graph`, `archiving`, `documents`, `reporting`, `entity_resolution`
- CLI entry points: `sleuth-setup`, `sleuth-task`, `sleuth-template`
- MCP server integration via `server/` module
- Skill definitions via `skills/` module
- Full `pyproject.toml` build configuration with `setuptools`
- MIT License
- README with architecture diagram, installation guide, and tool inventory
