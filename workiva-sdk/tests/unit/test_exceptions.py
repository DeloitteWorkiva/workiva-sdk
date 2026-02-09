"""Tests for workiva._hooks.exceptions."""

from __future__ import annotations

import pytest

from workiva._hooks.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
    _detail_str,
)
from workiva.models.operation import Operation, OperationStatus
from workiva.models.operationdetail import OperationDetail
from workiva.types import UNSET, UNSET_SENTINEL


class TestDetailStr:
    def test_all_fields(self):
        detail = OperationDetail(code="ERR_001", target="/files/1", message="not found")
        assert _detail_str(detail) == "[ERR_001] (/files/1) not found"

    def test_all_none(self):
        detail = OperationDetail(code=None, target=None, message=None)
        assert _detail_str(detail) == "<no detail>"

    def test_none_and_sentinel(self):
        detail = OperationDetail(code=None, target=UNSET_SENTINEL, message=None)
        assert _detail_str(detail) == "<no detail>"


class TestOperationFailed:
    def test_with_details(self):
        detail = OperationDetail(code="ERR", message="boom")
        op = Operation(
            id="op-fail",
            status=OperationStatus.FAILED,
            details=[detail],
        )
        exc = OperationFailed(op)
        assert exc.operation is op
        assert len(exc.details) == 1
        assert "op-fail" in str(exc)
        assert "boom" in str(exc)

    def test_without_details(self):
        op = Operation(id="op-fail", status=OperationStatus.FAILED)
        exc = OperationFailed(op)
        assert exc.details == []
        assert str(exc) == "Operation op-fail failed"

    def test_details_none(self):
        op = Operation(id="op-x", status=OperationStatus.FAILED, details=None)
        exc = OperationFailed(op)
        assert exc.details == []


class TestOperationCancelled:
    def test_message(self):
        op = Operation(id="op-cancel", status=OperationStatus.CANCELLED)
        exc = OperationCancelled(op)
        assert exc.operation is op
        assert "op-cancel" in str(exc)
        assert "cancelled" in str(exc)


class TestOperationTimeout:
    def test_with_last_status(self):
        exc = OperationTimeout("op-slow", 30.0, "started")
        assert exc.operation_id == "op-slow"
        assert exc.timeout == 30.0
        assert exc.last_status == "started"
        assert "30" in str(exc)
        assert "started" in str(exc)

    def test_without_last_status(self):
        exc = OperationTimeout("op-x", 60.0, None)
        assert "unknown" in str(exc)
