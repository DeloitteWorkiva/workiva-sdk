"""Tests for auth lifecycle (_CachedToken), pagination lazy generators,
BaseClient close lifecycle, and HTTP-date Retry-After parsing.
"""

from __future__ import annotations

import time
import warnings
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from typing import Any, Optional
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from workiva._auth import _CachedToken
from workiva._client import BaseClient
from workiva._pagination import (
    extract_next_link,
    paginate_lazy,
    paginate_lazy_async,
)
from workiva._retry import _parse_retry_after
from workiva.exceptions import PaginationError
from workiva.polling import _get_retry_after


# ---------------------------------------------------------------------------
# H12 — _CachedToken.is_expired()
# ---------------------------------------------------------------------------


class TestCachedTokenExpiry:
    def test_expires_at_none_is_not_expired(self):
        token = _CachedToken(access_token="tok", expires_at=None)
        assert token.is_expired() is False

    def test_far_future_is_not_expired(self):
        token = _CachedToken(access_token="tok", expires_at=time.time() + 1000)
        assert token.is_expired() is False

    def test_within_buffer_is_expired(self):
        # 30s remaining, default buffer 60s → expired
        token = _CachedToken(access_token="tok", expires_at=time.time() + 30)
        assert token.is_expired() is True

    def test_already_expired(self):
        token = _CachedToken(access_token="tok", expires_at=time.time() - 100)
        assert token.is_expired() is True

    def test_custom_buffer_zero(self):
        # 30s remaining, buffer=0 → not expired
        token = _CachedToken(access_token="tok", expires_at=time.time() + 30)
        assert token.is_expired(buffer_s=0) is False


# ---------------------------------------------------------------------------
# Helpers for pagination tests
# ---------------------------------------------------------------------------


def _make_response(body: dict[str, Any]) -> httpx.Response:
    """Build a minimal httpx.Response with a JSON body."""
    resp = httpx.Response(200, json=body)
    return resp


# ---------------------------------------------------------------------------
# H13 — paginate_lazy() sync
# ---------------------------------------------------------------------------


class TestPaginateLazy:
    def test_single_page_no_cursor(self):
        body = {"data": [1, 2, 3]}

        def fetch(cursor: Optional[str]) -> httpx.Response:
            return _make_response(body)

        items = list(paginate_lazy(fetch, extract_next_link, "data"))
        assert items == [1, 2, 3]

    def test_multi_page(self):
        pages = [
            {"data": ["a", "b"], "@nextLink": "cursor1"},
            {"data": ["c"], "@nextLink": None},
        ]
        call_count = 0

        def fetch(cursor: Optional[str]) -> httpx.Response:
            nonlocal call_count
            resp = _make_response(pages[call_count])
            call_count += 1
            return resp

        items = list(paginate_lazy(fetch, extract_next_link, "data"))
        assert items == ["a", "b", "c"]
        assert call_count == 2

    def test_empty_page_yields_nothing(self):
        body = {"data": []}

        def fetch(cursor: Optional[str]) -> httpx.Response:
            return _make_response(body)

        items = list(paginate_lazy(fetch, extract_next_link, "data"))
        assert items == []

    def test_max_pages_exceeded_raises_pagination_error(self):
        body = {"data": ["x"], "@nextLink": "always"}

        def fetch(cursor: Optional[str]) -> httpx.Response:
            return _make_response(body)

        with pytest.raises(PaginationError, match="exceeded 2 pages"):
            list(paginate_lazy(fetch, extract_next_link, "data", max_pages=2))


# ---------------------------------------------------------------------------
# H13 — paginate_lazy_async()
# ---------------------------------------------------------------------------


