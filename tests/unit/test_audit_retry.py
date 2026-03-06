"""Tests for untested code paths in workiva._retry.

Covers:
- Connection error retry (ConnectError, TimeoutException, retry_connection_errors=False)
- AsyncRetryTransport (429, POST 5xx, connection errors)
- Jitter on Retry-After header
- max_retries vs max_elapsed_ms interaction
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from workiva._config import RetryConfig
from workiva._retry import AsyncRetryTransport, RetryTransport, _sleep_interval


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_config(**overrides) -> RetryConfig:
    defaults = dict(
        max_retries=2,
        initial_interval_ms=1,
        max_interval_ms=100,
        max_elapsed_ms=999_999,
    )
    defaults.update(overrides)
    return RetryConfig(**defaults)


def _request(method: str = "GET") -> httpx.Request:
    return httpx.Request(method, "https://example.com/test")


# ===========================================================================
# C2 - Connection error retry
# ===========================================================================


class TestConnectionErrorRetry:
    """RetryTransport behaviour when the inner transport raises connection errors."""

    @patch("time.sleep")
    def test_connect_error_retried_then_reraised(self, mock_sleep: MagicMock):
        """ConnectError is retried up to max_retries, then re-raised."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.side_effect = httpx.ConnectError("refused")
        config = _make_config(max_retries=2)
        transport = RetryTransport(inner, config)

        with pytest.raises(httpx.ConnectError):
            transport.handle_request(_request())

        # 1 initial + 2 retries = 3 total calls
        assert inner.handle_request.call_count == 3
        assert mock_sleep.call_count == 2

    @patch("time.sleep")
    def test_connect_error_not_retried_when_disabled(self, mock_sleep: MagicMock):
        """retry_connection_errors=False → ConnectError re-raised immediately."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.side_effect = httpx.ConnectError("refused")
        config = _make_config(retry_connection_errors=False)
        transport = RetryTransport(inner, config)

        with pytest.raises(httpx.ConnectError):
            transport.handle_request(_request())

        assert inner.handle_request.call_count == 1
        mock_sleep.assert_not_called()

    @patch("time.sleep")
    def test_timeout_exception_retried(self, mock_sleep: MagicMock):
        """httpx.TimeoutException is retried the same as ConnectError."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.side_effect = [
            httpx.TimeoutException("timed out"),
            httpx.Response(200),
        ]
        config = _make_config(max_retries=3)
        transport = RetryTransport(inner, config)

        response = transport.handle_request(_request())
        assert response.status_code == 200
        assert inner.handle_request.call_count == 2
        assert mock_sleep.call_count == 1

    @patch("time.sleep")
    def test_max_retries_caps_connection_errors(self, mock_sleep: MagicMock):
        """max_retries=2 → exactly 3 calls total (1 initial + 2 retries)."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.side_effect = httpx.ConnectError("refused")
        config = _make_config(max_retries=2)
        transport = RetryTransport(inner, config)

        with pytest.raises(httpx.ConnectError):
            transport.handle_request(_request())

        assert inner.handle_request.call_count == 3

    @patch("time.sleep")
    def test_connect_error_recovers_on_retry(self, mock_sleep: MagicMock):
        """ConnectError on first call, success on retry."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.side_effect = [
            httpx.ConnectError("refused"),
            httpx.Response(200),
        ]
        config = _make_config(max_retries=3)
        transport = RetryTransport(inner, config)

        response = transport.handle_request(_request())
        assert response.status_code == 200
        assert inner.handle_request.call_count == 2


# ===========================================================================
# H14 - AsyncRetryTransport
# ===========================================================================


