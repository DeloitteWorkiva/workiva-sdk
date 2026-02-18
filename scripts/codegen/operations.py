"""OAS parser → OperationSpec → group by namespace.

Parses OpenAPI 3.x specs and extracts operation metadata needed for
Jinja2 code generation. Each operation becomes an OperationSpec dataclass.
"""

from __future__ import annotations

import keyword
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import yaml

from codegen.pagination import PaginationConfig, resolve_pagination

HTTP_METHODS = {"get", "post", "put", "delete", "patch", "head", "options", "trace"}

# Map of OpenAPI type → Python type annotation
TYPE_MAP: dict[str, str] = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list[Any]",
    "object": "dict[str, Any]",
}


def _snake_case(name: str) -> str:
    """Convert camelCase/PascalCase/spaces to snake_case."""
    # Replace non-alphanumeric chars (spaces, hyphens, brackets) with underscores
    name = re.sub(r"[^a-zA-Z0-9]", "_", name)
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s2 = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s1)
    result = re.sub(r"_+", "_", s2).strip("_").lower()
    # Avoid Python keywords
    if keyword.iskeyword(result) or result in ("filter", "type", "id", "format", "next"):
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


@dataclass
class ParamSpec:
    """A single operation parameter (path, query, or header)."""

    name: str  # Original name from spec (e.g. "$maxpagesize")
    python_name: str  # Snake-case Python name (e.g. "maxpagesize")
    location: str  # "path", "query", or "header"
    required: bool
    python_type: str  # Python type annotation
    default: Optional[str] = None  # Default value as Python literal
    description: Optional[str] = None


@dataclass
class RequestBodySpec:
    """Request body metadata."""

    content_type: str  # e.g. "application/json"
    required: bool
    schema_ref: Optional[str] = None  # $ref to model
    python_type: str = "dict[str, Any]"  # fallback type


@dataclass
class BodyFieldSpec:
    """A single field extracted from a JSON request body schema.

    Used to flatten object body schemas into individual method parameters
    (Stripe/OpenAI style) instead of requiring a single ``body=Model(...)`` param.
    """

    name: str  # OAS property name (camelCase) — used as JSON dict key
    python_name: str  # snake_case Python param name
    python_type: str  # Python type annotation (e.g. "str", "FileCopyOptions")
    required: bool  # Whether field is in schema's ``required`` array
    description: str  # From OAS property description


@dataclass
class ResponseSpec:
    """Success response metadata."""

    status_code: str  # e.g. "200", "201", "202", "204"
    content_type: Optional[str] = None  # e.g. "application/json"
    schema_ref: Optional[str] = None  # $ref to model
    python_type: str = "None"  # Response model type
    is_list: bool = False  # Whether it's a list response


@dataclass
class OperationSpec:
    """Full metadata for a single API operation."""

    operation_id: str  # Original operationId
    method_name: str  # Snake-case Python method name
    http_method: str  # GET, POST, etc.
    path: str  # URL path template (e.g. /files/{fileId})
    summary: str
    description: str
    tags: list[str]
    params: list[ParamSpec]
    request_body: Optional[RequestBodySpec] = None
    success_response: Optional[ResponseSpec] = None
    error_codes: list[str] = field(default_factory=list)
    pagination: Optional[PaginationConfig] = None
    scopes: list[str] = field(default_factory=list)
    deprecated: bool = False
    body_fields: list[BodyFieldSpec] = field(default_factory=list)

    @property
    def has_flat_body(self) -> bool:
        """True when the JSON body is flattened into keyword params."""
        return len(self.body_fields) > 0

    @property
    def path_params(self) -> list[ParamSpec]:
        return [p for p in self.params if p.location == "path"]

    @property
    def query_params(self) -> list[ParamSpec]:
        return [p for p in self.params if p.location == "query"]

    @property
    def header_params(self) -> list[ParamSpec]:
        return [p for p in self.params if p.location == "header"]

    @property
    def has_body(self) -> bool:
        return self.request_body is not None

    @property
    def returns_list(self) -> bool:
        return self.success_response is not None and self.success_response.is_list

    @property
    def cursor_param_name(self) -> Optional[str]:
        """The actual spec name of the pagination cursor query param, or None."""
        if not self.pagination:
            return None
        clean = self.pagination.cursor_param  # e.g. "next", "cursor", "page"
        for p in self.params:
            if p.location == "query" and p.name.lstrip("$") == clean:
                return p.name  # Exact spec name, e.g. "$next"
        return self.pagination.cursor_param  # fallback


