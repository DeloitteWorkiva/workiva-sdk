"""Retry transport for httpx — exponential backoff with jitter.

Implements retry as an httpx transport wrapper so it's transparent to
both sync and async clients.
"""

from __future__ import annotations

import asyncio
import random
import time
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import Optional

import httpx

from workiva._config import RetryConfig


def _parse_retry_after(response: httpx.Response) -> Optional[float]:
    """Parse Retry-After header → seconds, or None.

    Supports both integer/float seconds and HTTP-date formats.
    """
    value = response.headers.get("retry-after")
    if not value:
        return None

    # Try numeric seconds first
    try:
        return max(0.0, float(value))
    except ValueError:
        pass

    # Try HTTP-date
    try:
        retry_date = parsedate_to_datetime(value)
        delta = (retry_date - datetime.now(retry_date.tzinfo)).total_seconds()
        return max(0.0, delta)
    except (ValueError, TypeError):
        pass

    return None


def _should_retry(status_code: int, config: RetryConfig) -> bool:
    """Check if the status code matches any retry-eligible code."""
    return status_code in config.status_codes


def _sleep_interval(
    config: RetryConfig,
    attempt: int,
    retry_after: Optional[float] = None,
) -> float:
    """Calculate the sleep interval for a retry attempt.

    Uses Retry-After header if present, otherwise exponential backoff with
    jitter. Capped at max_interval_ms.
    """
    if retry_after is not None and retry_after > 0:
        return min(retry_after, config.max_interval_ms / 1000)

    interval_s = (config.initial_interval_ms / 1000) * (
        config.exponent**attempt
    ) + random.uniform(0, 1)
    return min(interval_s, config.max_interval_ms / 1000)


class RetryTransport(httpx.BaseTransport):
    """Sync transport wrapper that retries on configured status codes."""

    def __init__(
        self,
        transport: httpx.BaseTransport,
        config: RetryConfig,
    ) -> None:
        self._transport = transport
        self._config = config

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        start_ms = round(time.time() * 1000)
        attempt = 0

        while True:
            try:
                response = self._transport.handle_request(request)
            except (httpx.ConnectError, httpx.TimeoutException):
                if not self._config.retry_connection_errors:
                    raise
                elapsed = round(time.time() * 1000) - start_ms
                if elapsed > self._config.max_elapsed_ms:
                    raise
                sleep = _sleep_interval(self._config, attempt)
                time.sleep(sleep)
                attempt += 1
                continue

            if not _should_retry(response.status_code, self._config):
                return response

            elapsed = round(time.time() * 1000) - start_ms
            if elapsed > self._config.max_elapsed_ms:
                return response

            retry_after = _parse_retry_after(response)
            response.close()  # release the connection back to the pool
            sleep = _sleep_interval(self._config, attempt, retry_after)
            time.sleep(sleep)
            attempt += 1

    def close(self) -> None:
        self._transport.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async transport wrapper that retries on configured status codes."""

    def __init__(
        self,
        transport: httpx.AsyncBaseTransport,
        config: RetryConfig,
    ) -> None:
        self._transport = transport
        self._config = config

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        start_ms = round(time.time() * 1000)
        attempt = 0

        while True:
            try:
                response = await self._transport.handle_async_request(request)
            except (httpx.ConnectError, httpx.TimeoutException):
                if not self._config.retry_connection_errors:
                    raise
                elapsed = round(time.time() * 1000) - start_ms
                if elapsed > self._config.max_elapsed_ms:
                    raise
                sleep = _sleep_interval(self._config, attempt)
                await asyncio.sleep(sleep)
                attempt += 1
                continue

            if not _should_retry(response.status_code, self._config):
                return response

            elapsed = round(time.time() * 1000) - start_ms
            if elapsed > self._config.max_elapsed_ms:
                return response

            retry_after = _parse_retry_after(response)
            await response.aclose()  # release the connection back to the pool
            sleep = _sleep_interval(self._config, attempt, retry_after)
            await asyncio.sleep(sleep)
            attempt += 1

    async def aclose(self) -> None:
        await self._transport.aclose()
