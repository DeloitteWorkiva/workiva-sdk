"""OAuth2 Client Credentials authentication via httpx.Auth.

Token cache is global (ClassVar) with per-client locking to avoid
duplicate token requests across SDK instances in the same process.
"""

from __future__ import annotations

import asyncio
import hashlib
import threading
import time
from dataclasses import dataclass
from typing import Any, AsyncGenerator, ClassVar, Generator, Optional

import httpx

from workiva._constants import API_VERSION
from workiva._errors import WorkivaError


@dataclass
class _CachedToken:
    """A cached OAuth2 token with optional expiry."""

    access_token: str
    expires_at: Optional[float] = None  # epoch seconds, None = never expires

    def is_expired(self, buffer_s: float = 60.0) -> bool:
        """True if the token has expired (or will within *buffer_s* seconds)."""
        if self.expires_at is None:
            return False
        return time.time() + buffer_s >= self.expires_at


class OAuth2ClientCredentials(httpx.Auth):
    """httpx.Auth implementation for OAuth2 client_credentials flow.

    Features:
    - Global token cache keyed by (client_id, client_secret) hash
    - Per-client threading locks (no global lock contention)
    - 60-second expiry buffer (refresh before actual expiry)
    - Automatic 401-retry (httpx.Auth.auth_flow handles this natively)
    - Sync HTTP client for token requests (even in async flows)
    """

    requires_request_body = False
    requires_response_body = False

    # Class-level cache: session_key → CachedToken
    _global_lock: ClassVar[threading.Lock] = threading.Lock()
    _client_locks: ClassVar[dict[str, threading.Lock]] = {}
    _cache: ClassVar[dict[str, _CachedToken]] = {}

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        token_url: str,
        *,
        token_transport: Optional[httpx.BaseTransport] = None,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_url = token_url
        self._token_transport = token_transport
        self._session_key = hashlib.md5(
            f"{client_id}:{client_secret}".encode(),
            usedforsecurity=False,
        ).hexdigest()
        self._token_client: Optional[httpx.Client] = None

    # -- httpx.Auth interface --------------------------------------------------

    def sync_auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        """Sync auth flow — token fetch runs directly (blocking is expected)."""
        token = self._get_or_refresh_token()
        request.headers["Authorization"] = f"Bearer {token}"
        response = yield request

        # If we get a 401, invalidate the cached token and retry once
        if response is not None and response.status_code == 401:
            self._invalidate()
            token = self._get_or_refresh_token()
            request.headers["Authorization"] = f"Bearer {token}"
            yield request

    async def async_auth_flow(
        self, request: httpx.Request
    ) -> AsyncGenerator[httpx.Request, httpx.Response]:
        """Async auth flow — token fetch runs in a thread to avoid blocking."""
        token = await asyncio.to_thread(self._get_or_refresh_token)
        request.headers["Authorization"] = f"Bearer {token}"
        response = yield request

        if response is not None and response.status_code == 401:
            await asyncio.to_thread(self._invalidate)
            token = await asyncio.to_thread(self._get_or_refresh_token)
            request.headers["Authorization"] = f"Bearer {token}"
            yield request

    # -- Token management ------------------------------------------------------

    def _get_client_lock(self) -> threading.Lock:
        with self._global_lock:
            if self._session_key not in self._client_locks:
                self._client_locks[self._session_key] = threading.Lock()
            return self._client_locks[self._session_key]

    def _get_or_refresh_token(self) -> str:
        lock = self._get_client_lock()
        with lock:
            cached = self._cache.get(self._session_key)
            if cached is not None and not cached.is_expired():
                return cached.access_token
            # Token missing or expired — fetch a new one
            new_token = self._fetch_token()
            self._cache[self._session_key] = new_token
            return new_token.access_token

    def _invalidate(self) -> None:
        lock = self._get_client_lock()
        with lock:
            self._cache.pop(self._session_key, None)

    def _fetch_token(self) -> _CachedToken:
        """Make a sync POST to the token endpoint."""
        payload = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }
        if self._token_client is None:
            kwargs: dict[str, Any] = {}
            if self._token_transport is not None:
                kwargs["transport"] = self._token_transport
            self._token_client = httpx.Client(**kwargs)

        resp = self._token_client.post(
            self._token_url,
            data=payload,
            headers={"X-Version": API_VERSION},
        )

        if not (200 <= resp.status_code < 300):
            raise TokenAcquisitionError(
                f"Token request failed with status {resp.status_code}: "
                f"{resp.text[:500]}"
            )

        data = resp.json()
        if data.get("token_type", "").lower() != "bearer":
            raise TokenAcquisitionError(
                f"Unexpected token_type: {data.get('token_type')}"
            )

        access_token = data.get("access_token")
        if not access_token:
            raise TokenAcquisitionError(
                "Token response missing 'access_token' field"
            )

        expires_at = None
        expires_in = data.get("expires_in")
        if isinstance(expires_in, (int, float)) and expires_in > 0:
            expires_at = time.time() + expires_in

        return _CachedToken(
            access_token=access_token,
            expires_at=expires_at,
        )

    # -- Test helpers (not part of public API) ---------------------------------

    @classmethod
    def _clear_cache(cls) -> None:
        """Clear all cached tokens and locks. For testing only."""
        with cls._global_lock:
            cls._cache.clear()
            cls._client_locks.clear()


class TokenAcquisitionError(WorkivaError):
    """Raised when OAuth2 token acquisition fails."""
