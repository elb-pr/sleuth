#!/usr/bin/env python3
"""
claude-sleuth :: dependency installer
Installs pip dependencies for the investigation toolkit.
Supports module selection for targeted installs.

Usage:
    python3 setup.py                    # Install all modules
    python3 setup.py --modules core     # Install core only
    python3 setup.py --modules core,geo # Install core + geolocation
    python3 setup.py --list             # List available modules
    python3 setup.py --dry-run          # Show what would install
"""

import subprocess
import sys
import time
import argparse

MODULES = {
    "core": {
        "description": "Essential HTTP, data handling, and utility libraries",
        "packages": [
            "requests",
            "httpx",
            "aiohttp",
            "beautifulsoup4",
            "lxml",
            "pandas",
            "numpy",
            "rich",
            "tqdm",
            "python-dateutil",
            "pytz",
        ],
    },
    "identity": {
        "description": "Username enumeration and identity research",
        "packages": [
            "sherlock-project",
            "maigret",
        ],
    },
    "social": {
        "description": "Social media archiving and content capture",
        "packages": [
            "yt-dlp",
            "gallery-dl",
            "instaloader",
            "playwright",
        ],
    },
    "network": {
        "description": "DNS, domain, and infrastructure investigation",
        "packages": [
            "dnspython",
            "tldextract",
            "ipwhois",
            "whois",
        ],
    },
    "corporate": {
        "description": "Corporate registry and financial analysis",
        "packages": [
            "edgartools",
        ],
    },
    "sanctions": {
        "description": "Sanctions screening and fuzzy matching",
        "packages": [
            "rapidfuzz",
            "jellyfish",
            "nameparser",
        ],
    },
    "geo": {
        "description": "Geolocation, mapping, and spatial analysis",
        "packages": [
            "geopandas",
            "geopy",
            "folium",
            "pysolar",
            "exifread",
            "shapely",
        ],
    },
    "nlp": {
        "description": "Natural language processing and entity extraction",
        "packages": [
            "spacy",
            "nltk",
            "scikit-learn",
        ],
    },
    "graph": {
        "description": "Network graph analysis and visualisation",
        "packages": [
            "networkx",
            "pyvis",
            "matplotlib",
            "plotly",
            "seaborn",
        ],
    },
    "archiving": {
        "description": "Evidence preservation and web archiving",
        "packages": [
            "waybackpy",
            "warcio",
            "trafilatura",
        ],
    },
    "documents": {
        "description": "PDF processing, OCR, and document handling",
        "packages": [
            "pdfplumber",
            "pypdf",
            "pytesseract",
            "Pillow",
            "markitdown",
        ],
    },
    "reporting": {
        "description": "Report generation (HTML/PDF/Word)",
        "packages": [
            "jinja2",
            "weasyprint",
            "docxtpl",
            "markdown",
            "wordcloud",
        ],
    },
    "entity_resolution": {
        "description": "Record linkage and entity deduplication",
        "packages": [
            "recordlinkage",
        ],
    },
}


def install(package: str) -> tuple:
    t0 = time.time()
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package, "--break-system-packages", "-q"],
        capture_output=True,
        text=True,
    )
    elapsed = round((time.time() - t0) * 1000)
    ok = result.returncode == 0
    msg = (result.stdout + result.stderr).strip().split("\n")[-1][:120]
    return ok, elapsed, msg


def get_all_packages(module_names: list) -> list:
    seen = set()
    packages = []
    for name in module_names:
        for pkg in MODULES[name]["packages"]:
            if pkg not in seen:
                seen.add(pkg)
                packages.append(pkg)
    return packages


def main():
    parser = argparse.ArgumentParser(description="claude-sleuth dependency installer")
    parser.add_argument(
        "--modules",
        type=str,
        default=None,
        help="Comma-separated list of modules to install (default: all)",
    )
    parser.add_argument("--list", action="store_true", help="List available modules")
    parser.add_argument("--dry-run", action="store_true", help="Show packages without installing")
    args = parser.parse_args()

    if args.list:
        print("Available modules:\n")
        for name, info in MODULES.items():
            pkg_count = len(info["packages"])
            print(f"  {name:<20} {info['description']} ({pkg_count} packages)")
        total = len(set(pkg for m in MODULES.values() for pkg in m["packages"]))
        print(f"\nTotal unique packages across all modules: {total}")
        return

    if args.modules:
        selected = [m.strip() for m in args.modules.split(",")]
        invalid = [m for m in selected if m not in MODULES]
        if invalid:
            print(f"Unknown modules: {', '.join(invalid)}")
            print(f"Available: {', '.join(MODULES.keys())}")
            sys.exit(1)
    else:
        selected = list(MODULES.keys())

    packages = get_all_packages(selected)

    print("claude-sleuth :: dependency installer")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Modules: {', '.join(selected)}")
    print(f"Packages: {len(packages)}\n")

    if args.dry_run:
        print("Dry run -- packages that would be installed:")
        for pkg in packages:
            print(f"  {pkg}")
        return

    print(f"{'Package':<24} {'Status':<6} {'Time':>8}  Note")
    print("-" * 78)

    passed, failed = [], []

    for pkg in packages:
        ok, ms, note = install(pkg)
        status = "OK" if ok else "FAIL"
        note_display = note if not ok else ""
        print(f"{pkg:<24} {status:<6} {ms:>7}ms  {note_display}")
        (passed if ok else failed).append(pkg)

    print("-" * 78)
    print(f"\nDone. {len(passed)} installed, {len(failed)} failed.")

    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
