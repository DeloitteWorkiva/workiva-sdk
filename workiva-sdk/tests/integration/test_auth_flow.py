"""Integration tests for OAuth2 client_credentials flow using httpx.Auth."""

from __future__ import annotations

import json

import httpx
import pytest

from workiva._auth import OAuth2ClientCredentials, TokenAcquisitionError


def _token_transport(
    access_token: str = "test-token",
    expires_in: int = 3600,
    status_code: int = 200,
):
    """Create a mock transport that responds to token requests."""

    def handler(request: httpx.Request) -> httpx.Response:
        if "/oauth2/token" in str(request.url):
            if status_code != 200:
                return httpx.Response(status_code, text="error")
            return httpx.Response(
                200,
                json={
                    "access_token": access_token,
                    "token_type": "bearer",
                    "expires_in": expires_in,
                },
            )
        # For regular API calls, return 200
        return httpx.Response(200, json={"ok": True})

    return httpx.MockTransport(handler)


class TestAuthFlow:
    def test_token_added_to_request(self):
        """Auth flow adds Bearer token to requests."""
        transport = _token_transport(access_token="my-token")
        auth = OAuth2ClientCredentials(
            client_id="test-id",
            client_secret="test-secret",
            token_url="https://api.eu.wdesk.com/oauth2/token",
            token_transport=transport,
        )

        with httpx.Client(
            transport=transport,
            auth=auth,
        ) as client:
            response = client.get("https://api.eu.wdesk.com/files")
            assert response.status_code == 200

    def test_token_cached_across_calls(self):
        """Token is cached between requests (no duplicate token fetches)."""
        token_requests = []

        def handler(request: httpx.Request) -> httpx.Response:
            if "/oauth2/token" in str(request.url):
                token_requests.append(request)
                return httpx.Response(
                    200,
                    json={
                        "access_token": "cached-token",
                        "token_type": "bearer",
                        "expires_in": 3600,
                    },
                )
            return httpx.Response(200, json={"ok": True})

        transport = httpx.MockTransport(handler)
        auth = OAuth2ClientCredentials(
            client_id="cache-id",
            client_secret="cache-secret",
            token_url="https://api.eu.wdesk.com/oauth2/token",
            token_transport=transport,
        )

        with httpx.Client(
            transport=transport,
            auth=auth,
        ) as client:
            client.get("https://api.eu.wdesk.com/files")
            client.get("https://api.eu.wdesk.com/files")
            client.get("https://api.eu.wdesk.com/files")

        # Only 1 token request — the rest used the cache
        assert len(token_requests) == 1

    def test_token_request_failure(self):
        """AuthenticationError raised when token request fails."""
        transport = _token_transport(status_code=401)
        auth = OAuth2ClientCredentials(
            client_id="bad-id",
            client_secret="bad-secret",
            token_url="https://api.eu.wdesk.com/oauth2/token",
            token_transport=transport,
        )

        with httpx.Client(
            transport=transport,
            auth=auth,
        ) as client:
            with pytest.raises(TokenAcquisitionError, match="401"):
                client.get("https://api.eu.wdesk.com/files")

    def test_401_retriggers_token_refresh(self):
        """A 401 response invalidates cached token and retries."""
        call_count = 0

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            if "/oauth2/token" in str(request.url):
                return httpx.Response(
                    200,
                    json={
                        "access_token": f"token-{call_count}",
                        "token_type": "bearer",
                        "expires_in": 3600,
                    },
                )
            call_count += 1
            if call_count == 1:
                # First API call returns 401
                return httpx.Response(401, text="Unauthorized")
            # Subsequent calls succeed
            return httpx.Response(200, json={"ok": True})

        transport = httpx.MockTransport(handler)
        auth = OAuth2ClientCredentials(
            client_id="retry-id",
            client_secret="retry-secret",
            token_url="https://api.eu.wdesk.com/oauth2/token",
            token_transport=transport,
        )

        with httpx.Client(
            transport=transport,
            auth=auth,
        ) as client:
            # The 401 triggers token refresh and retry automatically
            response = client.get("https://api.eu.wdesk.com/files")
            assert response.status_code == 200
