"""Tests for the Workiva convenience client."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from workiva.client import Workiva
from workiva._constants import Region
from workiva.polling import OperationPoller


class TestWorkivaInit:
    def test_default_region(self):
        """Workiva defaults to EU region."""
        client = Workiva(client_id="id", client_secret="secret")
        assert client._config.region == Region.EU
        client.close()

    def test_custom_region(self):
        """Workiva accepts a custom region."""
        client = Workiva(client_id="id", client_secret="secret", region=Region.US)
        assert client._config.region == Region.US
        client.close()

    def test_has_namespace_attrs(self):
        """Workiva exposes namespace attributes."""
        client = Workiva(client_id="id", client_secret="secret")
        d = dir(client)
        assert "files" in d
        assert "operations" in d
        assert "chains" in d
        assert "wdata" in d
        client.close()


class TestWait:
    def test_creates_poller_with_correct_id(self):
        response = SimpleNamespace(
            headers={"location": "/platform/v1/operations/op-abc", "retry-after": "3"},
            result=None,
        )
        client = Workiva(client_id="id", client_secret="secret")
        poller = client.wait(response)

        assert isinstance(poller, OperationPoller)
        assert poller.operation_id == "op-abc"
        client.close()

    def test_extracts_retry_after(self):
        response = SimpleNamespace(
            headers={"location": "/operations/op-1", "retry-after": "5"},
            result=None,
        )
        client = Workiva(client_id="id", client_secret="secret")
        poller = client.wait(response)

        assert poller._retry_after == 5.0
        client.close()

    def test_preserves_response_body(self):
        response = SimpleNamespace(
            headers={"location": "/operations/op-1"},
            result={"uploadUrl": "https://upload.example.com"},
        )
        client = Workiva(client_id="id", client_secret="secret")
        poller = client.wait(response)

        assert poller.response_body == {"uploadUrl": "https://upload.example.com"}
        client.close()

    def test_missing_location_raises(self):
        response = SimpleNamespace(headers={}, result=None)
        client = Workiva(client_id="id", client_secret="secret")

        with pytest.raises(ValueError, match="no 'location' header"):
            client.wait(response)
        client.close()
