#!/usr/bin/env python3
"""Bump the SDK patch version across all version files atomically.

Reads current version from pyproject.toml, increments the patch number,
validates all files contain the expected old version, then writes all at once.

Usage:
    python scripts/bump_version.py

Prints the new version to stdout on success.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# All paths relative to repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILES = {
    "pyproject": REPO_ROOT / "pyproject.toml",
    "version_py": REPO_ROOT / "src" / "workiva" / "_version.py",
    "readme": REPO_ROOT / "README.md",
}


def read_current_version() -> str:
    """Read current version from pyproject.toml."""
    content = VERSION_FILES["pyproject"].read_text()
    match = re.search(r'^version\s*=\s*"(\d+\.\d+\.\d+)"', content, re.MULTILINE)
    if not match:
        print("ERROR: Could not find version in pyproject.toml", file=sys.stderr)
        sys.exit(2)
    return match.group(1)


def bump_patch(version: str) -> str:
    """Increment the patch component of a semver string."""
    major, minor, patch = version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


def prepare_replacements(
    old: str, new: str
) -> dict[str, tuple[str, str, str]]:
    """Prepare (content, old_pattern, new_pattern) for each file.

    Returns a dict of file_key → (original_content, search, replacement).
    Validates that each search pattern exists exactly once.
    """
    replacements: dict[str, tuple[str, str, str]] = {}

    # pyproject.toml: version = "X.Y.Z"
    content = VERSION_FILES["pyproject"].read_text()
    search = f'version = "{old}"'
    replacement = f'version = "{new}"'
    if content.count(search) != 1:
        print(f"ERROR: Expected exactly 1 occurrence of '{search}' in pyproject.toml, "
              f"found {content.count(search)}", file=sys.stderr)
        sys.exit(2)
    replacements["pyproject"] = (content, search, replacement)

    # _version.py: __version__ (user_agent uses f-string, updates automatically)
    content = VERSION_FILES["version_py"].read_text()
    search = f'__version__: str = "{old}"'
    replacement = f'__version__: str = "{new}"'
    if search not in content:
        print(f"ERROR: '{search}' not found in _version.py", file=sys.stderr)
        sys.exit(2)
    replacements["version_py"] = (content, search, replacement)

    # README.md: badge cache-buster ?v=X.Y.Z
    content = VERSION_FILES["readme"].read_text()
    search = f"?v={old}"
    replacement = f"?v={new}"
    if search not in content:
        print(f"ERROR: '{search}' not found in README.md", file=sys.stderr)
        sys.exit(2)
    replacements["readme"] = (content, search, replacement)

    return replacements


def main() -> int:
    old_version = read_current_version()
    new_version = bump_patch(old_version)

    # Validate all files before writing any
    replacements = prepare_replacements(old_version, new_version)

    # Write all files
    for key, (content, search, replacement) in replacements.items():
        path = VERSION_FILES[key]
        path.write_text(content.replace(search, replacement))

    print(new_version)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
