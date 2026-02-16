#!/usr/bin/env python3
"""Detect breaking changes between two versions of generated SDK models.

Uses Python's ast module to parse model files and compare enum members,
BaseModel fields, and OpenEnumMeta usage.

Usage:
    python scripts/detect_breaking_changes.py <old_models_dir> <new_models_dir> [oas_dir]

Exit codes:
    0 = no breaking changes (safe to auto-merge)
    1 = breaking changes detected (needs manual review)
    2 = script error
"""

from __future__ import annotations

import ast
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

# Schema renames handled by prepare_specs.py — these are NOT collisions
CHAINS_SCHEMA_RENAMES = {
    "Activity": "ChainActivity",
    "Permission": "ChainPermission",
    "User": "ChainUser",
    "Workspace": "ChainWorkspace",
    "SingleError": "ChainSingleError",
}


class Severity(Enum):
    BREAKING = "breaking"
    COMPATIBLE = "compatible"


@dataclass
class Change:
    severity: Severity
    category: str
    model: str
    detail: str


@dataclass
class FieldInfo:
    name: str
    annotation: str
    has_default: bool


@dataclass
class EnumInfo:
    name: str
    members: dict[str, str]  # member_name → value
    is_open: bool  # True if uses OpenEnumMeta


@dataclass
class ModelInfo:
    name: str
    fields: dict[str, FieldInfo]


@dataclass
class ParsedModels:
    enums: dict[str, EnumInfo] = field(default_factory=dict)
    models: dict[str, ModelInfo] = field(default_factory=dict)


def _annotation_to_str(node: ast.expr | None) -> str:
    """Best-effort conversion of an AST annotation node to a readable string."""
    if node is None:
        return ""
    return ast.unparse(node)


def _is_open_enum(class_node: ast.ClassDef) -> bool:
    """Check if a class uses OpenEnumMeta metaclass."""
    for kw in class_node.keywords:
        if kw.arg == "metaclass":
            src = ast.unparse(kw.value)
            if "OpenEnumMeta" in src:
                return True
    return False


def _is_enum_class(class_node: ast.ClassDef) -> bool:
    """Check if a class inherits from Enum."""
    for base in class_node.bases:
        src = ast.unparse(base)
        if src == "Enum" or src.endswith(".Enum"):
            return True
    return False


def _is_basemodel_class(class_node: ast.ClassDef) -> bool:
    """Check if a class inherits from BaseModel."""
    for base in class_node.bases:
        src = ast.unparse(base)
        if src == "BaseModel" or src.endswith(".BaseModel"):
            return True
    return False


def _is_typeddict_class(class_node: ast.ClassDef) -> bool:
    """Check if a class inherits from TypedDict."""
    for base in class_node.bases:
        src = ast.unparse(base)
        if "TypedDict" in src:
            return True
    return False


def _extract_enum_members(class_node: ast.ClassDef) -> dict[str, str]:
    """Extract enum member name → value mappings."""
    members: dict[str, str] = {}
    for stmt in class_node.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
            target = stmt.targets[0]
            if isinstance(target, ast.Name) and target.id.isupper():
                members[target.id] = ast.unparse(stmt.value)
    return members


def _extract_fields(class_node: ast.ClassDef) -> dict[str, FieldInfo]:
    """Extract BaseModel field definitions."""
    fields: dict[str, FieldInfo] = {}
    for stmt in class_node.body:
        if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            name = stmt.target.id
            # Skip private/dunder attributes
            if name.startswith("_"):
                continue
            annotation = _annotation_to_str(stmt.annotation)
            has_default = stmt.value is not None
            fields[name] = FieldInfo(
                name=name,
                annotation=annotation,
                has_default=has_default,
            )
    return fields


