"""Workiva SDK — convenience wrapper with namespace access and polling.

Usage::

    with Workiva(client_id="...", client_secret="...") as client:
        # Platform APIs — typed responses
        result = client.files.get_files()  # -> FilesListResult
        client.operations.get_operation_by_id(operation_id="...")

        # Chains API
        client.chains.get_chains()

        # Wdata API
        client.wdata.get_tables()

        # Long-running operations (202)
        response = client.files.copy_file(file_id="abc", destination_container="folder-123")
        operation = client.wait(response).result(timeout=300)
"""

from __future__ import annotations

import asyncio
import importlib
import types
from typing import TYPE_CHECKING, Any, Optional

import httpx

from workiva._client import BaseClient
from workiva._config import RetryConfig, SDKConfig
from workiva._constants import Region
from workiva.polling import OperationPoller, _extract_operation_id, _get_retry_after

if TYPE_CHECKING:
    from workiva.models.platform import Operation

    from workiva._operations.activities import Activities
    from workiva._operations.admin import Admin
    from workiva._operations.chains import Chains
    from workiva._operations.content import Content
    from workiva._operations.documents import Documents
    from workiva._operations.files import Files
    from workiva._operations.graph import Graph
    from workiva._operations.iam import Iam
    from workiva._operations.milestones import Milestones
    from workiva._operations.operations import Operations
    from workiva._operations.permissions import Permissions
    from workiva._operations.presentations import Presentations
    from workiva._operations.reports import Reports
    from workiva._operations.spreadsheets import Spreadsheets
    from workiva._operations.sustainability import Sustainability
    from workiva._operations.tasks import Tasks
    from workiva._operations.test_forms import TestForms
    from workiva._operations.wdata import Wdata


