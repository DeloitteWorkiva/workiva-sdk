"""Base HTTP client for the Workiva SDK.

Wraps ``httpx.Client`` and ``httpx.AsyncClient`` with:
- OAuth2 authentication (via httpx.Auth)
- Retry transport (exponential backoff)
- X-Version header injection
- Region-based URL resolution
- Timeout configuration
"""

from __future__ import annotations

import re
from typing import Any, Optional
from urllib.parse import quote

import httpx
from pydantic import BaseModel as PydanticBaseModel

from workiva._auth import OAuth2ClientCredentials
from workiva._config import SDKConfig
from workiva._constants import API_VERSION, Region, _API, get_base_url, get_token_url
from workiva._errors import raise_for_status
from workiva._retry import AsyncRetryTransport, RetryTransport
from workiva._version import __user_agent__, __version__

# Regex for path template variables: {variableName}
_PATH_PARAM_RE = re.compile(r"\{(\w+)\}")


def _version_header_hook(request: httpx.Request) -> None:
    """Event hook that injects ``X-Version`` on every request (sync client)."""
    request.headers.setdefault("X-Version", API_VERSION)


async def _async_version_header_hook(request: httpx.Request) -> None:
    """Event hook that injects ``X-Version`` on every request (async client)."""
    request.headers.setdefault("X-Version", API_VERSION)


class BaseClient:
    """Low-level HTTP wrapper around httpx.Client + AsyncClient.

    Clients are created lazily on first use to avoid resource leaks —
    only the client you actually use gets created and cleaned up.

    Not intended for direct use — the ``Workiva`` class builds on top.
    """

    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        config: SDKConfig,
        client: Optional[httpx.Client] = None,
        async_client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        self._config = config
        self._client_id = client_id
        self._client_secret = client_secret

        token_url = get_token_url(config.region)
        self._auth = OAuth2ClientCredentials(client_id, client_secret, token_url)

        self._timeout = (
            httpx.Timeout(config.timeout_s)
            if config.timeout_s is not None
            else httpx.Timeout(None)
        )

        # -- Sync client (lazy or supplied) ------------------------------------
        self._client_supplied = client is not None
        self._client: Optional[httpx.Client] = client
        self._client_created = client is not None

        # -- Async client (lazy or supplied) -----------------------------------
        self._async_client_supplied = async_client is not None
        self._async_client: Optional[httpx.AsyncClient] = async_client
        self._async_client_created = async_client is not None

    def _get_sync_client(self) -> httpx.Client:
        """Return the sync client, creating it on first use."""
        if self._client is None:
            transport = RetryTransport(
                httpx.HTTPTransport(), self._config.retry
            )
            self._client = httpx.Client(
                transport=transport,
                auth=self._auth,
                timeout=self._timeout,
                follow_redirects=True,
                event_hooks={"request": [_version_header_hook]},
                headers={"User-Agent": __user_agent__},
            )
            self._client_created = True
        return self._client

    def _get_async_client(self) -> httpx.AsyncClient:
        """Return the async client, creating it on first use."""
        if self._async_client is None:
            async_transport = AsyncRetryTransport(
                httpx.AsyncHTTPTransport(), self._config.retry
            )
            self._async_client = httpx.AsyncClient(
                transport=async_transport,
                auth=self._auth,
                timeout=self._timeout,
                follow_redirects=True,
                event_hooks={"request": [_async_version_header_hook]},
                headers={"User-Agent": __user_agent__},
            )
            self._async_client_created = True
        return self._async_client

    # -- URL building ----------------------------------------------------------

    def _build_url(
        self,
        api: _API,
        path: str,
        path_params: Optional[dict[str, Any]] = None,
    ) -> str:
        """Build a full URL from API, path template, and path params."""
        base = get_base_url(api, self._config.region)
        # Substitute path template variables
        if path_params:
            url_path = _PATH_PARAM_RE.sub(
                lambda m: quote(str(path_params.get(m.group(1), m.group(0))), safe=""),
                path,
            )
        else:
            url_path = path
        return base.rstrip("/") + "/" + url_path.lstrip("/")

    # -- Request helpers -------------------------------------------------------

    def _prepare_request(
        self,
        api: _API,
        path: str,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query_params: Optional[dict[str, Any]] = None,
        json_body: Any = None,
        content: Optional[bytes] = None,
        files: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> tuple[str, dict[str, Any]]:
        """Build URL and request kwargs shared by sync/async paths."""
        url = self._build_url(api, path, path_params)

        if query_params:
            query_params = {k: v for k, v in query_params.items() if v is not None}

        if headers:
            headers = {k: v for k, v in headers.items() if v is not None}
        kwargs: dict[str, Any] = {"headers": headers or {}}
        if json_body is not None:
            if isinstance(json_body, PydanticBaseModel):
                kwargs["json"] = json_body.model_dump(by_alias=True, exclude_none=True)
            else:
                kwargs["json"] = json_body
        elif content is not None:
            kwargs["content"] = content
        elif files is not None:
            kwargs["files"] = files
            if data is not None:
                kwargs["data"] = data
        elif data is not None:
            kwargs["data"] = data
        if query_params:
            kwargs["params"] = query_params
        if timeout is not None:
            kwargs["timeout"] = timeout

        return url, kwargs

    # -- Sync request ----------------------------------------------------------

    def request(
        self,
        method: str,
        api: _API,
        path: str,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query_params: Optional[dict[str, Any]] = None,
        json_body: Any = None,
        content: Optional[bytes] = None,
        files: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> httpx.Response:
        """Execute a sync HTTP request.

        Returns the raw httpx.Response. Raises WorkivaAPIError on non-2xx.
        """
        url, kwargs = self._prepare_request(
            api, path, path_params=path_params, query_params=query_params,
            json_body=json_body, content=content, files=files, data=data,
            headers=headers, timeout=timeout,
        )
        response = self._get_sync_client().request(method, url, **kwargs)
        raise_for_status(response)
        return response

    # -- Async request ---------------------------------------------------------

    async def request_async(
        self,
        method: str,
        api: _API,
        path: str,
        *,
        path_params: Optional[dict[str, Any]] = None,
        query_params: Optional[dict[str, Any]] = None,
        json_body: Any = None,
        content: Optional[bytes] = None,
        files: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> httpx.Response:
        """Execute an async HTTP request.

        Returns the raw httpx.Response. Raises WorkivaAPIError on non-2xx.
        """
        url, kwargs = self._prepare_request(
            api, path, path_params=path_params, query_params=query_params,
            json_body=json_body, content=content, files=files, data=data,
            headers=headers, timeout=timeout,
        )
        response = await self._get_async_client().request(method, url, **kwargs)
        raise_for_status(response)
        return response

    # -- Lifecycle -------------------------------------------------------------

    def close(self) -> None:
        """Close the sync client (if we created it).

        With lazy initialization, the async client is only created if
        async methods were called — and won't exist in sync-only usage.
        """
        if self._client_created and not self._client_supplied and self._client is not None:
            self._client.close()

    async def aclose(self) -> None:
        """Close both clients (if we created them).

        Handles the case where sync methods were used for token
        acquisition before switching to async.
        """
        if self._async_client_created and not self._async_client_supplied and self._async_client is not None:
            await self._async_client.aclose()
        if self._client_created and not self._client_supplied and self._client is not None:
            self._client.close()

    def __enter__(self) -> BaseClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    async def __aenter__(self) -> BaseClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.aclose()
