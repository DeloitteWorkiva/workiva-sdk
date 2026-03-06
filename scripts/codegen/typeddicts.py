"""Generate TypedDict classes from OpenAPI schemas for input parameters.

Produces TypedDict versions of Pydantic models used as method input params,
so users can pass plain dicts with IDE autocompletion.
"""

from __future__ import annotations

import keyword
import re
from typing import Any


# Map of OpenAPI type -> Python type annotation
_TYPE_MAP: dict[str, str] = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list[Any]",
    "object": "dict[str, Any]",
}


def _snake_case(name: str) -> str:
    """Convert camelCase to snake_case."""
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s2 = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s1)
    result = s2.lower()
    if keyword.iskeyword(result) or result in ("type", "id", "format", "next", "filter"):
        result += "_"
    return result


def _resolve_ref(ref: str, spec: dict[str, Any]) -> dict[str, Any]:
    """Resolve a $ref pointer within the spec."""
    if not ref.startswith("#/"):
        return {}
    parts = ref[2:].split("/")
    node = spec
    for part in parts:
        node = node.get(part, {})
    return node


def _get_field_type(prop_schema: dict[str, Any], spec: dict[str, Any]) -> str:
    """Resolve an OAS property schema to a Python type string for TypedDict."""
    # Enum -> Literal[...]
    enum_values = prop_schema.get("enum")
    if enum_values and prop_schema.get("type") == "string":
        quoted = ", ".join(f"'{v}'" for v in enum_values)
        return f"Literal[{quoted}]"

    # $ref -> resolve and recurse
    if "$ref" in prop_schema:
        resolved = _resolve_ref(prop_schema["$ref"], spec)
        return _get_field_type(resolved, spec)

    # allOf with single $ref
    all_of = prop_schema.get("allOf")
    if all_of and len(all_of) >= 1 and "$ref" in all_of[0]:
        resolved = _resolve_ref(all_of[0]["$ref"], spec)
        return _get_field_type(resolved, spec)

    schema_type = prop_schema.get("type", "object")

    # Array
    if schema_type == "array":
        items = prop_schema.get("items", {})
        item_type = _get_field_type(items, spec)
        return f"list[{item_type}]"

    # Binary
    if prop_schema.get("format") == "binary":
        return "bytes"

    return _TYPE_MAP.get(schema_type, "Any")


def generate_typeddict_source(
    model_name: str,
    schema: dict[str, Any],
    spec: dict[str, Any],
) -> str:
    """Generate a TypedDict class source string from an OAS object schema."""
    td_name = f"{model_name}Param"
    properties = schema.get("properties", {})
    required_set = set(schema.get("required", []))

    lines: list[str] = []
    lines.append(f"class {td_name}(TypedDict, total=False):")

    if not properties:
        lines.append("    pass")
        return "\n".join(lines)

    for prop_name, prop_schema in sorted(properties.items()):
        if prop_schema.get("readOnly", False):
            continue

        python_name = _snake_case(prop_name)
        python_type = _get_field_type(prop_schema, spec)

        if prop_name in required_set:
            lines.append(f"    {python_name}: Required[{python_type}]")
        else:
            lines.append(f"    {python_name}: {python_type}")

    return "\n".join(lines)


def generate_typeddicts_for_api(
    spec: dict[str, Any],
    input_model_names: set[str],
) -> dict[str, str]:
    """Generate TypedDict source for all input models in a spec."""
    schemas = spec.get("components", {}).get("schemas", {})
    results: dict[str, str] = {}

    for model_name in sorted(input_model_names):
        if model_name not in schemas:
            continue
        schema = schemas[model_name]
        if schema.get("type", "object") != "object" or "properties" not in schema:
            continue
        results[model_name] = generate_typeddict_source(model_name, schema, spec)

    return results
