#!/usr/bin/env python3
"""
claude-sleuth :: template builder

Assembles relevant templates into a single working document based on
phase, step, task, or explicit template names. Designed to chain with
task_runner.py so that advancing a task auto-stages the workspace.

Usage:
    python3 template_builder.py --phase 3          # All Phase 3 templates
    python3 template_builder.py --step 9            # Templates for Step 9
    python3 template_builder.py --task t6.2         # Templates for step 6
    python3 template_builder.py --templates pole.md,entity-register.md
    python3 template_builder.py --step 9 --output workspace.md
    python3 template_builder.py --step 9 --include-reference  # Also include phase reference doc
    python3 template_builder.py --list               # List all available templates
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Import shared configuration
sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import PHASE_FOLDERS, STEP_TO_PHASE, STEP_TEMPLATES

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCES = REPO_ROOT / "references"
TEMPLATES = REPO_ROOT / "templates"
REF_INDEX = REFERENCES / "reference-index.json"
TPL_INDEX = TEMPLATES / "template-index.json"


# ---------------------------------------------------------------------------
# Index loading
# ---------------------------------------------------------------------------
def load_json(path: Path) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        print(f"  Warning: could not load {path}: {e}", file=sys.stderr)
        return {}


def load_template_metadata() -> dict[str, dict]:
    """Build a flat lookup: filename → metadata from template-index.json."""
    tpl_index = load_json(TPL_INDEX)
    flat = {}
    for category, info in tpl_index.items():
        for tpl in info.get("templates", []):
            key = f"{category}/{tpl['file']}"
            flat[key] = {
                "title": tpl.get("title", tpl["file"]),
                "purpose": tpl.get("purpose", ""),
                "frameworks": tpl.get("frameworks", []),
                "category": category,
            }
    return flat


# ---------------------------------------------------------------------------
# Template resolution
# ---------------------------------------------------------------------------
def resolve_by_phase(phase_num: int) -> list[str]:
    """Get all template paths for a given phase."""
    ref_index = load_json(REF_INDEX)
    phases = ref_index.get("pipeline", {}).get("phases", [])
    for p in phases:
        if p["phase"] == phase_num:
            return p.get("templates_used", [])
    return []


def resolve_by_step(step_num: int) -> list[str]:
    """Get template paths for a specific step."""
    return STEP_TEMPLATES.get(step_num, [])


def resolve_by_task(task_id: str) -> list[str]:
    """Extract step number from task ID and resolve templates."""
    m = re.match(r"t?(\d+)\.\d+[ab]?", task_id.lower())
    if not m:
        return []
    step = int(m.group(1))
    return resolve_by_step(step)


def resolve_by_names(names: list[str]) -> list[str]:
    """Resolve bare filenames to category/filename paths."""
    results = []
    for name in names:
        name = name.strip()
        if "/" in name:
            results.append(name)
            continue
        # Search template dirs
        for category_dir in TEMPLATES.iterdir():
            if not category_dir.is_dir():
                continue
            candidate = category_dir / name
            if candidate.exists():
                results.append(f"{category_dir.name}/{name}")
                break
        else:
            print(f"  Warning: template '{name}' not found", file=sys.stderr)
    return results


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------
def assemble_document(
    template_paths: list[str],
    metadata: dict[str, dict],
    include_reference: bool = False,
    phase_num: int | None = None,
    step_num: int | None = None,
) -> str:
    """Build a single markdown document from multiple templates."""
    sections = []
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Header
    context_parts = []
    if phase_num:
        context_parts.append(f"Phase {phase_num}")
    if step_num:
        context_parts.append(f"Step {step_num}")
    context_label = " / ".join(context_parts) if context_parts else "Custom selection"

    header = f"""# Assembled Workspace
