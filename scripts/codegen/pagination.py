"""Pagination configuration for the Workiva SDK codegen.

Maps operationId → pagination strategy so the Jinja2 templates can
generate ``_all()`` generator methods for paginated endpoints.

Ported from prepare_specs.py pagination constants + resolver functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class PaginationPattern(str, Enum):
    """Pagination patterns across the three Workiva APIs."""

    # A: Platform standard — $next param → @nextLink response
    PLATFORM_NEXT = "platform_next"
    # B: Platform JSON:API — links.next URL
    PLATFORM_JSONAPI = "platform_jsonapi"
    # C: Chains cursor — cursor param → data.cursor response
    CHAINS_CURSOR = "chains_cursor"
    # D: Chains page-number — page param (0-based)
    CHAINS_PAGE = "chains_page"
    # E: Wdata cursor — cursor param → cursor response
    WDATA_CURSOR = "wdata_cursor"


@dataclass(frozen=True)
class PaginationConfig:
    """Configuration for a paginated operation."""

    pattern: PaginationPattern
    # The query parameter name that receives the cursor/page
    cursor_param: str
    # The JSONPath-like key to extract the next cursor from the response body
    cursor_response_path: str
    # The key to extract items from the response body (for _all generators)
    items_path: Optional[str] = None

    @property
    def extractor_func(self) -> str:
        """The name of the cursor extractor function in _pagination.py."""
        return {
            PaginationPattern.PLATFORM_NEXT: "extract_next_link",
            PaginationPattern.PLATFORM_JSONAPI: "extract_jsonapi_next",
            PaginationPattern.CHAINS_CURSOR: "extract_chains_cursor",
            PaginationPattern.CHAINS_PAGE: "extract_chains_cursor",  # same shape
            PaginationPattern.WDATA_CURSOR: "extract_wdata_cursor",
        }[self.pattern]


# Pre-built configs for each pattern
_PLATFORM_NEXT = PaginationConfig(
    pattern=PaginationPattern.PLATFORM_NEXT,
    cursor_param="next",
    cursor_response_path="@nextLink",
    items_path="value",
)

_PLATFORM_JSONAPI = PaginationConfig(
    pattern=PaginationPattern.PLATFORM_JSONAPI,
    cursor_param="next",
    cursor_response_path="links.next",
    items_path="data",
)

_CHAINS_CURSOR = PaginationConfig(
    pattern=PaginationPattern.CHAINS_CURSOR,
    cursor_param="cursor",
    cursor_response_path="data.cursor",
    items_path="data.items",
)

_CHAINS_PAGE = PaginationConfig(
    pattern=PaginationPattern.CHAINS_PAGE,
    cursor_param="page",
    cursor_response_path="data",
    items_path="data",
)

_WDATA_CURSOR = PaginationConfig(
    pattern=PaginationPattern.WDATA_CURSOR,
    cursor_param="cursor",
    cursor_response_path="cursor",
    items_path="body",
)


# Chains operationIds that use cursor pagination
CHAINS_CURSOR_OPS = {"chainFilterSearch", "chainInputsSearch", "chainRunHistory"}

# Chains operationIds that use page-number pagination
CHAINS_PAGE_OPS = {
    "getAuthorizationsActivity",
    "getLoginActivity",
    "getPermissions",
    "getUserGroups",
    "getUserGroupPermissions",
    "getUsers",
    "getUserUserGroups",
}

# Platform operationId that uses JSON:API pagination
PLATFORM_JSONAPI_OPS = {"getOrgReportUsers"}


def resolve_pagination(
    operation_id: str,
    api: str,
    has_next_param: bool = False,
    has_cursor_param: bool = False,
) -> Optional[PaginationConfig]:
    """Resolve the pagination config for an operation.

    Args:
        operation_id: The operationId from the OpenAPI spec.
        api: Which API this operation belongs to (platform, chains, wdata).
        has_next_param: Whether the operation has a ``$next`` or ``next`` query param.
        has_cursor_param: Whether the operation has a ``cursor`` query param.

    Returns:
        PaginationConfig if paginated, None otherwise.
    """
    if api == "platform":
        if operation_id in PLATFORM_JSONAPI_OPS:
            return _PLATFORM_JSONAPI
        if has_next_param:
            return _PLATFORM_NEXT
    elif api == "chains":
        if operation_id in CHAINS_CURSOR_OPS:
            return _CHAINS_CURSOR
        if operation_id in CHAINS_PAGE_OPS:
            return _CHAINS_PAGE
    elif api == "wdata":
        if has_cursor_param:
            return _WDATA_CURSOR

    return None
