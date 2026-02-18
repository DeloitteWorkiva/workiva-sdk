"""Pagination helpers for the Workiva SDK.

Provides cursor-extraction strategies and aggregation functions that fetch
ALL pages and return a single merged dict ready for Pydantic parsing.

Each pagination pattern maps to an extractor that reads the "next cursor"
from the response body.  ``paginate_all`` / ``paginate_all_async`` loop
through every page, accumulate items, and return the final body with all
items merged — so one ``Model.model_validate(body)`` call is all you need.
"""

from __future__ import annotations

from typing import Any, AsyncGenerator, Callable, Generator, Optional

import httpx


# -- Cursor extractors (one per pagination pattern) --------------------------


def extract_next_link(body: dict[str, Any]) -> Optional[str]:
    """Pattern A: Platform standard — ``@nextLink`` in response body."""
    cursor = body.get("@nextLink")
    if cursor and str(cursor).strip():
        return str(cursor)
    return None


def extract_jsonapi_next(body: dict[str, Any]) -> Optional[str]:
    """Pattern B: Platform JSON:API — ``links.next`` in response body."""
    links = body.get("links", {})
    if isinstance(links, dict):
        url = links.get("next")
        if url and str(url).strip():
            return str(url)
    return None


def extract_chains_cursor(body: dict[str, Any]) -> Optional[str]:
    """Pattern C: Chains cursor — ``data.cursor`` in response body."""
    data = body.get("data", {})
    if isinstance(data, dict):
        cursor = data.get("cursor")
        if cursor and str(cursor).strip():
            return str(cursor)
    return None


def extract_wdata_cursor(body: dict[str, Any]) -> Optional[str]:
    """Pattern E: Wdata cursor — ``cursor`` in response body."""
    cursor = body.get("cursor")
    if cursor and str(cursor).strip():
        return str(cursor)
    return None


# -- Nested dict helpers -----------------------------------------------------


def _get_nested(d: dict[str, Any], path: str) -> Any:
    """Get a value from a nested dict using dot-separated path."""
    for key in path.split("."):
        if isinstance(d, dict):
            d = d.get(key, {})
        else:
            return []
    return d


def _set_nested(d: dict[str, Any], path: str, value: Any) -> None:
    """Set a value in a nested dict using dot-separated path."""
    keys = path.split(".")
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value


# -- Aggregation functions ---------------------------------------------------


_MAX_PAGES = 1000
"""Safety limit to prevent infinite pagination loops."""


def paginate_all(
    fetch: Callable[[Optional[str]], httpx.Response],
    extract_cursor: Callable[[dict[str, Any]], Optional[str]],
    items_path: str,
    max_pages: int = _MAX_PAGES,
) -> dict[str, Any]:
    """Fetch ALL pages and return merged response body with all items.

    Loops through every page at the raw dict level, accumulates items,
    then returns the LAST response body with the items field replaced
    by all accumulated items.

    Args:
        fetch: Calls the API with an optional cursor. Returns httpx.Response.
        extract_cursor: Extracts the next cursor from the response body dict.
        items_path: Dot-separated path to the items list (e.g. "data",
            "body", "data.chainExecutors").
        max_pages: Safety limit to prevent infinite loops (default 1000).

    Returns:
        Merged response body dict with all items aggregated.

    Raises:
        RuntimeError: If ``max_pages`` is exceeded (likely a bug in the API).
    """
    all_items: list[Any] = []
    final_body: dict[str, Any] = {}
    cursor: Optional[str] = None

    for page in range(max_pages):
        response = fetch(cursor)
        body = response.json()
        final_body = body
        items = _get_nested(body, items_path)
        if isinstance(items, list):
            all_items.extend(items)
        cursor = extract_cursor(body)
        if cursor is None:
            break
    else:
        raise RuntimeError(
            f"Pagination exceeded {max_pages} pages — aborting to prevent "
            f"infinite loop. Use API parameters to limit results, or pass "
            f"max_pages= to increase the limit."
        )

    _set_nested(final_body, items_path, all_items)
    return final_body


async def paginate_all_async(
    fetch: Callable[[Optional[str]], Any],
    extract_cursor: Callable[[dict[str, Any]], Optional[str]],
    items_path: str,
    max_pages: int = _MAX_PAGES,
) -> dict[str, Any]:
    """Async version of :func:`paginate_all`.

    Same semantics — fetches ALL pages, returns merged body dict.

    Raises:
        RuntimeError: If ``max_pages`` is exceeded (likely a bug in the API).
    """
    all_items: list[Any] = []
    final_body: dict[str, Any] = {}
    cursor: Optional[str] = None

    for page in range(max_pages):
        response = await fetch(cursor)
        body = response.json()
        final_body = body
        items = _get_nested(body, items_path)
        if isinstance(items, list):
            all_items.extend(items)
        cursor = extract_cursor(body)
        if cursor is None:
            break
    else:
        raise RuntimeError(
            f"Pagination exceeded {max_pages} pages — aborting to prevent "
            f"infinite loop. Use API parameters to limit results, or pass "
            f"max_pages= to increase the limit."
        )

    _set_nested(final_body, items_path, all_items)
    return final_body


def paginate_lazy(
    fetch: Callable[[Optional[str]], httpx.Response],
    extract_cursor: Callable[[dict[str, Any]], Optional[str]],
    items_path: str,
    max_pages: int = _MAX_PAGES,
) -> Generator[Any, None, None]:
    """Yield items lazily one page at a time (sync).

    Unlike :func:`paginate_all`, items are yielded as they are fetched
    instead of being accumulated in memory. Use this for large datasets
    where loading all pages at once could cause memory issues.

    Args:
        fetch: Calls the API with an optional cursor. Returns httpx.Response.
        extract_cursor: Extracts the next cursor from the response body dict.
        items_path: Dot-separated path to the items list.
        max_pages: Safety limit to prevent infinite loops (default 1000).

    Yields:
        Individual items from each page.

    Raises:
        RuntimeError: If ``max_pages`` is exceeded.
    """
    cursor: Optional[str] = None

    for page in range(max_pages):
        response = fetch(cursor)
        body = response.json()
        items = _get_nested(body, items_path)
        if isinstance(items, list):
            yield from items
        cursor = extract_cursor(body)
        if cursor is None:
            return
    raise RuntimeError(
        f"Pagination exceeded {max_pages} pages — aborting to prevent "
        f"infinite loop. Use API parameters to limit results, or pass "
        f"max_pages= to increase the limit."
    )


async def paginate_lazy_async(
    fetch: Callable[[Optional[str]], Any],
    extract_cursor: Callable[[dict[str, Any]], Optional[str]],
    items_path: str,
    max_pages: int = _MAX_PAGES,
) -> AsyncGenerator[Any, None]:
    """Yield items lazily one page at a time (async).

    Async version of :func:`paginate_lazy`.

    Yields:
        Individual items from each page.

    Raises:
        RuntimeError: If ``max_pages`` is exceeded.
    """
    cursor: Optional[str] = None

    for page in range(max_pages):
        response = await fetch(cursor)
        body = response.json()
        items = _get_nested(body, items_path)
        if isinstance(items, list):
            for item in items:
                yield item
        cursor = extract_cursor(body)
        if cursor is None:
            return
    raise RuntimeError(
        f"Pagination exceeded {max_pages} pages — aborting to prevent "
        f"infinite loop. Use API parameters to limit results, or pass "
        f"max_pages= to increase the limit."
    )
