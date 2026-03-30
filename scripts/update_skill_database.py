#!/usr/bin/env python3
"""
Skill Packager: Creates a distributable .skill file from a skill folder.

Usage:
    python scripts/package_skill.py <path/to/skill-folder>
    python scripts/package_skill.py <path/to/skill-folder> ./dist

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

# Import validation from sibling module
try:
    from validate_skill import analyse_skill
except ImportError:
    # Handle running from different directories
    sys.path.insert(0, str(Path(__file__).parent))
    from validate_skill import analyse_skill


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
        error_messages = [f"  - {r.rule}: {r.message}" for r in analysis.results 
                        if r.severity.value == "ERROR"]
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
        warning_count = sum(1 for r in analysis.results if r.severity.value == "WARNING")
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
        print(f"❌ Error: Skill folder not found: {skill_path}")
        return None
    
    if not skill_path.is_dir():
        print(f"❌ Error: Path is not a directory: {skill_path}")
        return None
    
    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        print("   Every skill folder must contain a SKILL.md file.")
        return None
    
    # Run validation
    print("🔍 Validating skill...")
    valid, message = validate_skill_folder(skill_path)
    
    if not valid:
        print(f"❌ {message}")
        print("\n   Fix validation errors before packaging.")
        return None
    
    print(f"✅ {message}\n")
    
    # Determine output location
    skill_name = skill_path.name
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()
    
    skill_filename = output_path / f"{skill_name}.skill"
    
    # Create the .skill file (zip format)
    print(f"📦 Creating {skill_filename.name}...")
    
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
        
        print(f"\n✅ Successfully packaged {file_count} files to: {skill_filename}")
        print(f"   File size: {skill_filename.stat().st_size / 1024:.1f} KB")
        return skill_filename
        
    except PermissionError as e:
        print(f"❌ Permission denied: {e}")
        return None
    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
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
    
    print(f"📦 Packaging skill: {skill_path}")
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
