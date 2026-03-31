#!/usr/bin/env python3
"""
claude-sleuth :: task runner

Sequential task runner for the DI Claudian investigation workflow.
Discovers task files from references/, tracks completion state,
and serves the next task with its required scripts, templates, and tools.

Usage:
    python3 task_runner.py              # Show current task
    python3 task_runner.py next         # Show current task (alias)
    python3 task_runner.py done         # Mark current done, show next
    python3 task_runner.py status       # Show progress overview
    python3 task_runner.py reset        # Reset all progress
    python3 task_runner.py jump t6.2    # Jump to a specific task
    python3 task_runner.py peek t9.1    # Preview a task without changing position
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCES = REPO_ROOT / "references"
TEMPLATES = REPO_ROOT / "templates"
PROGRESS_FILE = REPO_ROOT / ".sleuth-progress.json"

# ---------------------------------------------------------------------------
# Phase metadata
# ---------------------------------------------------------------------------
PHASES = {
    "oppstrat": {
        "number": 1,
        "title": "Operational Direction & Strategic Foundation",
        "cycle_stage": "Direction",
    },
    "intelepi": {
        "number": 2,
        "title": "Intelligence Collection & Epistemic Filtering",
        "cycle_stage": "Collection",
    },
    "colent": {
        "number": 3,
        "title": "Collation & Entity Resolution",
        "cycle_stage": "Processing",
    },
    "chronrel": {
        "number": 4,
        "title": "Chronological & Relational Processing",
        "cycle_stage": "Processing",
    },
    "hypcog": {
        "number": 5,
        "title": "Hypothesis Reasoning & Cognitive De-biasing",
        "cycle_stage": "Analysis",
    },
    "findis": {
        "number": 6,
        "title": "Final Reporting & Dissemination",
        "cycle_stage": "Dissemination",
    },
}

# ---------------------------------------------------------------------------
# Step-level resource mappings
# ---------------------------------------------------------------------------
STEP_SCRIPTS = {
    1: [],
    2: [],
    3: ["source_grader.py"],
    4: ["database_manager.py"],
    5: ["evidence_preservation.py", "content_archiver.py"],
    6: ["entity_resolver.py"],
    7: ["database_manager.py", "entity_resolver.py"],
    8: ["corporate_intel.py", "domain_intel.py", "username_enum.py", "sanctions_screen.py"],
    9: ["chronological_matrix.py"],
    10: ["network_graph.py"],
    11: ["geolocation.py", "content_archiver.py"],
    12: [],
    13: ["report_generator.py"],
    14: ["report_generator.py"],
    15: ["report_generator.py", "financial_analysis.py"],
}

STEP_TEMPLATES = {
    1: ["research/case-decision-log.md"],
    2: ["research/investigation-strategy.md"],
    3: ["research/source-grading.md"],
    4: ["database/task-log.md"],
    5: ["database/evidence-register.md"],
    6: ["analysis/pole.md"],
    7: ["database/entity-register.md"],
    8: ["research/family-network-research.md", "research/cultural-context.md"],
    9: ["analysis/chronological-matrix.md"],
    10: ["analysis/network-architecture.md"],
    11: ["analysis/verification.md", "analysis/morphological.md"],
    12: ["analysis/ach.md"],
    13: ["working/briefing.md"],
    14: ["working/case-summary.md"],
    15: ["working/findings-memo.md", "working/report.md"],
}

STEP_MCP_TOOLS = {
    1: ["web_search"],
    2: ["web_search"],
    3: ["web_search"],
    4: [],
    5: ["web_search"],
    6: [],
    7: ["Notion (database sync)"],
    8: ["web_search", "web_fetch"],
    9: [],
    10: [],
    11: ["web_search", "web_fetch"],
    12: ["Thinking Toolkit (diagnose → ACH reasoning)"],
    13: [],
    14: [],
    15: [],
}

# ---------------------------------------------------------------------------
# Task discovery and ordering
# ---------------------------------------------------------------------------
TASK_RE = re.compile(r"^t(\d+)\.(\d+)([ab]?)\.md$")


def parse_task_id(filename: str) -> tuple | None:
    """Extract (step, subtask, suffix) from a task filename."""
    m = TASK_RE.match(filename)
    if not m:
        return None
    return (int(m.group(1)), int(m.group(2)), m.group(3))


def task_sort_key(entry: dict) -> tuple:
    """Sort key: step number, subtask number, suffix (a < b < '')."""
    suffix_order = {"a": 0, "b": 1, "": 2}
    return (entry["step"], entry["subtask"], suffix_order.get(entry["suffix"], 3))


def task_display_id(entry: dict) -> str:
    """Human-readable task ID like t3.1a or t9.2."""
    return f"t{entry['step']}.{entry['subtask']}{entry['suffix']}"


def discover_tasks() -> list[dict]:
    """Walk references/ and build an ordered task list."""
    tasks = []
    for phase_folder in PHASES:
        phase_dir = REFERENCES / phase_folder
        if not phase_dir.is_dir():
            continue
        for f in phase_dir.iterdir():
            parsed = parse_task_id(f.name)
            if parsed is None:
                continue
            step, subtask, suffix = parsed
            tasks.append({
                "id": task_display_id({"step": step, "subtask": subtask, "suffix": suffix}),
                "step": step,
                "subtask": subtask,
                "suffix": suffix,
                "phase": phase_folder,
                "file": str(f.relative_to(REPO_ROOT)),
                "abs_path": str(f),
            })
    tasks.sort(key=task_sort_key)
    return tasks


# ---------------------------------------------------------------------------
# Progress state
# ---------------------------------------------------------------------------
def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": [], "current_index": 0}


def save_progress(state: dict):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------
def print_divider(char: str = "─", width: int = 72):
    print(char * width)


def print_task_card(task: dict, tasks: list, state: dict, show_content: bool = True):
    """Print a full task card with context, resources, and file content."""
    tid = task["id"]
    phase_meta = PHASES[task["phase"]]
    step = task["step"]
    idx = next(i for i, t in enumerate(tasks) if t["id"] == tid)
    total = len(tasks)

    print()
    print_divider("━")
    print(f"  TASK {tid.upper()}")
    print(f"  Phase {phase_meta['number']}: {phase_meta['title']}")
    print(f"  Intelligence Cycle: {phase_meta['cycle_stage']}")
    print(f"  Progress: {len(state['completed'])}/{total} complete")
    print_divider("━")

    # Scripts
    scripts = STEP_SCRIPTS.get(step, [])
    if scripts:
        print(f"\n  Scripts required:")
        for s in scripts:
            path = REPO_ROOT / "scripts" / s
            exists = "✓" if path.exists() else "✗"
            print(f"    {exists} scripts/{s}")

    # Templates
    templates = STEP_TEMPLATES.get(step, [])
    if templates:
        print(f"\n  Templates:")
        for t in templates:
            path = TEMPLATES / t
            exists = "✓" if path.exists() else "✗"
            print(f"    {exists} templates/{t}")

    # MCP tools
    tools = STEP_MCP_TOOLS.get(step, [])
    if tools:
        print(f"\n  MCP/Tools:")
        for t in tools:
            print(f"    → {t}")

    # File content
    if show_content:
        print()
        print_divider()
        print(f"  FILE: {task['file']}")
        print_divider()
        try:
            content = Path(task["abs_path"]).read_text().strip()
            if not content:
                print("  [EMPTY FILE - needs content]")
            else:
                print(content)
        except Exception as e:
            print(f"  [Error reading file: {e}]")

    print()
    print_divider("━")

    # Navigation hint
    if idx + 1 < total:
        next_task = tasks[idx + 1]
        print(f"  Next up: {next_task['id'].upper()} ({next_task['file']})")
    else:
        print("  This is the final task.")
    print()


def print_status(tasks: list, state: dict):
    """Print a progress overview grouped by phase."""
    total = len(tasks)
    done = set(state["completed"])
    current_idx = state["current_index"]
    current_id = tasks[current_idx]["id"] if current_idx < total else None

    print()
    print_divider("━")
    print(f"  INVESTIGATION PROGRESS: {len(done)}/{total} tasks")
    print_divider("━")

    for phase_key, phase_meta in PHASES.items():
        phase_tasks = [t for t in tasks if t["phase"] == phase_key]
        phase_done = sum(1 for t in phase_tasks if t["id"] in done)
        pct = int(100 * phase_done / len(phase_tasks)) if phase_tasks else 0

        bar_width = 20
        filled = int(bar_width * phase_done / len(phase_tasks)) if phase_tasks else 0
        bar = "█" * filled + "░" * (bar_width - filled)

        print(f"\n  Phase {phase_meta['number']}: {phase_meta['title']}")
        print(f"  {bar} {phase_done}/{len(phase_tasks)} ({pct}%)")

        for t in phase_tasks:
            tid = t["id"]
            if tid in done:
                marker = "  ✓"
            elif tid == current_id:
                marker = "  →"
            else:
                marker = "   "
            print(f"    {marker} {tid}")

    print()
    print_divider("━")

    if current_id:
        print(f"  Current position: {current_id.upper()}")
    else:
        print("  All tasks complete.")
    print()


# ---------------------------------------------------------------------------
# Verification gate
# ---------------------------------------------------------------------------
HEADER_RE = re.compile(r"^###\s+\d+\.?\s*(.+)$")
BULLET_RE = re.compile(r"^\*\s+\*\*(.+?)(?::\*\*|:\s*\*\*)\s*(.*)$")
SUB_BULLET_RE = re.compile(r"^\s+\*\s+\*\*(.+?)(?::\*\*|:\s*\*\*)\s*(.*)$")


def extract_checklist(task: dict) -> list[dict]:
    """Parse a task file into checklist sections with items.

    Returns a list of sections, each with a title and list of requirement items
    extracted from the markdown structure.
    """
    try:
        content = Path(task["abs_path"]).read_text().strip()
    except Exception:
        return []

    if not content:
        return []

    sections = []
    current_section = None

    for line in content.splitlines():
        # Match section headers: ### 1. Title
        header_match = HEADER_RE.match(line.strip())
        if header_match:
            current_section = {
                "title": header_match.group(1).strip(),
                "items": [],
            }
            sections.append(current_section)
            continue

        if current_section is None:
            continue

        # Match top-level bullet requirements: *   **Label:** Description
        bullet_match = BULLET_RE.match(line.strip())
        if bullet_match:
            label = bullet_match.group(1).strip()
            # Clean trailing markdown artifacts
            label = label.rstrip("*").strip()
            current_section["items"].append(label)
            continue

        # Match sub-bullet requirements (indented): *   **Label:** Description
        sub_match = SUB_BULLET_RE.match(line)
        if sub_match:
            label = sub_match.group(1).strip().rstrip("*").strip()
            current_section["items"].append(f"  {label}")

    return sections


def print_verification_gate(task: dict, tasks: list, state: dict):
    """Print the completed task's requirements as a verification checklist.

    This forces the operator to review every requirement before the task
    is marked complete. The checklist is extracted from the task file's
    markdown structure (headers and bold bullet items).
    """
    tid = task["id"]
    phase_meta = PHASES[task["phase"]]
    step = task["step"]

    print()
    print_divider("━")
    print(f"  VERIFICATION GATE — {tid.upper()}")
    print(f"  Phase {phase_meta['number']}: {phase_meta['title']}")
    print_divider("━")

    sections = extract_checklist(task)

    if not sections:
        # Fallback: no structured content could be extracted
        print(f"\n  No structured checklist could be extracted from {task['file']}.")
        print(f"  Review the task file manually before confirming completion.")
        print()
        print_divider()
        print(f"  FILE: {task['file']}")
        print_divider()
        try:
            content = Path(task["abs_path"]).read_text().strip()
            if content:
                # Print first 20 lines as a reminder
                for line in content.splitlines()[:20]:
                    print(f"  {line}")
                if len(content.splitlines()) > 20:
                    print(f"  ... ({len(content.splitlines()) - 20} more lines)")
            else:
                print("  [EMPTY FILE]")
        except Exception as e:
            print(f"  [Error: {e}]")
        print()
        print_divider("━")
        return

    # Print structured checklist
    item_count = 0
    for section in sections:
        print(f"\n  {section['title']}")
        if section["items"]:
            for item in section["items"]:
                if item.startswith("  "):
                    # Sub-item
                    print(f"      [ ] {item.strip()}")
                else:
                    print(f"    [ ] {item}")
                item_count += 1
        else:
            print(f"    (no specific requirements extracted)")

    # Scripts and templates for this step
    scripts = STEP_SCRIPTS.get(step, [])
    templates = STEP_TEMPLATES.get(step, [])
    tools = STEP_MCP_TOOLS.get(step, [])

    if scripts or templates or tools:
        print(f"\n  Tooling used:")
        for s in scripts:
            print(f"    [ ] scripts/{s}")
        for t in templates:
            print(f"    [ ] templates/{t}")
        for t in tools:
            print(f"    [ ] {t}")

    print()
    print_divider("━")
    print(f"  {item_count} requirements to verify.")
    print(f"  Confirm ALL items were completed before proceeding.")
    print_divider("━")
    print()


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
def cmd_next(tasks: list, state: dict):
    """Show the current task."""
    idx = state["current_index"]
    if idx >= len(tasks):
        print("\n  All tasks complete. Run `task_runner.py status` for overview.\n")
        return
    print_task_card(tasks[idx], tasks, state)


def cmd_done(tasks: list, state: dict):
    """Mark current task done and advance, printing verification gate first."""
    idx = state["current_index"]
    if idx >= len(tasks):
        print("\n  All tasks already complete.\n")
        return

    task = tasks[idx]
    tid = task["id"]

    # Print verification gate for the completed task
    print_verification_gate(task, tasks, state)

    if tid not in state["completed"]:
        state["completed"].append(tid)

    state["current_index"] = idx + 1
    save_progress(state)

    print(f"\n  ✓ Marked {tid.upper()} complete.")

    if idx + 1 < len(tasks):
        print(f"  Loading next task...\n")
        print_task_card(tasks[idx + 1], tasks, state)
    else:
        print(f"\n  All {len(tasks)} tasks complete.")
        print(f"  Run `task_runner.py status` for final overview.\n")


def cmd_jump(tasks: list, state: dict, target: str):
    """Jump to a specific task by ID."""
    target_clean = target.lower().strip()
    if not target_clean.startswith("t"):
        target_clean = "t" + target_clean

    idx = next((i for i, t in enumerate(tasks) if t["id"] == target_clean), None)
    if idx is None:
        print(f"\n  Task '{target}' not found.")
        print(f"  Available: {', '.join(t['id'] for t in tasks[:10])}...\n")
        return

    state["current_index"] = idx
    save_progress(state)
    print(f"\n  Jumped to {target_clean.upper()}.")
    print_task_card(tasks[idx], tasks, state)


def cmd_peek(tasks: list, state: dict, target: str):
    """Preview a task without changing position."""
    target_clean = target.lower().strip()
    if not target_clean.startswith("t"):
        target_clean = "t" + target_clean

    task = next((t for t in tasks if t["id"] == target_clean), None)
    if task is None:
        print(f"\n  Task '{target}' not found.\n")
        return

    print_task_card(task, tasks, state)


def cmd_reset(tasks: list, state: dict):
    """Reset all progress."""
    state["completed"] = []
    state["current_index"] = 0
    save_progress(state)
    print("\n  Progress reset. Starting from t1.1.\n")


def cmd_list(tasks: list, state: dict):
    """List all task IDs grouped by phase."""
    for phase_key, phase_meta in PHASES.items():
        phase_tasks = [t for t in tasks if t["phase"] == phase_key]
        ids = ", ".join(t["id"] for t in phase_tasks)
        print(f"  Phase {phase_meta['number']} ({phase_key}): {ids}")
    print(f"\n  Total: {len(tasks)} tasks")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="claude-sleuth task runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="next",
        choices=["next", "done", "status", "reset", "jump", "peek", "list"],
        help="Command to execute (default: next)",
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="Task ID for jump/peek commands (e.g. t6.2)",
    )
    args = parser.parse_args()

    tasks = discover_tasks()
    if not tasks:
        print("\n  No task files found in references/. Check repo structure.\n")
        sys.exit(1)

    state = load_progress()

    # Clamp current_index if tasks were removed
    if state["current_index"] > len(tasks):
        state["current_index"] = len(tasks)

    if args.command == "next":
        cmd_next(tasks, state)
    elif args.command == "done":
        cmd_done(tasks, state)
    elif args.command == "status":
        print_status(tasks, state)
    elif args.command == "reset":
        cmd_reset(tasks, state)
    elif args.command == "jump":
        if not args.target:
            print("\n  Usage: task_runner.py jump t6.2\n")
            sys.exit(1)
        cmd_jump(tasks, state, args.target)
    elif args.command == "peek":
        if not args.target:
            print("\n  Usage: task_runner.py peek t9.1\n")
            sys.exit(1)
        cmd_peek(tasks, state, args.target)
    elif args.command == "list":
        cmd_list(tasks, state)


if __name__ == "__main__":
    main()
