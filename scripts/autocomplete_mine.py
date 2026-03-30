#!/usr/bin/env python3
"""
YouTube Autocomplete Miner

Systematically extracts keyword suggestions from YouTube's autocomplete API.
Use for discovering long-tail keywords and understanding real search patterns.

Usage:
    python autocomplete_mine.py "Drake Type Beat" --depth 2 --output keywords.json
"""

import argparse
import json
import time
import urllib.parse
import urllib.request
from typing import Optional
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class KeywordResult:
    """Single keyword result with metadata."""
    keyword: str
    seed: str
    depth: int
    suffix: str
    discovered_at: str


def fetch_suggestions(
    query: str,
    language: str = "en",
    country: str = "gb"
) -> list[str]:
    """
    Fetch autocomplete suggestions from YouTube.
    
    Args:
        query: Search query to get suggestions for
        language: Language code (hl parameter)
        country: Country code (gl parameter)
    
    Returns:
        List of suggestion strings
    """
    base_url = "http://suggestqueries.google.com/complete/search"
    params = {
        "client": "youtube",
        "q": query,
        "hl": language,
        "gl": country,
        "ds": "yt"  # YouTube dataset
    }
    
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            # Response is JSONP, need to extract JSON
            data = response.read().decode("utf-8")
            # Parse JSONP: window.google.ac.h(["query",[suggestions],...])
            # Extract the array portion
            start = data.find("(") + 1
            end = data.rfind(")")
            json_data = json.loads(data[start:end])
            
            # Suggestions are in index 1
            if len(json_data) > 1 and isinstance(json_data[1], list):
                return [item[0] for item in json_data[1] if isinstance(item, list)]
            return []
            
    except Exception as e:
        print(f"Error fetching suggestions for '{query}': {e}")
        return []


def mine_keyword_tree(
    seed: str,
    depth: int = 1,
    delay: float = 0.3,
    language: str = "en",
    country: str = "gb"
) -> list[KeywordResult]:
    """
    Mine keyword tree starting from seed.
    
    Args:
        seed: Starting keyword (e.g., "Drake Type Beat")
        depth: How many levels of alphabet suffixing to perform
        delay: Delay between requests (seconds) to avoid rate limiting
        language: Language code
        country: Country code
    
    Returns:
        List of KeywordResult objects
    """
    results: list[KeywordResult] = []
    seen: set[str] = set()
    timestamp = datetime.utcnow().isoformat()
    
    # Level 0: Base seed
    base_suggestions = fetch_suggestions(seed, language, country)
    for kw in base_suggestions:
        if kw not in seen:
            seen.add(kw)
            results.append(KeywordResult(
                keyword=kw,
                seed=seed,
                depth=0,
                suffix="",
                discovered_at=timestamp
            ))
    
    time.sleep(delay)
    
    # Alphabet soup: a-z, 0-9
    suffixes = list("abcdefghijklmnopqrstuvwxyz0123456789")
    
    # Additional type beat specific suffixes
    type_beat_suffixes = [
        "2024", "2025", "2026",
        "free", "hard", "dark", "sad", "emotional",
        "melodic", "aggressive", "chill"
    ]
    
    all_suffixes = suffixes + type_beat_suffixes
    
    for current_depth in range(1, depth + 1):
        print(f"Mining depth {current_depth}...")
        
        for suffix in all_suffixes:
            query = f"{seed} {suffix}"
            suggestions = fetch_suggestions(query, language, country)
            
            for kw in suggestions:
                if kw not in seen:
                    seen.add(kw)
                    results.append(KeywordResult(
                        keyword=kw,
                        seed=seed,
                        depth=current_depth,
                        suffix=suffix,
                        discovered_at=timestamp
                    ))
            
            time.sleep(delay)
    
    return results


def analyse_results(results: list[KeywordResult]) -> dict:
    """
    Analyse mined keywords for patterns.
    
    Returns summary statistics and grouped keywords.
    """
    analysis = {
        "total_keywords": len(results),
        "by_depth": {},
        "artist_mentions": [],
        "year_mentions": [],
        "mood_descriptors": [],
        "genre_descriptors": []
    }
    
    # Count by depth
    for r in results:
        depth_key = str(r.depth)
        analysis["by_depth"][depth_key] = analysis["by_depth"].get(depth_key, 0) + 1
    
    # Categorise keywords
    moods = ["dark", "sad", "emotional", "happy", "chill", "aggressive", "hard", "melodic", "evil"]
    genres = ["drill", "trap", "r&b", "rnb", "jazz", "lofi", "lo-fi", "rage", "sample"]
    years = ["2024", "2025", "2026"]
    
    for r in results:
        kw_lower = r.keyword.lower()
        
        for mood in moods:
            if mood in kw_lower:
                if mood not in analysis["mood_descriptors"]:
                    analysis["mood_descriptors"].append(mood)
        
        for genre in genres:
            if genre in kw_lower:
                if genre not in analysis["genre_descriptors"]:
                    analysis["genre_descriptors"].append(genre)
        
        for year in years:
            if year in kw_lower:
                if year not in analysis["year_mentions"]:
                    analysis["year_mentions"].append(year)
    
    return analysis


def export_results(
    results: list[KeywordResult],
    analysis: dict,
    output_path: str,
    format: str = "json"
) -> None:
    """Export results to file."""
    
    if format == "json":
        output = {
            "metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "total_keywords": len(results)
            },
            "analysis": analysis,
            "keywords": [asdict(r) for r in results]
        }
        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)
    
    elif format == "csv":
        import csv
        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["keyword", "seed", "depth", "suffix", "discovered_at"])
            for r in results:
                writer.writerow([r.keyword, r.seed, r.depth, r.suffix, r.discovered_at])
    
    elif format == "txt":
        with open(output_path, "w") as f:
            for r in results:
                f.write(r.keyword + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Mine YouTube autocomplete suggestions for keyword research"
    )
    parser.add_argument(
        "seed",
        help="Seed keyword to start mining (e.g., 'Drake Type Beat')"
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=1,
        help="Depth of alphabet soup mining (1-3 recommended)"
    )
    parser.add_argument(
        "--output",
        "-o",
        default="keywords.json",
        help="Output file path"
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["json", "csv", "txt"],
        default="json",
        help="Output format"
    )
    parser.add_argument(
        "--language",
        "-l",
        default="en",
        help="Language code (default: en)"
    )
    parser.add_argument(
        "--country",
        "-c",
        default="gb",
        help="Country code (default: gb)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.3,
        help="Delay between requests in seconds (default: 0.3)"
    )
    
    args = parser.parse_args()
    
    print(f"Mining keywords for: {args.seed}")
    print(f"Depth: {args.depth}, Language: {args.language}, Country: {args.country}")
    print("-" * 50)
    
    results = mine_keyword_tree(
        seed=args.seed,
        depth=args.depth,
        delay=args.delay,
        language=args.language,
        country=args.country
    )
    
    print(f"\nFound {len(results)} unique keywords")
    
    analysis = analyse_results(results)
    print(f"\nAnalysis:")
    print(f"  By depth: {analysis['by_depth']}")
    print(f"  Moods found: {analysis['mood_descriptors']}")
    print(f"  Genres found: {analysis['genre_descriptors']}")
    
    export_results(results, analysis, args.output, args.format)
    print(f"\nResults exported to: {args.output}")


if __name__ == "__main__":
    main()
