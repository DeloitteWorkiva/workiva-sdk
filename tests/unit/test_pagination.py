"""Tests for workiva._pagination."""

from __future__ import annotations

import json

import httpx
import pytest

from workiva._pagination import (
    _get_nested,
    _set_nested,
    extract_chains_cursor,
    extract_jsonapi_next,
    extract_next_link,
    extract_wdata_cursor,
    paginate_all,
    paginate_all_async,
)


def _mock_response(body: dict) -> httpx.Response:
    """Build an httpx.Response with a JSON body."""
    return httpx.Response(200, json=body)


class TestExtractNextLink:
    def test_present(self):
        body = {"@nextLink": "https://api.example.com/files?next=abc"}
        assert extract_next_link(body) == "https://api.example.com/files?next=abc"

    def test_missing(self):
        assert extract_next_link({}) is None

    def test_empty_string(self):
        assert extract_next_link({"@nextLink": ""}) is None

    def test_whitespace_only(self):
        assert extract_next_link({"@nextLink": "  "}) is None

    def test_none_value(self):
        assert extract_next_link({"@nextLink": None}) is None


class TestExtractJsonApiNext:
    def test_present(self):
        body = {"links": {"next": "https://example.com/page2"}}
        assert extract_jsonapi_next(body) == "https://example.com/page2"

    def test_missing_links(self):
        assert extract_jsonapi_next({}) is None

    def test_missing_next(self):
        assert extract_jsonapi_next({"links": {}}) is None


class TestExtractChainsCursor:
    def test_present(self):
        body = {"data": {"cursor": "cursor-abc", "chainExecutors": []}}
        assert extract_chains_cursor(body) == "cursor-abc"

    def test_missing(self):
        assert extract_chains_cursor({"data": {}}) is None


class TestExtractWdataCursor:
    def test_present(self):
        body = {"cursor": "wdata-cursor-xyz", "body": []}
        assert extract_wdata_cursor(body) == "wdata-cursor-xyz"

    def test_missing(self):
        assert extract_wdata_cursor({}) is None


class TestGetNested:
    def test_single_level(self):
        assert _get_nested({"data": [1, 2]}, "data") == [1, 2]

    def test_two_levels(self):
        assert _get_nested({"data": {"items": [3]}}, "data.items") == [3]

    def test_missing_key(self):
        assert _get_nested({"data": {}}, "data.items") == {}

    def test_non_dict_intermediate(self):
        assert _get_nested({"data": "string"}, "data.items") == []


class TestSetNested:
    def test_single_level(self):
        d = {"data": [1]}
        _set_nested(d, "data", [1, 2, 3])
        assert d == {"data": [1, 2, 3]}

    def test_two_levels(self):
        d = {"data": {"items": [1]}}
        _set_nested(d, "data.items", [1, 2, 3])
        assert d == {"data": {"items": [1, 2, 3]}}

    def test_creates_intermediate(self):
        d: dict = {}
        _set_nested(d, "data.items", [1])
        assert d == {"data": {"items": [1]}}


class TestPaginateAll:
    def test_single_page(self):
        """Aggregator returns items from a single page."""
        body = paginate_all(
            fetch=lambda cursor: _mock_response({"data": [1, 2, 3], "@nextLink": None}),
            extract_cursor=extract_next_link,
            items_path="data",
        )
        assert body["data"] == [1, 2, 3]

    def test_multiple_pages(self):
        """Aggregator merges items across pages."""
        pages = [
            {"data": ["a", "b"], "@nextLink": "page2"},
            {"data": ["c"], "@nextLink": None},
        ]
        call_count = 0

        def fetch(cursor):
            nonlocal call_count
            result = _mock_response(pages[call_count])
            call_count += 1
            return result

        body = paginate_all(
            fetch=fetch,
            extract_cursor=extract_next_link,
            items_path="data",
        )
        assert body["data"] == ["a", "b", "c"]

    def test_empty_first_page(self):
        """Aggregator handles empty page gracefully."""
        body = paginate_all(
            fetch=lambda cursor: _mock_response({"data": [], "@nextLink": None}),
            extract_cursor=extract_next_link,
            items_path="data",
        )
        assert body["data"] == []

    def test_nested_items_path(self):
        """Aggregator handles dot-separated items_path (e.g. Chains)."""
        pages = [
            {"data": {"chainExecutors": [{"id": 1}], "cursor": "c2"}},
            {"data": {"chainExecutors": [{"id": 2}], "cursor": None}},
        ]
        call_count = 0

        def fetch(cursor):
            nonlocal call_count
            result = _mock_response(pages[call_count])
            call_count += 1
            return result

        body = paginate_all(
            fetch=fetch,
            extract_cursor=extract_chains_cursor,
            items_path="data.chainExecutors",
        )
        assert body["data"]["chainExecutors"] == [{"id": 1}, {"id": 2}]


    def test_max_pages_guard(self):
        """Aggregator raises RuntimeError when max_pages is exceeded."""

        def fetch(cursor):
            return _mock_response({"data": ["item"], "@nextLink": "always-more"})

        with pytest.raises(RuntimeError, match="exceeded 3 pages"):
            paginate_all(
                fetch=fetch,
                extract_cursor=extract_next_link,
                items_path="data",
                max_pages=3,
            )


class TestPaginateAllAsync:
    @pytest.mark.asyncio(loop_scope="function")
    async def test_single_page(self):
        """Async aggregator returns items from a single page."""

        async def fetch(cursor):
            return _mock_response({"data": [1, 2, 3], "@nextLink": None})

        body = await paginate_all_async(
            fetch=fetch,
            extract_cursor=extract_next_link,
            items_path="data",
        )
        assert body["data"] == [1, 2, 3]

    @pytest.mark.asyncio(loop_scope="function")
    async def test_multiple_pages(self):
        """Async aggregator merges items across pages."""
        pages = [
            {"data": ["a", "b"], "@nextLink": "page2"},
            {"data": ["c"], "@nextLink": None},
        ]
        call_count = 0

        async def fetch(cursor):
            nonlocal call_count
            result = _mock_response(pages[call_count])
            call_count += 1
            return result

        body = await paginate_all_async(
            fetch=fetch,
            extract_cursor=extract_next_link,
            items_path="data",
        )
        assert body["data"] == ["a", "b", "c"]

    @pytest.mark.asyncio(loop_scope="function")
    async def test_max_pages_guard(self):
        """Async aggregator raises RuntimeError when max_pages is exceeded."""

        async def fetch(cursor):
            return _mock_response({"data": ["item"], "@nextLink": "always-more"})

        with pytest.raises(RuntimeError, match="exceeded 3 pages"):
            await paginate_all_async(
                fetch=fetch,
                extract_cursor=extract_next_link,
                items_path="data",
                max_pages=3,
            )
