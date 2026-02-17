"""Tests for auto-pagination in generated operations.

Verifies that paginated operations (Code path A) automatically fetch
all pages and return a single typed Pydantic model with all items.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from workiva._constants import _API
from workiva.models.platform import FilesListResult


def _make_pages(pages: list[dict]) -> MagicMock:
    """Create a MagicMock BaseClient that returns pages in sequence."""
    responses = [httpx.Response(200, json=p) for p in pages]
    client = MagicMock()
    client.request.side_effect = responses
    return client


class TestPlatformAutoPagination:
    """Platform NEXT pattern: $next param → @nextLink cursor."""

    def test_single_page_returns_typed_model(self):
        """get_files() with one page returns FilesListResult."""
        from workiva._operations.files import Files

        page = {
            "data": [{"name": "a.xlsx", "kind": "Spreadsheet"}],
            "@nextLink": None,
        }
        client = _make_pages([page])
        ns = Files(client)

        result = ns.get_files()

        assert isinstance(result, FilesListResult)
        assert len(result.data) == 1
        assert result.data[0].name == "a.xlsx"

    def test_multiple_pages_aggregated(self):
        """get_files() with 2 pages returns all items in one model."""
        from workiva._operations.files import Files

        page1 = {
            "data": [{"name": "a.xlsx", "kind": "Spreadsheet"}],
            "@nextLink": "cursor-page2",
        }
        page2 = {
            "data": [{"name": "b.docx", "kind": "Document"}],
            "@nextLink": None,
        }
        client = _make_pages([page1, page2])
        ns = Files(client)

        result = ns.get_files()

        assert isinstance(result, FilesListResult)
        assert len(result.data) == 2
        assert result.data[0].name == "a.xlsx"
        assert result.data[1].name == "b.docx"

    def test_cursor_injected_in_second_request(self):
        """The cursor from page 1 should be sent as $next in page 2 request."""
        from workiva._operations.files import Files

        page1 = {
            "data": [{"name": "a.xlsx"}],
            "@nextLink": "cursor-abc",
        }
        page2 = {
            "data": [],
            "@nextLink": None,
        }
        client = _make_pages([page1, page2])
        ns = Files(client)

        ns.get_files()

        # First call: cursor is None
        first_call = client.request.call_args_list[0]
        assert first_call.kwargs.get("query_params", {}).get("$next") is None

        # Second call: cursor is "cursor-abc"
        second_call = client.request.call_args_list[1]
        assert second_call.kwargs.get("query_params", {}).get("$next") == "cursor-abc"

    def test_cursor_param_not_in_signature(self):
        """get_files() should NOT accept a 'next_' parameter."""
        from workiva._operations.files import Files
        import inspect

        sig = inspect.signature(Files.get_files)
        param_names = list(sig.parameters.keys())
        assert "next_" not in param_names


class TestPlatformAutoPaginationAsync:
    """Async version of Platform NEXT pagination."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_multiple_pages_async(self):
        """get_files_async() aggregates all pages."""
        from workiva._operations.files import Files

        pages = [
            httpx.Response(200, json={
                "data": [{"name": "a.xlsx"}],
                "@nextLink": "page2",
            }),
            httpx.Response(200, json={
                "data": [{"name": "b.docx"}],
                "@nextLink": None,
            }),
        ]
        client = MagicMock()
        client.request_async = AsyncMock(side_effect=pages)
        ns = Files(client)

        result = await ns.get_files_async()

        assert isinstance(result, FilesListResult)
        assert len(result.data) == 2