def parse_models(directory: Path) -> ParsedModels:
    """Parse all .py files in a directory, extracting enum and model info."""
    result = ParsedModels()

    if not directory.is_dir():
        print(f"ERROR: {directory} is not a directory", file=sys.stderr)
        sys.exit(2)

    for py_file in sorted(directory.glob("*.py")):
        if py_file.name.startswith("_"):
            continue
        try:
            tree = ast.parse(py_file.read_text())
        except SyntaxError:
            print(f"WARNING: Could not parse {py_file}", file=sys.stderr)
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue

            # Skip TypedDicts — they're internal transport types
            if _is_typeddict_class(node):
                continue

            if _is_enum_class(node):
                members = _extract_enum_members(node)
                result.enums[node.name] = EnumInfo(
                    name=node.name,
                    members=members,
                    is_open=_is_open_enum(node),
                )
            elif _is_basemodel_class(node):
                fields = _extract_fields(node)
                result.models[node.name] = ModelInfo(
                    name=node.name,
                    fields=fields,
                )

    return result


def compare_models(old: ParsedModels, new: ParsedModels) -> list[Change]:
    """Compare old and new parsed models, producing a list of changes."""
    changes: list[Change] = []

    # --- Enum comparison ---
    for name, old_enum in old.enums.items():
        if name not in new.enums:
            changes.append(Change(
                Severity.BREAKING,
                "Enum removed",
                name,
                f"Enum `{name}` was removed entirely",
            ))
            continue

        new_enum = new.enums[name]

        # OpenEnumMeta → strict Enum
        if old_enum.is_open and not new_enum.is_open:
            changes.append(Change(
                Severity.BREAKING,
                "Forward-compatibility lost",
                name,
                f"`{name}` lost `OpenEnumMeta` — unknown values will now raise `ValueError`",
            ))

        # Removed members
        for member in old_enum.members:
            if member not in new_enum.members:
                changes.append(Change(
                    Severity.BREAKING,
                    "Enum value removed",
                    name,
                    f"`{name}.{member}` was removed (was `{old_enum.members[member]}`)",
                ))

        # New members
        for member in new_enum.members:
            if member not in old_enum.members:
                changes.append(Change(
                    Severity.COMPATIBLE,
                    "Enum value added",
                    name,
                    f"`{name}.{member}` = `{new_enum.members[member]}`",
                ))

    # New enums
    for name in new.enums:
        if name not in old.enums:
            changes.append(Change(
                Severity.COMPATIBLE,
                "Enum added",
                name,
                f"New enum `{name}` with {len(new.enums[name].members)} members",
            ))

    # --- Model comparison ---
    for name, old_model in old.models.items():
        if name not in new.models:
            changes.append(Change(
                Severity.BREAKING,
                "Model removed",
                name,
                f"Model `{name}` was removed entirely",
            ))
            continue

        new_model = new.models[name]

        # Removed fields
        for field_name in old_model.fields:
            if field_name not in new_model.fields:
                changes.append(Change(
                    Severity.BREAKING,
                    "Field removed",
                    name,
                    f"`{name}.{field_name}` was removed",
                ))

        # New fields
        for field_name, new_field in new_model.fields.items():
            if field_name not in old_model.fields:
                if new_field.has_default:
                    changes.append(Change(
                        Severity.COMPATIBLE,
                        "Optional field added",
                        name,
                        f"`{name}.{field_name}`: `{new_field.annotation}`",
                    ))
                else:
                    changes.append(Change(
                        Severity.BREAKING,
                        "Required field added",
                        name,
                        f"`{name}.{field_name}`: `{new_field.annotation}` (no default)",
                    ))

        # Type annotation changes
        for field_name in old_model.fields:
            if field_name not in new_model.fields:
                continue
            old_ann = old_model.fields[field_name].annotation
            new_ann = new_model.fields[field_name].annotation
            if old_ann != new_ann:
                changes.append(Change(
                    Severity.COMPATIBLE,
                    "Type annotation changed",
                    name,
                    f"`{name}.{field_name}`: `{old_ann}` → `{new_ann}`",
                ))

    # New models
    for name in new.models:
        if name not in old.models:
            field_count = len(new.models[name].fields)
            changes.append(Change(
                Severity.COMPATIBLE,
                "Model added",
                name,
                f"New model `{name}` with {field_count} fields",
            ))

    return changes


