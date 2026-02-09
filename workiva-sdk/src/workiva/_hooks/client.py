"""Convenience wrapper for the Workiva SDK.

This file lives in _hooks/ which Speakeasy preserves across regenerations.
"""

from __future__ import annotations

from workiva import models
from workiva._hooks.polling import OperationPoller, _extract_operation_id, _get_retry_after
from workiva.sdk import SDK


class Workiva(SDK):
    """Workiva SDK with simplified authentication.

    Usage:
        with Workiva(client_id="...", client_secret="...") as client:
            client.activities.get_organization_activities()
            client.wdata.get_tables()
            client.chains.get_chains()

    Long-running operations::

        response = client.files.copy_file(file_id="abc", file_copy=params)
        operation = client.wait(response).result(timeout=300)
    """

    def __init__(self, client_id: str, client_secret: str, **kwargs):
        super().__init__(
            security=models.Security(
                client_id=client_id,
                client_secret=client_secret,
            ),
            **kwargs,
        )

    def wait(self, response) -> OperationPoller:
        """Create an :class:`OperationPoller` from an HTTP 202 response.

        Extracts the operation ID from the ``Location`` header and the
        initial polling interval from the ``Retry-After`` header.

        Args:
            response: Any SDK response object that has a ``headers`` dict
                      (and optionally a ``result`` body).

        Returns:
            An :class:`OperationPoller` ready for ``.result()`` or
            ``.result_async()``.
        """
        headers = response.headers
        operation_id = _extract_operation_id(headers)
        retry_after = _get_retry_after(headers)
        response_body = getattr(response, "result", None)
        return OperationPoller(
            sdk=self,
            operation_id=operation_id,
            initial_retry_after=retry_after,
            response_body=response_body,
        )