def _get_python_type(schema: dict[str, Any], spec: dict[str, Any]) -> str:
    """Resolve a schema to a Python type annotation."""
    if "$ref" in schema:
        ref = schema["$ref"]
        # Resolve the ref to check if it's a simple scalar type alias
        resolved = _resolve_ref(ref, spec)
        if resolved.get("type") in TYPE_MAP and "properties" not in resolved and "allOf" not in resolved:
            # Simple scalar alias (e.g. ID → string) — use the primitive type
            return TYPE_MAP[resolved["type"]]
        # Extract model name from #/components/schemas/ModelName
        parts = ref.split("/")
        return parts[-1] if parts else "Any"

    schema_type = schema.get("type", "object")
    if schema_type == "array":
        items = schema.get("items", {})
        item_type = _get_python_type(items, spec)
        return f"list[{item_type}]"

    if schema.get("format") == "binary":
        return "bytes"

    return TYPE_MAP.get(schema_type, "Any")


def _extract_param(
    param_data: dict[str, Any], spec: dict[str, Any]
) -> ParamSpec:
    """Extract a ParamSpec from an OpenAPI parameter object."""
    # Resolve $ref if present
    if "$ref" in param_data:
        param_data = _resolve_ref(param_data["$ref"], spec)

    name = param_data.get("name", "")
    schema = param_data.get("schema", {})
    if "$ref" in schema:
        schema = _resolve_ref(schema["$ref"], spec)

    # Check for enum values — use Literal[...] instead of plain str
    enum_values = schema.get("enum")
    if enum_values and schema.get("type") == "string":
        quoted = ", ".join(f'"{v}"' for v in enum_values)
        python_type = f"Literal[{quoted}]"
    else:
        python_type = _get_python_type(schema, spec)

    required = param_data.get("required", False)

    # Handle default values
    default = None
    if "default" in schema:
        raw = schema["default"]
        if isinstance(raw, str):
            default = f'"{raw}"'
        elif isinstance(raw, bool):
            default = str(raw)
        elif raw is None:
            default = "None"
        else:
            default = str(raw)

    # Clean up param name (strip $ prefix)
    clean_name = name.lstrip("$")

    # Use x-speakeasy-name-override if present in spec (legacy extension)
    override = param_data.get("x-speakeasy-name-override")
    python_name = _snake_case(override or clean_name)

    return ParamSpec(
        name=name,
        python_name=python_name,
        location=param_data.get("in", "query"),
        required=required,
        python_type=python_type if required else f"Optional[{python_type}]",
        default=default if not required else None,
        description=param_data.get("description"),
    )


def _extract_request_body(
    body_data: dict[str, Any], spec: dict[str, Any]
) -> Optional[RequestBodySpec]:
    """Extract request body metadata."""
    if not body_data:
        return None

    content = body_data.get("content", {})
    required = body_data.get("required", False)

    # Prefer application/json
    for ct in ("application/json", "application/octet-stream", "multipart/form-data"):
        if ct in content:
            schema = content[ct].get("schema", {})
            schema_ref = schema.get("$ref")
            python_type = _get_python_type(schema, spec)
            return RequestBodySpec(
                content_type=ct,
                required=required,
                schema_ref=schema_ref,
                python_type=python_type,
            )

    # Fallback: first content type
    if content:
        ct = next(iter(content))
        schema = content[ct].get("schema", {})
        return RequestBodySpec(
            content_type=ct,
            required=required,
            schema_ref=schema.get("$ref"),
            python_type=_get_python_type(schema, spec),
        )

    return None


