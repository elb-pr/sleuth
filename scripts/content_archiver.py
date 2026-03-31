#!/usr/bin/env python3
"""
claude-sleuth :: content archiver
Unified media capture: yt-dlp + gallery-dl + Playwright screenshots.
Downloads, hashes, and catalogues captured media.

Usage:
    from scripts.content_archiver import ContentArchiver
    ca = ContentArchiver(output_dir="./captures")
    result = await ca.archive("https://youtube.com/watch?v=...")
"""

import asyncio
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    from playwright.async_api import async_playwright
    HAS_PLAYWRIGHT = True
except ImportError:
    HAS_PLAYWRIGHT = False


def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _has_tool(name: str) -> bool:
    return shutil.which(name) is not None


class ContentArchiver:
    """Multi-tool content archiver with hash verification."""

    def __init__(self, output_dir: str = "./captures"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.has_ytdlp = _has_tool("yt-dlp")
        self.has_gallery_dl = _has_tool("gallery-dl")

    def _capture_dir(self, url: str) -> Path:
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        safe = url.replace("https://", "").replace("http://", "").replace("/", "_")[:50]
        path = self.output_dir / f"{ts}_{safe}"
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _hash_directory(self, directory: Path) -> list:
        """Hash all files in a directory."""
        hashes = []
        for f in sorted(directory.rglob("*")):
            if f.is_file():
                hashes.append({
                    "file": str(f.relative_to(directory)),
                    "sha256": sha256_file(f),
                    "bytes": f.stat().st_size,
                })
        return hashes

    async def download_ytdlp(self, url: str, capture_dir: Path) -> dict:
        """Download media via yt-dlp."""
        if not self.has_ytdlp:
            return {"tool": "yt-dlp", "status": "skipped", "reason": "not installed"}

        media_dir = capture_dir / "media"
        media_dir.mkdir(exist_ok=True)

        cmd = [
            "yt-dlp",
            url,
            "-o", str(media_dir / "%(title)s.%(ext)s"),
            "--write-info-json",
            "--write-thumbnail",
            "--write-description",
            "--write-subs",
            "--no-progress",
            "--restrict-filenames",
        ]

        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=300)

            files = self._hash_directory(media_dir)
            return {
                "tool": "yt-dlp",
                "status": "success" if proc.returncode == 0 else "partial",
                "return_code": proc.returncode,
                "files": files,
                "total_files": len(files),
            }
        except asyncio.TimeoutError:
            return {"tool": "yt-dlp", "status": "timeout"}
        except Exception as e:
            return {"tool": "yt-dlp", "status": "error", "message": str(e)}

    async def download_gallery_dl(self, url: str, capture_dir: Path) -> dict:
        """Download images via gallery-dl."""
        if not self.has_gallery_dl:
            return {"tool": "gallery-dl", "status": "skipped", "reason": "not installed"}

        images_dir = capture_dir / "images"
        images_dir.mkdir(exist_ok=True)

        cmd = [
            "gallery-dl",
            url,
            "-d", str(images_dir),
            "--write-metadata",
        ]

        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=300)

            files = self._hash_directory(images_dir)
            return {
                "tool": "gallery-dl",
                "status": "success" if proc.returncode == 0 else "partial",
                "return_code": proc.returncode,
                "files": files,
                "total_files": len(files),
            }
        except asyncio.TimeoutError:
            return {"tool": "gallery-dl", "status": "timeout"}
        except Exception as e:
            return {"tool": "gallery-dl", "status": "error", "message": str(e)}

    async def screenshot(self, url: str, capture_dir: Path) -> dict:
        """Full-page screenshot via Playwright."""
        if not HAS_PLAYWRIGHT:
            return {"tool": "playwright", "status": "skipped", "reason": "not installed"}

        screenshot_path = capture_dir / "screenshot.png"
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page(viewport={"width": 1920, "height": 1080})
                await page.goto(url, wait_until="networkidle", timeout=30000)
                title = await page.title()
                await page.screenshot(path=str(screenshot_path), full_page=True)
                await browser.close()

            return {
                "tool": "playwright",
                "status": "success",
                "path": str(screenshot_path),
                "sha256": sha256_file(screenshot_path),
                "page_title": title,
                "bytes": screenshot_path.stat().st_size,
            }
        except Exception as e:
            return {"tool": "playwright", "status": "error", "message": str(e)}

    async def archive(self, url: str) -> dict:
        """Full archive pipeline: screenshot + media download + image download."""
        capture_dir = self._capture_dir(url)

        result = {
            "url": url,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "capture_directory": str(capture_dir),
            "captures": [],
        }

        # Screenshot first (fast)
        screenshot = await self.screenshot(url, capture_dir)
        result["captures"].append(screenshot)

        # Try yt-dlp for video/media
        ytdlp = await self.download_ytdlp(url, capture_dir)
        result["captures"].append(ytdlp)

        # Try gallery-dl for images
        gallery = await self.download_gallery_dl(url, capture_dir)
        result["captures"].append(gallery)

        # Write manifest
        manifest_path = capture_dir / "manifest.json"
        manifest_path.write_text(json.dumps(result, indent=2))

        successful = sum(1 for c in result["captures"] if c.get("status") == "success")
        result["summary"] = f"{successful}/{len(result['captures'])} tools succeeded"

        return result


async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Content archiver")
    parser.add_argument("urls", nargs="+", help="URLs to archive")
    parser.add_argument("--output", "-o", default="./captures", help="Output directory")
    args = parser.parse_args()

    ca = ContentArchiver(output_dir=args.output)
    for url in args.urls:
        result = await ca.archive(url)
        print(f"{url} -> {result['summary']} -> {result['capture_directory']}")


if __name__ == "__main__":
    asyncio.run(main())
