"""Tests for the Workiva convenience client."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from workiva._hooks.client import Workiva
from workiva._hooks.polling import OperationPoller


class TestWorkivaInit:
    def test_inherits_from_sdk(self):
        """Workiva should be a subclass of SDK."""
        from workiva.sdk import SDK
        assert issubclass(Workiva, SDK)


class TestWait:
    def test_creates_poller_with_correct_id(self):
        response = MagicMock()
        response.headers = {
            "location": "/platform/v1/operations/op-abc",
            "retry-after": "3",
        }
        response.result = None

        with patch.object(Workiva, "__init__", return_value=None):
            client = Workiva.__new__(Workiva)
            poller = client.wait(response)

        assert isinstance(poller, OperationPoller)
        assert poller.operation_id == "op-abc"

    def test_extracts_retry_after(self):
        response = MagicMock()
        response.headers = {
            "location": "/operations/op-1",
            "retry-after": "5",
        }
        response.result = None

        with patch.object(Workiva, "__init__", return_value=None):
            client = Workiva.__new__(Workiva)
            poller = client.wait(response)

        assert poller._retry_after == 5.0

    def test_preserves_response_body(self):
        response = MagicMock()
        response.headers = {
            "location": "/operations/op-1",
        }
        response.result = {"uploadUrl": "https://upload.example.com"}

        with patch.object(Workiva, "__init__", return_value=None):
            client = Workiva.__new__(Workiva)
            poller = client.wait(response)

        assert poller.response_body == {"uploadUrl": "https://upload.example.com"}

    def test_missing_location_raises(self):
        response = MagicMock()
        response.headers = {}
        response.result = None

        with patch.object(Workiva, "__init__", return_value=None):
            client = Workiva.__new__(Workiva)
            with pytest.raises(ValueError, match="no 'location' header"):
                client.wait(response)
