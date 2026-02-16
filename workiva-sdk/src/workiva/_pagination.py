"""Pagination generators for the Workiva SDK.

Standard Python generators for iterating over paginated API responses.
Each pagination pattern maps to a cursor-extraction strategy.

Usage in generated code::

    def get_files_all(self, **kwargs) -> Generator[File, None, None]:
        yield from paginate(
            fetch=lambda cursor: self.get_files(next=cursor, **kwargs),
            extract_cursor=extract_next_link,
            extract_items=lambda r: r.value or [],
        )
"""

from __future__ import annotations

from typing import (
    Any,
    AsyncGenerator,
    Awaitable,
    Callable,
    Generator,
    Optional,
    TypeVar,
)

T = TypeVar("T")
R = TypeVar("R")  # Response type


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


# -- Generic paginator -------------------------------------------------------


def paginate(
    fetch: Callable[[Optional[str]], R],
    extract_cursor: Callable[[dict[str, Any]], Optional[str]],
    extract_items: Callable[[R], list[T]],
    get_body: Callable[[R], dict[str, Any]],
    initial_cursor: Optional[str] = None,
) -> Generator[T, None, None]:
    """Sync pagination generator.

    Args:
        fetch: Function that takes a cursor (or None for first page) and
            returns a response object.
        extract_cursor: Extracts the next cursor from the raw response body.
        extract_items: Extracts the list of items from the response.
        get_body: Extracts the raw dict body from the response (for cursor parsing).
        initial_cursor: Starting cursor value (None for first page).

    Yields:
        Individual items from each page.
    """
    cursor = initial_cursor
    while True:
        response = fetch(cursor)
        items = extract_items(response)
        yield from items

        body = get_body(response)
        cursor = extract_cursor(body)
        if cursor is None:
            break


async def paginate_async(
    fetch: Callable[[Optional[str]], Awaitable[R]],
    extract_cursor: Callable[[dict[str, Any]], Optional[str]],
    extract_items: Callable[[R], list[T]],
    get_body: Callable[[R], dict[str, Any]],
    initial_cursor: Optional[str] = None,
) -> AsyncGenerator[T, None]:
    """Async pagination generator.

    Same interface as ``paginate()`` but ``fetch`` is an async callable.

    Yields:
        Individual items from each page.
    """
    cursor = initial_cursor
    while True:
        response = await fetch(cursor)
        items = extract_items(response)
        for item in items:
            yield item

        body = get_body(response)
        cursor = extract_cursor(body)
        if cursor is None:
            break