def _extract_body_fields(
    body_spec: Optional[RequestBodySpec],
    spec: dict[str, Any],
    existing_param_names: set[str],
) -> list[BodyFieldSpec]:
    """Extract individual fields from a JSON body schema for flat param signatures.

    Returns an empty list (keeping the ``body=`` pattern) when:
    - No body, non-JSON content type, no schema_ref
    - Schema is not ``type: object`` (e.g. array bodies like JSONPatchDocument)
    - Schema has no ``properties``
    """
    if not body_spec:
        return []
    if body_spec.content_type != "application/json":
        return []
    if not body_spec.schema_ref:
        return []

    resolved = _resolve_ref(body_spec.schema_ref, spec)
    # Must have properties to flatten. Allow missing "type" (some OAS schemas
    # omit type: object but still define properties). Skip arrays/strings/etc.
    if "properties" not in resolved:
        return []
    schema_type = resolved.get("type")
    if schema_type is not None and schema_type != "object":
        return []

    required_set = set(resolved.get("required", []))
    properties = resolved["properties"]

    # Names that would collide with existing params or Python builtins
    reserved = existing_param_names | {"timeout", "self"}

    fields: list[BodyFieldSpec] = []
    for prop_name, prop_schema in properties.items():
        # Skip readOnly properties (response-only fields).
        # readOnly can be on the property itself or as a sibling of allOf.
        if prop_schema.get("readOnly", False):
            continue

        # Resolve type
        python_type = _resolve_body_field_type(prop_schema, spec)

        python_name = _snake_case(prop_name)

        # Handle name collisions with path/query/header params
        if python_name in reserved:
            python_name += "_"

        description = prop_schema.get("description", "")

        fields.append(BodyFieldSpec(
            name=prop_name,
            python_name=python_name,
            python_type=python_type,
            required=prop_name in required_set and not prop_schema.get("readOnly", False),
            description=description,
        ))

    # Sort: required first, then optional, alphabetical within each group
    fields.sort(key=lambda f: (not f.required, f.python_name))
    return fields


def _resolve_body_field_type(prop_schema: dict[str, Any], spec: dict[str, Any]) -> str:
    """Resolve a property schema to a Python type for a body field parameter."""
    # Direct $ref → model name
    if "$ref" in prop_schema:
        return _get_python_type(prop_schema, spec)

    # allOf: [{$ref: X}] → model name (common OAS pattern for nullable/readOnly wrappers)
    all_of = prop_schema.get("allOf")
    if all_of and len(all_of) >= 1 and "$ref" in all_of[0]:
        return _get_python_type(all_of[0], spec)

    # Array of items
    if prop_schema.get("type") == "array":
        items = prop_schema.get("items", {})
        item_type = _resolve_body_field_type(items, spec)
        return f"list[{item_type}]"

    # Enum → Literal[...]
    enum_values = prop_schema.get("enum")
    if enum_values and prop_schema.get("type") == "string":
        quoted = ", ".join(f'"{v}"' for v in enum_values)
        return f"Literal[{quoted}]"

    # Primitives
    return TYPE_MAP.get(prop_schema.get("type", "object"), "Any")


def _extract_success_response(
    responses: dict[str, Any], spec: dict[str, Any]
) -> Optional[ResponseSpec]:
    """Extract the primary success response."""
    for code in ("200", "201", "202", "204"):
        if code not in responses:
            continue
        resp = responses[code]
        if "$ref" in resp:
            resp = _resolve_ref(resp["$ref"], spec)

        content = resp.get("content", {})
        if not content:
            return ResponseSpec(status_code=code)

        # Prefer application/json
        if "application/json" in content:
            schema = content["application/json"].get("schema", {})
            python_type = _get_python_type(schema, spec)
            is_list = schema.get("type") == "array"
            return ResponseSpec(
                status_code=code,
                content_type="application/json",
                schema_ref=schema.get("$ref"),
                python_type=python_type,
                is_list=is_list,
            )

        return ResponseSpec(status_code=code)

    return None


