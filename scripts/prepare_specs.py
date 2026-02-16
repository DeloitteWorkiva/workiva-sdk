#!/usr/bin/env python3
"""Pre-process OpenAPI specs for merging into a single Speakeasy SDK.

Handles:
- Schema renaming to avoid conflicts between chains.yaml and platform.yaml
- OperationId prefixing to avoid duplicates across specs
- x-speakeasy-name-override to keep clean SDK method names
- Path-level server injection so each API hits its correct base URL
- x-speakeasy-group extension for SDK namespace organization
"""

import yaml
import sys
from pathlib import Path

CHAINS_SCHEMA_RENAMES = {
    "Activity": "ChainActivity",
    "Permission": "ChainPermission",
    "User": "ChainUser",
    "Workspace": "ChainWorkspace",
    "SingleError": "ChainSingleError",
}

CHAINS_SERVERS = [
    {"url": "https://h.eu.wdesk.com/s/wdata/oc/api", "description": "EU"},
    {"url": "https://h.app.wdesk.com/s/wdata/oc/api", "description": "US"},
    {"url": "https://h.apac.wdesk.com/s/wdata/oc/api", "description": "APAC"},
]

WDATA_SERVERS = [
    {"url": "https://h.eu.wdesk.com/s/wdata/prep", "description": "EU"},
    {"url": "https://h.app.wdesk.com/s/wdata/prep", "description": "US"},
    {"url": "https://h.apac.wdesk.com/s/wdata/prep", "description": "APAC"},
]

HTTP_METHODS = {"get", "post", "put", "delete", "patch", "head", "options", "trace"}

# ---------------------------------------------------------------------------
# Pagination configs — one per pattern (A-E)
# ---------------------------------------------------------------------------

# A: Platform standard — 60 endpoints with $next param and @nextLink response
PAGINATION_PLATFORM_NEXT = {
    "type": "cursor",
    "inputs": [{"name": "$next", "in": "parameters", "type": "cursor"}],
    "outputs": {"nextCursor": "$['@nextLink']"},
}

# B: Platform JSON:API — getOrgReportUsers only
PAGINATION_PLATFORM_JSONAPI = {
    "type": "url",
    "outputs": {"nextUrl": "$.links.next"},
}

# C: Chains cursor — chainFilterSearch, chainInputsSearch, chainRunHistory
PAGINATION_CHAINS_CURSOR = {
    "type": "cursor",
    "inputs": [{"name": "cursor", "in": "parameters", "type": "cursor"}],
    "outputs": {"nextCursor": "$.data.cursor"},
}

# D: Chains page-number — security endpoints (0-based page)
PAGINATION_CHAINS_PAGE = {
    "type": "offsetLimit",
    "inputs": [{"name": "page", "in": "parameters", "type": "page"}],
    "outputs": {"results": "$.data"},
}

# E: Wdata cursor — all paginated wdata endpoints
PAGINATION_WDATA_CURSOR = {
    "type": "cursor",
    "inputs": [{"name": "cursor", "in": "parameters", "type": "cursor"}],
    "outputs": {"nextCursor": "$.cursor"},
}

# Chains: explicit operationId → pagination config mapping
CHAINS_CURSOR_OPS = {"chainFilterSearch", "chainInputsSearch", "chainRunHistory"}
CHAINS_PAGE_OPS = {
    "getAuthorizationsActivity",
    "getLoginActivity",
    "getPermissions",
    "getUserGroups",
    "getUserGroupPermissions",
    "getUsers",
    "getUserUserGroups",
}


