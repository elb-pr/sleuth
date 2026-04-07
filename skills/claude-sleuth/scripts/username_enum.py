#!/usr/bin/env python3
"""
claude-sleuth :: username enumeration
Thin wrapper around Maigret/Sherlock with standardised JSON output.
Falls back to direct HTTP checks against WhatsMyName data if neither is installed.

Usage:
    from scripts.username_enum import UsernameEnumerator
    ue = UsernameEnumerator()
    results = await ue.search("target_username")
"""

import asyncio
import json
import subprocess
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def _find_tool(name: str) -> Optional[str]:
    """Check if a CLI tool is available."""
    return shutil.which(name)


class UsernameEnumerator:
    """Username enumeration with fallback chain."""

    def __init__(self):
        self.maigret_path = _find_tool("maigret")
        self.sherlock_path = _find_tool("sherlock")

    async def search(self, username: str, timeout: int = 120) -> dict:
        """Search for username across platforms. Tries Maigret -> Sherlock -> WhatsMyName."""
        result = {
            "username": username,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "tool_used": None,
            "profiles_found": [],
            "total_found": 0,
            "total_checked": 0,
        }

        if self.maigret_path:
            return await self._search_maigret(username, result, timeout)
        elif self.sherlock_path:
            return await self._search_sherlock(username, result, timeout)
        else:
            return await self._search_whatsmyname(username, result)

    async def _search_maigret(self, username: str, result: dict, timeout: int) -> dict:
        """Run Maigret and parse output."""
        result["tool_used"] = "maigret"
        output_dir = Path(f"/tmp/maigret_{username}")
        output_dir.mkdir(exist_ok=True)
        json_path = output_dir / "report.json"

        cmd = [
            self.maigret_path, username,
            "--json", "simple",
            "-o", str(json_path),
            "--timeout", str(timeout),
            "--no-color",
        ]

        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout + 30)

            if json_path.exists():
                data = json.loads(json_path.read_text())
                if isinstance(data, list):
                    for entry in data:
                        if isinstance(entry, dict):
                            result["profiles_found"].append({
                                "platform": entry.get("sitename", entry.get("site", "")),
                                "url": entry.get("url", ""),
                                "status": entry.get("status", ""),
                            })
                elif isinstance(data, dict):
                    for site, info in data.items():
                        if isinstance(info, dict) and info.get("status", "").lower() == "claimed":
                            result["profiles_found"].append({
                                "platform": site,
                                "url": info.get("url", ""),
                                "status": "claimed",
                            })

            result["total_found"] = len(result["profiles_found"])
        except asyncio.TimeoutError:
            result["error"] = f"Maigret timed out after {timeout}s"
        except Exception as e:
            result["error"] = str(e)

        return result

    async def _search_sherlock(self, username: str, result: dict, timeout: int) -> dict:
        """Run Sherlock and parse output."""
        result["tool_used"] = "sherlock"
        output_path = Path(f"/tmp/sherlock_{username}.json")

        cmd = [
            self.sherlock_path, username,
            "--output", str(output_path),
            "--json",
            "--timeout", "15",
        ]

        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            await asyncio.wait_for(proc.communicate(), timeout=timeout)

            if output_path.exists():
                data = json.loads(output_path.read_text())
                for site, info in data.items():
                    if info.get("status", "").lower() == "claimed":
                        result["profiles_found"].append({
                            "platform": site,
                            "url": info.get("url_user", ""),
                            "status": "claimed",
                        })

            result["total_found"] = len(result["profiles_found"])
        except asyncio.TimeoutError:
            result["error"] = f"Sherlock timed out after {timeout}s"
        except Exception as e:
            result["error"] = str(e)

        return result

    async def _search_whatsmyname(self, username: str, result: dict) -> dict:
        """Fallback: direct HTTP checks using WhatsMyName data."""
        result["tool_used"] = "whatsmyname_direct"

        if not HAS_REQUESTS:
            result["error"] = "No enumeration tools available (install maigret, sherlock, or requests)"
            return result

        # Fetch WhatsMyName data
        wmn_url = "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"
        try:
            resp = requests.get(wmn_url, timeout=15)
            if resp.status_code != 200:
                result["error"] = f"Failed to fetch WhatsMyName data: HTTP {resp.status_code}"
                return result
            sites = resp.json().get("sites", [])
        except Exception as e:
            result["error"] = f"Failed to fetch WhatsMyName data: {e}"
            return result

        result["total_checked"] = len(sites)

        # Check top 100 sites (rate-limited)
        checked = 0
        for site in sites[:100]:
            uri_check = site.get("uri_check", "").replace("{account}", username)
            if not uri_check:
                continue
            try:
                resp = requests.get(uri_check, timeout=5, allow_redirects=True, headers={"User-Agent": "claude-sleuth/1.0"})
                e_code = site.get("e_code", 200)
                e_string = site.get("e_string", "")

                if resp.status_code == e_code:
                    if not e_string or e_string in resp.text:
                        result["profiles_found"].append({
                            "platform": site.get("name", ""),
                            "url": uri_check,
                            "status": "claimed",
                            "category": site.get("cat", ""),
                        })
                checked += 1
            except Exception:
                continue

        result["total_checked"] = checked
        result["total_found"] = len(result["profiles_found"])
        result["note"] = "Limited to 100 sites in fallback mode. Install maigret for full 3000+ site coverage."
        return result


async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Username enumeration")
    parser.add_argument("username", help="Username to search")
    parser.add_argument("--output", "-o", help="Output JSON file")
    args = parser.parse_args()

    ue = UsernameEnumerator()
    results = await ue.search(args.username)

    print(f"Tool: {results['tool_used']}")
    print(f"Found: {results['total_found']} profiles")

    if args.output:
        Path(args.output).write_text(json.dumps(results, indent=2))
    else:
        for p in results["profiles_found"]:
            print(f"  {p['platform']}: {p['url']}")


if __name__ == "__main__":
    asyncio.run(main())
