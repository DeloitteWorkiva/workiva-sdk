"""Invoke datamodel-code-generator to produce Pydantic v2 models per spec.

Each API (platform, chains, wdata) gets its own model namespace under
``workiva/models/{api}/``.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def generate_models(
    spec_path: Path,
    output_dir: Path,
    api_name: str,
) -> None:
    """Run datamodel-code-generator for a single OpenAPI spec.

    Args:
        spec_path: Path to the OpenAPI YAML file.
        output_dir: Base output directory (e.g. src/workiva/models/).
        api_name: Sub-directory name (platform, chains, wdata).
    """
    target_file = output_dir / f"{api_name}.py"

    # Clean previous output
    if target_file.exists():
        target_file.unlink()

    # Ensure parent exists
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable, "-m", "datamodel_code_generator",
        "--input", str(spec_path),
        "--input-file-type", "openapi",
        "--output", str(target_file),
        "--output-model-type", "pydantic_v2.BaseModel",
        "--use-field-description",
        "--use-default",
        # Use List/Dict/Optional from typing, NOT list/dict/None — required
        # for Python 3.14 where PEP 749 defers annotations and Pydantic 2.12
        # fails to resolve `list[Foo]` in some evaluation contexts.
        "--no-use-standard-collections",
        "--no-use-union-operator",
        "--enum-field-as-literal", "all",
        "--use-default-kwarg",
        "--use-annotated",
        "--target-python-version", "3.10",
        "--collapse-root-models",
        "--reuse-model",
        "--snake-case-field",
        "--capitalise-enum-members",
        "--strict-nullable",
        "--allow-extra-fields",
        "--disable-future-imports",
    ]

    print(f"[codegen] Generating models for {api_name}: {spec_path}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] datamodel-code-generator failed for {api_name}:")
        print(result.stderr)
        sys.exit(1)

    if not target_file.exists():
        print(f"[ERROR] {api_name}: output file not created")
        return

    # Post-process generated models
    _fix_self_references(target_file)
    _fix_non_optional_none_defaults(target_file)
    _fix_override_without_default(target_file)

    line_count = len(target_file.read_text().splitlines())
    print(f"[OK] {api_name}: {target_file.name} ({line_count} lines)")


def _fix_self_references(filepath: Path) -> None:
    """Fix self-referential model fields for Python 3.14 compatibility.

    Python 3.14 (PEP 749) defers annotation evaluation, but Pydantic 2.12
    eagerly evaluates them during class construction. Self-referencing types
    like ``children: Optional[List[Section1]] = None`` fail because ``Section1``
    isn't in scope yet during its own class body.

    Fix: wrap self-references in string quotes so Pydantic defers resolution
    until model_rebuild() is called.
    """
    import re

    source = filepath.read_text()
    lines = source.splitlines()
    output_lines = []

    current_class = None
    class_re = re.compile(r"^class (\w+)\(")

    for line in lines:
        class_match = class_re.match(line)
        if class_match:
            current_class = class_match.group(1)

        # If we're inside a class and the line references the class name
        # in a type annotation, wrap it in quotes
        if current_class and ":" in line and current_class in line:
            # Only fix if it's a field annotation (has : and the class name in type position)
            stripped = line.lstrip()
            if not stripped.startswith("#") and not stripped.startswith("class "):
                # Replace Type[ClassName] patterns with Type['ClassName']
                # Be careful not to quote strings that are already quoted
                if f"[{current_class}]" in line and f"['{current_class}']" not in line:
                    line = line.replace(f"[{current_class}]", f"['{current_class}']")
                # Also handle bare ClassName in Optional[ClassName]
                if f"Optional[{current_class}]" in line and f"Optional['{current_class}']" not in line:
                    line = line.replace(f"Optional[{current_class}]", f"Optional['{current_class}']")

        output_lines.append(line)

    filepath.write_text("\n".join(output_lines))


def _fix_override_without_default(filepath: Path) -> None:
    """Fix child class fields that override a parent field but lose the default.

    datamodel-code-generator sometimes re-emits a field in a child class
    without preserving the parent's default value, which pyright flags as
    an error.  We detect this by looking for fields in subclasses that
    share a name with a field in a known parent but have no ``=`` default.

    Currently handles the known case: TextSpan.length overrides
    BaseTextElement.length which has default=1.
    """
    import re

    source = filepath.read_text()

    # Pattern: class Foo(Bar): ... field: int\n (no = default, not followed by =)
    # We fix known problematic fields. If more arise, add them here.
    known_overrides = {
        # (class_name, field_pattern, replacement)
        ("TextSpan", r"^(\s+length): int$", r"\1: int = 1"),
    }
    for class_name, pattern, replacement in known_overrides:
        # Only apply within the class body
        if f"class {class_name}(" in source:
            source = re.sub(pattern, replacement, source, flags=re.MULTILINE)

    filepath.write_text(source)


def _fix_non_optional_none_defaults(filepath: Path) -> None:
    """Fix fields declared as non-optional but defaulting to None.

    datamodel-code-generator sometimes emits ``field: str = None`` or
    ``field: Annotated[str, ...] = None`` when the spec marks a field as
    non-required.  Pyright rightly flags this: ``None`` is not assignable
    to ``str``.

    Fix: wrap the bare type in ``Optional[...]``.
    """
    import re

    source = filepath.read_text()
    # Pattern 1: field: str = None  →  field: Optional[str] = None
    source = re.sub(
        r"^(\s+\w+): (str|int|float|bool) = None$",
        r"\1: Optional[\2] = None",
        source,
        flags=re.MULTILINE,
    )
    # Pattern 2: field: Annotated[str, ...] = None  →  field: Annotated[Optional[str], ...] = None
    source = re.sub(
        r"^(\s+\w+): (Annotated\[)(str|int|float|bool)(, .+?\]) = None$",
        r"\1: \2Optional[\3]\4 = None",
        source,
        flags=re.MULTILINE,
    )
    filepath.write_text(source)


def generate_all_models(
    oas_dir: Path,
    output_dir: Path,
) -> None:
    """Generate models for all three APIs.

    Args:
        oas_dir: Directory containing platform.yaml, chains.yaml, wdata.yaml.
        output_dir: Base output directory for models.
    """
    specs = [
        ("platform", oas_dir / "platform.yaml"),
        ("chains", oas_dir / "chains.yaml"),
        ("wdata", oas_dir / "wdata.yaml"),
    ]

    for api_name, spec_path in specs:
        if not spec_path.exists():
            print(f"[WARN] Spec not found: {spec_path}, skipping {api_name}")
            continue
        generate_models(spec_path, output_dir, api_name)
