#!/usr/bin/env python3
"""
claude-sleuth :: source & credibility grader
Admiralty 6x6 Matrix scoring system.
Grades source reliability (A-F) independently from information credibility (1-6).

Usage:
    from scripts.source_grader import SourceGrader
    sg = SourceGrader()
    grade = sg.grade(
        source_name="BBC News",
        claim="Suspect was seen at location X",
        reliability="B",
        credibility="2",
        justification="Established media, corroborated by CCTV"
    )
"""

import json
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


# Admiralty 6x6 Matrix definitions
RELIABILITY_SCALE = {
    "A": "Completely reliable -- no doubt of authenticity, trustworthiness, or competency; history of complete reliability",
    "B": "Usually reliable -- minor doubt; history of mostly valid information",
    "C": "Fairly reliable -- doubt of reliability; provided valid information in the past",
    "D": "Not usually reliable -- significant doubt; history of invalid information",
    "E": "Unreliable -- lacking in authenticity, trustworthiness, or competency; history of invalid information",
    "F": "Reliability cannot be judged -- no basis for evaluating reliability",
}

CREDIBILITY_SCALE = {
    "1": "Confirmed by other independent sources -- logical in itself, consistent with other information",
    "2": "Probably true -- not confirmed; logical in itself; consistent with other information on the subject",
    "3": "Possibly true -- not confirmed; reasonably logical in itself; agrees with some other information",
    "4": "Doubtfully true -- not confirmed; possible but not logical; no other information on the subject",
    "5": "Improbable -- not confirmed; not logical in itself; contradicted by other information",
    "6": "Truth cannot be judged -- no basis exists for evaluating the validity of the information",
}


@dataclass
class IntelligenceGrade:
    grade_id: str
    source_name: str
    claim: str
    reliability: str  # A-F
    credibility: str  # 1-6
    combined_grade: str  # e.g. "B2"
    justification: str = ""
    graded_by: str = "claude-sleuth"
    graded_utc: str = ""
    reliability_description: str = ""
    credibility_description: str = ""
    action_recommendation: str = ""
    linked_evidence: list = field(default_factory=list)
    notes: str = ""


def recommend_action(reliability: str, credibility: str) -> str:
    """Determine recommended action based on grade combination."""
    r_score = ord(reliability.upper()) - ord("A")  # 0-5
    c_score = int(credibility) - 1  # 0-5

    combined = r_score + c_score  # 0-10

    if combined <= 2:
        return "ACCEPT: High confidence. Suitable for direct use in analysis."
    elif combined <= 4:
        return "ACCEPT WITH CAUTION: Moderate confidence. Seek corroboration where possible."
    elif combined <= 6:
        return "CORROBORATION REQUIRED: Low confidence. Do not use without independent verification."
    elif combined <= 8:
        return "TREAT WITH SUSPICION: Minimal confidence. May be disinformation. Investigate source motives."
    else:
        return "REJECT UNLESS VERIFIED: Near-zero confidence. Do not incorporate without extraordinary corroboration."


class SourceGrader:
    """Admiralty 6x6 Matrix source and credibility grading system."""

    def __init__(self):
        self.grades: list[IntelligenceGrade] = []
        self._counter = 0

    def grade(
        self,
        source_name: str,
        claim: str,
        reliability: str,
        credibility: str,
        justification: str = "",
        linked_evidence: list = None,
        notes: str = "",
    ) -> IntelligenceGrade:
        """Grade a source/claim combination."""
        reliability = reliability.upper().strip()
        credibility = credibility.strip()

        if reliability not in RELIABILITY_SCALE:
            raise ValueError(f"Invalid reliability grade: {reliability}. Must be A-F.")
        if credibility not in CREDIBILITY_SCALE:
            raise ValueError(f"Invalid credibility grade: {credibility}. Must be 1-6.")

        self._counter += 1
        grade_id = f"SG-{self._counter:04d}"

        ig = IntelligenceGrade(
            grade_id=grade_id,
            source_name=source_name,
            claim=claim,
            reliability=reliability,
            credibility=credibility,
            combined_grade=f"{reliability}{credibility}",
            justification=justification,
            graded_utc=datetime.now(timezone.utc).isoformat(),
            reliability_description=RELIABILITY_SCALE[reliability],
            credibility_description=CREDIBILITY_SCALE[credibility],
            action_recommendation=recommend_action(reliability, credibility),
            linked_evidence=linked_evidence or [],
            notes=notes,
        )
        self.grades.append(ig)
        return ig

    def summary(self) -> dict:
        """Summary statistics of all grades."""
        if not self.grades:
            return {"total": 0}

        reliability_counts = {}
        credibility_counts = {}
        for g in self.grades:
            reliability_counts[g.reliability] = reliability_counts.get(g.reliability, 0) + 1
            credibility_counts[g.credibility] = credibility_counts.get(g.credibility, 0) + 1

        return {
            "total_grades": len(self.grades),
            "reliability_distribution": reliability_counts,
            "credibility_distribution": credibility_counts,
            "grades": [asdict(g) for g in self.grades],
        }

    @staticmethod
    def print_matrix():
        """Print the Admiralty 6x6 reference matrix."""
        print("\nAdmiralty 6x6 Source Grading Matrix")
        print("=" * 60)
        print("\nSource Reliability:")
        for code, desc in RELIABILITY_SCALE.items():
            print(f"  {code}: {desc}")
        print("\nInformation Credibility:")
        for code, desc in CREDIBILITY_SCALE.items():
            print(f"  {code}: {desc}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Admiralty 6x6 source grading")
    sub = parser.add_subparsers(dest="command")

    grade_p = sub.add_parser("grade", help="Grade a source")
    grade_p.add_argument("source", help="Source name")
    grade_p.add_argument("claim", help="The claim being graded")
    grade_p.add_argument("reliability", help="Reliability grade (A-F)")
    grade_p.add_argument("credibility", help="Credibility grade (1-6)")
    grade_p.add_argument("--justification", default="", help="Grading justification")

    matrix_p = sub.add_parser("matrix", help="Print reference matrix")

    args = parser.parse_args()

    if args.command == "grade":
        sg = SourceGrader()
        result = sg.grade(
            source_name=args.source,
            claim=args.claim,
            reliability=args.reliability,
            credibility=args.credibility,
            justification=args.justification,
        )
        print(json.dumps(asdict(result), indent=2))
    elif args.command == "matrix":
        SourceGrader.print_matrix()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
