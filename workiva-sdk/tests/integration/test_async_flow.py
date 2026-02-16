"""Integration tests for the full async request pipeline.

Covers: auth flow, response handling, X-Version header injection,
retry transport on 429, and 401 → token refresh.

All token fetches are SYNC (via httpx.MockTransport) because
OAuth2ClientCredentials always uses a sync HTTP client internally —
even in async flows it runs via ``asyncio.to_thread``.
"""

from __future__ import annotations

import json

import httpx
import pytest

from workiva._auth import OAuth2ClientCredentials, TokenAcquisitionError
from workiva._client import BaseClient, _async_version_header_hook
from workiva._config import RetryConfig, SDKConfig
from workiva._constants import API_VERSION, Region, _API
from workiva._retry import AsyncRetryTransport


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

TOKEN_URL = "https://api.eu.wdesk.com/oauth2/token"


def _make_token_handler(
    access_token: str = "async-test-token",
    expires_in: int = 3600,
    status_code: int = 200,
):
    """Return a sync handler that serves token responses.

    This handler is used with ``httpx.MockTransport`` which is passed as
    ``token_transport`` to ``OAuth2ClientCredentials`` (always sync).
    """

    def handler(request: httpx.Request) -> httpx.Response:
        if status_code != 200:
            return httpx.Response(status_code, text="token error")
        return httpx.Response(
            200,
            json={
                "access_token": access_token,
                "token_type": "bearer",
                "expires_in": expires_in,
            },
        )

    return handler


def _make_api_handler(
    response_json: dict | None = None,
    status_code: int = 200,
):
    """Return an async-compatible handler for API calls (non-token)."""
    body = response_json or {"ok": True}

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code, json=body)

    return handler


def _build_async_client(
    *,
    token_access_token: str = "async-test-token",
    token_expires_in: int = 3600,
    api_handler=None,
    token_handler=None,
    retry_config: RetryConfig | None = None,
) -> tuple[BaseClient, OAuth2ClientCredentials]:
    """Build a BaseClient wired with mock transports for async testing.

    Returns (client, auth) so tests can inspect the auth object if needed.

    The token transport is always sync (``httpx.MockTransport``).
    The API transport is async (``httpx.MockTransport`` works for both).
    """
    # Token transport — sync, used by OAuth2ClientCredentials._fetch_token
    if token_handler is None:
        token_handler = _make_token_handler(
            access_token=token_access_token,
            expires_in=token_expires_in,
        )
    token_transport = httpx.MockTransport(token_handler)

    auth = OAuth2ClientCredentials(
        client_id="test-id",
        client_secret="test-secret",
        token_url=TOKEN_URL,
        token_transport=token_transport,
    )

    # API transport — used by the async client for actual API requests
    if api_handler is None:
        api_handler = _make_api_handler()

    api_transport: httpx.AsyncBaseTransport = httpx.MockTransport(api_handler)

    # Wrap with retry transport if config provided
    if retry_config is not None:
        api_transport = AsyncRetryTransport(api_transport, retry_config)

    async_client = httpx.AsyncClient(
        transport=api_transport,
        auth=auth,
        timeout=httpx.Timeout(None),
        follow_redirects=True,
        event_hooks={"request": [_async_version_header_hook]},
    )

    config = SDKConfig(region=Region.EU)
    client = BaseClient(
        client_id="test-id",
        client_secret="test-secret",
        config=config,
        async_client=async_client,
    )

    return client, auth


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestAsyncAuthFlow:
    """Async auth flow adds Bearer token to requests."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_bearer_token_added(self):
        """Auth flow injects Authorization: Bearer header on async requests."""
        captured_requests: list[httpx.Request] = []

        def api_handler(request: httpx.Request) -> httpx.Response:
            captured_requests.append(request)
            return httpx.Response(200, json={"ok": True})

        client, _ = _build_async_client(
            token_access_token="my-async-token",
            api_handler=api_handler,
        )

        async with client:
            response = await client.request_async(
                "GET", _API.PLATFORM, "/api/v1/files"
            )

        assert response.status_code == 200
        assert len(captured_requests) == 1
        assert captured_requests[0].headers["Authorization"] == "Bearer my-async-token"

    @pytest.mark.asyncio(loop_scope="function")
    async def test_token_cached_across_async_calls(self):
        """Token is fetched once and cached across multiple async requests."""
        token_fetch_count = 0

        def token_handler(request: httpx.Request) -> httpx.Response:
            nonlocal token_fetch_count
            token_fetch_count += 1
            return httpx.Response(
                200,
                json={
                    "access_token": "cached-async-token",
                    "token_type": "bearer",
                    "expires_in": 3600,
                },
            )

        client, _ = _build_async_client(token_handler=token_handler)

        async with client:
            await client.request_async("GET", _API.PLATFORM, "/api/v1/files")
            await client.request_async("GET", _API.PLATFORM, "/api/v1/files")
            await client.request_async("GET", _API.PLATFORM, "/api/v1/files")

        assert token_fetch_count == 1


class TestAsyncResponse:
    """Async request returns response correctly."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_json_response_body(self):
        """Async request returns the expected JSON response body."""
        expected = {"id": "file-123", "name": "report.xlsx"}

        client, _ = _build_async_client(
            api_handler=_make_api_handler(response_json=expected),
        )

        async with client:
            response = await client.request_async(
                "GET", _API.PLATFORM, "/api/v1/files/{file_id}",
                path_params={"file_id": "file-123"},
            )

        assert response.status_code == 200
        assert response.json() == expected

    @pytest.mark.asyncio(loop_scope="function")
    async def test_post_with_json_body(self):
        """Async POST sends JSON body and receives response."""
        captured: list[httpx.Request] = []

        def api_handler(request: httpx.Request) -> httpx.Response:
            captured.append(request)
            return httpx.Response(201, json={"id": "new-file"})

        client, _ = _build_async_client(api_handler=api_handler)

        async with client:
            response = await client.request_async(
                "POST", _API.PLATFORM, "/api/v1/files",
                json_body={"name": "new.xlsx"},
            )

        assert response.status_code == 201
        assert response.json() == {"id": "new-file"}
        # Verify the body was sent
        body = json.loads(captured[0].content.decode())
        assert body == {"name": "new.xlsx"}

    @pytest.mark.asyncio(loop_scope="function")
    async def test_query_params_forwarded(self):
        """Async request forwards query parameters."""
        captured: list[httpx.Request] = []

        def api_handler(request: httpx.Request) -> httpx.Response:
            captured.append(request)
            return httpx.Response(200, json={"ok": True})

        client, _ = _build_async_client(api_handler=api_handler)

        async with client:
            await client.request_async(
                "GET", _API.PLATFORM, "/api/v1/files",
                query_params={"limit": 10, "offset": 0},
            )

        assert "limit=10" in str(captured[0].url)
        assert "offset=0" in str(captured[0].url)


