"""Invoke datamodel-code-generator to produce Pydantic v2 models per spec.

Each API (platform, chains, wdata) gets its own model namespace under
``workiva/models/{api}/``.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable

import yaml


# ---------------------------------------------------------------------------
# Rename map for platform.py collision classes
# ---------------------------------------------------------------------------
# datamodel-code-generator appends numeric suffixes when multiple schemas
# share a name.  This map restores meaningful names.
_PLATFORM_RENAMES: dict[str, str] = {
    "Section1": "Section",
    "Section": "SectionHyperlink",
    "Slide1": "Slide",
    "Slide": "SlideHyperlink",
    "Sheet1": "Sheet",
    "Sheet": "SheetHyperlink",
    "WorkspaceMembership1": "WorkspaceMembership",
    "WorkspaceMembership": "WorkspaceMembershipRef",
    "Dimensions2": "DimensionsCompact",
}

# Numeric-suffix classes that are acceptable as-is (too generic to rename).
_KNOWN_SUFFIXED: set[str] = {"Datum1", "Links1", "PageNumber1"}


# ---------------------------------------------------------------------------
# Pre-processing: fix type+$ref coexistence in OAS specs
# ---------------------------------------------------------------------------
def _preprocess_spec(spec_path: Path) -> Path:
    """Fix ``type`` + ``$ref`` coexistence and return a cleaned temp file.

    Some OAS specs (e.g. chains.yaml) place ``type: object`` alongside a
    ``$ref`` at the same schema level — an invalid pattern that causes
    datamodel-code-generator to create empty wrapper classes (``Data1``,
    ``Data2``, …).  Stripping ``type`` (and ``properties``) when ``$ref``
    is present lets the generator use the referenced schema directly.

    The original spec file is never modified.
    """
    spec = yaml.safe_load(spec_path.read_text())

    def _strip_type_alongside_ref(node: object) -> None:
        if isinstance(node, dict):
            if "$ref" in node and "type" in node:
                node.pop("type", None)
                node.pop("properties", None)
            for v in node.values():
                _strip_type_alongside_ref(v)
        elif isinstance(node, list):
            for item in node:
                _strip_type_alongside_ref(item)

    _strip_type_alongside_ref(spec)

    fd, tmp_path = tempfile.mkstemp(suffix=spec_path.suffix)
    os.close(fd)
    tmp = Path(tmp_path)
    tmp.write_text(yaml.dump(spec, default_flow_style=False, sort_keys=False))
    return tmp


# ---------------------------------------------------------------------------
# Post-processing: rename collision classes in platform.py
# ---------------------------------------------------------------------------
def _rename_collision_classes(source: str) -> str:
    """Two-phase placeholder swap to handle bidirectional renames safely."""
    # Phase 1: old names → unique placeholders (longest-first to avoid partial matches)
    placeholders = {old: f"__RENAME_{i}__" for i, old in enumerate(_PLATFORM_RENAMES)}
    pattern = re.compile(
        r"\b("
        + "|".join(re.escape(k) for k in sorted(placeholders, key=len, reverse=True))
        + r")\b"
    )
    result = pattern.sub(lambda m: placeholders[m.group(0)], source)

    # Phase 2: placeholders → final names
    for old, placeholder in placeholders.items():
        result = result.replace(placeholder, _PLATFORM_RENAMES[old])
    return result


# ---------------------------------------------------------------------------
# Guardrail: detect unexpected numeric-suffix classes
# ---------------------------------------------------------------------------
def _check_numeric_suffixes(filepath: Path, known: set[str]) -> None:
    """Fail if unexpected numeric-suffix classes appear after generation."""
    source = filepath.read_text()
    found = set(re.findall(r"^class (\w+\d+)\(", source, re.MULTILINE))
    unexpected = found - known
    if unexpected:
        raise RuntimeError(
            f"New collision classes detected in {filepath.name}: "
            f"{sorted(unexpected)}.  "
            f"Add them to _PLATFORM_RENAMES or _KNOWN_SUFFIXED in models.py."
        )


def generate_models(
    spec_path: Path,
    output_dir: Path,
    api_name: str,
    *,
    post_processors: list[Callable[[str], str]] | None = None,
    known_suffixed: set[str] | None = None,
) -> None:
    """Run datamodel-code-generator for a single OpenAPI spec.

    Args:
        spec_path: Path to the OpenAPI YAML file.
        output_dir: Base output directory (e.g. src/workiva/models/).
        api_name: Sub-directory name (platform, chains, wdata).
        post_processors: Optional callables ``(str) -> str`` applied to the
            generated source before the standard fixups.
        known_suffixed: Set of numeric-suffix class names to allow.  If
            *None*, the guardrail is skipped.
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

    # Apply custom post-processors (e.g. rename collision classes)
    if post_processors:
        source = target_file.read_text()
        for processor in post_processors:
            source = processor(source)
        target_file.write_text(source)

    # Standard post-processing fixups
    _fix_self_references(target_file)
    _fix_non_optional_none_defaults(target_file)
    _fix_override_without_default(target_file)

    # Guardrail: detect unexpected numeric-suffix classes
    if known_suffixed is not None:
        _check_numeric_suffixes(target_file, known_suffixed)

    line_count = len(target_file.read_text().splitlines())
    print(f"[OK] {api_name}: {target_file.name} ({line_count} lines)")


def _fix_self_references(filepath: Path) -> None:
    """Fix self-referential model fields for Python 3.14 compatibility.

    Python 3.14 (PEP 749) defers annotation evaluation, but Pydantic 2.12
    eagerly evaluates them during class construction. Self-referencing types
    like ``children: Optional[List[Section]] = None`` fail because ``Section``
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

        effective_spec = spec_path
        post_processors: list[Callable[[str], str]] | None = None
        known: set[str] | None = set()  # guardrail on by default

        if api_name == "chains":
            # Pre-process: strip type+$ref coexistence that creates Data* wrappers
            effective_spec = _preprocess_spec(spec_path)
            print(f"[codegen] Pre-processed {spec_path.name} → {effective_spec}")

        if api_name == "platform":
            post_processors = [_rename_collision_classes]
            known = _KNOWN_SUFFIXED | set(_PLATFORM_RENAMES.values())

        try:
            generate_models(
                effective_spec,
                output_dir,
                api_name,
                post_processors=post_processors,
                known_suffixed=known,
            )
        finally:
            # Clean up temp file if we created one
            if effective_spec != spec_path and effective_spec.exists():
                effective_spec.unlink()
