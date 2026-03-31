#!/usr/bin/env python3
"""
claude-sleuth :: corporate intelligence aggregator
Cross-jurisdictional company research across UK, US, and global registries.

Data sources:
    - UK Companies House API (free key required, set CH_API_KEY env var)
    - SEC EDGAR (US, no key needed)
    - GLEIF LEI API (global, no key needed)
    - ICIJ Offshore Leaks reconciliation API (no key needed)
    - OpenSanctions bulk data (no key for bulk download)

Usage:
    from scripts.corporate_intel import CorporateIntel
    ci = CorporateIntel(ch_api_key="your_key")
    result = ci.investigate("Acme Corp")
"""

import json
import os
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    import httpx
    HAS_HTTPX = True
except ImportError:
    HAS_HTTPX = False


@dataclass
class CompanyRecord:
    source: str
    name: str
    jurisdiction: str = ""
    company_number: str = ""
    status: str = ""
    incorporation_date: str = ""
    address: str = ""
    officers: list = field(default_factory=list)
    sic_codes: list = field(default_factory=list)
    lei: str = ""
    parent_entity: str = ""
    raw_data: dict = field(default_factory=dict)


class CompaniesHouse:
    """UK Companies House API wrapper."""
    BASE = "https://api.company-information.service.gov.uk"

    def __init__(self, api_key: str):
        self.session = requests.Session()
        self.session.auth = (api_key, "")
        self.session.headers["Accept"] = "application/json"

    def search(self, query: str, limit: int = 5) -> list:
        resp = self.session.get(f"{self.BASE}/search/companies", params={"q": query, "items_per_page": limit})
        if resp.status_code != 200:
            return []
        items = resp.json().get("items", [])
        results = []
        for item in items:
            results.append(CompanyRecord(
                source="companies_house",
                name=item.get("title", ""),
                jurisdiction="GB",
                company_number=item.get("company_number", ""),
                status=item.get("company_status", ""),
                incorporation_date=item.get("date_of_creation", ""),
                address=item.get("address_snippet", ""),
                raw_data=item,
            ))
        return results

    def get_officers(self, company_number: str) -> list:
        resp = self.session.get(f"{self.BASE}/company/{company_number}/officers")
        if resp.status_code != 200:
            return []
        return [
            {
                "name": o.get("name", ""),
                "role": o.get("officer_role", ""),
                "appointed": o.get("appointed_on", ""),
                "resigned": o.get("resigned_on", ""),
                "nationality": o.get("nationality", ""),
            }
            for o in resp.json().get("items", [])
        ]

    def get_psc(self, company_number: str) -> list:
        """Persons with Significant Control (beneficial ownership)."""
        resp = self.session.get(f"{self.BASE}/company/{company_number}/persons-with-significant-control")
        if resp.status_code != 200:
            return []
        return resp.json().get("items", [])


class SECEdgar:
    """US SEC EDGAR API wrapper (no key needed)."""
    BASE = "https://efts.sec.gov/LATEST/search-index?q="
    COMPANY_SEARCH = "https://efts.sec.gov/LATEST/search-index"
    SUBMISSIONS = "https://data.sec.gov/submissions"

    def __init__(self):
        self.headers = {
            "User-Agent": "claude-sleuth/1.0 (investigation@example.com)",
            "Accept": "application/json",
        }

    def search(self, query: str, limit: int = 5) -> list:
        url = "https://efts.sec.gov/LATEST/search-index"
        params = {"q": query, "dateRange": "custom", "startdt": "2020-01-01", "forms": "10-K"}
        resp = requests.get(url, params=params, headers=self.headers)
        if resp.status_code != 200:
            # Fallback: company tickers
            return self._search_tickers(query, limit)
        return []

    def _search_tickers(self, query: str, limit: int) -> list:
        """Search via company tickers JSON."""
        url = "https://www.sec.gov/files/company_tickers.json"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code != 200:
            return []
        tickers = resp.json()
        query_lower = query.lower()
        matches = []
        for _, entry in tickers.items():
            if query_lower in entry.get("title", "").lower():
                cik = str(entry["cik_str"]).zfill(10)
                matches.append(CompanyRecord(
                    source="sec_edgar",
                    name=entry.get("title", ""),
                    jurisdiction="US",
                    company_number=cik,
                    raw_data=entry,
                ))
                if len(matches) >= limit:
                    break
        return matches

    def get_submissions(self, cik: str) -> dict:
        """Get company filings by CIK number."""
        url = f"{self.SUBMISSIONS}/CIK{cik.zfill(10)}.json"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code != 200:
            return {}
        return resp.json()