def rename_refs(obj, renames):
    """Recursively find and rename $ref values pointing to renamed schemas."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "$ref" and isinstance(value, str):
                for old_name, new_name in renames.items():
                    old_ref = f"#/components/schemas/{old_name}"
                    if value == old_ref:
                        obj[key] = f"#/components/schemas/{new_name}"
                        break
            else:
                rename_refs(value, renames)
    elif isinstance(obj, list):
        for item in obj:
            rename_refs(item, renames)


def prefix_operation_ids(spec, prefix):
    """Prefix all operationIds and add x-speakeasy-name-override with the original name."""
    paths = spec.get("paths", {})
    renamed = []
    for path_key, path_item in paths.items():
        for method in HTTP_METHODS:
            if method in path_item and "operationId" in path_item[method]:
                original_id = path_item[method]["operationId"]
                path_item[method]["operationId"] = f"{prefix}_{original_id}"
                path_item[method]["x-speakeasy-name-override"] = original_id
                renamed.append(original_id)
    return renamed


def unify_security_scheme(spec, old_name, new_name):
    """Rename a security scheme and all operation references to it.

    chains.yaml uses 'oauth2' pointing to an external tokenUrl.
    Platform uses 'oauth' pointing to /iam/v1/oauth2/token.
    Since the same credentials work for all 3 APIs, we unify to 'oauth'
    so the merged spec has a single auth flow.
    """
    schemes = spec.get("components", {}).get("securitySchemes", {})
    if old_name in schemes:
        schemes.pop(old_name)  # Remove — platform's 'oauth' will win in merge

    # Update operation-level security references
    paths = spec.get("paths", {})
    for path_item in paths.values():
        for method in HTTP_METHODS:
            if method in path_item:
                op = path_item[method]
                if "security" in op:
                    op["security"] = [
                        {new_name: v} if old_name in entry and (v := entry[old_name]) is not None
                        else ({new_name: entry[old_name]} if old_name in entry else entry)
                        for entry in op["security"]
                    ]

    # Update global security
    if "security" in spec:
        spec["security"] = [
            {new_name: v} if old_name in entry and (v := entry[old_name]) is not None
            else ({new_name: entry[old_name]} if old_name in entry else entry)
            for entry in spec["security"]
        ]


def add_group_and_servers(spec, group_name, servers):
    """Add x-speakeasy-group to all operations and path-level servers."""
    paths = spec.get("paths", {})
    for path_item in paths.values():
        path_item["servers"] = servers
        for method in HTTP_METHODS:
            if method in path_item:
                path_item[method]["x-speakeasy-group"] = group_name


def has_query_param(operation, param_name):
    """Check if an operation has a specific query parameter (inline or $ref)."""
    for param in operation.get("parameters", []):
        # Inline parameter
        if param.get("name") == param_name and param.get("in") == "query":
            return True
        # $ref to components/parameters — match by the ref name fragment
        ref = param.get("$ref", "")
        if ref.endswith(f"/{param_name}") or ref.endswith(f"/parameters/{param_name}"):
            return True
    return False


def has_next_param_ref(operation):
    """Check if an operation references the platform $next / Next parameter."""
    for param in operation.get("parameters", []):
        ref = param.get("$ref", "")
        if "parameters/Next" in ref or "parameters/$next" in ref:
            return True
        if param.get("name") == "$next" and param.get("in") == "query":
            return True
    return False


def add_pagination_extensions(spec, resolver, prefix=None):
    """Walk all operations and apply x-speakeasy-pagination via resolver.

    resolver(operation, original_operation_id) → pagination config dict | None
    prefix: if set, operationIds have been prefixed — strip to get original id.
    """
    paths = spec.get("paths", {})
    count = 0
    for path_key, path_item in paths.items():
        for method in HTTP_METHODS:
            if method not in path_item:
                continue
            op = path_item[method]
            op_id = op.get("operationId", "")
            original_id = op_id
            if prefix and op_id.startswith(f"{prefix}_"):
                original_id = op_id[len(prefix) + 1:]
            config = resolver(op, original_id)
            if config is not None:
                op["x-speakeasy-pagination"] = config
                count += 1
    return count


def resolve_platform_pagination(operation, original_id):
    """Auto-detect platform pagination pattern from parameters."""
    if original_id == "getOrgReportUsers":
        return PAGINATION_PLATFORM_JSONAPI
    if has_next_param_ref(operation):
        return PAGINATION_PLATFORM_NEXT
    return None


def resolve_chains_pagination(operation, original_id):
    """Map chains operationIds to their pagination config."""
    if original_id in CHAINS_CURSOR_OPS:
        return PAGINATION_CHAINS_CURSOR
    if original_id in CHAINS_PAGE_OPS:
        return PAGINATION_CHAINS_PAGE
    return None


def resolve_wdata_pagination(operation, original_id):
    """Auto-detect wdata pagination from cursor query parameter."""
    if has_query_param(operation, "cursor"):
        return PAGINATION_WDATA_CURSOR
    return None


def process_chains(base_dir):
    input_path = base_dir / "chains.yaml"
    output_path = base_dir / "chains_processed.yaml"

    with open(input_path, "r") as f:
        spec = yaml.safe_load(f)

    # 1. Rename conflicting schemas
    schemas = spec.get("components", {}).get("schemas", {})
    for old_name, new_name in CHAINS_SCHEMA_RENAMES.items():
        if old_name in schemas:
            schemas[new_name] = schemas.pop(old_name)

    # 2. Update all $ref references
    rename_refs(spec, CHAINS_SCHEMA_RENAMES)

    # 3. Unify security scheme: oauth2 → oauth (same credentials, platform tokenUrl wins)
    unify_security_scheme(spec, "oauth2", "oauth")

    # 4. Prefix operationIds to avoid collisions
    renamed_ops = prefix_operation_ids(spec, "chains")

    # 5. Add group and servers
    add_group_and_servers(spec, "chains", CHAINS_SERVERS)

    # 6. Add pagination extensions (after prefixing, so we strip prefix)
    pag_count = add_pagination_extensions(spec, resolve_chains_pagination, prefix="chains")

    with open(output_path, "w") as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)

    print(f"[OK] chains: {input_path} -> {output_path}")
    print(f"     Renamed schemas: {list(CHAINS_SCHEMA_RENAMES.keys())}")
    print(f"     Prefixed operationIds: {len(renamed_ops)} operations")
    print(f"     Unified security: oauth2 → oauth")
    print(f"     Pagination extensions: {pag_count} operations")


def fix_recursive_schemas(spec):
    """Fix recursive schema references that Speakeasy can't handle.

    Section, Slide, and Sheet all have parent properties that self-reference
    their own schema via allOf, creating infinite recursion.
    """
    schemas = spec.get("components", {}).get("schemas", {})
    fixed = []

    for schema_name in ("Section", "Slide", "Sheet"):
        schema = schemas.get(schema_name, {})
        parent_prop = schema.get("properties", {}).get("parent", {})
        if "allOf" in parent_prop:
            schema["properties"]["parent"] = {
                "description": f"Partial reference to the parent {schema_name.lower()}",
                "nullable": True,
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                },
            }
            fixed.append(schema_name)

    return fixed


def remove_security_scheme(spec, scheme_name):
    """Remove a security scheme and all operation references to it.

    contextless-oauth is a subset of oauth (fewer scopes, same tokenUrl).
    Since the same credentials work for everything, we keep only 'oauth'.
    Speakeasy doesn't support multiple OAuth2 Client Credentials flows.
    """
    schemes = spec.get("components", {}).get("securitySchemes", {})
    schemes.pop(scheme_name, None)

    paths = spec.get("paths", {})
    for path_item in paths.values():
        for method in HTTP_METHODS:
            if method in path_item and "security" in path_item[method]:
                path_item[method]["security"] = [
                    entry for entry in path_item[method]["security"]
                    if scheme_name not in entry
                ]


def update_token_url(spec, old_url, new_url):
    """Update tokenUrl in securitySchemes to the 2026-01-01 endpoint."""
    schemes = spec.get("components", {}).get("securitySchemes", {})
    updated = []
    for name, scheme in schemes.items():
        flows = scheme.get("flows", {})
        for flow_name, flow in flows.items():
            if flow.get("tokenUrl") == old_url:
                flow["tokenUrl"] = new_url
                updated.append(f"{name}.{flow_name}")
    return updated


def rename_dollar_params(spec):
    """Add x-speakeasy-name-override to $-prefixed query params so SDK uses clean names."""
    renamed = []
    # components/parameters (shared refs)
    for param_name, param in spec.get("components", {}).get("parameters", {}).items():
        name = param.get("name", "")
        if name.startswith("$"):
            param["x-speakeasy-name-override"] = name[1:]
            renamed.append(name)
    # Inline parameters in operations
    for path_item in spec.get("paths", {}).values():
        for method in HTTP_METHODS:
            if method not in path_item:
                continue
            for param in path_item[method].get("parameters", []):
                name = param.get("name", "")
                if name.startswith("$") and "x-speakeasy-name-override" not in param:
                    param["x-speakeasy-name-override"] = name[1:]
                    renamed.append(name)
    return renamed


def process_platform(base_dir):
    input_path = base_dir / "platform.yaml"
    output_path = base_dir / "platform_processed.yaml"

    with open(input_path, "r") as f:
        spec = yaml.safe_load(f)

    # Fix recursive schema references
    fixed = fix_recursive_schemas(spec)

    # Remove contextless-oauth (subset of oauth, same tokenUrl, same credentials)
    remove_security_scheme(spec, "contextless-oauth")

    # Update tokenUrl to 2026-01-01 endpoint (was /iam/v1/oauth2/token)
    updated_flows = update_token_url(spec, "/iam/v1/oauth2/token", "/oauth2/token")

    # Reorder global servers: EU first (default), then US, APAC
    servers = spec.get("servers", [])
    by_desc = {s.get("description", ""): s for s in servers}
    if "EU" in by_desc and "US" in by_desc:
        spec["servers"] = [by_desc["EU"], by_desc["US"]] + [
            s for s in servers if s.get("description") not in ("EU", "US")
        ]

    # Rename $-prefixed params to clean names (e.g. $maxpagesize → maxpagesize)
    dollar_params = rename_dollar_params(spec)

    # Add pagination extensions (platform has no prefix)
    pag_count = add_pagination_extensions(spec, resolve_platform_pagination)

    with open(output_path, "w") as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)

    print(f"[OK] platform: {input_path} -> {output_path}")
    print(f"     Fixed recursive parent in: {fixed}")
    print(f"     Removed contextless-oauth scheme")
    print(f"     Updated tokenUrl: {updated_flows}")
    print(f"     Renamed $params: {len(dollar_params)}")
    print(f"     Pagination extensions: {pag_count} operations")


def mark_open_enums(spec):
    """Add x-speakeasy-unknown-values: allow to enums that may gain new values.

    Without this, Speakeasy generates strict Enum classes that raise ValueError
    on unknown values.  The Wdata spec explicitly states "more types may be
    added in the future" for SelectListDto.type, so it MUST remain open.
    """
    open_enum_paths = [
        ("SelectListDto", "type"),
    ]
    schemas = spec.get("components", {}).get("schemas", {})
    marked = []
    for schema_name, prop_name in open_enum_paths:
        prop = schemas.get(schema_name, {}).get("properties", {}).get(prop_name)
        if prop and "enum" in prop:
            prop["x-speakeasy-unknown-values"] = "allow"
            marked.append(f"{schema_name}.{prop_name}")
    return marked


def process_wdata(base_dir):
    input_path = base_dir / "wdata.yaml"
    output_path = base_dir / "wdata_processed.yaml"

    with open(input_path, "r") as f:
        spec = yaml.safe_load(f)

    # 1. Mark enums that must stay forward-compatible
    marked_enums = mark_open_enums(spec)

    # 2. Prefix operationIds to avoid collisions
    renamed_ops = prefix_operation_ids(spec, "wdata")

    # 3. Add group and servers
    add_group_and_servers(spec, "wdata", WDATA_SERVERS)

    # 4. Add pagination extensions (after prefixing, so we strip prefix)
    pag_count = add_pagination_extensions(spec, resolve_wdata_pagination, prefix="wdata")

    with open(output_path, "w") as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)

    print(f"[OK] wdata: {input_path} -> {output_path}")
    print(f"     Open enums: {marked_enums}")
    print(f"     Prefixed operationIds: {len(renamed_ops)} operations")
    print(f"     Pagination extensions: {pag_count} operations")


if __name__ == "__main__":
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    process_chains(base_dir)
    process_wdata(base_dir)
    process_platform(base_dir)
    print("\nReady for merge.")
