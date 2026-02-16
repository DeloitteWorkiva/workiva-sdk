#!/usr/bin/env python3
"""Master SDK code generation orchestrator.

1. datamodel-code-generator for Pydantic v2 models (per spec)
2. Custom Jinja2 codegen for operation namespaces (sync + async)

Usage:
    python scripts/generate_sdk.py
    python scripts/generate_sdk.py --models-only
    python scripts/generate_sdk.py --operations-only
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

# Add scripts/ to path so codegen package is importable
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

from codegen.models import generate_all_models
from codegen.operations import parse_spec, _snake_case

# Try to import jinja2 and formatting tools
try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("[ERROR] jinja2 not installed. Run: uv pip install jinja2")
    sys.exit(1)

# Paths
ROOT = SCRIPTS_DIR.parent
OAS_DIR = ROOT / "oas"
SDK_SRC = ROOT / "workiva-sdk" / "src" / "workiva"
MODELS_DIR = SDK_SRC / "models"
OPERATIONS_DIR = SDK_SRC / "_operations"
TEMPLATES_DIR = SCRIPTS_DIR / "codegen" / "templates"

# API → (spec filename, group overrides)
API_SPECS = {
    "platform": "platform.yaml",
    "chains": "chains.yaml",
    "wdata": "wdata.yaml",
}

# Primitive types that don't need model imports
_BUILTIN_TYPES = {"str", "int", "float", "bool", "bytes", "Any", "None", "dict", "list"}


def _collect_model_types(type_str: str, out: set[str]) -> None:
    """Extract model type names from a type annotation string.

    Skips builtins like str, int, dict[str, Any], list[...], etc.
    Handles nested types like list[ModelName].
    """
    # Strip list[...] wrapper
    import re
    inner = re.sub(r"^list\[(.+)\]$", r"\1", type_str)
    # Strip dict[...] wrapper
    inner = re.sub(r"^dict\[.+\]$", "", inner)
    # Strip Optional[...] wrapper
    inner = re.sub(r"^Optional\[(.+)\]$", r"\1", inner)
    inner = inner.strip()
    if inner and inner not in _BUILTIN_TYPES and inner.isidentifier():
        out.add(inner)


def _validate_python(source: str, filename: str) -> bool:
    """Validate that generated Python is syntactically correct."""
    try:
        ast.parse(source)
        return True
    except SyntaxError as e:
        print(f"[ERROR] Syntax error in {filename}: {e}")
        return False


def _format_source(source: str) -> str:
    """Format Python source with black + isort if available."""
    try:
        import black

        source = black.format_str(source, mode=black.Mode(
            target_versions={black.TargetVersion.PY310},
            line_length=100,
        ))
    except ImportError:
        pass

    try:
        import isort

        source = isort.code(source, profile="black", line_length=100)
    except ImportError:
        pass

    return source


def generate_operations(
    env: Environment,
) -> int:
    """Parse all specs and generate namespace files.

    Returns:
        Total number of operations generated.
    """
    total_ops = 0
    OPERATIONS_DIR.mkdir(parents=True, exist_ok=True)

    # Ensure __init__.py exists
    init_path = OPERATIONS_DIR / "__init__.py"
    if not init_path.exists():
        init_path.write_text("")

    # Write _base.py (always overwrite — it's generated)
    base_template = '''"""Base namespace class for generated operation modules."""

from __future__ import annotations

from typing import TYPE_CHECKING

from workiva._constants import _API

if TYPE_CHECKING:
    from workiva._client import BaseClient


class BaseNamespace:
    """Base class for API namespace groups (Files, Chains, Wdata, etc.)."""

    _api: _API = _API.PLATFORM

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
'''
    (OPERATIONS_DIR / "_base.py").write_text(base_template)

    namespace_template = env.get_template("namespace.py.j2")

    for api, spec_filename in API_SPECS.items():
        spec_path = OAS_DIR / spec_filename
        if not spec_path.exists():
            print(f"[WARN] Spec not found: {spec_path}, skipping {api}")
            continue

        print(f"\n[codegen] Parsing {api}: {spec_path}")
        groups = parse_spec(spec_path, api)

        for tag, operations in groups.items():
            # Convert snake_case tag to PascalCase class name
            class_name = "".join(
                word.capitalize() for word in tag.split("_")
            )
            description = f"{class_name} operations."

            # Collect model types used as body parameters
            model_types: set[str] = set()
            for op in operations:
                if op.request_body and op.request_body.python_type:
                    _collect_model_types(op.request_body.python_type, model_types)

            # Render template
            source = namespace_template.render(
                api=api,
                namespace_name=tag,
                class_name=class_name,
                description=description,
                operations=operations,
                model_imports=sorted(model_types),
            )

            # Validate syntax
            if not _validate_python(source, f"{tag}.py"):
                print(f"[ERROR] Skipping {tag}.py due to syntax errors")
                continue

            # Format
            source = _format_source(source)

            # Write
            output_path = OPERATIONS_DIR / f"{tag}.py"
            output_path.write_text(source)
            print(f"  [OK] {tag}.py: {len(operations)} operations ({class_name})")
            total_ops += len(operations)

    return total_ops


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate Workiva SDK")
    parser.add_argument("--models-only", action="store_true", help="Only generate models")
    parser.add_argument("--operations-only", action="store_true", help="Only generate operations")
    args = parser.parse_args()

    do_models = not args.operations_only
    do_operations = not args.models_only

    print("=" * 60)
    print("Workiva SDK Code Generator")
    print("=" * 60)

    if do_models:
        print("\n--- Phase 1: Generate Models ---")
        generate_all_models(OAS_DIR, MODELS_DIR)

    if do_operations:
        print("\n--- Phase 2: Generate Operations ---")
        env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )
        total = generate_operations(env)
        print(f"\n[DONE] Total operations generated: {total}")

    print("\n" + "=" * 60)
    print("Generation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
