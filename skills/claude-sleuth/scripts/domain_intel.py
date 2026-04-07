#!/usr/bin/env python3
"""
claude-sleuth :: domain intelligence collector
Unified domain investigation pipeline combining DNS, RDAP, crt.sh,
Shodan InternetDB, and HTTP probing.

All sources are zero-auth, zero-cost.

Usage:
    from scripts.domain_intel import DomainIntel
    di = DomainIntel()
    report = di.investigate("example.com")
"""

import json
import socket
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
    import dns.resolver
    HAS_DNS = True
except ImportError:
    HAS_DNS = False

try:
    import tldextract
    HAS_TLD = True
except ImportError:
    HAS_TLD = False


class DNSCollector:
    """Standard DNS record enumeration."""
    RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA", "SRV", "CAA"]

    def query_all(self, domain: str) -> dict:
        if not HAS_DNS:
            return {"error": "dnspython not installed"}

        results = {}
        resolver = dns.resolver.Resolver()
        resolver.timeout = 5
        resolver.lifetime = 10

        for rtype in self.RECORD_TYPES:
            try:
                answers = resolver.resolve(domain, rtype)
                results[rtype] = [str(r) for r in answers]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
                continue
            except dns.exception.Timeout:
                results[rtype] = ["TIMEOUT"]
            except Exception:
                continue

        return results


class CrtSh:
    """Certificate Transparency log search via crt.sh."""
    BASE = "https://crt.sh"

    def search(self, domain: str) -> list:
        if not HAS_REQUESTS:
            return []
        try:
            resp = requests.get(
                f"{self.BASE}/",
                params={"q": f"%.{domain}", "output": "json"},
                timeout=30,
            )
            if resp.status_code != 200:
                return []
            entries = resp.json()
            # Deduplicate by common_name
            seen = set()
            unique = []
            for e in entries:
                cn = e.get("common_name", "")
                if cn not in seen:
                    seen.add(cn)
                    unique.append({
                        "common_name": cn,
                        "name_value": e.get("name_value", ""),
                        "issuer_name": e.get("issuer_name", ""),
                        "not_before": e.get("not_before", ""),
                        "not_after": e.get("not_after", ""),
                    })
            return unique
        except Exception:
            return []


class RDAP:
    """RDAP domain registration lookup."""
    BASE = "https://rdap.org/domain"

    def lookup(self, domain: str) -> dict:
        if not HAS_REQUESTS:
            return {"error": "requests not installed"}
        try:
            resp = requests.get(f"{self.BASE}/{domain}", timeout=15)
            if resp.status_code != 200:
                return {"error": f"HTTP {resp.status_code}"}
            data = resp.json()
            # Extract key fields
            result = {
                "status": data.get("status", []),
                "events": [],
                "entities": [],
                "nameservers": [ns.get("ldhName", "") for ns in data.get("nameservers", [])],
            }
            for event in data.get("events", []):
                result["events"].append({
                    "action": event.get("eventAction", ""),
                    "date": event.get("eventDate", ""),
                })
            for entity in data.get("entities", []):
                result["entities"].append({
                    "roles": entity.get("roles", []),
                    "handle": entity.get("handle", ""),
                })
            return result
        except Exception as e:
            return {"error": str(e)}


class ShodanInternetDB:
    """Shodan InternetDB -- zero auth IP enrichment."""
    BASE = "https://internetdb.shodan.io"

    def lookup(self, ip: str) -> dict:
        if not HAS_REQUESTS:
            return {"error": "requests not installed"}
        try:
            resp = requests.get(f"{self.BASE}/{ip}", timeout=10)
            if resp.status_code == 404:
                return {"status": "not_found"}
            if resp.status_code != 200:
                return {"error": f"HTTP {resp.status_code}"}
            return resp.json()
        except Exception as e:
            return {"error": str(e)}


class DomainIntel:
    """Unified domain intelligence pipeline."""

    def __init__(self):
        self.dns = DNSCollector()
        self.crtsh = CrtSh()
        self.rdap = RDAP()
        self.shodan = ShodanInternetDB()

    def _resolve_ips(self, domain: str) -> list:
        """Resolve domain to IP addresses."""
        try:
            results = socket.getaddrinfo(domain, None)
            return list(set(r[4][0] for r in results))
        except socket.gaierror:
            return []

    def investigate(self, domain: str) -> dict:
        """Full domain intelligence report."""
        report = {
            "domain": domain,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "sections": {},
        }

        # Extract registrable domain
        if HAS_TLD:
            extracted = tldextract.extract(domain)
            report["parsed"] = {
                "subdomain": extracted.subdomain,
                "domain": extracted.domain,
                "suffix": extracted.suffix,
                "registered_domain": extracted.registered_domain,
            }

        # 1. DNS records
        report["sections"]["dns"] = self.dns.query_all(domain)

        # 2. RDAP registration
        report["sections"]["rdap"] = self.rdap.lookup(domain)

        # 3. Certificate transparency (subdomains)
        ct_results = self.crtsh.search(domain)
        report["sections"]["certificate_transparency"] = {
            "unique_entries": len(ct_results),
            "subdomains": list(set(e["common_name"] for e in ct_results)),
            "certificates": ct_results[:50],  # Cap at 50 for readability
        }

        # 4. IP resolution + Shodan enrichment
        ips = self._resolve_ips(domain)
        ip_intel = []
        for ip in ips:
            shodan_data = self.shodan.lookup(ip)
            ip_intel.append({"ip": ip, "shodan": shodan_data})
            time.sleep(0.2)
        report["sections"]["ip_intelligence"] = ip_intel

        # 5. Summary
        dns_data = report["sections"]["dns"]
        report["summary"] = {
            "ips_found": len(ips),
            "subdomains_found": len(ct_results),
            "has_mx": "MX" in dns_data,
            "has_spf": any("v=spf1" in txt for txt in dns_data.get("TXT", [])),
            "has_dmarc": False,  # Would need _dmarc.domain query
            "nameservers": dns_data.get("NS", []),
        }

        # Check DMARC
        if HAS_DNS:
            try:
                dmarc_answers = dns.resolver.resolve(f"_dmarc.{domain}", "TXT")
                report["summary"]["has_dmarc"] = True
                report["sections"]["dns"]["DMARC"] = [str(r) for r in dmarc_answers]
            except Exception:
                pass

        return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Domain intelligence collector")
    parser.add_argument("domain", help="Domain to investigate")
    parser.add_argument("--output", "-o", help="Output JSON file")
    args = parser.parse_args()

    di = DomainIntel()
    report = di.investigate(args.domain)

    if args.output:
        Path(args.output).write_text(json.dumps(report, indent=2))
        print(f"Report written to {args.output}")
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