class TestAsyncRetryTransport:
    """Async mirror of key sync retry transport tests."""

    @pytest.mark.asyncio(loop_scope="function")
    @patch("asyncio.sleep", new_callable=AsyncMock)
    async def test_429_retried_successfully(self, mock_sleep: AsyncMock):
        inner = AsyncMock(spec=httpx.AsyncBaseTransport)
        inner.handle_async_request.side_effect = [
            httpx.Response(429, headers={"retry-after": "0"}),
            httpx.Response(200),
        ]
        config = _make_config()
        transport = AsyncRetryTransport(inner, config)

        response = await transport.handle_async_request(_request())
        assert response.status_code == 200
        assert inner.handle_async_request.call_count == 2

    @pytest.mark.asyncio(loop_scope="function")
    @patch("asyncio.sleep", new_callable=AsyncMock)
    async def test_post_5xx_not_retried(self, mock_sleep: AsyncMock):
        inner = AsyncMock(spec=httpx.AsyncBaseTransport)
        inner.handle_async_request.return_value = httpx.Response(500)
        config = _make_config()
        transport = AsyncRetryTransport(inner, config)

        response = await transport.handle_async_request(_request("POST"))
        assert response.status_code == 500
        assert inner.handle_async_request.call_count == 1
        mock_sleep.assert_not_called()

    @pytest.mark.asyncio(loop_scope="function")
    @patch("asyncio.sleep", new_callable=AsyncMock)
    async def test_connect_error_retried(self, mock_sleep: AsyncMock):
        inner = AsyncMock(spec=httpx.AsyncBaseTransport)
        inner.handle_async_request.side_effect = [
            httpx.ConnectError("refused"),
            httpx.Response(200),
        ]
        config = _make_config(max_retries=3)
        transport = AsyncRetryTransport(inner, config)

        response = await transport.handle_async_request(_request())
        assert response.status_code == 200
        assert inner.handle_async_request.call_count == 2

    @pytest.mark.asyncio(loop_scope="function")
    @patch("asyncio.sleep", new_callable=AsyncMock)
    async def test_connect_error_exhausts_retries(self, mock_sleep: AsyncMock):
        inner = AsyncMock(spec=httpx.AsyncBaseTransport)
        inner.handle_async_request.side_effect = httpx.ConnectError("refused")
        config = _make_config(max_retries=2)
        transport = AsyncRetryTransport(inner, config)

        with pytest.raises(httpx.ConnectError):
            await transport.handle_async_request(_request())

        assert inner.handle_async_request.call_count == 3
        assert mock_sleep.call_count == 2

    @pytest.mark.asyncio(loop_scope="function")
    @patch("asyncio.sleep", new_callable=AsyncMock)
    async def test_connect_error_not_retried_when_disabled(self, mock_sleep: AsyncMock):
        inner = AsyncMock(spec=httpx.AsyncBaseTransport)
        inner.handle_async_request.side_effect = httpx.ConnectError("refused")
        config = _make_config(retry_connection_errors=False)
        transport = AsyncRetryTransport(inner, config)

        with pytest.raises(httpx.ConnectError):
            await transport.handle_async_request(_request())

        assert inner.handle_async_request.call_count == 1
        mock_sleep.assert_not_called()

    @pytest.mark.asyncio(loop_scope="function")
    @patch("asyncio.sleep", new_callable=AsyncMock)
    async def test_post_429_retried(self, mock_sleep: AsyncMock):
        """POST + 429 is always retried, even for non-idempotent methods."""
        inner = AsyncMock(spec=httpx.AsyncBaseTransport)
        inner.handle_async_request.side_effect = [
            httpx.Response(429, headers={"retry-after": "0"}),
            httpx.Response(200),
        ]
        config = _make_config()
        transport = AsyncRetryTransport(inner, config)

        response = await transport.handle_async_request(_request("POST"))
        assert response.status_code == 200
        assert inner.handle_async_request.call_count == 2


# ===========================================================================
# M1 - Jitter on Retry-After
# ===========================================================================


