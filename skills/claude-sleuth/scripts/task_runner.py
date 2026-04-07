#!/usr/bin/env python3
"""
claude-sleuth :: task runner

Sequential task runner for the Claude Sleuth investigation workflow.
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
    python3 task_runner.py notebook     # Print the Investigation Notebook
"""

import argparse
import importlib.metadata
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Import shared configuration and module/package definitions
sys.path.insert(0, str(Path(__file__).resolve().parent))
from setup import MODULES
from config import (
    PHASES, PHASE_FOLDERS, STEP_TO_PHASE,
    STEP_TEMPLATES, STEP_SCRIPTS, STEP_MCP_TOOLS, SCRIPT_MODULES,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCES = REPO_ROOT / "references"
TEMPLATES = REPO_ROOT / "templates"
PROGRESS_FILE = REPO_ROOT / ".sleuth-progress.json"
NOTEBOOK_PATH = REPO_ROOT / "templates" / "working" / "investigation-notebook.md"

# ---------------------------------------------------------------------------
# Dependency resolution and install
# ---------------------------------------------------------------------------

def get_cumulative_modules(tasks: list, up_to_index: int) -> list[str]:
    """Return the union of all modules required from task 0 through up_to_index."""
    seen = set()
    modules = ["core"]  # always required
    for task in tasks[:up_to_index + 1]:
        step = task["step"]
        for script in STEP_SCRIPTS.get(step, []):
            for module in SCRIPT_MODULES.get(script, []):
                if module not in seen:
                    seen.add(module)
                    modules.append(module)
    return modules


def get_installed_packages() -> set[str]:
    """Return set of currently installed package names (normalised)."""
    installed = set()
    for dist in importlib.metadata.distributions():
        name = dist.metadata["Name"]
        if name:
            installed.add(name.lower().replace("-", "_"))
            installed.add(name.lower().replace("_", "-"))
    return installed


def install_for_task(tasks: list, state: dict):
    """Install any packages required for the current task that aren't yet present."""
    idx = state["current_index"]
    if idx >= len(tasks):
        return

    required_modules = get_cumulative_modules(tasks, idx)

    # Flatten to package list, deduplicated
    seen = set()
    packages = []
    for module in required_modules:
        for pkg in MODULES.get(module, {}).get("packages", []):
            key = pkg.lower().replace("-", "_")
            if key not in seen:
                seen.add(key)
                packages.append(pkg)

    installed = get_installed_packages()
    missing = [p for p in packages if p.lower().replace("-", "_") not in installed
               and p.lower().replace("_", "-") not in installed]

    if not missing:
        return

    print(f"\n  Installing {len(missing)} missing package(s) for this task...")
    print(f"  Modules: {', '.join(required_modules)}")
    print()

    passed, failed = [], []
    for pkg in missing:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", pkg, "--break-system-packages", "-q"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            passed.append(pkg)
            print(f"  \u2713 {pkg}")
        else:
            failed.append(pkg)
            note = (result.stdout + result.stderr).strip().split("\n")[-1][:80]
            print(f"  \u2717 {pkg}  \u2014  {note}")

    print(f"\n  {len(passed)} installed, {len(failed)} failed.\n")


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
    """Sort key: phase first, then step, subtask, suffix.

    Phase number MUST be primary. Without it, tasks with overlapping step
    numbers at phase boundaries (e.g. t3.1a in oppstrat and t3.1b in
    intelepi) interleave incorrectly in the execution sequence, causing
    cross-phase tasks to run consecutively when they should not.
    """
    suffix_order = {"a": 0, "b": 1, "": 2}
    phase_number = PHASES[entry["phase"]]["number"]
    return (phase_number, entry["step"], entry["subtask"], suffix_order.get(entry["suffix"], 3))


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
def print_divider(char: str = "\u2500", width: int = 72):
    print(char * width)


def print_task_card(task: dict, tasks: list, state: dict, show_content: bool = True):
    """Print a full task card with context, resources, and file content."""
    tid = task["id"]
    phase_meta = PHASES[task["phase"]]
    step = task["step"]
    idx = next(i for i, t in enumerate(tasks) if t["id"] == tid)
    total = len(tasks)

    print()
    print_divider("\u2501")
    print(f"  TASK {tid.upper()}")
    print(f"  Phase {phase_meta['number']}: {phase_meta['title']}")
    print(f"  Intelligence Cycle: {phase_meta['cycle_stage']}")
    print(f"  Progress: {len(state['completed'])}/{total} complete")
    print(f"  Notebook:  {NOTEBOOK_PATH.relative_to(REPO_ROOT)}")
    print_divider("\u2501")

    # Scripts
    scripts = STEP_SCRIPTS.get(step, [])
    if scripts:
        print(f"\n  Scripts required (MUST execute via bash before calling done):")
        for s in scripts:
            path = REPO_ROOT / "scripts" / s
            exists = "\u2713" if path.exists() else "\u2717"
            print(f"    {exists} python3 scripts/{s}")

    # Templates
    templates = STEP_TEMPLATES.get(step, [])
    if templates:
        print(f"\n  Templates:")
        for t in templates:
            path = TEMPLATES / t
            exists = "\u2713" if path.exists() else "\u2717"
            print(f"    {exists} templates/{t}")

    # MCP tools
    tools = STEP_MCP_TOOLS.get(step, [])
    if tools:
        print(f"\n  MCP/Tools:")
        for t in tools:
            print(f"    \u2192 {t}")

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
    print_divider("\u2501")

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
    print_divider("\u2501")
    print(f"  INVESTIGATION PROGRESS: {len(done)}/{total} tasks")
    print_divider("\u2501")

    for phase_key, phase_meta in PHASES.items():
        phase_tasks = [t for t in tasks if t["phase"] == phase_key]
        phase_done = sum(1 for t in phase_tasks if t["id"] in done)
        pct = int(100 * phase_done / len(phase_tasks)) if phase_tasks else 0

        bar_width = 20
        filled = int(bar_width * phase_done / len(phase_tasks)) if phase_tasks else 0
        bar = "\u2588" * filled + "\u2591" * (bar_width - filled)

        print(f"\n  Phase {phase_meta['number']}: {phase_meta['title']}")
        print(f"  {bar} {phase_done}/{len(phase_tasks)} ({pct}%)")

        for t in phase_tasks:
            tid = t["id"]
            if tid in done:
                marker = "  \u2713"
            elif tid == current_id:
                marker = "  \u2192"
            else:
                marker = "   "
            print(f"    {marker} {tid}")

    print()
    print_divider("\u2501")

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
    """Parse a task file into checklist sections with items."""
    try:
        content = Path(task["abs_path"]).read_text().strip()
    except Exception:
        return []

    if not content:
        return []

    sections = []
    current_section = None

    for line in content.splitlines():
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

        bullet_match = BULLET_RE.match(line.strip())
        if bullet_match:
            label = bullet_match.group(1).strip().rstrip("*").strip()
            current_section["items"].append(label)
            continue

        sub_match = SUB_BULLET_RE.match(line)
        if sub_match:
            label = sub_match.group(1).strip().rstrip("*").strip()
            current_section["items"].append(f"  {label}")

    return sections


def print_verification_gate(task: dict, tasks: list, state: dict):
    """Print the completed task's requirements as a verification checklist."""
    tid = task["id"]
    phase_meta = PHASES[task["phase"]]
    step = task["step"]

    print()
    print_divider("\u2501")
    print(f"  VERIFICATION GATE \u2014 {tid.upper()}")
    print(f"  Phase {phase_meta['number']}: {phase_meta['title']}")
    print_divider("\u2501")

    sections = extract_checklist(task)

    if not sections:
        print(f"\n  No structured checklist could be extracted from {task['file']}.")
        print(f"  Review the task file manually before confirming completion.")
        print()
        print_divider()
        print(f"  FILE: {task['file']}")
        print_divider()
        try:
            content = Path(task["abs_path"]).read_text().strip()
            if content:
                for line in content.splitlines()[:20]:
                    print(f"  {line}")
                if len(content.splitlines()) > 20:
                    print(f"  ... ({len(content.splitlines()) - 20} more lines)")
            else:
                print("  [EMPTY FILE]")
        except Exception as e:
            print(f"  [Error: {e}]")
        print()
        print_divider("\u2501")
        return

    item_count = 0
    for section in sections:
        print(f"\n  {section['title']}")
        if section["items"]:
            for item in section["items"]:
                if item.startswith("  "):
                    print(f"      [ ] {item.strip()}")
                else:
                    print(f"    [ ] {item}")
                item_count += 1
        else:
            print(f"    (no specific requirements extracted)")

    scripts = STEP_SCRIPTS.get(step, [])
    templates = STEP_TEMPLATES.get(step, [])
    tools = STEP_MCP_TOOLS.get(step, [])

    if scripts or templates or tools:
        print(f"\n  Tooling used:")
        for s in scripts:
            print(f"    [ ] python3 scripts/{s}  -- executed and output reviewed")
        for t in templates:
            print(f"    [ ] templates/{t}")
        for t in tools:
            print(f"    [ ] {t}")

    # Notebook checkpoint
    print(f"\n  Investigation Notebook:")
    print(f"    [ ] Update notebook with findings from this task")
    print(f"    [ ] If findings materially shift the picture, call CSDb:save_notebook")
    print(f"    Notebook path: {NOTEBOOK_PATH.relative_to(REPO_ROOT)}")

    print()
    print_divider("\u2501")
    print(f"  {item_count} requirements to verify.")
    print(f"  Confirm ALL items were completed before proceeding.")
    print_divider("\u2501")
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
    install_for_task(tasks, state)
    print_task_card(tasks[idx], tasks, state)


def cmd_done(tasks: list, state: dict):
    """Mark current task done and advance, printing verification gate first."""
    idx = state["current_index"]
    if idx >= len(tasks):
        print("\n  All tasks already complete.\n")
        return

    task = tasks[idx]
    tid = task["id"]

    print_verification_gate(task, tasks, state)

    if tid not in state["completed"]:
        state["completed"].append(tid)

    state["current_index"] = idx + 1
    save_progress(state)

    print(f"\n  \u2713 Marked {tid.upper()} complete.")

    if idx + 1 < len(tasks):
        print(f"  Loading next task...\n")
        install_for_task(tasks, state)
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
    install_for_task(tasks, state)
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


def cmd_notebook(state: dict):
    """Print the Investigation Notebook content."""
    print()
    print_divider("\u2501")
    print(f"  INVESTIGATION NOTEBOOK")
    print(f"  {NOTEBOOK_PATH.relative_to(REPO_ROOT)}")
    print_divider("\u2501")

    if not NOTEBOOK_PATH.exists():
        print(f"\n  Notebook not found at {NOTEBOOK_PATH}")
        print(f"  The notebook is created when template_builder.py first runs.")
        print(f"  Template source: templates/working/investigation-notebook.md\n")
        return

    try:
        content = NOTEBOOK_PATH.read_text().strip()
        if not content:
            print("  [NOTEBOOK IS EMPTY]")
        else:
            print(content)
    except Exception as e:
        print(f"  [Error reading notebook: {e}]")

    print()
    print_divider("\u2501")
    print(f"  Sync reminder: call CSDb:save_notebook after any material update.")
    print()


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
        choices=["next", "done", "status", "reset", "jump", "peek", "list", "notebook"],
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
    elif args.command == "notebook":
        cmd_notebook(state)


if __name__ == "__main__":
    main()