class GLEIF:
    """Global Legal Entity Identifier Foundation API."""
    BASE = "https://api.gleif.org/api/v1"

    def search(self, query: str, limit: int = 5) -> list:
        params = {"filter[fulltext]": query, "page[size]": limit}
        resp = requests.get(f"{self.BASE}/lei-records", params=params)
        if resp.status_code != 200:
            return []
        records = []
        for item in resp.json().get("data", []):
            attrs = item.get("attributes", {})
            entity = attrs.get("entity", {})
            legal_name = entity.get("legalName", {}).get("name", "")
            jurisdiction = entity.get("jurisdiction", "")
            status = entity.get("status", "")
            address_parts = entity.get("legalAddress", {})
            address = ", ".join(filter(None, [
                address_parts.get("addressLines", [""])[0] if address_parts.get("addressLines") else "",
                address_parts.get("city", ""),
                address_parts.get("country", ""),
            ]))
            records.append(CompanyRecord(
                source="gleif",
                name=legal_name,
                jurisdiction=jurisdiction,
                lei=item.get("id", ""),
                status=status,
                address=address,
                raw_data=item,
            ))
        return records


class ICIJOffshoreLeaks:
    """ICIJ Offshore Leaks reconciliation API."""
    BASE = "https://offshoreleaks.icij.org/api/v1/reconcile"

    def search(self, query: str, limit: int = 5) -> list:
        payload = {"queries": json.dumps({"q0": {"query": query, "limit": limit}})}
        resp = requests.post(self.BASE, data=payload)
        if resp.status_code != 200:
            return []
        data = resp.json()
        results = data.get("q0", {}).get("result", [])
        records = []
        for r in results:
            records.append(CompanyRecord(
                source="icij_offshore_leaks",
                name=r.get("name", ""),
                jurisdiction=r.get("jurisdiction", ""),
                raw_data=r,
            ))
        return records


class CorporateIntel:
    """Unified cross-jurisdictional corporate intelligence aggregator."""

    def __init__(self, ch_api_key: Optional[str] = None):
        self.ch_api_key = ch_api_key or os.environ.get("CH_API_KEY")
        self.ch = CompaniesHouse(self.ch_api_key) if self.ch_api_key and HAS_REQUESTS else None
        self.edgar = SECEdgar() if HAS_REQUESTS else None
        self.gleif = GLEIF() if HAS_REQUESTS else None
        self.icij = ICIJOffshoreLeaks() if HAS_REQUESTS else None

    def investigate(self, query: str, limit: int = 5) -> dict:
        """Run cross-jurisdictional search and return unified results."""
        results = {
            "query": query,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "sources": {},
        }

        # Companies House (UK)
        if self.ch:
            try:
                ch_results = self.ch.search(query, limit)
                # Enrich with officers and PSC
                for r in ch_results:
                    if r.company_number:
                        r.officers = self.ch.get_officers(r.company_number)
                        time.sleep(0.5)  # Rate limit: 600 req/5 min
                results["sources"]["companies_house"] = [asdict(r) for r in ch_results]
            except Exception as e:
                results["sources"]["companies_house"] = {"error": str(e)}

        # SEC EDGAR (US)
        if self.edgar:
            try:
                edgar_results = self.edgar.search(query, limit)
                results["sources"]["sec_edgar"] = [asdict(r) for r in edgar_results]
            except Exception as e:
                results["sources"]["sec_edgar"] = {"error": str(e)}

        # GLEIF (Global)
        if self.gleif:
            try:
                gleif_results = self.gleif.search(query, limit)
                results["sources"]["gleif"] = [asdict(r) for r in gleif_results]
            except Exception as e:
                results["sources"]["gleif"] = {"error": str(e)}

        # ICIJ Offshore Leaks
        if self.icij:
            try:
                icij_results = self.icij.search(query, limit)
                results["sources"]["icij_offshore_leaks"] = [asdict(r) for r in icij_results]
            except Exception as e:
                results["sources"]["icij_offshore_leaks"] = {"error": str(e)}

        return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Corporate intelligence aggregator")
    parser.add_argument("query", help="Company name to investigate")
    parser.add_argument("--limit", type=int, default=5, help="Max results per source")
    parser.add_argument("--output", "-o", help="Output JSON file")
    args = parser.parse_args()

    ci = CorporateIntel()
    results = ci.investigate(args.query, limit=args.limit)

    if args.output:
        Path(args.output).write_text(json.dumps(results, indent=2))
        print(f"Results written to {args.output}")
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
