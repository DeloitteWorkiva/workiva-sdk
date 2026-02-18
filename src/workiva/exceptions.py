"""Custom exceptions for long-running operation polling."""

from __future__ import annotations

from typing import Optional

from workiva.models.platform import Operation, OperationDetail


def _detail_str(detail: OperationDetail) -> str:
    """Format a single OperationDetail into a human-readable string."""
    parts: list[str] = []

    code = detail.code
    if code is not None:
        parts.append(f"[{code}]")

    target = detail.target
    if target is not None:
        parts.append(f"({target})")

    message = detail.message
    if message is not None:
        parts.append(str(message))

    return " ".join(parts) if parts else "<no detail>"


class OperationFailed(Exception):
    """Raised when a polled operation reaches ``status == "failed"``."""

    def __init__(self, operation: Operation) -> None:
        self.operation = operation
        self.details: list[OperationDetail] = self._extract_details(operation)
        super().__init__(self._build_message())

    @staticmethod
    def _extract_details(operation: Operation) -> list[OperationDetail]:
        raw = operation.details
        if raw is None:
            return []
        return list(raw)

    def _build_message(self) -> str:
        op_id = self.operation.id or "unknown"
        if not self.details:
            return f"Operation {op_id} failed"
        detail_lines = [f"  {_detail_str(d)}" for d in self.details]
        return f"Operation {op_id} failed:\n" + "\n".join(detail_lines)


class OperationCancelled(Exception):
    """Raised when a polled operation reaches ``status == "cancelled"``."""

    def __init__(self, operation: Operation) -> None:
        self.operation = operation
        op_id = operation.id or "unknown"
        super().__init__(f"Operation {op_id} was cancelled")


class OperationTimeout(Exception):
    """Raised when polling exceeds the requested timeout."""

    def __init__(
        self,
        operation_id: str,
        timeout: float,
        last_status: Optional[str],
    ) -> None:
        self.operation_id = operation_id
        self.timeout = timeout
        self.last_status = last_status
        super().__init__(
            f"Operation {operation_id} timed out after {timeout}s "
            f"(last status: {last_status or 'unknown'})"
        )
