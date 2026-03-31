#!/usr/bin/env python3
"""
dci-claudian :: imports setup
Installs all verified pip dependencies for the scripts/imports bundle.
Run with: python3 setup.py
"""

import subprocess
import sys
import time

PACKAGES = [
    # Core investigation tools
    "geopandas",
    "instaloader",
    "maigret",
    "markitdown",
    # Analysis & visualisation
    "matplotlib",
    "networkx",
    "plotly",
    "seaborn",
    "wordcloud",
    # NLP & text analysis
    "nltk",
    "scikit-learn",
    # Data handling
    "pandas",
    "numpy",
]

def install(package: str) -> tuple[bool, int, str]:
    t0 = time.time()
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package, "--break-system-packages", "-q"],
        capture_output=True,
        text=True,
    )
    elapsed = round((time.time() - t0) * 1000)
    ok = result.returncode == 0
    msg = (result.stdout + result.stderr).strip().split("\n")[-1][:100]
    return ok, elapsed, msg


def main():
    print("dci-claudian :: dependency installer")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Packages: {len(PACKAGES)}\n")
    print(f"{'Package':<20} {'Status':<6} {'Time':>8}  Note")
    print("-" * 70)

    passed, failed = [], []

    for pkg in PACKAGES:
        ok, ms, note = install(pkg)
        status = "OK" if ok else "FAIL"
        note_display = note if not ok else ""
        print(f"{pkg:<20} {status:<6} {ms:>7}ms  {note_display}")
        (passed if ok else failed).append(pkg)

    print("-" * 70)
    print(f"\nDone. {len(passed)} installed, {len(failed)} failed.")

    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
