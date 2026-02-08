#!/usr/bin/env python3
"""Post-generation patches for the Workiva SDK.

This script runs AFTER `speakeasy generate` and applies idempotent patches
to files that Speakeasy regenerates on every run:

  1. __init__.py — appends custom re-exports (Workiva, OperationPoller, etc.)
  2. README.md  — removes Speakeasy scaffolding, adds real install instructions

Usage:
    python scripts/patch_sdk.py python-sdk
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SENTINEL = "# --- Custom exports (added by scripts/patch_sdk.py) ---"

CUSTOM_EXPORTS = f"""\

{SENTINEL}
from workiva._hooks.client import Workiva
from workiva._hooks.polling import OperationPoller
from workiva._hooks.exceptions import OperationFailed, OperationCancelled, OperationTimeout
"""

INSTALL_INSTRUCTIONS = """\
### PyPI

```bash
pip install workiva
```

### uv

```bash
uv add workiva
```

### Poetry

```bash
poetry add workiva
```"""

SCRIPTING_SECTION = """
## Workiva Scripting

To use this SDK from the Workiva scripting module, add it to your `requirements.txt`:

```
workiva==0.4.0
```

Then in your script:

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    # List files
    response = client.files.list_files()

    # Copy a file and wait for completion
    response = client.files.copy_file(file_id="abc", file_copy=params)
    operation = client.wait(response).result(timeout=300)
```
"""


def patch_init(sdk_dir: Path) -> None:
    """Append custom re-exports to __init__.py (idempotent)."""
    init_path = sdk_dir / "src" / "workiva" / "__init__.py"
    if not init_path.exists():
        print(f"  SKIP __init__.py — not found at {init_path}")
        return

    content = init_path.read_text()
    if SENTINEL in content:
        print("  __init__.py — custom exports already present, skipping")
        return

    init_path.write_text(content.rstrip("\n") + "\n" + CUSTOM_EXPORTS)
    print("  __init__.py — appended custom exports")


def patch_readme(sdk_dir: Path) -> None:
    """Clean up README.md for production use (idempotent)."""
    readme_path = sdk_dir / "README.md"
    if not readme_path.exists():
        print(f"  SKIP README.md — not found at {readme_path}")
        return

    content = readme_path.read_text()
    original = content

    # Remove license badge line
    content = re.sub(
        r"^\[!\[License: MIT\].*\n",
        "",
        content,
        flags=re.MULTILINE,
    )

    # Remove > [!IMPORTANT] block (multi-line, ends at blank line)
    content = re.sub(
        r"^<br /><br />\n> \[!IMPORTANT\].*?\n(?:>.*\n)*\n",
        "",
        content,
        flags=re.MULTILINE,
    )

    # Remove > [!TIP] block about running first generation action
    content = re.sub(
        r"^> \[!TIP\]\n> .*?first generation action.*?\n\n+",
        "",
        content,
        flags=re.MULTILINE,
    )

    # Replace the uv/pip/poetry install sections that contain git+<UNSET>.git
    content = re.sub(
        r"### uv\n.*?### PIP\n.*?### Poetry\n.*?```\n",
        INSTALL_INSTRUCTIONS + "\n",
        content,
        flags=re.DOTALL,
    )

    # Add Workiva Scripting section if not already present
    scripting_sentinel = "## Workiva Scripting"
    if scripting_sentinel not in content:
        content = content.rstrip("\n") + "\n" + SCRIPTING_SECTION

    if content != original:
        readme_path.write_text(content)
        print("  README.md — patched for production")
    else:
        print("  README.md — already patched, skipping")


PYPROJECT_URLS_SENTINEL = "[project.urls]"

PYPROJECT_URLS = """
[project.urls]
Homepage = "https://github.com/DeloitteWorkiva/workiva-sdk"
Documentation = "https://deloitteworkiva.github.io/workiva-sdk/"
Repository = "https://github.com/DeloitteWorkiva/workiva-sdk"
Issues = "https://github.com/DeloitteWorkiva/workiva-sdk/issues"
Changelog = "https://github.com/DeloitteWorkiva/workiva-sdk/releases"
"""


def patch_pyproject(sdk_dir: Path) -> None:
    """Add project URLs and license to pyproject.toml (idempotent)."""
    pyproject_path = sdk_dir / "pyproject.toml"
    if not pyproject_path.exists():
        print(f"  SKIP pyproject.toml — not found at {pyproject_path}")
        return

    content = pyproject_path.read_text()
    original = content

    # Add project URLs if missing (after dependencies, before [tool.poetry])
    if PYPROJECT_URLS_SENTINEL not in content:
        content = content.replace(
            "\n[tool.poetry]",
            "\n" + PYPROJECT_URLS.strip() + "\n\n[tool.poetry]",
        )

    if content != original:
        pyproject_path.write_text(content)
        print("  pyproject.toml — patched (license + URLs)")
    else:
        print("  pyproject.toml — already patched, skipping")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <sdk-dir>")
        sys.exit(1)

    sdk_dir = Path(sys.argv[1])
    if not sdk_dir.is_dir():
        print(f"Error: {sdk_dir} is not a directory")
        sys.exit(1)

    print(f"Patching SDK in {sdk_dir} ...")
    patch_init(sdk_dir)
    patch_readme(sdk_dir)
    patch_pyproject(sdk_dir)
    print("Done.")


if __name__ == "__main__":
    main()