class TestAsyncVersionHeader:
    """Async event hook injects X-Version header."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_x_version_header_injected(self):
        """The _async_version_header_hook adds X-Version to every request."""
        captured: list[httpx.Request] = []

        def api_handler(request: httpx.Request) -> httpx.Response:
            captured.append(request)
            return httpx.Response(200, json={"ok": True})

        client, _ = _build_async_client(api_handler=api_handler)

        async with client:
            await client.request_async("GET", _API.PLATFORM, "/api/v1/files")

        assert len(captured) == 1
        assert captured[0].headers["X-Version"] == API_VERSION

    @pytest.mark.asyncio(loop_scope="function")
    async def test_x_version_not_overwritten_if_present(self):
        """If X-Version is already set, the hook does not overwrite it."""
        captured: list[httpx.Request] = []

        def api_handler(request: httpx.Request) -> httpx.Response:
            captured.append(request)
            return httpx.Response(200, json={"ok": True})

        client, _ = _build_async_client(api_handler=api_handler)

        async with client:
            await client.request_async(
                "GET", _API.PLATFORM, "/api/v1/files",
                headers={"X-Version": "2099-12-31"},
            )

        assert len(captured) == 1
        assert captured[0].headers["X-Version"] == "2099-12-31"


class TestAsyncRetryOn429:
    """Async retry transport retries on 429 Too Many Requests."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_retry_on_429_with_retry_after(self):
        """429 with Retry-After header triggers retry and eventually succeeds."""
        call_count = 0

        def api_handler(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            if call_count <= 2:
                return httpx.Response(
                    429,
                    json={"error": "rate limited"},
                    headers={"Retry-After": "0"},
                )
            return httpx.Response(200, json={"ok": True})

        # Fast retry config for testing — no real delays
        retry_config = RetryConfig(
            initial_interval_ms=1,
            max_interval_ms=10,
            max_elapsed_ms=5_000,
            status_codes=(429,),
        )

        client, _ = _build_async_client(
            api_handler=api_handler,
            retry_config=retry_config,
        )

        async with client:
            response = await client.request_async(
                "GET", _API.PLATFORM, "/api/v1/files",
            )

        assert response.status_code == 200
        assert response.json() == {"ok": True}
        # Two 429s + one 200 = 3 calls
        assert call_count == 3

    @pytest.mark.asyncio(loop_scope="function")
    async def test_retry_exhausted_returns_last_response(self):
        """When retries are exhausted, the last 429 response is returned
        and raise_for_status raises RateLimitError."""
        from workiva._errors import RateLimitError

        call_count = 0

        def api_handler(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            return httpx.Response(
                429,
                json={"error": {"message": "rate limited"}},
                headers={"Retry-After": "0"},
            )

        # Very short max_elapsed so it gives up quickly
        retry_config = RetryConfig(
            initial_interval_ms=1,
            max_interval_ms=5,
            max_elapsed_ms=50,
            status_codes=(429,),
        )

        client, _ = _build_async_client(
            api_handler=api_handler,
            retry_config=retry_config,
        )

        async with client:
            with pytest.raises(RateLimitError) as exc_info:
                await client.request_async(
                    "GET", _API.PLATFORM, "/api/v1/files",
                )

        assert exc_info.value.status_code == 429
        # Must have retried at least once
        assert call_count >= 2


class TestAsync401TokenRefresh:
    """Async 401 triggers token refresh via httpx.Auth.async_auth_flow."""

    @pytest.mark.asyncio(loop_scope="function")
    async def test_401_triggers_token_refresh(self):
        """A 401 from the API invalidates the cached token, refreshes, and retries."""
        api_call_count = 0
        token_fetch_count = 0

        def token_handler(request: httpx.Request) -> httpx.Response:
            nonlocal token_fetch_count
            token_fetch_count += 1
            return httpx.Response(
                200,
                json={
                    "access_token": f"token-v{token_fetch_count}",
                    "token_type": "bearer",
                    "expires_in": 3600,
                },
            )

        def api_handler(request: httpx.Request) -> httpx.Response:
            nonlocal api_call_count
            api_call_count += 1
            if api_call_count == 1:
                # First API call returns 401 — triggers refresh
                return httpx.Response(401, text="Unauthorized")
            return httpx.Response(200, json={"ok": True})

        client, _ = _build_async_client(
            token_handler=token_handler,
            api_handler=api_handler,
        )

        async with client:
            response = await client.request_async(
                "GET", _API.PLATFORM, "/api/v1/files",
            )

        # The retry after 401 should succeed
        assert response.status_code == 200
        assert response.json() == {"ok": True}
        # Token fetched once initially, then again after 401 invalidation
        assert token_fetch_count == 2
        # Two API calls: first 401, second 200
        assert api_call_count == 2

    @pytest.mark.asyncio(loop_scope="function")
    async def test_401_refresh_uses_new_token(self):
        """After a 401 refresh, the retried request uses the NEW token."""
        token_fetch_count = 0
        captured_auth_headers: list[str] = []

        def token_handler(request: httpx.Request) -> httpx.Response:
            nonlocal token_fetch_count
            token_fetch_count += 1
            return httpx.Response(
                200,
                json={
                    "access_token": f"token-{token_fetch_count}",
                    "token_type": "bearer",
                    "expires_in": 3600,
                },
            )

        api_call_count = 0

        def api_handler(request: httpx.Request) -> httpx.Response:
            nonlocal api_call_count
            api_call_count += 1
            captured_auth_headers.append(request.headers.get("Authorization", ""))
            if api_call_count == 1:
                return httpx.Response(401, text="Unauthorized")
            return httpx.Response(200, json={"ok": True})

        client, _ = _build_async_client(
            token_handler=token_handler,
            api_handler=api_handler,
        )

        async with client:
            await client.request_async("GET", _API.PLATFORM, "/api/v1/files")

        # First request used token-1, retry after 401 used token-2
        assert captured_auth_headers[0] == "Bearer token-1"
        assert captured_auth_headers[1] == "Bearer token-2"
