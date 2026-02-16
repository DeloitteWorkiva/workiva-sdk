"""Tests for workiva.exceptions."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from workiva.exceptions import (
    OperationCancelled,
    OperationFailed,
    OperationTimeout,
    _detail_str,
)


def _make_detail(**kwargs):
    """Create a SimpleNamespace mimicking an OperationDetail."""
    defaults = {"code": None, "target": None, "message": None}
    defaults.update(kwargs)
    return SimpleNamespace(**defaults)


def _make_operation(op_id="op-123", status="completed", details=None):
    """Create a SimpleNamespace mimicking an Operation."""
    return SimpleNamespace(id=op_id, status=status, details=details)


class TestDetailStr:
    def test_all_fields(self):
        detail = _make_detail(code="ERR_001", target="/files/1", message="not found")
        assert _detail_str(detail) == "[ERR_001] (/files/1) not found"

    def test_all_none(self):
        detail = _make_detail()
        assert _detail_str(detail) == "<no detail>"


class TestOperationFailed:
    def test_with_details(self):
        detail = _make_detail(code="ERR", message="boom")
        op = _make_operation(op_id="op-fail", status="failed", details=[detail])
        exc = OperationFailed(op)
        assert exc.operation is op
        assert len(exc.details) == 1
        assert "op-fail" in str(exc)
        assert "boom" in str(exc)

    def test_without_details(self):
        op = _make_operation(op_id="op-fail", status="failed")
        exc = OperationFailed(op)
        assert exc.details == []
        assert str(exc) == "Operation op-fail failed"

    def test_details_none(self):
        op = _make_operation(op_id="op-x", status="failed", details=None)
        exc = OperationFailed(op)
        assert exc.details == []


class TestOperationCancelled:
    def test_message(self):
        op = _make_operation(op_id="op-cancel", status="cancelled")
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