def _extract_error_codes(responses: dict[str, Any]) -> list[str]:
    """Extract all error status codes from responses."""
    codes = []
    for code in sorted(responses.keys()):
        if code.startswith(("4", "5")) and code != "default":
            codes.append(code)
    return codes


def _extract_scopes(operation: dict[str, Any], spec: dict[str, Any]) -> list[str]:
    """Extract OAuth2 scopes from operation security requirements."""
    security = operation.get("security", spec.get("security", []))
    scopes: list[str] = []
    for req in security:
        for scheme_name, scheme_scopes in req.items():
            scopes.extend(scheme_scopes)
    return sorted(set(scopes))


def _get_method_name(operation_id: str, api: str) -> str:
    """Generate the Python method name from operationId.

    For chains/wdata, strip any API prefix if present.
    """
    name = operation_id
    # If operationId was prefixed (e.g. chains_listChains), strip the prefix
    for prefix in ("chains_", "wdata_"):
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    return _snake_case(name)


def parse_spec(
    spec_path: Path, api: str
) -> dict[str, list[OperationSpec]]:
    """Parse an OpenAPI spec and return operations grouped by tag (namespace).

    Args:
        spec_path: Path to the OpenAPI YAML file.
        api: API identifier ("platform", "chains", "wdata").

    Returns:
        Dict mapping tag name → list of OperationSpec.
    """
    with open(spec_path) as f:
        spec = yaml.safe_load(f)

    groups: dict[str, list[OperationSpec]] = {}

    paths = spec.get("paths", {})
    for path, path_item in paths.items():
        for method in HTTP_METHODS:
            if method not in path_item:
                continue

            operation = path_item[method]
            operation_id = operation.get("operationId", "")
            if not operation_id:
                continue

            # Extract parameters (merge path-level + operation-level)
            params = []
            for p in path_item.get("parameters", []) + operation.get("parameters", []):
                params.append(_extract_param(p, spec))

            # Detect pagination
            has_next = any(
                p.name in ("$next", "next") and p.location == "query"
                for p in params
            )
            has_cursor = any(
                p.name == "cursor" and p.location == "query"
                for p in params
            )
            pagination = resolve_pagination(
                operation_id, api, has_next_param=has_next, has_cursor_param=has_cursor
            )

            # Extract request body
            request_body = _extract_request_body(
                operation.get("requestBody", {}), spec
            )

            # Extract flat body fields (Stripe/OpenAI style)
            existing_param_names = {p.python_name for p in params}
            body_fields = _extract_body_fields(request_body, spec, existing_param_names)

            # Extract responses
            responses = operation.get("responses", {})
            success_response = _extract_success_response(responses, spec)
            error_codes = _extract_error_codes(responses)

            # Extract scopes
            scopes = _extract_scopes(operation, spec)

            # Determine tag (namespace)
            # Chains and Wdata merge all OAS tags into a single flat namespace
            # (e.g. "Table Management", "Query Management" → "wdata").
            # Platform keeps one namespace per tag.
            _MERGE_TAGS = {"chains", "wdata"}
            tags = operation.get("tags", [api])
            if api in _MERGE_TAGS:
                tag = api
            else:
                tag = _snake_case(tags[0]) if tags else api

            method_name = _get_method_name(operation_id, api)

            op_spec = OperationSpec(
                operation_id=operation_id,
                method_name=method_name,
                http_method=method.upper(),
                path=path,
                summary=operation.get("summary", ""),
                description=operation.get("description", ""),
                tags=tags,
                params=params,
                request_body=request_body,
                success_response=success_response,
                error_codes=error_codes,
                pagination=pagination,
                scopes=scopes,
                deprecated=operation.get("deprecated", False),
                body_fields=body_fields,
            )

            groups.setdefault(tag, []).append(op_spec)

    return groups
