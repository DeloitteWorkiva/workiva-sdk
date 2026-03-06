"""Tests for the Workiva convenience client."""

from __future__ import annotations

import json

import httpx
import pytest

from workiva.client import Workiva
from workiva._constants import Region
from workiva.polling import OperationPoller


def _make_202_response(
    location: str = "/platform/v1/operations/op-abc",
    retry_after: str = "3",
    body: dict | None = None,
) -> httpx.Response:
    headers = {}
    if location:
        headers["location"] = location
    if retry_after:
        headers["retry-after"] = retry_after
    content = json.dumps(body).encode() if body else b""
    return httpx.Response(202, headers=headers, content=content)


class TestWorkivaInit:
    def test_default_region(self):
        client = Workiva(client_id="id", client_secret="secret")
        assert client._config.region == Region.EU
        client.close()

    def test_custom_region(self):
        client = Workiva(client_id="id", client_secret="secret", region=Region.US)
        assert client._config.region == Region.US
        client.close()

    def test_has_namespace_attrs(self):
        client = Workiva(client_id="id", client_secret="secret")
        d = dir(client)
        assert "files" in d
        assert "operations" in d
        assert "chains" in d
        assert "wdata" in d
        client.close()


class TestWait:
    def test_creates_poller_with_correct_id(self):
        response = _make_202_response(location="/platform/v1/operations/op-abc")
        client = Workiva(client_id="id", client_secret="secret")
        poller = client.wait(response)

        assert isinstance(poller, OperationPoller)
        assert poller.operation_id == "op-abc"
        client.close()

    def test_extracts_retry_after(self):
        response = _make_202_response(location="/operations/op-1", retry_after="5")
        client = Workiva(client_id="id", client_secret="secret")
        poller = client.wait(response)

        assert poller._retry_after == 5.0
        client.close()

    def test_preserves_response_body(self):
        body = {"uploadUrl": "https://upload.example.com"}
        response = _make_202_response(location="/operations/op-1", body=body)
        client = Workiva(client_id="id", client_secret="secret")
        poller = client.wait(response)

        assert poller.response_body == body
        client.close()

    def test_missing_location_raises(self):
        response = _make_202_response(location="", retry_after="")
        client = Workiva(client_id="id", client_secret="secret")

        with pytest.raises(ValueError, match="no 'location' header"):
            client.wait(response)
        client.close()
