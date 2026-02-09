"""Shared fixtures for the Workiva SDK test suite."""

from __future__ import annotations

from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from workiva._hooks.clientcredentials import ClientCredentialsHook
from workiva.models.operation import Operation, OperationStatus
from workiva.models.operationdetail import OperationDetail
from workiva.models.getoperationbyidop import GetOperationByIDResponse
from workiva.types import UNSET


@pytest.fixture(autouse=True)
def _clear_oauth_cache():
    """Clear the class-level OAuth token cache between tests."""
    ClientCredentialsHook._sessions.clear()
    ClientCredentialsHook._client_locks.clear()
    yield
    ClientCredentialsHook._sessions.clear()
    ClientCredentialsHook._client_locks.clear()


@pytest.fixture()
def make_operation():
    """Factory that builds an ``Operation`` with sensible defaults."""

    def _factory(
        status: OperationStatus = OperationStatus.COMPLETED,
        op_id: str = "op-123",
        details: Optional[List[OperationDetail]] = UNSET,
    ) -> Operation:
        return Operation(id=op_id, status=status, details=details)

    return _factory


@pytest.fixture()
def make_poll_response(make_operation):
    """Factory that builds a ``GetOperationByIDResponse``."""

    def _factory(
        status: OperationStatus = OperationStatus.STARTED,
        retry_after: Optional[str] = "2",
        op_id: str = "op-123",
    ) -> GetOperationByIDResponse:
        headers: Dict[str, List[str]] = {}
        if retry_after is not None:
            headers["retry-after"] = [retry_after]
        return GetOperationByIDResponse(
            headers=headers,
            result=make_operation(status=status, op_id=op_id),
        )

    return _factory


@pytest.fixture()
def mock_sdk(make_poll_response):
    """A ``MagicMock`` that quacks like the SDK with operations stubbed."""
    sdk = MagicMock()
    # Default: return a STARTED response
    sdk.operations.get_operation_by_id.return_value = make_poll_response(
        status=OperationStatus.STARTED,
    )
    return sdk