> Generated: {timestamp}
> Context: {context_label}
> Templates: {len(template_paths)}
"""
    sections.append(header)

    # Optionally include the phase reference document
    if include_reference and phase_num:
        folder = PHASE_FOLDERS.get(phase_num)
        if folder:
            ref_index = load_json(REF_INDEX)
            phases = ref_index.get("pipeline", {}).get("phases", [])
            for p in phases:
                if p["phase"] == phase_num:
                    ref_file = REFERENCES / folder / p.get("file", "")
                    if ref_file.exists():
                        content = ref_file.read_text().strip()
                        sections.append(f"---\n\n## Phase Reference: {p.get('title', folder)}\n\n{content}")
                    break

    # Assemble each template
    for tpl_path in template_paths:
        full_path = TEMPLATES / tpl_path
        meta = metadata.get(tpl_path, {})
        title = meta.get("title", tpl_path)
        purpose = meta.get("purpose", "")
        frameworks = meta.get("frameworks", [])

        sections.append(f"---\n")
        sections.append(f"## {title}")
        sections.append(f"> Source: `templates/{tpl_path}`")

        if purpose:
            sections.append(f"> Purpose: {purpose}")
        if frameworks:
            sections.append(f"> Frameworks: {', '.join(frameworks)}")

        sections.append("")

        if full_path.exists():
            content = full_path.read_text().strip()
            if content:
                sections.append(content)
            else:
                sections.append("*[Template file is empty]*")
        else:
            sections.append(f"*[Template file not found: {full_path}]*")

    return "\n\n".join(sections)


# ---------------------------------------------------------------------------
# List command
# ---------------------------------------------------------------------------
def cmd_list():
    """List all available templates with metadata."""
    metadata = load_template_metadata()
    print()
    for category_dir in sorted(TEMPLATES.iterdir()):
        if not category_dir.is_dir():
            continue
        cat = category_dir.name
        print(f"  {cat}/")
        for f in sorted(category_dir.iterdir()):
            if not f.suffix == ".md":
                continue
            key = f"{cat}/{f.name}"
            meta = metadata.get(key, {})
            title = meta.get("title", f.name)
            print(f"    {f.name:<32} {title}")
        print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="claude-sleuth template builder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--phase", type=int, help="Assemble all templates for a phase (1-6)")
    group.add_argument("--step", type=int, help="Assemble templates for a step (1-15)")
    group.add_argument("--task", type=str, help="Assemble templates for a task ID (e.g. t6.2)")
    group.add_argument("--templates", type=str, help="Comma-separated template filenames")
    group.add_argument("--list", action="store_true", help="List all available templates")

    parser.add_argument("--output", "-o", type=str, default=None, help="Output file path (default: stdout)")
    parser.add_argument(
        "--include-reference", action="store_true",
        help="Include the phase reference document in output",
    )

    args = parser.parse_args()

    if args.list:
        cmd_list()
        return

    if not any([args.phase, args.step, args.task, args.templates]):
        parser.print_help()
        return

    # Resolve template paths
    phase_num = None
    step_num = None

    if args.phase:
        phase_num = args.phase
        template_paths = resolve_by_phase(args.phase)
    elif args.step:
        step_num = args.step
        phase_num = STEP_TO_PHASE.get(args.step)
        template_paths = resolve_by_step(args.step)
    elif args.task:
        template_paths = resolve_by_task(args.task)
        m = re.match(r"t?(\d+)\.\d+", args.task.lower())
        if m:
            step_num = int(m.group(1))
            phase_num = STEP_TO_PHASE.get(step_num)
    elif args.templates:
        names = [n.strip() for n in args.templates.split(",")]
        template_paths = resolve_by_names(names)

    if not template_paths:
        print("  No templates found for the given query.", file=sys.stderr)
        sys.exit(1)

    # Load metadata and assemble
    metadata = load_template_metadata()
    document = assemble_document(
        template_paths,
        metadata,
        include_reference=args.include_reference,
        phase_num=phase_num,
        step_num=step_num,
    )

    # Output
    if args.output:
        out_path = Path(args.output)
        out_path.write_text(document)
        print(f"  Assembled {len(template_paths)} templates → {out_path}")
    else:
        print(document)


if __name__ == "__main__":
    main()
