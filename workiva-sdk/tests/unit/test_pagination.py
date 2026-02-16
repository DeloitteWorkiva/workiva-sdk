"""Tests for workiva._pagination."""

from __future__ import annotations

import pytest

from workiva._pagination import (
    extract_chains_cursor,
    extract_jsonapi_next,
    extract_next_link,
    extract_wdata_cursor,
    paginate,
)


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
        body = {"data": {"cursor": "cursor-abc", "items": []}}
        assert extract_chains_cursor(body) == "cursor-abc"

    def test_missing(self):
        assert extract_chains_cursor({"data": {}}) is None


class TestExtractWdataCursor:
    def test_present(self):
        body = {"cursor": "wdata-cursor-xyz", "body": []}
        assert extract_wdata_cursor(body) == "wdata-cursor-xyz"

    def test_missing(self):
        assert extract_wdata_cursor({}) is None


class TestPaginate:
    def test_single_page(self):
        """Paginator yields items from a single page when no next cursor."""
        results = list(paginate(
            fetch=lambda cursor: {"value": [1, 2, 3], "@nextLink": None},
            extract_cursor=extract_next_link,
            extract_items=lambda r: r["value"],
            get_body=lambda r: r,
        ))
        assert results == [1, 2, 3]

    def test_multiple_pages(self):
        """Paginator follows cursors across pages."""
        pages = [
            {"value": ["a", "b"], "@nextLink": "page2"},
            {"value": ["c"], "@nextLink": None},
        ]
        call_count = 0

        def fetch(cursor):
            nonlocal call_count
            result = pages[call_count]
            call_count += 1
            return result

        results = list(paginate(
            fetch=fetch,
            extract_cursor=extract_next_link,
            extract_items=lambda r: r["value"],
            get_body=lambda r: r,
        ))
        assert results == ["a", "b", "c"]

    def test_empty_first_page(self):
        """Paginator handles empty first page gracefully."""
        results = list(paginate(
            fetch=lambda cursor: {"value": [], "@nextLink": None},
            extract_cursor=extract_next_link,
            extract_items=lambda r: r["value"],
            get_body=lambda r: r,
        ))
        assert results == []
