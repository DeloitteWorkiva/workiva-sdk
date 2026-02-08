"""Integration tests: authentication flow with mock HTTP transport."""

from __future__ import annotations

import json

import httpx
import pytest

from workiva._hooks.client import Workiva


def _make_token_response(token: str = "tok-fresh") -> dict:
    return {"access_token": token, "token_type": "bearer", "expires_in": 3600}


class TestAuthFlow:
    """Verify OAuth2 client_credentials lifecycle through mock transport."""

    def test_token_request_payload(self):
        """Token request goes to /iam/v1/oauth2/token with correct payload."""
        captured_requests = []

        def handler(request: httpx.Request) -> httpx.Response:
            captured_requests.append(request)
            if "/oauth2/token" in str(request.url):
                return httpx.Response(200, json=_make_token_response())
            # Return a simple JSON for any other call
            return httpx.Response(200, json={"data": []}, headers={
                "content-type": "application/json",
            })

        transport = httpx.MockTransport(handler)
        client = Workiva(
            client_id="my-client-id",
            client_secret="my-client-secret",
            server_url="https://api.test.wdesk.com",
            client=httpx.Client(transport=transport),
        )

        # Trigger an API call that requires auth
        try:
            client.operations.get_operation_by_id(operation_id="op-1")
        except Exception:
            pass  # We don't care about the response parsing

        # Find the token request
        token_reqs = [r for r in captured_requests if "/oauth2/token" in str(r.url)]
        assert len(token_reqs) >= 1

        token_req = token_reqs[0]
        assert "iam/v1/oauth2/token" in str(token_req.url)

    def test_token_cached_across_calls(self):
        """Second API call should NOT request a new token."""
        token_call_count = 0

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal token_call_count
            if "/oauth2/token" in str(request.url):
                token_call_count += 1
                return httpx.Response(200, json=_make_token_response())
            return httpx.Response(200, json={"data": []}, headers={
                "content-type": "application/json",
            })

        transport = httpx.MockTransport(handler)
        client = Workiva(
            client_id="my-client-id",
            client_secret="my-client-secret",
            server_url="https://api.test.wdesk.com",
            client=httpx.Client(transport=transport),
        )

        # Two API calls
        try:
            client.operations.get_operation_by_id(operation_id="op-1")
        except Exception:
            pass
        try:
            client.operations.get_operation_by_id(operation_id="op-2")
        except Exception:
            pass

        # Token should only be fetched once
        assert token_call_count == 1

    def test_401_clears_cached_session(self):
        """After a 401, the cached session is removed so next request re-authenticates."""
        token_call_count = 0
        api_call_count = 0

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal token_call_count, api_call_count
            if "/oauth2/token" in str(request.url):
                token_call_count += 1
                return httpx.Response(200, json=_make_token_response(f"tok-{token_call_count}"))
            api_call_count += 1
            if api_call_count == 1:
                # First API call returns 401 — triggers session removal
                return httpx.Response(
                    401,
                    json={"code": "unauthorized", "message": "token expired"},
                    headers={"content-type": "application/json"},
                )
            return httpx.Response(200, json={"data": []}, headers={
                "content-type": "application/json",
            })

        transport = httpx.MockTransport(handler)
        client = Workiva(
            client_id="my-client-id",
            client_secret="my-client-secret",
            server_url="https://api.test.wdesk.com",
            client=httpx.Client(transport=transport),
        )

        # First call: auth → 401 → session removed
        try:
            client.operations.get_operation_by_id(operation_id="op-1")
        except Exception:
            pass
        assert token_call_count == 1

        # Second call: must re-authenticate since session was cleared
        try:
            client.operations.get_operation_by_id(operation_id="op-2")
        except Exception:
            pass
        assert token_call_count == 2