def detect_schema_collisions(oas_dir: Path) -> list[Change]:
    """Detect schema name collisions between OAS specs (excluding known renames)."""
    changes: list[Change] = []

    try:
        import yaml
    except ImportError:
        print("WARNING: PyYAML not available, skipping schema collision check", file=sys.stderr)
        return changes

    spec_schemas: dict[str, dict[str, set[str]]] = {}  # spec_name → {schema_name: set}

    for spec_file in sorted(oas_dir.glob("*.yaml")):
        if spec_file.name.endswith("_processed.yaml") or spec_file.name == "merged.yaml":
            continue

        try:
            with open(spec_file) as f:
                spec = yaml.safe_load(f)
        except Exception as e:
            print(f"WARNING: Could not parse {spec_file}: {e}", file=sys.stderr)
            continue

        schemas = set()
        if spec and "components" in spec and "schemas" in spec["components"]:
            schemas = set(spec["components"]["schemas"].keys())

        spec_schemas[spec_file.stem] = schemas

    # Compare each pair of specs
    spec_names = list(spec_schemas.keys())
    for i, spec_a in enumerate(spec_names):
        for spec_b in spec_names[i + 1 :]:
            collisions = spec_schemas[spec_a] & spec_schemas[spec_b]
            # Filter out known renames
            collisions -= set(CHAINS_SCHEMA_RENAMES.keys())
            for schema_name in sorted(collisions):
                changes.append(Change(
                    Severity.BREAKING,
                    "Schema name collision",
                    schema_name,
                    f"`{schema_name}` exists in both `{spec_a}` and `{spec_b}`",
                ))

    return changes


def format_report(changes: list[Change]) -> str:
    """Format changes into a markdown report for PR body."""
    breaking = [c for c in changes if c.severity == Severity.BREAKING]
    compatible = [c for c in changes if c.severity == Severity.COMPATIBLE]

    lines: list[str] = []
    lines.append("## Breaking Change Detection Report\n")

    if not breaking and not compatible:
        lines.append("No changes detected between model versions.\n")
        return "\n".join(lines)

    if breaking:
        lines.append(f"### :x: {len(breaking)} Breaking Change(s)\n")
        # Group by category
        categories: dict[str, list[Change]] = {}
        for c in breaking:
            categories.setdefault(c.category, []).append(c)
        for cat, items in categories.items():
            lines.append(f"**{cat}** ({len(items)})")
            for item in items:
                lines.append(f"- {item.detail}")
            lines.append("")
    else:
        lines.append("### :white_check_mark: No Breaking Changes\n")

    if compatible:
        lines.append("<details>")
        lines.append(f"<summary>:information_source: {len(compatible)} Compatible Change(s)</summary>\n")
        categories_c: dict[str, list[Change]] = {}
        for c in compatible:
            categories_c.setdefault(c.category, []).append(c)
        for cat, items in categories_c.items():
            lines.append(f"**{cat}** ({len(items)})")
            for item in items:
                lines.append(f"- {item.detail}")
            lines.append("")
        lines.append("</details>\n")

    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 3:
        print(
            "Usage: detect_breaking_changes.py <old_models_dir> <new_models_dir> [oas_dir]",
            file=sys.stderr,
        )
        return 2

    old_dir = Path(sys.argv[1])
    new_dir = Path(sys.argv[2])
    oas_dir = Path(sys.argv[3]) if len(sys.argv) > 3 else None

    print(f"Parsing old models from {old_dir}...")
    old = parse_models(old_dir)
    print(f"  Found {len(old.enums)} enums, {len(old.models)} models")

    print(f"Parsing new models from {new_dir}...")
    new = parse_models(new_dir)
    print(f"  Found {len(new.enums)} enums, {len(new.models)} models")

    print("Comparing models...")
    changes = compare_models(old, new)

    if oas_dir:
        print(f"Checking schema collisions in {oas_dir}...")
        changes.extend(detect_schema_collisions(oas_dir))

    report = format_report(changes)
    print("\n" + report)

    # Write report to file for CI consumption
    report_path = Path("breaking_changes_report.md")
    report_path.write_text(report)
    print(f"Report written to {report_path}")

    breaking = [c for c in changes if c.severity == Severity.BREAKING]
    if breaking:
        print(f"\n❌ {len(breaking)} breaking change(s) detected")
        return 1

    compatible = [c for c in changes if c.severity == Severity.COMPATIBLE]
    print(f"\n✅ No breaking changes ({len(compatible)} compatible change(s))")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