class TestJitter:
    """Verify that Retry-After gets jitter applied (not exact value)."""

    def test_retry_after_jitter_not_exact(self):
        """With Retry-After: 5, the sleep interval should NOT be exactly 5.0."""
        config = RetryConfig(max_interval_ms=30_000)
        # Run multiple times — random.uniform(0,1) should produce non-zero jitter
        results = [_sleep_interval(config, attempt=0, retry_after=5.0) for _ in range(50)]
        # At least some results must differ from 5.0 exactly
        assert any(v != 5.0 for v in results), "Expected jitter to produce values != 5.0"

    def test_retry_after_jitter_in_range(self):
        """Jittered value should be between 5.0 and 6.0 (retry_after + uniform(0,1))."""
        config = RetryConfig(max_interval_ms=30_000)
        for _ in range(100):
            interval = _sleep_interval(config, attempt=0, retry_after=5.0)
            assert 5.0 <= interval <= 6.0, f"Expected 5.0 <= {interval} <= 6.0"

    def test_retry_after_jitter_capped_by_max_interval(self):
        """When max_interval_ms is low, jittered retry_after gets capped."""
        config = RetryConfig(max_interval_ms=3_000)  # 3 seconds cap
        interval = _sleep_interval(config, attempt=0, retry_after=5.0)
        assert interval == 3.0


# ===========================================================================
# max_retries vs max_elapsed_ms interaction
# ===========================================================================


class TestRetryLimits:
    """Verify that max_retries and max_elapsed_ms independently cap retries."""

    @patch("time.sleep")
    def test_max_retries_stops_before_elapsed(self, mock_sleep: MagicMock):
        """max_retries=2, max_elapsed_ms=999999 → stops after 3 total attempts."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.return_value = httpx.Response(429, headers={"retry-after": "0"})
        config = _make_config(max_retries=2, max_elapsed_ms=999_999)
        transport = RetryTransport(inner, config)

        response = transport.handle_request(_request())
        assert response.status_code == 429
        # 1 initial + 2 retries = 3 total
        assert inner.handle_request.call_count == 3

    @patch("time.sleep")
    @patch("time.time")
    def test_max_elapsed_stops_before_retries(self, mock_time: MagicMock, mock_sleep: MagicMock):
        """max_retries=999, max_elapsed_ms=1 → stops due to elapsed time."""
        # Simulate: first call at t=0, second check at t=0.1 (100ms > 1ms)
        mock_time.side_effect = [
            0.0,    # start_ms = 0
            0.0,    # first handle_request → elapsed check: 0ms <= 1ms? Yes, but ...
            0.1,    # second elapsed check after retry: 100ms > 1ms → stop
        ]
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.return_value = httpx.Response(429, headers={"retry-after": "0"})
        config = _make_config(max_retries=999, max_elapsed_ms=1)
        transport = RetryTransport(inner, config)

        response = transport.handle_request(_request())
        assert response.status_code == 429
        # Should stop early due to elapsed time, NOT exhaust 999 retries
        assert inner.handle_request.call_count < 999

    @patch("time.sleep")
    def test_zero_max_retries_no_retry(self, mock_sleep: MagicMock):
        """max_retries=0 → exactly 1 attempt, no retries at all."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.return_value = httpx.Response(429, headers={"retry-after": "0"})
        config = _make_config(max_retries=0)
        transport = RetryTransport(inner, config)

        response = transport.handle_request(_request())
        assert response.status_code == 429
        assert inner.handle_request.call_count == 1
        mock_sleep.assert_not_called()

    @patch("time.sleep")
    def test_connection_error_zero_max_retries(self, mock_sleep: MagicMock):
        """max_retries=0 + ConnectError → raised immediately, no retry."""
        inner = MagicMock(spec=httpx.BaseTransport)
        inner.handle_request.side_effect = httpx.ConnectError("refused")
        config = _make_config(max_retries=0)
        transport = RetryTransport(inner, config)

        with pytest.raises(httpx.ConnectError):
            transport.handle_request(_request())

        assert inner.handle_request.call_count == 1
        mock_sleep.assert_not_called()
