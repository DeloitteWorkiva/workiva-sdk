"""Integration tests: token URL resolves against global server, not operation server.

Bug: Speakeasy generates ``urljoin(hook_ctx.base_url, token_url)`` which resolves
the relative ``/oauth2/token`` against the *operation-specific* server
(e.g. ``h.eu.wdesk.com``).  The token endpoint only exists on the *global*
API server (``api.eu.wdesk.com``), so the SDK must resolve against
``hook_ctx.config.get_server_details()`` instead.

These tests verify that when calling Wdata or Chains operations (which have
their own per-operation servers), the OAuth token request still goes to the
global server configured via ``server_url``.
"""

from __future__ import annotations

import httpx
import pytest

from workiva._hooks.client import Workiva


def _make_token_response(token: str = "tok-test") -> dict:
    return {"access_token": token, "token_type": "bearer", "expires_in": 3600}


class TestTokenUrlResolution:
    """Token requests must resolve against the global server, not op servers."""

    def test_wdata_token_resolves_to_global_server(self):
        """Wdata health_check uses h.eu.wdesk.com, but token must go to server_url."""
        captured: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            captured.append(request)
            if "/oauth2/token" in str(request.url):
                return httpx.Response(200, json=_make_token_response())
            return httpx.Response(
                200,
                json={"status": "ok"},
                headers={"content-type": "application/json"},
            )

        transport = httpx.MockTransport(handler)
        client = Workiva(
            client_id="test-id",
            client_secret="test-secret",
            server_url="https://api.test.wdesk.com",
            client=httpx.Client(transport=transport),
        )

        try:
            client.wdata.health_check()
        except Exception:
            pass  # Response parsing may fail — we only care about the token URL

        token_reqs = [r for r in captured if "/oauth2/token" in str(r.url)]
        assert len(token_reqs) >= 1

        token_url = str(token_reqs[0].url)
        assert token_url == "https://api.test.wdesk.com/oauth2/token", (
            f"Token URL resolved to wrong server: {token_url}"
        )

    def test_chains_token_resolves_to_global_server(self):
        """Chains get_environments uses h.*.wdesk.com, but token must go to server_url."""
        captured: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            captured.append(request)
            if "/oauth2/token" in str(request.url):
                return httpx.Response(200, json=_make_token_response())
            return httpx.Response(
                200,
                json={"environments": []},
                headers={"content-type": "application/json"},
            )

        transport = httpx.MockTransport(handler)
        client = Workiva(
            client_id="test-id",
            client_secret="test-secret",
            server_url="https://api.test.wdesk.com",
            client=httpx.Client(transport=transport),
        )

        try:
            client.chains.get_environments(workspace_id="ws-1")
        except Exception:
            pass

        token_reqs = [r for r in captured if "/oauth2/token" in str(r.url)]
        assert len(token_reqs) >= 1

        token_url = str(token_reqs[0].url)
        assert token_url == "https://api.test.wdesk.com/oauth2/token", (
            f"Token URL resolved to wrong server: {token_url}"
        )

    def test_platform_token_still_works(self):
        """Platform operations use the global server — token URL must still work."""
        captured: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            captured.append(request)
            if "/oauth2/token" in str(request.url):
                return httpx.Response(200, json=_make_token_response())
            return httpx.Response(
                200,
                json={"data": []},
                headers={"content-type": "application/json"},
            )

        transport = httpx.MockTransport(handler)
        client = Workiva(
            client_id="test-id",
            client_secret="test-secret",
            server_url="https://api.test.wdesk.com",
            client=httpx.Client(transport=transport),
        )

        try:
            client.operations.get_operation_by_id(operation_id="op-1")
        except Exception:
            pass

        token_reqs = [r for r in captured if "/oauth2/token" in str(r.url)]
        assert len(token_reqs) >= 1

        token_url = str(token_reqs[0].url)
        assert token_url == "https://api.test.wdesk.com/oauth2/token", (
            f"Token URL resolved to wrong server: {token_url}"
        )