class TestPaginateLazyAsync:
    @pytest.mark.asyncio(loop_scope="function")
    async def test_single_page_async(self):
        body = {"data": [10, 20]}

        async def fetch(cursor: Optional[str]) -> httpx.Response:
            return _make_response(body)

        items = [item async for item in paginate_lazy_async(fetch, extract_next_link, "data")]
        assert items == [10, 20]

    @pytest.mark.asyncio(loop_scope="function")
    async def test_multi_page_async(self):
        pages = [
            {"data": [1], "@nextLink": "c1"},
            {"data": [2, 3]},
        ]
        call_count = 0

        async def fetch(cursor: Optional[str]) -> httpx.Response:
            nonlocal call_count
            resp = _make_response(pages[call_count])
            call_count += 1
            return resp

        items = [item async for item in paginate_lazy_async(fetch, extract_next_link, "data")]
        assert items == [1, 2, 3]

    @pytest.mark.asyncio(loop_scope="function")
    async def test_empty_page_async(self):
        body = {"data": []}

        async def fetch(cursor: Optional[str]) -> httpx.Response:
            return _make_response(body)

        items = [item async for item in paginate_lazy_async(fetch, extract_next_link, "data")]
        assert items == []

    @pytest.mark.asyncio(loop_scope="function")
    async def test_max_pages_exceeded_async(self):
        body = {"data": ["x"], "@nextLink": "always"}

        async def fetch(cursor: Optional[str]) -> httpx.Response:
            return _make_response(body)

        with pytest.raises(PaginationError, match="exceeded 3 pages"):
            _ = [item async for item in paginate_lazy_async(fetch, extract_next_link, "data", max_pages=3)]


# ---------------------------------------------------------------------------
# M15 — BaseClient.close() lifecycle
# ---------------------------------------------------------------------------


def _make_base_client(**overrides: Any) -> BaseClient:
    """Build a BaseClient with mocked internals (no real network)."""
    with patch.object(BaseClient, "__init__", lambda self, **kw: None):
        bc = BaseClient.__new__(BaseClient)
        bc._auth = MagicMock()
        bc._client = None
        bc._client_created = False
        bc._client_supplied = False
        bc._async_client = None
        bc._async_client_created = False
        bc._async_client_supplied = False
        for k, v in overrides.items():
            setattr(bc, k, v)
        return bc


class TestBaseClientLifecycle:
    def test_close_sync_only(self):
        mock_sync = MagicMock()
        bc = _make_base_client(_client=mock_sync, _client_created=True)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            bc.close()

        mock_sync.close.assert_called_once()
        bc._auth.close.assert_called_once()
        resource_warnings = [x for x in w if issubclass(x.category, ResourceWarning)]
        assert resource_warnings == []

    def test_close_with_async_client_warns(self):
        mock_sync = MagicMock()
        mock_async = MagicMock()
        bc = _make_base_client(
            _client=mock_sync,
            _client_created=True,
            _async_client=mock_async,
            _async_client_created=True,
        )

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            bc.close()

        resource_warnings = [x for x in w if issubclass(x.category, ResourceWarning)]
        assert len(resource_warnings) == 1
        assert "aclose()" in str(resource_warnings[0].message)

    @pytest.mark.asyncio(loop_scope="function")
    async def test_aclose_closes_both(self):
        mock_sync = MagicMock()
        mock_async = AsyncMock()
        bc = _make_base_client(
            _client=mock_sync,
            _client_created=True,
            _async_client=mock_async,
            _async_client_created=True,
        )

        await bc.aclose()

        mock_sync.close.assert_called_once()
        mock_async.aclose.assert_called_once()
        bc._auth.close.assert_called_once()

    def test_supplied_client_not_closed(self):
        mock_supplied = MagicMock()
        bc = _make_base_client(
            _client=mock_supplied,
            _client_created=True,
            _client_supplied=True,
        )

        bc.close()

        mock_supplied.close.assert_not_called()


# ---------------------------------------------------------------------------
# M16 — HTTP-date Retry-After parsing
# ---------------------------------------------------------------------------


class TestHttpDateRetryAfter:
    def test_retry_transport_parse_retry_after_http_date(self):
        future = datetime.now(timezone.utc) + timedelta(seconds=10)
        date_str = format_datetime(future, usegmt=True)
        response = httpx.Response(429, headers={"retry-after": date_str})

        result = _parse_retry_after(response)

        assert result is not None
        assert result > 0.0
        # Should be approximately 10 seconds (allow some tolerance)
        assert 5.0 < result < 15.0

    def test_polling_get_retry_after_http_date(self):
        future = datetime.now(timezone.utc) + timedelta(seconds=10)
        date_str = format_datetime(future, usegmt=True)
        headers = {"retry-after": date_str}

        result = _get_retry_after(headers)

        assert result > 0.0
        assert 5.0 < result < 15.0
