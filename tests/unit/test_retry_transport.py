"""Tests for workiva._retry.RetryTransport."""

from __future__ import annotations

from unittest.mock import MagicMock

import httpx
import pytest

from workiva._config import RetryConfig
from workiva._retry import (
    AsyncRetryTransport,
    RetryTransport,
    _parse_retry_after,
    _should_retry,
    _sleep_interval,
)


class TestParseRetryAfter:
    def test_numeric_seconds(self):
        resp = httpx.Response(429, headers={"retry-after": "5"})
        assert _parse_retry_after(resp) == 5.0

    def test_float_seconds(self):
        resp = httpx.Response(429, headers={"retry-after": "1.5"})
        assert _parse_retry_after(resp) == 1.5

    def test_missing_header(self):
        resp = httpx.Response(429)
        assert _parse_retry_after(resp) is None

    def test_invalid_value(self):
        resp = httpx.Response(429, headers={"retry-after": "not-a-number"})
        # Falls through to HTTP-date parsing, which also fails → None
        assert _parse_retry_after(resp) is None

    def test_negative_clamped(self):
        resp = httpx.Response(429, headers={"retry-after": "-1"})
        assert _parse_retry_after(resp) == 0.0


class TestShouldRetry:
    def test_429_retries(self):
        config = RetryConfig(status_codes=(429,))
        assert _should_retry(429, config) is True

    def test_200_no_retry(self):
        config = RetryConfig()
        assert _should_retry(200, config) is False

    def test_500_retries_with_default_config(self):
        config = RetryConfig()
        assert _should_retry(500, config) is True

    def test_custom_codes(self):
        config = RetryConfig(status_codes=(502, 503))
        assert _should_retry(502, config) is True
        assert _should_retry(500, config) is False


class TestSleepInterval:
    def test_respects_retry_after(self):
        config = RetryConfig()
        interval = _sleep_interval(config, attempt=0, retry_after=10.0)
        assert interval == 10.0

    def test_caps_retry_after(self):
        config = RetryConfig(max_interval_ms=5000)
        interval = _sleep_interval(config, attempt=0, retry_after=10.0)
        assert interval == 5.0

    def test_exponential_backoff(self):
        config = RetryConfig(initial_interval_ms=1000, exponent=2.0)
        # Attempt 0: 1s * 2^0 + jitter = ~1-2s
        interval = _sleep_interval(config, attempt=0)
        assert 1.0 <= interval <= 2.0
        # Attempt 2: 1s * 2^2 + jitter = ~4-5s
        interval = _sleep_interval(config, attempt=2)
        assert 4.0 <= interval <= 5.0


class TestRetryTransport:
    def test_no_retry_on_success(self):
        inner = MagicMock()
        inner.handle_request.return_value = httpx.Response(200)
        transport = RetryTransport(inner, RetryConfig())

        response = transport.handle_request(httpx.Request("GET", "https://example.com"))
        assert response.status_code == 200
        assert inner.handle_request.call_count == 1

    def test_retries_on_429(self):
        inner = MagicMock()
        inner.handle_request.side_effect = [
            httpx.Response(429, headers={"retry-after": "0"}),
            httpx.Response(200),
        ]
        config = RetryConfig(initial_interval_ms=1, max_elapsed_ms=5000)
        transport = RetryTransport(inner, config)

        response = transport.handle_request(httpx.Request("GET", "https://example.com"))
        assert response.status_code == 200
        assert inner.handle_request.call_count == 2

    def test_returns_last_response_on_timeout(self):
        inner = MagicMock()
        inner.handle_request.return_value = httpx.Response(500)
        config = RetryConfig(initial_interval_ms=1, max_elapsed_ms=1)
        transport = RetryTransport(inner, config)

        response = transport.handle_request(httpx.Request("GET", "https://example.com"))
        assert response.status_code == 500


class TestRegionRouting:
    """Test that region-based URL resolution works correctly."""

    def test_eu_default(self):
        from workiva._constants import Region, _API, get_base_url

        assert get_base_url(_API.PLATFORM, Region.EU) == "https://api.eu.wdesk.com"

    def test_us_region(self):
        from workiva._constants import Region, _API, get_base_url

        assert get_base_url(_API.PLATFORM, Region.US) == "https://api.app.wdesk.com"

    def test_apac_region(self):
        from workiva._constants import Region, _API, get_base_url

        assert get_base_url(_API.PLATFORM, Region.APAC) == "https://api.apac.wdesk.com"

    def test_chains_urls(self):
        from workiva._constants import Region, _API, get_base_url

        assert get_base_url(_API.CHAINS, Region.EU) == "https://h.eu.wdesk.com/s/wdata/oc/api"
        assert get_base_url(_API.CHAINS, Region.US) == "https://h.app.wdesk.com/s/wdata/oc/api"

    def test_wdata_urls(self):
        from workiva._constants import Region, _API, get_base_url

        assert get_base_url(_API.WDATA, Region.EU) == "https://h.eu.wdesk.com/s/wdata/prep"
        assert get_base_url(_API.WDATA, Region.US) == "https://h.app.wdesk.com/s/wdata/prep"

    def test_token_url_resolution(self):
        from workiva._constants import Region, get_token_url

        assert get_token_url(Region.EU) == "https://api.eu.wdesk.com/oauth2/token"
        assert get_token_url(Region.US) == "https://api.app.wdesk.com/oauth2/token"
