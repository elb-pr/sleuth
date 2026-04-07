#!/usr/bin/env python3
"""
claude-sleuth :: chronological matrix
UTC-normalised timeline construction with gap detection and conflict flagging.

Usage:
    from scripts.chronological_matrix import ChronologicalMatrix
    cm = ChronologicalMatrix()
    cm.add_event("2025-06-15T14:30:00+01:00", "Meeting at cafe", source="witness_1")
    cm.add_event("2025-06-15T13:30:00Z", "Meeting at cafe", source="cctv")
    report = cm.analyse()
"""

import json
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


@dataclass
class TimelineEvent:
    event_id: str
    original_datetime: str
    utc_datetime: str
    description: str
    source: str = ""
    source_reliability: str = ""  # A-F (Admiralty)
    info_credibility: str = ""   # 1-6 (Admiralty)
    entities_involved: list = field(default_factory=list)
    location: str = ""
    category: str = ""  # communication, movement, financial, meeting, incident, document, other
    evidence_ref: str = ""
    notes: str = ""
    conflicts_with: list = field(default_factory=list)


def parse_to_utc(dt_string: str) -> Optional[datetime]:
    """Parse various datetime formats and normalise to UTC."""
    formats = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S%z",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
        "%d/%m/%Y %H:%M:%S",
        "%d/%m/%Y %H:%M",
        "%d/%m/%Y",
        "%m/%d/%Y %H:%M:%S",
        "%m/%d/%Y",
    ]

    # Handle Z suffix
    dt_string = dt_string.strip()
    if dt_string.endswith("Z"):
        dt_string = dt_string[:-1] + "+00:00"

    for fmt in formats:
        try:
            dt = datetime.strptime(dt_string, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            continue

    # Try Python's fromisoformat
    try:
        dt = datetime.fromisoformat(dt_string)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


class ChronologicalMatrix:
    """UTC-normalised investigation timeline."""

    def __init__(self):
        self.events: list[TimelineEvent] = []
        self._counter = 0

    def add_event(
        self,
        datetime_str: str,
        description: str,
        source: str = "",
        source_reliability: str = "",
        info_credibility: str = "",
        entities: list = None,
        location: str = "",
        category: str = "other",
        evidence_ref: str = "",
        notes: str = "",
    ) -> Optional[str]:
        """Add an event to the timeline."""
        utc_dt = parse_to_utc(datetime_str)
        if utc_dt is None:
            return None

        self._counter += 1
        event_id = f"EVT-{self._counter:04d}"

        event = TimelineEvent(
            event_id=event_id,
            original_datetime=datetime_str,
            utc_datetime=utc_dt.isoformat(),
            description=description,
            source=source,
            source_reliability=source_reliability,
            info_credibility=info_credibility,
            entities_involved=entities or [],
            location=location,
            category=category,
            evidence_ref=evidence_ref,
            notes=notes,
        )
        self.events.append(event)
        return event_id

    def _sorted_events(self) -> list:
        """Return events sorted by UTC datetime."""
        return sorted(self.events, key=lambda e: e.utc_datetime)

    def detect_gaps(self, min_gap_hours: float = 24.0) -> list:
        """Identify temporal gaps exceeding threshold."""
        sorted_events = self._sorted_events()
        gaps = []

        for i in range(1, len(sorted_events)):
            dt1 = datetime.fromisoformat(sorted_events[i - 1].utc_datetime)
            dt2 = datetime.fromisoformat(sorted_events[i].utc_datetime)
            delta = dt2 - dt1
            hours = delta.total_seconds() / 3600

            if hours >= min_gap_hours:
                gaps.append({
                    "gap_start": sorted_events[i - 1].utc_datetime,
                    "gap_end": sorted_events[i].utc_datetime,
                    "duration_hours": round(hours, 2),
                    "before_event": sorted_events[i - 1].event_id,
                    "after_event": sorted_events[i].event_id,
                    "flag": "INTELLIGENCE_UNKNOWN",
                })

        return gaps

    def detect_conflicts(self, time_window_minutes: float = 30.0) -> list:
        """Find events from different sources describing the same thing at conflicting times."""
        sorted_events = self._sorted_events()
        conflicts = []

        for i in range(len(sorted_events)):
            for j in range(i + 1, len(sorted_events)):
                e1 = sorted_events[i]
                e2 = sorted_events[j]

                # Only flag conflicts between different sources
                if e1.source == e2.source:
                    continue

                # Check if descriptions are similar (same event, different times)
                desc_overlap = set(e1.description.lower().split()) & set(e2.description.lower().split())
                if len(desc_overlap) < 3:
                    continue

                dt1 = datetime.fromisoformat(e1.utc_datetime)
                dt2 = datetime.fromisoformat(e2.utc_datetime)
                delta_minutes = abs((dt2 - dt1).total_seconds()) / 60

                if 0 < delta_minutes <= time_window_minutes:
                    conflict = {
                        "event_1": e1.event_id,
                        "event_2": e2.event_id,
                        "time_difference_minutes": round(delta_minutes, 2),
                        "source_1": e1.source,
                        "source_2": e2.source,
                        "description_overlap": list(desc_overlap),
                        "flag": "TEMPORAL_CONFLICT",
                    }
                    conflicts.append(conflict)
                    e1.conflicts_with.append(e2.event_id)
                    e2.conflicts_with.append(e1.event_id)

        return conflicts

    def entity_timeline(self, entity: str) -> list:
        """Extract timeline for a specific entity."""
        relevant = [
            e for e in self.events
            if entity.lower() in [ent.lower() for ent in e.entities_involved]
        ]
        return sorted(relevant, key=lambda e: e.utc_datetime)

    def category_breakdown(self) -> dict:
        """Count events by category."""
        breakdown = defaultdict(int)
        for e in self.events:
            breakdown[e.category] += 1
        return dict(breakdown)

    def analyse(self, gap_threshold_hours: float = 24.0, conflict_window_minutes: float = 30.0) -> dict:
        """Full chronological analysis."""
        sorted_events = self._sorted_events()
        gaps = self.detect_gaps(gap_threshold_hours)
        conflicts = self.detect_conflicts(conflict_window_minutes)

        # Entities involved across all events
        all_entities = set()
        for e in self.events:
            all_entities.update(e.entities_involved)

        return {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "total_events": len(self.events),
            "date_range": {
                "earliest": sorted_events[0].utc_datetime if sorted_events else None,
                "latest": sorted_events[-1].utc_datetime if sorted_events else None,
            },
            "category_breakdown": self.category_breakdown(),
            "entities_mentioned": sorted(all_entities),
            "gaps": {
                "threshold_hours": gap_threshold_hours,
                "count": len(gaps),
                "gaps": gaps,
            },
            "conflicts": {
                "window_minutes": conflict_window_minutes,
                "count": len(conflicts),
                "conflicts": conflicts,
            },
            "timeline": [asdict(e) for e in sorted_events],
        }

    def export_csv(self, filepath: str):
        """Export timeline as CSV."""
        import csv
        sorted_events = self._sorted_events()
        fieldnames = [
            "event_id", "utc_datetime", "original_datetime", "category",
            "description", "source", "source_reliability", "info_credibility",
            "location", "entities_involved", "evidence_ref", "conflicts_with", "notes",
        ]
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for e in sorted_events:
                row = asdict(e)
                row["entities_involved"] = "; ".join(row["entities_involved"])
                row["conflicts_with"] = "; ".join(row["conflicts_with"])
                writer.writerow(row)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Chronological matrix analyser")
    parser.add_argument("input", help="JSON file with events array")
    parser.add_argument("--gap-hours", type=float, default=24.0, help="Gap detection threshold")
    parser.add_argument("--conflict-minutes", type=float, default=30.0, help="Conflict detection window")
    parser.add_argument("--output", "-o", help="Output JSON file")
    parser.add_argument("--csv", help="Export CSV")
    args = parser.parse_args()

    cm = ChronologicalMatrix()
    events = json.loads(Path(args.input).read_text())
    if isinstance(events, dict):
        events = events.get("events", [])

    for evt in events:
        cm.add_event(
            datetime_str=evt.get("datetime", evt.get("timestamp", "")),
            description=evt.get("description", ""),
            source=evt.get("source", ""),
            entities=evt.get("entities", []),
            location=evt.get("location", ""),
            category=evt.get("category", "other"),
        )

    result = cm.analyse(args.gap_hours, args.conflict_minutes)
    print(f"Timeline: {result['total_events']} events, {result['gaps']['count']} gaps, {result['conflicts']['count']} conflicts")

    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2))
    if args.csv:
        cm.export_csv(args.csv)
        print(f"CSV exported to {args.csv}")


if __name__ == "__main__":
    main()
