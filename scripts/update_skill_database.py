#!/usr/bin/env python3
"""
Skill Packager: Creates a distributable .skill file from a skill folder.

Usage:
    python scripts/update_skill_database.py <path/to/skill-folder>
    python scripts/update_skill_database.py <path/to/skill-folder> ./dist

The .skill file is a zip archive containing the complete skill folder structure,
ready for distribution and installation.

Exit codes:
    0 - Packaging successful
    1 - Validation failed (fix errors and retry)
    2 - File/path error
"""

import sys
import zipfile
import re
from pathlib import Path
from typing import Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0

    @property
    def has_warnings(self) -> bool:
        return len(self.warnings) > 0


def analyse_skill(skill_md: Path) -> ValidationResult:
    """
    Minimal skill validation for packaging purposes.

    Checks:
    - File exists and is readable
    - Has YAML frontmatter with name and description
    - Has required XML tags: <identity>, <constraints>, <methodology>
    - Has at least one <example>
    - Has <constraints_reminder>
    """
    result = ValidationResult()

    if not skill_md.exists():
        result.errors.append(f"SKILL.md not found at {skill_md}")
        return result

    content = skill_md.read_text(encoding="utf-8")

    # Check frontmatter
    if not content.startswith("---"):
        result.errors.append("Missing YAML frontmatter (must start with ---)")
    else:
        end = content.find("---", 3)
        if end == -1:
            result.errors.append("Unclosed frontmatter (missing closing ---)")
        else:
            fm = content[3:end]
            if not re.search(r"^name:", fm, re.MULTILINE):
                result.errors.append("Frontmatter missing 'name' field")
            if not re.search(r"^description:", fm, re.MULTILINE):
                result.errors.append("Frontmatter missing 'description' field")

    # Check required XML tags
    required_tags = ["identity", "constraints", "methodology"]
    for tag in required_tags:
        if f"<{tag}>" not in content:
            result.errors.append(f"Missing required <{tag}> tag")

    # Warnings
    if "<example>" not in content and "<examples>" not in content:
        result.warnings.append("No <example> or <examples> tag found")
    if "<constraints_reminder>" not in content:
        result.warnings.append("No <constraints_reminder> tag found")
    if "<output_format>" not in content:
        result.warnings.append("No <output_format> tag found")

    return result


def validate_skill_folder(skill_path: Path) -> Tuple[bool, str]:
    """
    Validate a skill folder for packaging.

    Checks:
    - SKILL.md exists and passes validation
    - Folder name matches frontmatter name
    - Directory structure is valid

    Args:
        skill_path: Path to the skill folder

    Returns:
        Tuple of (is_valid, message)
    """
    skill_md = skill_path / "SKILL.md"

    # Run content validation
    analysis = analyse_skill(skill_md)

    if analysis.has_errors:
        error_messages = [f"  - {e}" for e in analysis.errors]
        return False, "Content validation failed:\n" + "\n".join(error_messages)
    
    # Extract name from frontmatter and verify it matches folder name
    frontmatter_name = extract_frontmatter_name(skill_md)
    folder_name = skill_path.name
    
    if frontmatter_name and frontmatter_name != folder_name:
        return False, f"Name mismatch: frontmatter name '{frontmatter_name}' does not match folder name '{folder_name}'"
    
    # Check naming convention (kebab-case)
    if not re.match(r'^[a-z][a-z0-9]*(-[a-z0-9]+)*$', folder_name):
        return False, f"Invalid folder name '{folder_name}': must be kebab-case (e.g., 'my-skill-name')"
    
    # Warnings don't block packaging
    if analysis.has_warnings:
        warning_count = len(analysis.warnings)
        return True, f"Validation passed with {warning_count} warning(s)"
    
    return True, "Validation passed"


def extract_frontmatter_name(skill_md: Path) -> Optional[str]:
    """Extract the name field from SKILL.md frontmatter."""
    content = skill_md.read_text(encoding='utf-8')
    
    # Find frontmatter block
    if not content.startswith('---'):
        return None
    
    end_marker = content.find('---', 3)
    if end_marker == -1:
        return None
    
    frontmatter = content[3:end_marker]
    
    # Extract name field
    name_match = re.search(r'^name:\s*["\']?([^"\'#\n]+)', frontmatter, re.MULTILINE)
    if name_match:
        return name_match.group(1).strip()
    
    return None


def package_skill(skill_path: Path, output_dir: Optional[Path] = None, force: bool = False) -> Optional[Path]:
    """
    Package a skill folder into a .skill file.
    
    Args:
        skill_path: Path to the skill folder
        output_dir: Optional output directory (defaults to current directory)
        force: If True, package even with warnings (errors still block)
        
    Returns:
        Path to created .skill file, or None if packaging failed
    """
    skill_path = skill_path.resolve()
    
    # Validate folder exists
    if not skill_path.exists():
        print(f" Error: Skill folder not found: {skill_path}")
        return None
    
    if not skill_path.is_dir():
        print(f" Error: Path is not a directory: {skill_path}")
        return None
    
    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f" Error: SKILL.md not found in {skill_path}")
        print("   Every skill folder must contain a SKILL.md file.")
        return None
    
    # Run validation
    print(" Validating skill...")
    valid, message = validate_skill_folder(skill_path)
    
    if not valid:
        print(f" {message}")
        print("\n   Fix validation errors before packaging.")
        return None
    
    print(f" {message}\n")
    
    # Determine output location
    skill_name = skill_path.name
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()
    
    skill_filename = output_path / f"{skill_name}.skill"
    
    # Create the .skill file (zip format)
    print(f" Creating {skill_filename.name}...")
    
    try:
        with zipfile.ZipFile(skill_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            file_count = 0
            for file_path in skill_path.rglob('*'):
                if file_path.is_file():
                    # Skip common unwanted files
                    if file_path.name.startswith('.') or file_path.name == '__pycache__':
                        continue
                    if file_path.suffix in ['.pyc', '.pyo']:
                        continue
                    
                    # Calculate relative path within zip (preserves folder name)
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)
                    print(f"   Added: {arcname}")
                    file_count += 1
        
        print(f"\n Successfully packaged {file_count} files to: {skill_filename}")
        print(f"   File size: {skill_filename.stat().st_size / 1024:.1f} KB")
        return skill_filename
        
    except PermissionError as e:
        print(f" Permission denied: {e}")
        return None
    except Exception as e:
        print(f" Error creating .skill file: {e}")
        return None


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Package a skill folder into a distributable .skill file"
    )
    parser.add_argument('skill_path', help="Path to the skill folder")
    parser.add_argument('output_dir', nargs='?', default=None,
                        help="Output directory for .skill file (default: current directory)")
    parser.add_argument('-f', '--force', action='store_true',
                        help="Package even if validation has warnings (errors still block)")
    
    args = parser.parse_args()
    
    skill_path = Path(args.skill_path)
    output_dir = Path(args.output_dir) if args.output_dir else None
    
    print(f" Packaging skill: {skill_path}")
    if output_dir:
        print(f"   Output directory: {output_dir}")
    if args.force:
        print(f"   Force mode: packaging despite warnings")
    print()
    
    result = package_skill(skill_path, output_dir, force=args.force)
    
    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()