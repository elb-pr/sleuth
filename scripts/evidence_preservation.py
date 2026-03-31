#!/usr/bin/env python3
"""
claude-sleuth :: evidence preservation pipeline
Captures, hashes, and archives web evidence with chain-of-custody logging.

Capabilities:
    - Full-page screenshots via Playwright
    - HTML/DOM capture
    - SHA-256 hashing of all artefacts
    - WARC file creation (ISO 28500)
    - Wayback Machine submission
    - Chain-of-custody JSON log generation

Usage:
    from scripts.evidence_preservation import EvidencePreserver
    ep = EvidencePreserver(output_dir="./evidence")
    result = await ep.preserve("https://example.com")
"""

import asyncio
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    from playwright.async_api import async_playwright
    HAS_PLAYWRIGHT = True
except ImportError:
    HAS_PLAYWRIGHT = False

try:
    from warcio.warcwriter import WARCWriter
    from warcio.statusandheaders import StatusAndHeaders
    HAS_WARCIO = True
except ImportError:
    HAS_WARCIO = False

try:
    import waybackpy
    HAS_WAYBACK = True
except ImportError:
    HAS_WAYBACK = False

try:
    import httpx
    HAS_HTTPX = True
except ImportError:
    HAS_HTTPX = False


class EvidencePreserver:
    """Captures and preserves web evidence with forensic-grade chain of custody."""

    def __init__(self, output_dir: str = "./evidence", analyst_id: str = "claude-sleuth"):
        self.output_dir = Path(output_dir)
        self.analyst_id = analyst_id
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def sha256_file(filepath: Path) -> str:
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    @staticmethod
    def sha256_bytes(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    def _case_dir(self, url: str) -> Path:
        """Create a timestamped directory for this capture."""
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_")[:60]
        case_path = self.output_dir / f"{ts}_{safe_name}"
        case_path.mkdir(parents=True, exist_ok=True)
        return case_path

    async def capture_screenshot(self, url: str, case_dir: Path) -> Optional[dict]:
        """Full-page screenshot via Playwright."""
        if not HAS_PLAYWRIGHT:
            return {"type": "screenshot", "status": "skipped", "reason": "playwright not installed"}

        screenshot_path = case_dir / "screenshot.png"
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page(viewport={"width": 1920, "height": 1080})
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await page.screenshot(path=str(screenshot_path), full_page=True)
                title = await page.title()
                await browser.close()

            file_hash = self.sha256_file(screenshot_path)
            return {
                "type": "screenshot",
                "status": "captured",
                "path": str(screenshot_path),
                "sha256": file_hash,
                "page_title": title,
                "bytes": screenshot_path.stat().st_size,
            }
        except Exception as e:
            return {"type": "screenshot", "status": "failed", "error": str(e)}

    async def capture_html(self, url: str, case_dir: Path) -> Optional[dict]:
        """Raw HTML capture via httpx."""
        if not HAS_HTTPX:
            return {"type": "html", "status": "skipped", "reason": "httpx not installed"}

        html_path = case_dir / "page.html"
        headers_path = case_dir / "response_headers.json"
        try:
            async with httpx.AsyncClient(follow_redirects=True, timeout=30.0) as client:
                resp = await client.get(url, headers={"User-Agent": "claude-sleuth/1.0 (evidence-preservation)"})

            html_bytes = resp.content
            html_path.write_bytes(html_bytes)
            headers_path.write_text(json.dumps(dict(resp.headers), indent=2))

            return {
                "type": "html",
                "status": "captured",
                "path": str(html_path),
                "sha256": self.sha256_bytes(html_bytes),
                "status_code": resp.status_code,
                "bytes": len(html_bytes),
                "headers_path": str(headers_path),
            }
        except Exception as e:
            return {"type": "html", "status": "failed", "error": str(e)}

    def create_warc(self, url: str, case_dir: Path, html_path: Path) -> Optional[dict]:
        """Create ISO 28500 WARC file from captured HTML."""
        if not HAS_WARCIO:
            return {"type": "warc", "status": "skipped", "reason": "warcio not installed"}
        if not html_path.exists():
            return {"type": "warc", "status": "skipped", "reason": "no HTML capture to archive"}

        warc_path = case_dir / "capture.warc.gz"
        try:
            with open(warc_path, "wb") as fh:
                writer = WARCWriter(fh, gzip=True)
                with open(html_path, "rb") as payload:
                    headers = StatusAndHeaders(
                        "200 OK",
                        [("Content-Type", "text/html")],
                        protocol="HTTP/1.1",
                    )
                    record = writer.create_warc_record(
                        url,
                        "response",
                        payload=payload,
                        http_headers=headers,
                    )
                    writer.write_record(record)

            return {
                "type": "warc",
                "status": "created",
                "path": str(warc_path),
                "sha256": self.sha256_file(warc_path),
                "bytes": warc_path.stat().st_size,
            }
        except Exception as e:
            return {"type": "warc", "status": "failed", "error": str(e)}

    def submit_wayback(self, url: str) -> dict:
        """Submit URL to Wayback Machine for independent corroboration."""
        if not HAS_WAYBACK:
            return {"type": "wayback", "status": "skipped", "reason": "waybackpy not installed"}

        try:
            user_agent = "claude-sleuth/1.0 (evidence-preservation)"
            save_api = waybackpy.WaybackMachineSaveAPI(url, user_agent)
            save_api.save()
            return {
                "type": "wayback",
                "status": "submitted",
                "archive_url": save_api.archive_url,
                "timestamp": save_api.timestamp().isoformat() if hasattr(save_api, 'timestamp') else None,
            }
        except Exception as e:
            return {"type": "wayback", "status": "failed", "error": str(e)}

    async def preserve(self, url: str, submit_to_wayback: bool = True) -> dict:
        """Full evidence preservation pipeline for a single URL."""
        case_dir = self._case_dir(url)
        capture_utc = datetime.now(timezone.utc).isoformat()

        artefacts = []

        # 1. Screenshot
        screenshot = await self.capture_screenshot(url, case_dir)
        artefacts.append(screenshot)

        # 2. HTML capture
        html_result = await self.capture_html(url, case_dir)
        artefacts.append(html_result)

        # 3. WARC creation
        html_path = case_dir / "page.html"
        warc_result = self.create_warc(url, case_dir, html_path)
        artefacts.append(warc_result)

        # 4. Wayback Machine submission
        if submit_to_wayback:
            wb_result = self.submit_wayback(url)
            artefacts.append(wb_result)

        # 5. Chain-of-custody log
        custody_log = {
            "schema_version": "1.0",
            "case_directory": str(case_dir),
            "target_url": url,
            "capture_utc": capture_utc,
            "analyst_id": self.analyst_id,
            "tool": "claude-sleuth/evidence_preservation",
            "tool_version": "1.0.0",
            "python_version": sys.version.split()[0],
            "artefacts": artefacts,
        }

        log_path = case_dir / "chain_of_custody.json"
        log_path.write_text(json.dumps(custody_log, indent=2))

        return custody_log

    async def preserve_batch(self, urls: list, submit_to_wayback: bool = True) -> list:
        """Preserve multiple URLs sequentially (respects rate limits)."""
        results = []
        for url in urls:
            result = await self.preserve(url, submit_to_wayback=submit_to_wayback)
            results.append(result)
            time.sleep(1)  # Rate limit courtesy
        return results


async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Evidence preservation pipeline")
    parser.add_argument("urls", nargs="+", help="URLs to preserve")
    parser.add_argument("--output", "-o", default="./evidence", help="Output directory")
    parser.add_argument("--analyst", default="claude-sleuth", help="Analyst identifier")
    parser.add_argument("--no-wayback", action="store_true", help="Skip Wayback Machine submission")
    args = parser.parse_args()

    ep = EvidencePreserver(output_dir=args.output, analyst_id=args.analyst)
    results = await ep.preserve_batch(args.urls, submit_to_wayback=not args.no_wayback)

    for r in results:
        captured = sum(1 for a in r["artefacts"] if a.get("status") in ("captured", "created", "submitted"))
        total = len(r["artefacts"])
        print(f"{r['target_url']} -- {captured}/{total} artefacts preserved -> {r['case_directory']}")


if __name__ == "__main__":
    asyncio.run(main())