class Workiva:
    """Workiva SDK with simplified authentication and namespace access.

    All three APIs (Platform, Chains, Wdata) are accessible via
    attribute namespaces that lazy-load their operation modules.
    """

    # -- Type annotations for IDE autocompletion (Pylance, Pyright, mypy) ------
    # These are never set at class level; __getattr__ handles lazy-loading.
    activities: Activities
    admin: Admin
    chains: Chains
    content: Content
    documents: Documents
    files: Files
    graph: Graph
    iam: Iam
    milestones: Milestones
    operations: Operations
    permissions: Permissions
    presentations: Presentations
    reports: Reports
    spreadsheets: Spreadsheets
    sustainability: Sustainability
    tasks: Tasks
    test_forms: TestForms
    wdata: Wdata

    # Maps attribute name → (module_path, class_name)
    # Auto-populated from generated namespace files.
    _NAMESPACE_MAP: types.MappingProxyType[str, tuple[str, str]] = types.MappingProxyType({
        # Platform namespaces
        "activities": ("workiva._operations.activities", "Activities"),
        "admin": ("workiva._operations.admin", "Admin"),
        "content": ("workiva._operations.content", "Content"),
        "documents": ("workiva._operations.documents", "Documents"),
        "files": ("workiva._operations.files", "Files"),
        "graph": ("workiva._operations.graph", "Graph"),
        "iam": ("workiva._operations.iam", "Iam"),
        "milestones": ("workiva._operations.milestones", "Milestones"),
        "operations": ("workiva._operations.operations", "Operations"),
        "permissions": ("workiva._operations.permissions", "Permissions"),
        "presentations": ("workiva._operations.presentations", "Presentations"),
        "reports": ("workiva._operations.reports", "Reports"),
        "spreadsheets": ("workiva._operations.spreadsheets", "Spreadsheets"),
        "sustainability": ("workiva._operations.sustainability", "Sustainability"),
        "tasks": ("workiva._operations.tasks", "Tasks"),
        "test_forms": ("workiva._operations.test_forms", "TestForms"),
        # Chains — all OAS tags merged into single namespace
        "chains": ("workiva._operations.chains", "Chains"),
        # Wdata — all OAS tags merged into single namespace
        "wdata": ("workiva._operations.wdata", "Wdata"),
    })

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *,
        region: Region = Region.EU,
        timeout: Optional[float] = None,
        retry: Optional[RetryConfig] = None,
        client: Optional[httpx.Client] = None,
        async_client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        if not client_id or not isinstance(client_id, str):
            raise ValueError("client_id must be a non-empty string")
        if not client_secret or not isinstance(client_secret, str):
            raise ValueError("client_secret must be a non-empty string")

        config = SDKConfig(
            region=region,
            timeout_s=timeout,
            retry=retry or RetryConfig(),
        )

        self._base_client = BaseClient(
            client_id=client_id,
            client_secret=client_secret,
            config=config,
            client=client,
            async_client=async_client,
        )
        self._config = config

    def __repr__(self) -> str:
        region = self._config.region.value
        return f"Workiva(region={region!r})"

    # -- Namespace lazy-loading ------------------------------------------------

    def __getattr__(self, name: str) -> Any:
        if name in self._NAMESPACE_MAP:
            module_path, class_name = self._NAMESPACE_MAP[name]
            module = importlib.import_module(module_path)
            klass = getattr(module, class_name)
            instance = klass(self._base_client)
            setattr(self, name, instance)
            return instance
        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def __dir__(self) -> list[str]:
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._NAMESPACE_MAP.keys())
        return sorted(set(default_attrs + lazy_attrs))

    # -- Polling ---------------------------------------------------------------

    def wait(self, response: httpx.Response) -> OperationPoller:
        """Create an :class:`OperationPoller` from an HTTP 202 response.

        Extracts the operation ID from the ``Location`` header and the
        initial polling interval from the ``Retry-After`` header.

        Args:
            response: The ``httpx.Response`` from a long-running operation
                (copy_file, export_file, etc.) that returned HTTP 202.

        Returns:
            An :class:`OperationPoller` ready for ``.result()`` or
            ``.result_async()``.

        Raises:
            TypeError: If ``response`` is not an ``httpx.Response``.
        """
        if not isinstance(response, httpx.Response):
            actual_type = type(response).__name__
            raise TypeError(
                f"wait() expects an httpx.Response from a 202 operation, "
                f"but got {actual_type}. Only long-running operations "
                f"(copy_file, export_file, etc.) return pollable responses. "
                f"If you used wait=True, the operation already returns an "
                f"Operation directly — no need to call wait()."
            )
        if isinstance(response, httpx.Response):
            headers = dict(response.headers)
            body = None
            try:
                body = response.json()
            except (ValueError, RuntimeError):
                pass
        else:
            headers = getattr(response, "headers", {})
            if not isinstance(headers, dict):
                headers = dict(headers)
            body = getattr(response, "result", None)

        operation_id = _extract_operation_id(headers)
        retry_after = _get_retry_after(headers)
        return OperationPoller(
            client=self,
            operation_id=operation_id,
            initial_retry_after=retry_after,
            response_body=body,
        )

    # -- Batch helpers ---------------------------------------------------------

    async def copy_sheets(
        self,
        *,
        spreadsheet_id: str,
        copies: list[dict[str, Any]],
        wait_timeout: float = 300,
        max_concurrency: int = 10,
    ) -> list[Operation]:
        """Copy multiple sheets concurrently using async (convenience method).

        The Workiva API does not support batch sheet operations, so this
        method launches ``copy_sheet_async`` calls concurrently with a
        semaphore to limit parallelism.

        Each dict in ``copies`` is passed as keyword arguments to
        ``spreadsheets.copy_sheet_async``.  At minimum, each must include
        ``sheet_id`` and ``spreadsheet`` (destination spreadsheet ID).

        Args:
            spreadsheet_id: Source spreadsheet ID.
            copies: List of dicts with per-copy params (sheet_id,
                spreadsheet, sheet_name, sheet_parent, sheet_index).
            wait_timeout: Timeout per individual copy operation.
            max_concurrency: Maximum concurrent copy operations.

        Returns:
            List of completed ``Operation`` objects (one per copy, in
            the same order as ``copies``).

        Example::

            async with Workiva(client_id="...", client_secret="...") as w:
                ops = await w.copy_sheets(
                    spreadsheet_id=sid,
                    copies=[
                        {"sheet_id": tid, "spreadsheet": sid, "sheet_name": "Sheet A"},
                        {"sheet_id": tid, "spreadsheet": sid, "sheet_name": "Sheet B"},
                    ],
                )
        """
        sem = asyncio.Semaphore(max_concurrency)

        async def _copy_one(params: dict[str, Any]) -> Any:
            async with sem:
                return await self.spreadsheets.copy_sheet_async(
                    spreadsheet_id=spreadsheet_id,
                    wait=True,
                    wait_timeout=wait_timeout,
                    **params,
                )

        return list(await asyncio.gather(*[_copy_one(p) for p in copies]))

    # -- Context manager -------------------------------------------------------

    def close(self) -> None:
        """Close all HTTP connections."""
        self._base_client.close()

    async def aclose(self) -> None:
        """Close all async HTTP connections."""
        await self._base_client.aclose()

    def __enter__(self) -> Workiva:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    async def __aenter__(self) -> Workiva:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.aclose()
