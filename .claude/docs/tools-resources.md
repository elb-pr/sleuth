# Free OSINT tools and data sources for programmatic investigative research

**Every tool, database, and scriptable capability an AI agent needs for open-source intelligence — verified free, verified current, and verified programmable.** This inventory catalogues **150+ tools and data sources** across nine investigation domains, confirms their actual access requirements (many "free" tools are not), and maps ten custom script capabilities that replicate paid-tool functionality using only open data. The core finding: a remarkably capable OSINT toolkit can be assembled at zero cost, but the social media landscape has fractured badly since 2023, and face-search remains the single largest gap that money cannot easily bridge for free.

---

## PART 1: TOOL AND DATA SOURCE INVENTORY

---

## Category 1 — Person and identity research

### Fully free tools (no signup, no API key)

| Field | Sherlock | Maigret | WhatsMyName |
|-------|---------|---------|-------------|
| **URL** | github.com/sherlock-project/sherlock | github.com/soxoj/maigret | github.com/WebBreacher/WhatsMyName |
| **What it does** | Checks username existence across **400+ sites**, [Bellingcat](https://bellingcat.gitbook.io/toolkit/more/all-tools/sherlock) [Apify](https://apify.com/anshumanatrey/holehe-email-osint) returning profile URLs | Fork of Sherlock covering **3,000+ sites** with profile-page parsing, metadata extraction, and recursive searches [Grokipedia](https://grokipedia.com/page/Maigret_OSINT_tool) | Community-curated JSON database of **600+ site definitions** [FootprintIQ](https://footprintiq.app/username-osint-guide) with web front-end at whatsmyname.app [GitHub](https://github.com/WebBreacher/WhatsMyName) [Whatsmyname](https://whatsmyname.dev/) |
| **Programmatic access** | CLI, pip install, Docker, Python import | CLI, pip install, Docker, Flask web UI, MCP server for Claude | JSON data file downloadable for custom HTTP checks; no native CLI [Osintbay](https://osintbay.com/tool/whatsmyname) |
| **Status** | Actively maintained — v0.16.0 (Sept 2025), [Bellingcat](https://bellingcat.gitbook.io/toolkit/more/all-tools/sherlock) last commit Mar 2026 [GitHub](https://github.com/sherlock-project) | Actively maintained — 17k+ stars, [Open-source Projects](https://www.opensourceprojects.dev/post/1952269489807978971) MCP integration | Actively maintained — regular community data updates |
| **Limitations** | False positives on common usernames; no profile content scraping [Bellingcat](https://bellingcat.gitbook.io/toolkit/more/all-tools/sherlock) | CAPTCHAs hamper some sites; [GitHub](https://github.com/bellingcat/toolkit/blob/main/gitbook/tools/maigret/README.md) full 3,000-site scan is slow | Requires custom wrapper for programmatic use |
| **AI agent usability** | Excellent — JSON/CSV output, fully scriptable | Excellent — MCP server, JSON/HTML/PDF output | Moderate — download JSON and build own checker |

| Field | Holehe | PhoneInfoga |
|-------|--------|-------------|
| **URL** | github.com/megadose/holehe | github.com/sundowndev/phoneinfoga |
| **What it does** | Checks if an email is registered on **120+ platforms** [Grokipedia](https://grokipedia.com/page/Maigret_OSINT_tool) via password-reset probing; returns partial recovery emails and phone numbers [Medevel](https://medevel.com/holehe/) | Phone number footprinting: [GitHub](https://github.com/tracelabs/awesome-osint) country, carrier, line type, VoIP detection, [GitHub](https://github.com/sundowndev/phoneinfoga) plus Google dorking for OSINT [Talkwalker](https://www.talkwalker.com/blog/best-osint-tools) |
| **Programmatic access** | CLI, async Python library (httpx/trio) | CLI (Go binary), REST API, web UI [InfosecOne](https://infosecone.com/blog/phoneinfoga-osint-information-gathering-framework-for-phone-numbers/) |
| **Status** | Original repo last updated 2022–2023; community forks functional | Stable but **explicitly unmaintained** by author; still functional [GitHub](https://github.com/sundowndev/phoneinfoga) |
| **Limitations** | Sites change password-reset flows, breaking modules; IP rate-limiting common | Google dorking triggers CAPTCHAs; [GitHub](https://github.com/la-deep-web/Phoneinfoga) no real-time tracking; results vary by country |
| **AI agent usability** | Excellent — async Python returns standardised JSON per module | Good — REST API provides JSON; CLI accepts E.164 format |

| Field | Wayback Machine APIs | DeepFace |
|-------|---------------------|----------|
| **URL** | archive.org/help/wayback_api.php | github.com/serengil/deepface |
| **What it does** | Three APIs: Availability (check if URL archived), CDX (list all captures with filtering), SavePageNow (trigger archiving) [GitHub](https://github.com/akamhy/waybackpy/wiki/Wayback-Machine-APIs) [PyPI](https://pypi.org/project/waybackpy/) | Open-source face verification/recognition/analysis supporting VGG-Face, FaceNet, ArcFace backends; **local processing only** |
| **Programmatic access** | REST API (JSON), Python wrapper `waybackpy` [waybackpy](https://akamhy.github.io/waybackpy/) | Python library (`pip install deepface`) |
| **Status** | Production infrastructure, actively maintained | Actively maintained |
| **Limitations** | Rate-limited; some content blocked by robots.txt | Compares faces within your own dataset — **does not search the web** |
| **AI agent usability** | Excellent — simple HTTP GET, JSON output | Excellent for local face comparison; no web-search capability |

### Free with account

| Tool | Requirements | What it adds |
|------|-------------|-------------|
| **Have I Been Pwned** (Pwned Passwords API) | None — **fully free, no key** for password hash lookups. [Have I Been Pwned](https://haveibeenpwned.com/api/v3) Email breach API requires **paid subscription** [Have I Been Pwned](https://haveibeenpwned.com/API/Key) ($3.50+/month) | k-anonymity password checking at `api.pwnedpasswords.com/range/{hash5}` [DEV Community](https://dev.to/0012303/have-i-been-pwned-has-a-free-api-check-if-any-email-was-in-a-data-breach-g5k) |
| **GHunt** | Google account cookies (via browser extension) | Extracts name, photo, Maps reviews, Calendar data from Google accounts by email [GitHub](https://github.com/mxrch/GHunt) |

### Free data sources

| Source | URL | Coverage | Access |
|--------|-----|----------|--------|
| **JudyRecords** | judyrecords.com | 760M+ US court cases [Judy Records](https://www.judyrecords.com/) | Free, no signup |
| **VoterRecords** | voterrecords.com | 100M+ US voter records | Free, no signup |
| **TruePeopleSearch** | truepeoplesearch.com | US name/address/phone/relatives | Free, no signup |
| **UK Companies House** | find-and-update.company-information.service.gov.uk | Directors, registered addresses | Free, no signup (API needs free key) |
| **BT Phone Book** | thephonebook.bt.com | UK residential/business directory | Free, no signup |
| **Canada411** | canada411.ca | Canadian people/business directory [GitHub](https://github.com/jivoi/awesome-osint) | Free, no signup |

### Notable exclusions

**Pipl** (enterprise-only, no free tier), [Galadon](https://galadon.com/spokeo-alternatives) **Spokeo/BeenVerified/Intelius/TruthFinder** (paid subscriptions behind teaser results), **OSINT Industries** (commercial), **Hunter.io** (25 searches/month, requires signup), **PimEyes/FaceCheck.ID** (freemium — payment required to view result URLs), [X](https://x.com/OSINT_Community/status/1875946501530153441) **TinEye API** (web search free, API starts at $200/month), **Clearview AI** (law enforcement only), [X](https://x.com/OSINT_Community/status/1875946501530153441) **192.com** (UK, paid for full data).

---

## Category 2 — Business and corporate research

### Fully free tools (no signup, no API key)

| Field | SEC EDGAR | GLEIF LEI API | ICIJ Offshore Leaks |
|-------|-----------|---------------|---------------------|
| **URL** | data.sec.gov | api.gleif.org | offshoreleaks.icij.org |
| **What it does** | Complete US public company filings — 10-K, 10-Q, 8-K, 13-F, insider trades, XBRL data; **20M+ filings** since 1993 | Global Legal Entity Identifiers [GLEIF](https://www.gleif.org/en/lei-data/access-and-use-lei-data) — **2.5M+ entities** with corporate parent/child ownership relationships | **810,000+ offshore entities** from Panama Papers, Paradise Papers, Pandora Papers, and Bahamas Leaks [ICIJ](https://offshoreleaks.icij.org/) |
| **Programmatic access** | REST API (JSON) — Submissions, Company Facts, Frames APIs; bulk ZIP downloads | REST API (JSON:API), bulk CSV/XML downloads updated 3×/day [GLEIF](https://www.gleif.org/en/lei-data/gleif-api) | Bulk CSV/Neo4j dump download; [ICIJ](https://offshoreleaks.icij.org/pages/database) Reconciliation API (`POST /api/v1/reconcile`) [ICIJ](https://offshoreleaks.icij.org/docs/reconciliation) |
| **Signup** | None — set User-Agent header with contact email [SEC](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | None | None for downloads and Reconciliation API |
| **Rate limits** | 10 req/sec [SEC](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data) | Generous, undisclosed | N/A (bulk download) |
| **AI agent usability** | Excellent — `edgartools` Python library (MIT) wraps API with MCP server [GitHub](https://github.com/dgunning/edgartools) | Excellent — fuzzy name matching supported | Good — CSV for bulk analysis; Neo4j for graph queries |

| Field | OFAC SDN List | UN Sanctions List | EU Sanctions List | UK Sanctions List |
|-------|--------------|-------------------|-------------------|-------------------|
| **URL** | ofac.treasury.gov | main.un.org/securitycouncil | data.europa.eu | gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets |
| **Formats** | CSV, XML, JSON, fixed-field [Office of Foreign Assets Control](https://ofac.treasury.gov/faqs/topic/1641) | XML, HTML, PDF [United Nations](https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list) | XML, SPARQL | CSV, XML, ODS, PDF |
| **Signup** | None | None | None | None |
| **Update frequency** | Near-real-time | Event-driven | On regulation publication | Often weekly |

| Field | USASpending | UK Contracts Finder | EU TED | PatentsView (USPTO) | LittleSis |
|-------|------------|--------------------|---------|--------------------|-----------|
| **URL** | api.usaspending.gov | contractsfinder.service.gov.uk | ted.europa.eu | patentsview.org | littlesis.org |
| **What it does** | US federal spending — contracts, grants, loans [Usaspending](https://api.usaspending.gov/) | UK public procurement above £10k [GitHub](https://github.com/alphagov/govuk-archive/blob/master/www.gov.uk/api/contracts-finder.json) | 800K+ annual EU procurement notices [Data Basis](https://data-basis.org/dataset/51aa4b1c-5502-4c13-a3eb-f618e634546b) [European Commission](https://single-market-economy.ec.europa.eu/single-market/public-procurement/digital-procurement/tenders-electronic-daily_en) | US patent data with inventor disambiguation | Power-mapping database: 400K+ entities, 1.6M+ relationships [GitHub](https://github.com/public-accountability/littlesis-rails) |
| **Programmatic access** | REST API (JSON), bulk PostgreSQL [PublicAPI](https://publicapi.dev/us-aspending-gov-api) | REST API (OCDS JSON) [GOV.UK](https://www.gov.uk/government/publications/open-contracting) | Bulk XML via FTP (guest/guest), [Data Basis](https://data-basis.org/dataset/51aa4b1c-5502-4c13-a3eb-f618e634546b) SPARQL, TED API v3 [Data Basis](https://data-basis.org/dataset/51aa4b1c-5502-4c13-a3eb-f618e634546b) | REST API (JSON) — **no key** | API (JSON), MCP server |
| **Signup** | None | None | None for reading | None | None for reads |

### Free with account

**Companies House API** (UK) — free account, free API key, no payment info. [GitHub](https://github.com/MarckK/companies-house-api) [GlobalDatabase](https://www.globaldatabase.com/top-5-companies-house-api-alternatives-for-uk-company-data) Returns company profiles, officers, PSC (beneficial ownership), filing history, charges. [GlobalDatabase](https://www.globaldatabase.com/top-5-companies-house-api-alternatives-for-uk-company-data) Rate limit: **600 req/5 min**. [GitHub](https://github.com/MarckK/companies-house-api) [Temenos](https://journey.temenos.com/images/exchange-packages/companieshouse-Readme.html) Streaming API for real-time changes.

**OpenSanctions** — bulk data download is **free, no login** (JSON/CSV). [OpenSanctions +2](https://www.opensanctions.org/) [OpenSanctions](https://www.opensanctions.org/datasets/eu_fsf/) Hosted API requires free key (non-commercial). [OpenSanctions](https://www.opensanctions.org/api/) [OpenSanctions](https://www.opensanctions.org/datasets/eu_fsf/) Self-hosted API available via open-source `yente` on GitHub. [21 Analytics](https://21analytics.co/blog/opensanction-open-source-approach-compliance/) [GitHub](https://github.com/opensanctions)

**EPO Open Patent Services** — free account, free API key. REST API for bibliographic patent data, legal status, patent families. [PQAI](https://projectpq.ai/best-patent-search-apis-2025/)

**OpenCorporates** — 200M+ companies across 140+ jurisdictions. [Maltego](https://www.maltego.com/transform-hub/opencorporates/) [Zephira](https://zephira.ai/8-opencorporates-alternatives-for-kyb-company-registry-lookup/) Free for public-benefit projects; [Bellingcat](https://www.bellingcat.com/resources/2023/08/24/following-the-money-a-beginners-guide-to-using-the-opencorporates-api/) commercial API starts at **£2,250/year**. [Zephira](https://zephira.ai/8-opencorporates-alternatives-for-kyb-company-registry-lookup/) Despite "open" branding, meaningful programmatic access is effectively paid for commercial use.

### Notable exclusions

**sec-api.io** (commercial wrapper), **Dun & Bradstreet/Orbis** (enterprise), **Endole/Global Database** (paid enrichment), **EPO PATSTAT** (€1,250/year).

---

## Category 3 — Social media and platform intelligence

### The post-API reality of 2025–2026

The era of free, generous social media APIs is over. [Emergent Mind](https://www.emergentmind.com/topics/pushshift-reddit-dataset) **Twitter/X, Reddit, and Meta have all paywalled or severely restricted API access.** This has created a fragmented ecosystem where truly free, no-signup tools are limited to username enumeration, media downloading, and archived data access.

### Fully free tools (no signup)

| Field | yt-dlp | gallery-dl | Arctic Shift (Reddit) | PullPush (Reddit) |
|-------|--------|-----------|----------------------|-------------------|
| **URL** | github.com/yt-dlp/yt-dlp | github.com/mikf/gallery-dl | github.com/ArthurHeitmann/arctic_shift | pullpush.io |
| **What it does** | Downloads video/audio from **1,700+ sites** including YouTube, Twitter/X, TikTok, Instagram [Roundproxies Blog](https://roundproxies.com/blog/yt-dlp/) [Free Codecs](https://www.free-codecs.com/download/yt-dlp.htm) | Downloads image galleries from **100+ sites** including Twitter/X, Reddit, Tumblr [Grokipedia](https://grokipedia.com/page/Gallery-dl) [GitHub](https://github.com/metril/gallery-dl) | Large-scale Reddit archive — submissions, comments, subreddits; successor to Pushshift | Spiritual successor to Pushshift; free Reddit data search API [GitHub](https://github.com/maxjo020418/BAScraper) |
| **Status** | Very actively maintained — release 2026.03.17 [Videohelp](https://www.videohelp.com/software/yt-dlp) | Actively maintained — Dec 2025 release | Actively maintained — data current early 2025 | Intermittent — back online mid-2025; [Ihsoyct](https://ihsoyct.github.io/changelog.html) Reddit has threatened legal action |
| **Programmatic access** | CLI, Python library, JSON metadata output | CLI, Python library, JSON config [GitHub](https://github.com/metril/gallery-dl) | REST API (JSON), bulk data dumps via torrents | REST API (JSON), no auth for basic use |
| **Rate limits** | Platform-dependent | Platform-dependent | Soft limits on API | 15 req/min soft, 30 req/min hard [GitHub](https://github.com/maxjo020418/BAScraper) |

### Free with account

| Tool | Account needed | Status | Notes |
|------|---------------|--------|-------|
| **twscrape** | X/Twitter account credentials | Active (2025) | Async Python; accounts risk being banned [GitHub](https://github.com/vladkens/twscrape) |
| **Instaloader** | Instagram login for most functionality | Active — v4.15 (Nov 2025) [Bellingcat](https://bellingcat.gitbook.io/toolkit/more/all-tools/instaloader) | Best-maintained Instagram tool; risk of account suspension |
| **Telegram OSINT tools** (Geogramint, Telepathy) | Telegram API credentials (free from my.telegram.org) [GitHub](https://github.com/jivoi/awesome-osint) | Various | Most require API ID/Hash [GitHub](https://github.com/yusiqo/telegram-osint) |
| **snscrape** | No key needed but Twitter login wall blocks most scraping | **Degraded/partially broken** | Not reliably working for Twitter at scale |

### Current platform API access

| Platform | Free API? | Research cost | Best free alternative |
|----------|----------|--------------|----------------------|
| **Twitter/X** | ❌ Free tier is write-only | $100/month minimum for reads [Xpoz](https://www.xpoz.ai/blog/guides/understanding-twitter-api-pricing-tiers-and-alternatives/) | twscrape (needs account), yt-dlp (video only) |
| **Reddit** | ⚠️ 100 QPM non-commercial [TechTarget](https://www.techtarget.com/whatis/feature/Reddit-pricing-API-charge-explained) | $12,000/year commercial [BBN Times](https://www.bbntimes.com/technology/complete-guide-to-reddit-api-pricing-and-usage-tiers-in-2026) | Arctic Shift, PullPush |
| **Meta (Facebook/Instagram)** | ⚠️ Restricted, business verification needed | Complex approval | Instaloader (needs login) |
| **TikTok** | ⚠️ Academic only (verified researchers) | None for eligible academics | tiktok-scraper (fragile, needs cookies) |
| **LinkedIn** | ❌ None | N/A — actively hostile to scraping | None reliable |
| **YouTube** | ✅ 10,000 units/day free | N/A | yt-dlp for downloads |
| **Bluesky** | ✅ Fully open AT Protocol | Free | Best current option for social media API research |
| **Mastodon/Fediverse** | ✅ Open APIs on all instances | Free | ActivityPub protocol; fully open |

### Notable exclusions

**Twint** (completely broken/abandoned), [GitHub +2](https://github.com/twintproject/twint) **Nitter** (public instances mostly dead since Jan 2024; [No Bullshit Bitcoin](https://www.nobsbitcoin.com/nitter-is-shutting-down-following-x-changes-to-guest-accounts/) self-hosted with tokens still fragile), [TheFix](https://blog.thefix.it.com/is-nitter-still-working-the-definitive-2026-status-report/) [Wikipedia](https://en.wikipedia.org/wiki/Nitter) **Maltego** (CE requires signup, transforms need subscriptions), **OSINT Industries/ShadowDragon/SkopeNow** (commercial), **Intelligence X** (3 searches/day free).

---

## Category 4 — Domain, IP, and technical infrastructure

### Tier 1: zero-friction tools (no signup, no key, JSON output)

| Tool | Endpoint / Install | What it does | Rate limit |
|------|-------------------|-------------|------------|
| **crt.sh** | `crt.sh/?q=%.example.com&output=json` | Certificate transparency log search [Apify](https://apify.com/ryanclinton/crt-sh-search) [DEV Community](https://dev.to/0012303/crtsh-has-a-free-api-find-every-ssl-certificate-for-any-domain-3ph7) — **the single most powerful free OSINT API**. Wildcard subdomain enumeration. Direct PostgreSQL access at port 5432 [Medium](https://medium.com/@MuhammedAsfan/certificate-transparency-a-technical-overview-and-osint-toolkit-%EF%B8%8F-30d4f556f7f8) | No formal limit; timeouts under heavy load |
| **Shodan InternetDB** | `internetdb.shodan.io/{ip}` | IP enrichment: open ports, hostnames, CPEs, tags, vulns — **zero auth** [shodan](https://blog.shodan.io/5-free-things-for-everybody/) | Generous; no published cap |
| **Shodan CVEDB** | `cvedb.shodan.io` | CVE vulnerability database with CVSS, EPSS, CISA KEV status [shodan](https://blog.shodan.io/5-free-things-for-everybody/) | Free, no auth |
| **RDAP (via rdap.org)** | `rdap.org/domain/{domain}` | Structured JSON domain/IP registration data — **modern WHOIS replacement** [Rdap](https://about.rdap.org/) | Cloudflare rate-limited |
| **Who-Dat** | `who-dat.as93.net/{domain}` | Open-source WHOIS/RDAP API with batch support. Self-hostable [GitHub](https://github.com/Lissy93/who-dat) | No key, no auth |
| **ip-api.com** | `ip-api.com/json/{ip}` | IP geolocation (country, city, ISP, ASN) — **HTTP only** on free tier [DEV Community](https://dev.to/0012303/ip-api-has-a-free-api-get-geolocation-for-any-ip-address-without-an-api-key-mmg) | 45 req/min [IP-API](https://ip-api.com/) |
| **ipwhois.io** | `ipwhois.io/json/{ip}` | IP geolocation with HTTPS | 1 req/sec |
| **FreeIPAPI** | `freeipapi.com/api/json/{ip}` | IP geolocation, free for commercial use [Freeipapi](https://freeipapi.com/) | 60 req/min [Freeipapi](https://freeipapi.com/) |
| **IPinfo Lite** | `ipinfo.io/lite` | Country + ASN data — **unlimited, no key** (CC BY-SA 4.0) [IPinfo](https://ipinfo.io/lite) | None |
| **Team Cymru** | `dig +short {reversed}.origin.asn.cymru.com TXT` | IP-to-ASN mapping via DNS; bulk mode supported [Team Cymru](https://www.team-cymru.com/ip-asn-mapping) | Free, updated 4-hourly [Team Cymru](https://www.team-cymru.com/ip-asn-mapping) |
| **bgp.tools** | `bgp.tools` (WHOIS TCP 43, JSONL exports) | BGP table, ASN-to-name mappings; successor to BGPView (shut down Nov 2025) [BGPView](https://bgpview.io/) | Cache exports ≥30 min [BGP.Tools](https://bgp.tools/kb/api) |
| **RIPEstat** | `stat.ripe.net/data/...` | Announced prefixes, AS paths, routing history, RPKI validation | Free, no auth |
| **CertStream** | `wss://certstream.calidog.io/` | Real-time stream of newly issued CT log entries via WebSocket | Free, high volume |

### Tier 2: open-source CLI tools (install and run, no keys for basic use)

| Tool | Install | Key capability |
|------|---------|---------------|
| **dig/whois/nslookup/host** | Pre-installed on Linux | DNS and WHOIS lookups; `dig +json` for structured output (BIND 9.17+) |
| **WhatWeb** | `apt install whatweb` | Website tech detection — **1,800+ plugins**, JSON/XML output [Hackertarget](https://hackertarget.com/whatweb-scan/) |
| **httpx** (ProjectDiscovery) | Go install | Fast HTTP toolkit [ProjectDiscovery](https://docs.projectdiscovery.io/opensource/httpx/overview) with `-tech-detect` using Wappalyzer signatures [Hacking Articles](https://www.hackingarticles.in/a-detailed-guide-on-httpx/) |
| **Subfinder** (ProjectDiscovery) | Go install | Subdomain enumeration [GitHub](https://github.com/projectdiscovery/subfinder) from **~25 free sources without keys** (crt.sh, Wayback, AlienVault) [Trickest](https://trickest.com/docs/library/recon/tools) |
| **Amass** (OWASP) | Go install | Most comprehensive subdomain tool; passive mode works without keys [Trickest](https://trickest.com/docs/library/recon/tools) [Subdomain Finder](https://subdomainfinder.com/blog/subdomain-enumeration-tools) |
| **asn** (nitefood) | github.com/nitefood/asn | Bash CLI combining Team Cymru, pWhois, PeeringDB, RPKI for IP/ASN investigation [GitHub](https://github.com/nitefood/asn) |
| **OpenRDAP** | `go install github.com/openrdap/rdap@latest` | CLI RDAP client outputting JSON, text, or WHOIS-style [Openrdap](https://www.openrdap.org/) |

### Free with account

**Censys** (free account) — Lookup API only (host/cert retrieval); [Censys](https://community.censys.com/other-security-topics-39/how-can-i-get-the-api-uid-and-secret-key-456) **Search API requires paid Starter plan ($250/month+)**. [Medium](https://medium.com/@MuhammedAsfan/certificate-transparency-a-technical-overview-and-osint-toolkit-%EF%B8%8F-30d4f556f7f8) **GreyNoise Community** — free API key, IP reputation lookups, [GreyNoise](https://docs.greynoise.io/docs/using-the-greynoise-community-api) [GreyNoise](https://docs.greynoise.io/reference/get_v3-community-ip) modest daily cap. [Risky](https://risky.biz/catalog/greynoise/) **Shodan free account** — marginal value beyond InternetDB. **VirusTotal** — free key, 4 req/min, 500/day. **DNSdumpster** — free API key via signup. [DNSDumpster](https://dnsdumpster.com/developer/)

### Notable exclusions

**SecurityTrails** (now Recorded Future; heavily restricted free tier), **BuiltWith** (API starts $295/month), [Revealera](https://www.revealera.com/blog/7-builtwith-alternatives-2025/) **Censys Search API** (paid), **WhoisXML API** (freemium), **BinaryEdge** (250 queries/month free).

---

## Category 5 — Geospatial and location intelligence

### Fully free tools (no signup)

| Tool | Access | OSINT use |
|------|--------|-----------|
| **Nominatim** (OSM geocoding) | REST API at `nominatim.openstreetmap.org` — no key, 1 req/sec [OpenStreetMap Foundation](https://operations.osmfoundation.org/policies/nominatim/) | Forward/reverse geocoding; [Nominatim](https://nominatim.org/) self-hosting removes all limits |
| **Photon** (Komoot geocoder) | `photon.komoot.io/api/?q=berlin` — no key | Search-as-you-type geocoding with typo tolerance [GitHub](https://github.com/komoot/photon/blob/master/README.md) |
| **Overpass API** (OSM data queries) | `overpass-api.de/api/interpreter` — no key | Query any tagged OSM feature within any geographic area [Ldodds](https://osm-queries.ldodds.com/) |
| **SunCalc JS/Python library** | `npm install suncalc` / Python `pysuncalc` | Sun position, shadow direction/length for any date/time/location [GitHub](https://github.com/3ls3if/Cybersecurity-Notes/blob/main/readme/reconnaissance/passive-recon/geoint/suncalc-geospatial-osint-using-shadows.md) [GitHub](https://github.com/mourner/suncalc) — **all local computation, no network calls** [Bellingcat](https://bellingcat.gitbook.io/toolkit/more/all-tools/suncalc) |
| **Bellingcat ShadowFinder** | `pip install shadowfinder` | Estimates geographic locations from object height + shadow length + date/time [Tekkix](https://tekkix.com/articles/security/2024/09/in-pursuit-of-shadows-image-geolocation-usi) [GitHub](https://github.com/bellingcat/ShadowFinder) |
| **Open-Meteo** | `api.open-meteo.com` — **no key, no signup, no cookies** | Global weather forecasts [GitHub](https://github.com/open-meteo/open-meteo) + **historical data [Open-Meteo](https://open-meteo.com/) from 1940** — ideal for chronolocation verification |
| **NASA GIBS** | WMTS/WMS tiles at `gibs.earthdata.nasa.gov` — **no auth** | 1,200+ satellite imagery layers, many updated daily, ~30 years of history [SkyWatch](https://skywatch.com/free-sources-of-satellite-data/) |
| **Open-Elevation** | `open-elevation.com` — no key | Elevation data from SRTM [GitHub](https://github.com/sacridini/Awesome-Geospatial) |
| **OpenSky Network** (anonymous) | `opensky-network.org/api/states/all` — no account | Live aircraft tracking — **1 request per 10 seconds**, current data only [Tcl Wiki](https://wiki.tcl-lang.org/page/OpenSky+API) |
| **GeoPandas / Shapely / Rasterio / Folium / OSMnx** | pip install | Full geospatial analysis, mapping, and visualisation stack |

### Free with account

**Copernicus Data Space Ecosystem** (Sentinel satellite data) — free account, OAuth2 credentials. [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) Full Sentinel-1 (SAR), Sentinel-2 (10m optical), Sentinel-3 archives. Python SDK `sentinelhub-py`. This is the **primary free satellite imagery source** for investigation work.

**USGS Earth Explorer** (Landsat) — free EROS account. 40+ years of Landsat imagery, 30m resolution. M2M REST API.

**OpenSky Network** (authenticated) — free account, OAuth2 (since March 2026). [GitHub](https://github.com/openskynetwork/opensky-api) **4,000–8,000 credits/day**, [github](https://openskynetwork.github.io/opensky-api/rest.html) historical flights. [Openskynetwork](https://openskynetwork.github.io/opensky-api/rest.html)

**aisstream.io** — free API key for global AIS vessel tracking via WebSocket. [GitHub](https://github.com/aisstream/aisstream)

### Notable exclusions

**ADS-B Exchange API** (no longer free — paid via RapidAPI [ADS-B Exchange](https://www.adsbexchange.com/data/) since ~2024; web globe map still freely browsable), **FlightRadar24 API** (commercial only), **MarineTraffic/VesselFinder API** (commercial), **Google Earth Engine** (requires Google Cloud account + approval), **Mapbox/Google Maps geocoding** (requires billing account).

---

## Category 6 — Financial and sanctions research

### Sanctions screening can be done entirely free

Combining **OFAC SDN** (CSV/XML download), **UN Consolidated List** (XML), **EU Sanctions List** (XML/SPARQL), [BEX](https://www.bex.ag/en/sanctioned-party-lists/) **UK Sanctions List** (CSV/XML — consolidated to single list on 28 January 2026), and **OpenSanctions bulk data** (JSON/CSV, free for non-commercial) [OpenSanctions](https://www.opensanctions.org/docs/bulk/) provides comprehensive global coverage with zero cost and zero signup. [OpenSanctions](https://www.opensanctions.org/)

### Financial filing analysis

**SEC EDGAR** is the gold standard: fully free [SEC](https://www.sec.gov/search-filings) REST API, [SEC](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data) XBRL-extracted financial data in JSON, [SEC](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) 20M+ filings. [GitHub](https://github.com/janlukasschroeder/sec-api-python) The `edgartools` Python library (MIT licence) wraps this with zero keys, includes an MCP server for AI integration, and provides typed Python objects for 20+ filing types. [GitHub](https://github.com/dgunning/edgartools)

**UK HM Land Registry Price Paid Data** — free CSV download of all residential property sales in England and Wales since January 1995 [GOV.UK](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads) (**24M+ transactions**). SPARQL endpoint available. [HM Land Registry](https://landregistry.data.gov.uk/)

### Court records

**CourtListener/RECAP** (Free Law Project) — largest free US legal research platform. [CourtListener](https://www.courtlistener.com/) REST API (free account), bulk S3 data. [CourtListener](https://www.courtlistener.com/help/api/rest/) Includes **32,000+ judge profiles** with financial disclosures. [CourtListener](https://www.courtlistener.com/help/api/bulk-data/)

**Find Case Law** (UK National Archives) — free database of England and Wales court judgments. [GitHub](https://github.com/openlegaldata/awesome-legal-data)

**HUDOC** (ECHR) — complete European Court of Human Rights case law. [European Court of Human Rights](https://hudoc.echr.coe.int/) ECHR Open Data project provides structured JSON API. [Wetsuite](https://www.wetsuite.nl/datasetcatalogus/)

### Blockchain investigation

| Explorer | Signup | Daily limit | Chains |
|----------|--------|------------|--------|
| **Blockstream.info** | None | Undisclosed | Bitcoin, Liquid |
| **Blockchair** | None for 1K/day | 1,000 calls/day, 30 req/min [GitHub](https://github.com/Blockchair/Blockchair.Support/blob/master/API_DOCUMENTATION_EN.md) | 48+ chains [DataWallet](https://www.datawallet.com/crypto/blockchair-review) |
| **Blockchain.com** | None for reads | Undisclosed | Bitcoin, Ethereum, BCH |
| **GraphSense** (self-hosted) | None | Unlimited | Open-source analytics platform used by INTERPOL [Netacea](https://netacea.com/blog/follow-the-crypto-tools-and-techniques/) |

### Notable exclusions

**PACER** ($0.10/page — use CourtListener/RECAP instead), **Bloomberg/Refinitiv** (enterprise), **Chainalysis/Elliptic/TRM Labs** (commercial blockchain investigation), **LexisNexis/Westlaw** (paid legal research), **sec-api.io** (commercial EDGAR wrapper — use official free APIs).

---

## Category 7 — Web archiving and content preservation

### Core archiving tools

| Tool | Access | Evidence grade |
|------|--------|---------------|
| **Wayback Machine CDX API** | `web.archive.org/cdx/search/cdx?url={URL}&output=json` — no auth | Partial (content digests in CDX metadata) |
| **ArchiveBox** (self-hosted) | CLI, Python API, Docker — 27k+ GitHub stars [ArchiveBox](http://archivebox.io/) | Partial — WARC + manual hashing |
| **Playwright** (Microsoft) | `pip install playwright` — Apache-2.0 | No built-in hashing — add `hashlib` |
| **gowitness** | Go binary — GPLv3 | Screenshots with SQLite/JSONL logging |
| **changedetection.io** | Self-hosted Docker — 22k+ stars, REST API [I Love Free Software](https://www.ilovefreesoftware.com/06/webware/free-self-hosted-website-change-monitor-changedetection-io.html) | Change tracking with visual diff |
| **urlwatch** | `pip install urlwatch` — BSD [Snyk](https://snyk.io/advisor/python/urlwatch) | YAML-configured change monitoring |

### Content extraction and downloading

**yt-dlp** remains the gold standard for video/media download [Roundproxies Blog](https://roundproxies.com/blog/yt-dlp/) [Free Codecs](https://www.free-codecs.com/download/yt-dlp.htm) (stable release March 2026, 1,700+ sites). **gallery-dl** covers image galleries from 100+ sites. [Grokipedia](https://grokipedia.com/page/Gallery-dl) [GitHub](https://github.com/metril/gallery-dl) **Trafilatura** has displaced newspaper3k as the leading text extraction tool [Readthedocs](https://trafilatura.readthedocs.io/) — outperforms all alternatives in academic benchmarks, [PyPI](https://pypi.org/project/trafilatura/) used by HuggingFace, IBM, Microsoft Research. [Readthedocs](https://trafilatura.readthedocs.io/)

**Google Cache is dead** (February 2024). [Yahoo!](https://tech.yahoo.com/general/articles/google-cache-gone-view-archived-190441488.html) **Bing Cache reportedly discontinued** (December 2024). [Local Search Forum](https://localsearchforum.com/threads/anyone-have-a-quality-replacement-for-googles-cache-view-in-chrome.61929/) The Wayback Machine is now the primary cache alternative. [Semrush](https://www.semrush.com/blog/google-cached-pages/)

### Evidence-grade archiving workflow

No single free tool provides a complete chain-of-custody solution. The recommended free pipeline is: **(1)** capture with ArchiveBox or Playwright into WARC/HTML/PNG, **(2)** hash all outputs with SHA-256 (`hashlib`), **(3)** record metadata (URL, UTC timestamp, collector identity), **(4)** submit to Wayback Machine via `waybackpy` for independent corroboration, **(5)** create WARC files with `warcio` for ISO 28500-compliant archiving. [Ebu](https://spotlight.ebu.ch/p/advanced-wayback-machine-and-archival)

### Notable exclusions

**Hunchly** ($129.99/year — excellent but paid), **archive.today** (operational but facing Wikipedia delinking, FBI investigation, and content-tampering allegations as of February 2026 [Wikipedia](https://en.wikipedia.org/wiki/Archive.today) — use with caution for evidentiary purposes), **Perma.cc** (10 links/month for free individuals; unlimited only via academic affiliation). [Texas A&M University School of Law](https://law.tamu.libguides.com/c.php?g=1241968&p=9089139)

---

## Category 8 — Data processing and analysis

### Essential Python OSINT toolkit

**Network graph and link analysis:** NetworkX (graph algorithms, centrality, community detection), pyvis (interactive HTML visualisations via vis.js), [Readthedocs](https://pyvis.readthedocs.io/en/latest/tutorial.html) [Pythonhumanities](https://python-textbook.pythonhumanities.com/06_sna/06_01_05_networkx_pyvis.html) python-igraph (high-performance for large graphs), [Ona-book](https://ona-book.org/gitbook/viz-graphs.html) Neo4j Community Edition (graph database, [SoftRadar](https://softradar.com/neo4j-community-edition/) Cypher queries). [GitHub](https://github.com/neo4j/neo4j)

**Natural language processing:** spaCy (production NER — persons, organisations, locations, dates from documents), [Real Python](https://realpython.com/natural-language-processing-spacy-python/) Hugging Face Transformers (local models for NER, sentiment, zero-shot classification, summarisation — **no API calls**), Stanza (Stanford NLP, 70+ languages), [Stanza](https://stanfordnlp.github.io/stanza/) Gensim (topic modelling, document similarity).

**Image analysis:** ExifTool + PyExifTool (gold standard for metadata extraction [PyPI](https://pypi.org/project/PyExifTool/) from 400+ file types), OpenCV (image comparison, feature matching, face detection), imagehash (perceptual hashing for duplicate detection), DeepFace (local face verification).

**PDF and document processing:** pdfplumber (superior table extraction), [Medium](https://sangeethasaravanan.medium.com/unlocking-pdf-data-the-smart-way-a-practical-guide-to-pdfplumber-3c80b5d9d491) pypdf (text/metadata), Camelot (CV-based table extraction), [Unstract](https://unstract.com/blog/extract-tables-from-pdf-python/) Tesseract OCR + pytesseract (100+ languages), OCRmyPDF (adds OCR layer to scanned PDFs), [PyPI](https://pypi.org/project/ocrmypdf/) PyMuPDF (fast processing of large collections). [arXiv](https://arxiv.org/html/2410.09871v1)

**Data pipeline:** Pandas (standard manipulation), Polars (Rust-based, ~9× faster), DuckDB (embedded SQL, queries CSV/Parquet directly), [CodeCut](https://codecut.ai/pandas-vs-polars-vs-duckdb-comparison/) SQLite (built-in, zero dependencies).

**Entity resolution:** **Splink** (UK Ministry of Justice, probabilistic record linkage at scale [GitHub](https://github.com/moj-analytical-services/splink) — millions of records on a laptop), [Moj-analytical-services](https://moj-analytical-services.github.io/splink/index.html) RapidFuzz (C++ fuzzy matching, production replacement for thefuzz), [DataCamp](https://www.datacamp.com/tutorial/fuzzy-string-python) jellyfish (Soundex, Metaphone, Jaro-Winkler for phonetic name matching), [Protiviti](https://www.protiviti.com/gl-en/whitepaper/advanced-analytics-sanctions-compliance) dedupe (ML-based, active learning). [GitHub](https://github.com/dedupeio/dedupe)

**Visualisation:** Matplotlib (static), Plotly (interactive charts, Sankey diagrams, geographic maps), Folium (Leaflet.js maps [Carmatec](https://www.carmatec.com/blog/10-best-python-data-visualization-libraries/) with OSM tiles — no API key), Bokeh (streaming dashboards), [Datapane](https://datapane.com/post/python-visualization-libraries-every-data-scientist-should-know-about) Seaborn (statistical).

---

## Category 9 — Automation and orchestration

### OSINT framework status summary

| Framework | Stars | Status | Free modules without keys |
|-----------|-------|--------|--------------------------|
| **SpiderFoot** (open source) | 13k+ | v4.0 released; commits slowed 2023–2024 but still functional | ~200 modules: [GitHub](https://github.com/smicallef/spiderfoot) DNS, WHOIS, certs, abuse lists, social media checks, web crawling [GitHub](https://github.com/smicallef/spiderfoot) |
| **theHarvester** | 13k+ | **Actively maintained** — Jan 2026 update | anubis, baidu, bing, certspotter, crtsh, dnsdumpster, duckduckgo, hackertarget, otx, rapiddns [GitHub](https://github.com/laramies/theHarvester) [GitHub](https://github.com/skybersec/theHarvester-osint) |
| **Recon-ng** | 5.1k | Semi-abandoned — issues unanswered | bing_domain_web, certificate_transparency, [Qazeer](https://notes.qazeer.io/general/external_recon) all reporting modules [GitHub](https://github.com/lanmaster53/recon-ng) |
| **Photon** | 12k+ | Unmaintained since ~2020 but functional; in Kali Linux | All features — pure crawler, no API dependencies |
| **OSRFramework** | 967 [Snyk](https://snyk.io/advisor/python/osrframework) | **Inactive** — many platform checks broken | N/A — avoid |
| **Sn1per Community** | 6.5k+ | Active | Basic recon, Nmap, WHOIS, DNS, subdomain brute-force, Google dorking |

### Recommended automation stack

**Orchestration:** n8n Community (self-hosted, fair-code licence, 400+ integrations, native AI/LangChain support, [GitHub](https://github.com/n8n-io/n8n) 60k+ stars) [GitHub](https://github.com/n8n-io) **or** Apache Airflow (Apache-2.0, Python DAGs, complex pipeline scheduling).

**Monitoring:** changedetection.io (22k+ stars, [GitHub](https://github.com/mattwolfe/changedetection) REST API, 70+ notification channels) for website surveillance; [GitHub](https://github.com/mattwolfe/changedetection) [I Love Free Software](https://www.ilovefreesoftware.com/06/webware/free-self-hosted-website-change-monitor-changedetection-io.html) Huginn (45k+ stars, MIT) for RSS/event-based agent chains. [GitHub](https://github.com/huginn/huginn)

**Browser automation:** **Playwright (Python)** is the recommended choice [Browserless](https://www.browserless.io/blog/playwright-vs-selenium-2025-browser-automation-comparison) — 30% faster than Selenium, [Latenode](https://latenode.com/blog/web-automation-scraping/headless-browser-overview/python-headless-browser-best-libraries-for-automation) auto-wait mechanisms, network interception, [Browserless](https://www.browserless.io/blog/playwright-vs-selenium-2025-browser-automation-comparison) screenshot/PDF capture, geolocation spoofing, device emulation. Microsoft-backed, [Browserless](https://www.browserless.io/blog/playwright-vs-selenium-2025-browser-automation-comparison) 74k+ stars.

**Request management:** `requests-cache` (transparent caching), `fake-useragent` (User-Agent rotation), `tenacity` (retry/backoff), `ratelimit` (rate-limiting decorator), `httpx` (async HTTP/2).

### Notable exclusions

**SpiderFoot HX** (paid cloud — $800+/year), **Maltego Professional** (~€999/year; CE requires account and is severely limited), **Sn1per Professional** ($299+/year), **n8n Cloud** (€20+/month — self-hosted is free).

---

## PART 2: CUSTOM SCRIPT CAPABILITY MAPPING

---

### 1. Username enumeration engine

**Existing projects:** Maigret (3,000+ sites, MIT, actively maintained) is the most comprehensive. Sherlock (400+ sites) is the most popular. Blackbird (600+ sites) uses WhatsMyName data.

**Architecture:** All follow the same pattern — load JSON site database → substitute `{username}` into URL template → send async HTTP requests → detect account existence via status code, page content matching, or JSON response → optionally parse profile pages for metadata.

| Component | Recommendation |
|-----------|---------------|
| **Data sources** | Maigret data.json (3,000+ sites), WhatsMyName wmn-dat.json (600+, lowest false-positive rate) |
| **Libraries** | `aiohttp`, `beautifulsoup4`, `rich` |
| **Output** | JSON/CSV/HTML with profile URLs and extracted metadata |
| **Legal boundaries** | Only queries public pages; GDPR applies to collected personal data; rate-limit all requests |
| **Complexity** | Moderate — 500–800 LOC, 5–7 dependencies |
| **Verdict** | **Use Maigret directly** — it already has MCP integration and exceeds what a custom build would achieve |

### 2. Corporate intelligence aggregator

**Existing projects:** `edgartools` (SEC EDGAR, MIT, MCP server), `opyncorporates` (OpenCorporates wrapper). No single tool aggregates across multiple jurisdictions.

| Component | Recommendation |
|-----------|---------------|
| **Data sources** | Companies House API (UK, free key), SEC EDGAR (US, no key), OpenSanctions (ownership), GLEIF LEI (global entity IDs), ICIJ Offshore Leaks (leaked data) |
| **Libraries** | `edgartools`, `requests`, `pandas` |
| **Pipeline** | Input company name → query each registry → merge officer/director data → map corporate relationships → generate unified report |
| **Legal boundaries** | All public registries; GDPR applies to director personal data; OpenCorporates requires attribution |
| **Complexity** | Moderate — 600–1,000 LOC, 6–8 dependencies |
| **Verdict** | **Custom build recommended** — no comprehensive cross-jurisdictional tool exists |

### 3. Domain intelligence collector

**Existing projects:** SpiderFoot (200+ modules), Recon-ng (modular but aging), Subfinder + Amass (subdomain enumeration).

| Component | Recommendation |
|-----------|---------------|
| **Data sources** | DNS (`dnspython`), RDAP (`rdap.org`), crt.sh (CT logs), Shodan InternetDB (ports/vulns), Wayback Machine CDX (history) |
| **Libraries** | `dnspython`, `requests`, `tldextract`, `socket` |
| **Pipeline** | Input domain → DNS enumeration (all record types) → RDAP lookup → crt.sh subdomain discovery → Shodan InternetDB enrichment → HTTP probing → tech fingerprinting → compile report |
| **Legal boundaries** | Passive queries are non-intrusive and legal; active scanning requires authorisation; WHOIS increasingly GDPR-redacted |
| **Complexity** | Moderate — 700–1,200 LOC, 8–10 dependencies |
| **Verdict** | **Wrap existing tools** — combine Subfinder + crt.sh + InternetDB + WhatWeb into unified pipeline |

### 4. Sanctions and PEP screening tool

**Existing projects:** OpenSanctions/Yente (self-hosted matching API, FollowTheMoney model), `sanction_list_search` (EU/OFAC/UN fuzzy matching).

| Component | Recommendation |
|-----------|---------------|
| **Data sources** | OFAC SDN (CSV), UN list (XML), EU list (XML), UK list (CSV), OpenSanctions bulk (JSON) |
| **Libraries** | `rapidfuzz` (5× faster than thefuzz), `jellyfish` (Soundex/Metaphone), `nameparser`, `pandas`, `lxml` |
| **Matching pipeline** | Normalise names → phonetic indexing (Soundex/Metaphone keys) → candidate generation → Jaro-Winkler scoring → DOB/nationality adjustment → threshold filtering |
| **Legal boundaries** | Data is public; must not be used to circumvent sanctions; false positives require manual review; OpenSanctions requires licence for commercial use |
| **Complexity** | Complex — 1,000–1,500 LOC, 8–10 dependencies |
| **Verdict** | **Use Yente (self-hosted)** for comprehensive screening, **or build custom** for maximum control over matching logic |

### 5. Social media archiver

**Existing projects:** **Bellingcat Auto Archiver** (150,000+ items archived, modular: extractors → enrichers → formatters → storage), ArchiveBox (27k+ stars, WARC/HTML/PDF/PNG).

| Component | Recommendation |
|-----------|---------------|
| **Data sources** | Public social media URLs |
| **Libraries** | `yt-dlp`, `gallery-dl`, `playwright`, `hashlib` (stdlib), `waybackpy`, `warcio` |
| **Pipeline** | Download media (yt-dlp/gallery-dl) → screenshot (Playwright) → hash all artefacts (SHA-256) → record metadata → submit to Wayback Machine → log chain of custody |
| **Legal boundaries** | Copyright restricts redistribution; platform ToS may prohibit automated downloading; GDPR applies to personal data; delay publication where safety is at risk |
| **Complexity** | Complex — 800–1,500 LOC, 10–12 dependencies including browser binaries |
| **Verdict** | **Use Bellingcat Auto Archiver** — purpose-built for investigative evidence preservation with hashing and timestamping |

### 6. Financial filing analyser

**Existing projects:** `edgartools` (best-in-class — typed Python objects for 20+ filing types, XBRL parsing, pandas DataFrames, MCP server).

| Component | Recommendation |
|-----------|---------------|
| **Data sources** | SEC EDGAR Company Facts API, Companies House filing downloads |
| **Libraries** | `edgartools`, `pandas`, `numpy` |
| **Anomaly detection** | Year-over-year variance (>20% flag), Benford's Law analysis, revenue-vs-cash-flow divergence, Altman Z-Score computation |
| **Complexity** | Complex — 800–1,200 LOC, 6–8 dependencies |
| **Verdict** | **Build on edgartools** — it handles EDGAR parsing; add anomaly detection and Companies House integration |

### 7. Geolocation toolkit

**Existing projects:** pysolar (validated against US Naval Observatory, <0.1° accuracy), Bellingcat ShadowFinder.

| Component | Recommendation |
|-----------|---------------|
| **Data sources** | pysolar/suncalc (local computation), Nominatim (geocoding), Open-Elevation, Open-Meteo (historical weather), EXIF GPS extraction |
| **Libraries** | `pysolar`, `geopy`, `exifread`, `Pillow`, `requests`, `pytz` |
| **Pipeline** | Extract EXIF GPS → calculate sun position for candidate location/time → compare with observed shadows → cross-reference weather data → reverse geocode → query elevation → generate confidence report |
| **Complexity** | Moderate — 500–800 LOC, 7–9 dependencies |
| **Verdict** | **Custom build recommended** — combine pysolar + Open-Meteo + Nominatim into unified toolkit |

### 8. Evidence preservation pipeline

**Existing projects:** ArchiveBox, Bellingcat Auto Archiver, `waybackpy` (MIT, Python interface to all 3 Wayback APIs).

| Component | Recommendation |
|-----------|---------------|
| **Libraries** | `waybackpy`, `playwright`, `hashlib` (stdlib), `warcio`, `Pillow` |
| **Pipeline** | Input URLs → Playwright full-page screenshot (PNG) + HTML/DOM capture → `warcio` WARC creation → SHA-256 hash all artefacts → submit to Wayback Machine → generate JSON evidence log with chain-of-custody metadata |
| **Legal boundaries** | Evidence must come from publicly accessible sources; hash-verified WARC files are the gold standard; courts accept under FRE 901 (US) and eIDAS 2 (EU) |
| **Complexity** | Moderate — 600–900 LOC, 7–9 dependencies |
| **Verdict** | **Custom build recommended** — existing tools handle parts but none provide the complete evidence-grade pipeline with chain-of-custody logging |

### 9. Network graph builder

**Existing projects:** NetworkX + pyvis (standard combination), SpiderFoot (exports GEXF for Gephi).

| Component | Recommendation |
|-----------|---------------|
| **Libraries** | `networkx`, `pyvis`, `pandas`, `matplotlib` |
| **Data model** | Node types: Person, Organisation, Domain, Email, Phone, Address, Account, Document, Event, Location. Edge types: owns, employs, director_of, registered_to, linked_to, communicates_with |
| **Output** | Interactive HTML (pyvis/vis.js), GEXF/GraphML (Gephi import), JSON (web apps) |
| **Complexity** | Moderate — 400–700 LOC, 4–5 dependencies |
| **Verdict** | **Straightforward custom build** — NetworkX + pyvis is the proven pattern; add standardised OSINT entity model |

### 10. OSINT report generator

**Existing projects:** Nixintel's pattern using `python-docx-template` (Jinja2 + Word), Jinja2 + WeasyPrint (HTML→PDF).

| Component | Recommendation |
|-----------|---------------|
| **Libraries** | `jinja2`, `weasyprint` (HTML→PDF), `docxtpl` (Word), `markdown`, `plotly`/`matplotlib` (charts) |
| **Pipeline** | Investigation data model (JSON) → Jinja2 template rendering → HTML/PDF/Word output with embedded charts and graph visualisations |
| **Complexity** | Simple to moderate — 300–600 LOC, 4–6 dependencies |
| **Verdict** | **Custom build recommended** — define standard investigation data model, create templates, render with Jinja2 |

---

## META-ANALYSES

---

### 1. Capability matrix

| Investigation need | Free tool(s) | Custom script option | Gap? |
|-------------------|-------------|---------------------|------|
| Username enumeration | Sherlock, Maigret | Wrap existing tools | ❌ Fully covered |
| Email-to-accounts | Holehe | Extend with HIBP Pwned Passwords | ❌ Covered (email breach API is paid) |
| Phone number lookup | PhoneInfoga | Combine with `phonenumbers` library | ⚠️ Limited — carrier data only |
| Face search (web) | None free + programmatic | DeepFace for local comparison only | **✅ Major gap** |
| Company registry lookup | Companies House API, SEC EDGAR, GLEIF | Cross-jurisdictional aggregator | ⚠️ No unified global free API |
| Beneficial ownership | UK PSC, ICIJ Offshore Leaks, GLEIF L2 | Aggregate multiple sources | ⚠️ Fragmented coverage |
| Sanctions screening | OFAC/UN/EU/UK lists, OpenSanctions | Yente or custom fuzzy matcher | ❌ Fully covered |
| Domain intelligence | crt.sh, Subfinder, RDAP, WhatWeb, InternetDB | Unified domain report pipeline | ❌ Fully covered |
| IP investigation | InternetDB, ip-api.com, Team Cymru, bgp.tools | Combine for comprehensive IP report | ❌ Fully covered |
| Social media monitoring | yt-dlp, gallery-dl, Arctic Shift | Platform-specific scrapers | **✅ Major gap** — Twitter/X, LinkedIn blocked |
| Satellite imagery | NASA GIBS (no auth), Copernicus (free account) | Python + STAC API | ❌ Covered |
| Flight tracking | OpenSky (free account) | N/A | ⚠️ ADS-B Exchange API now paid |
| Vessel tracking | aisstream.io (free key) | N/A | ⚠️ Limited free options |
| Court records | CourtListener (US), Find Case Law (UK), HUDOC | N/A | ⚠️ Incomplete — PACER still charges |
| Property records | UK Land Registry PPD | US county records vary wildly | ⚠️ US highly fragmented |
| Web archiving | Wayback Machine, ArchiveBox | Evidence preservation pipeline | ❌ Covered |
| Document OCR | Tesseract, OCRmyPDF | Batch processing pipeline | ❌ Covered |
| Entity resolution | Splink, RapidFuzz, jellyfish | N/A | ❌ Covered |
| Link analysis | NetworkX, pyvis, Neo4j CE | Investigation graph builder | ❌ Covered |
| Workflow automation | n8n, Airflow, Huginn | Custom Python pipelines | ❌ Covered |

### 2. AI agent toolkit — minimum installation set

**Essential (install always):**
- `sherlock-project` — username enumeration
- `maigret` — deep username + metadata extraction
- `holehe` — email-to-account discovery
- `yt-dlp` — media downloading
- `playwright` — browser automation + screenshots
- `waybackpy` — Wayback Machine API
- `trafilatura` — web content extraction
- `dnspython` — DNS resolution
- `requests` + `httpx` — HTTP clients
- `pandas` — data manipulation
- `networkx` + `pyvis` — graph analysis and visualisation
- `spacy` — named entity recognition
- `pdfplumber` + `pytesseract` — document processing
- `rapidfuzz` + `jellyfish` — fuzzy string matching
- `hashlib` (stdlib) — evidence hashing

**Domain-specific (install when needed):**
- `edgartools` — SEC EDGAR financial analysis
- `pysolar` + `geopy` + `folium` — geolocation toolkit
- `gallery-dl` — image gallery downloading
- `warcio` — WARC file creation
- `splink` — large-scale entity resolution
- `exifread` + `opencv-python` — image analysis
- `polars` + `duckdb` — high-performance data processing
- `scrapy` — structured web crawling
- `transformers` + `torch` — local NLP models
- `neo4j` (driver) — graph database

**Nice-to-have:**
- `changedetection.io` (Docker) — website change monitoring
- `archivebox` (Docker) — self-hosted web archiving
- `jinja2` + `weasyprint` — report generation
- `certstream` — real-time CT log monitoring
- `ocrmypdf` — batch OCR processing
- `stanza` — multi-language NLP

### 3. Custom script priority ranking

| Rank | Capability | Impact | Feasibility | Uniqueness | Build order rationale |
|------|-----------|--------|-------------|-----------|----------------------|
| 1 | **Evidence preservation pipeline** | High | High | High | No complete free tool exists; critical for legal admissibility |
| 2 | **Corporate intelligence aggregator** | High | High | High | No cross-jurisdictional free aggregator exists |
| 3 | **Domain intelligence collector** | High | High | Medium | Existing tools cover parts; unification adds significant value |
| 4 | **Sanctions screening tool** | High | Medium | Medium | Yente exists but custom build gives control over matching logic |
| 5 | **Geolocation toolkit** | Medium | High | High | Unique combination of sun/weather/elevation/geocoding |
| 6 | **Financial filing analyser** | Medium | Medium | Medium | edgartools covers most; anomaly detection adds value |
| 7 | **Network graph builder** | Medium | High | Low | NetworkX + pyvis pattern is well-established; add OSINT data model |
| 8 | **OSINT report generator** | Medium | High | Low | Jinja2 templates are straightforward; define standard data model |
| 9 | **Username enumeration** | High | N/A | N/A | **Use Maigret** — no custom build needed |
| 10 | **Social media archiver** | High | N/A | N/A | **Use Bellingcat Auto Archiver** — purpose-built |

### 4. Python dependency map

**Standard library (no installation):**
`hashlib`, `json`, `datetime`, `sqlite3`, `socket`, `csv`, `os`, `re`, `urllib`, `pathlib`, `logging`, `asyncio`, `subprocess`, `collections`, `math`

**pip install (Python packages):**

| Package | Category | Size |
|---------|---------|------|
| `requests`, `httpx`, `aiohttp` | HTTP clients | Small |
| `beautifulsoup4`, `lxml` | HTML/XML parsing | Small |
| `pandas`, `polars` | Data manipulation | Medium |
| `duckdb` | Embedded SQL | Medium |
| `networkx`, `pyvis`, `igraph` | Graph analysis | Medium |
| `spacy`, `stanza`, `transformers`, `gensim`, `scikit-learn` | NLP | Large (models require GB) |
| `matplotlib`, `plotly`, `folium`, `seaborn`, `altair`, `bokeh` | Visualisation | Medium |
| `Pillow`, `opencv-python`, `imagehash` | Image processing | Medium |
| `pypdf`, `pdfplumber`, `camelot-py`, `PyMuPDF` | PDF processing | Small–Medium |
| `pytesseract`, `ocrmypdf`, `pdf2image` | OCR | Small (require system deps) |
| `rapidfuzz`, `jellyfish`, `thefuzz`, `recordlinkage`, `splink`, `dedupe` | Entity resolution | Small–Medium |
| `dnspython`, `tldextract`, `ipwhois` | Network | Small |
| `geopy`, `shapely`, `geopandas`, `rasterio`, `osmnx` | Geospatial | Medium |
| `pysolar`, `exifread`, `pyexiftool` | OSINT-specific | Small |
| `playwright`, `selenium` | Browser automation | Large (browser binaries) |
| `scrapy`, `trafilatura` | Web scraping | Medium |
| `waybackpy`, `warcio` | Archiving | Small |
| `edgartools` | SEC EDGAR | Small |
| `jinja2`, `weasyprint`, `docxtpl`, `markdown` | Report generation | Medium |
| `requests-cache`, `fake-useragent`, `tenacity`, `ratelimit` | Request management | Small |
| `sqlalchemy`, `neo4j` | Database | Small |
| `rich` | Terminal UI | Small |

**System-level dependencies:**
`ExifTool` (Perl), `Tesseract OCR` (C++), `Ghostscript` (PDF interpreter), `Poppler` (PDF rendering), `FFmpeg` (media processing), `Chrome/Chromium` (for Playwright/Selenium), `Go` (for Subfinder/Amass/httpx/gowitness), `Ruby` (for WhatWeb)

### 5. Gap register

| Capability gap | Paid tool that fills it | Why it cannot be replicated free | Workaround |
|----------------|------------------------|-------------------------------|-----------|
| **Web-scale face search** | PimEyes ($29.95/month), Clearview AI (law enforcement) | Requires massive indexed image database and facial recognition infrastructure | DeepFace for local face comparison against own dataset; Yandex Images (manual, browser only) |
| **Twitter/X API research** | Twitter/X Basic ($100/month), Pro ($5,000/month) | Platform paywall; scraping blocked | twscrape (needs accounts, risks bans); archived data via Wayback Machine |
| **LinkedIn data** | LinkedIn Sales Navigator, Proxycurl | Actively hostile to scraping; legal action against scrapers | Google dorking (`site:linkedin.com`); very limited |
| **Full PACER access** | PACER ($0.10/page) | Government system with per-page charges | CourtListener/RECAP (crowd-sourced, incomplete) |
| **Real-time unfiltered flight data** | ADS-B Exchange API (paid RapidAPI) | Infrastructure cost of receiver network; API now monetised | OpenSky (limited free), ADS-B Exchange web globe (manual) |
| **Comprehensive vessel tracking** | MarineTraffic ($), VesselFinder ($) | AIS receiver network infrastructure costs | aisstream.io (free key, limited coverage) |
| **Deep corporate intelligence** | Bureau van Dijk/Orbis, Dun & Bradstreet | Proprietary enriched databases built over decades | Query individual national registries; GLEIF for entity linking |
| **Email breach data** | HIBP API ($3.50/month), Intelligence X ($) | Responsible disclosure model requires payment to prevent abuse | HIBP Pwned Passwords (free); manual web search on haveibeenpwned.com |
| **Dark web monitoring** | Recorded Future, Flashpoint, DarkOwl | Requires specialised infrastructure and access | SpiderFoot has some dark web modules; Tor-based manual access |
| **Satellite imagery <1m resolution** | Maxar, Planet ($) | Satellite hardware and processing costs | Sentinel-2 (10m free); Google Earth (manual viewing); historical comparison possible |

### 6. Legal and ethical framework for automated OSINT

**What can be automated freely across jurisdictions:**

Querying public government databases (company registries, court records, sanctions lists, patent databases, land registries), DNS/WHOIS/RDAP lookups, certificate transparency log searches, IP geolocation, public procurement data, financial filings, geocoding, weather data, and satellite imagery access are all **legally unproblematic** to automate across the UK, US, and EU. These are public data sources intended for public access.

**What requires caution:**

Social media scraping occupies a legal grey zone. In the **US**, the Ninth Circuit's *hiQ v. LinkedIn* decision (2022) held that scraping publicly available data likely does not violate the Computer Fraud and Abuse Act, but this is not settled law and platforms continue to bring ToS-based claims. In the **EU**, the GDPR (and **UK** Data Protection Act 2018) apply to any processing of personal data — even publicly available data. Automated collection of personal data requires a **lawful basis** (typically legitimate interest under Article 6(1)(f)), and data subjects retain rights to erasure and objection. The **EU AI Act** (effective August 2025) additionally restricts untargeted scraping of facial images for facial recognition databases.

Username enumeration, email-to-account checking, and phone number investigation all involve personal data. Under GDPR/UK DPA, these activities require documented legitimate interest, data minimisation, and security measures. **Rate limiting and robots.txt compliance** are both legal best practices and ethical requirements. Automated OSINT tools should always identify themselves via User-Agent headers, respect rate limits, and avoid circumventing access controls.

**What should never be automated:**

Accessing systems behind authentication without authorisation (Computer Misuse Act 1990 in UK, CFAA in US), circumventing technical protection measures, building facial recognition databases from scraped images (EU AI Act prohibition), processing special-category data (ethnicity, health, political opinions, biometrics) without explicit consent, and any collection designed to facilitate harassment, stalking, or discrimination.

All tools in this inventory access only publicly available information. Investigators must ensure their specific use case has a lawful basis, maintain documentation of their methodology, and consult legal counsel before publishing findings that involve personal data.
