"""Workiva SDK — convenience wrapper with namespace access and polling.

Usage::

    with Workiva(client_id="...", client_secret="...") as client:
        # Platform APIs
        client.files.get_files()
        client.operations.get_operation_by_id(operation_id="...")

        # Chains API
        client.chains.list_chains()

        # Wdata API
        client.wdata.get_tables()

        # Long-running operations
        response = client.files.copy_file(file_id="abc", file_copy=params)
        operation = client.wait(response).result(timeout=300)
"""

from __future__ import annotations

import importlib
from typing import Any, Optional

import httpx

from workiva._client import BaseClient
from workiva._config import SDKConfig
from workiva._constants import Region
from workiva.polling import OperationPoller, _extract_operation_id, _get_retry_after


class Workiva:
    """Workiva SDK with simplified authentication and namespace access.

    All three APIs (Platform, Chains, Wdata) are accessible via
    attribute namespaces that lazy-load their operation modules.
    """

    # Maps attribute name → (module_path, class_name)
    # Auto-populated from generated namespace files.
    _NAMESPACE_MAP: dict[str, tuple[str, str]] = {
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
        # Chains namespaces (split by OAS tag)
        "chain": ("workiva._operations.chain", "Chain"),
        "dataprep": ("workiva._operations.dataprep", "Dataprep"),
        "execution": ("workiva._operations.execution", "Execution"),
        "workspace": ("workiva._operations.workspace", "Workspace"),
        "environment": ("workiva._operations.environment", "Environment"),
        "security": ("workiva._operations.security", "Security"),
        # Wdata namespaces (split by OAS tag)
        "administrative_tasks": ("workiva._operations.administrative_tasks", "AdministrativeTasks"),
        "connection_management": ("workiva._operations.connection_management", "ConnectionManagement"),
        "folder_management": ("workiva._operations.folder_management", "FolderManagement"),
        "file_management": ("workiva._operations.file_management", "FileManagement"),
        "parameter_management": ("workiva._operations.parameter_management", "ParameterManagement"),
        "pivot_view_management": ("workiva._operations.pivot_view_management", "PivotViewManagement"),
        "query_management": ("workiva._operations.query_management", "QueryManagement"),
        "select_list_management": ("workiva._operations.select_list_management", "SelectListManagement"),
        "shared_table_management": ("workiva._operations.shared_table_management", "SharedTableManagement"),
        "table_management": ("workiva._operations.table_management", "TableManagement"),
        "tag_management": ("workiva._operations.tag_management", "TagManagement"),
        "token_management": ("workiva._operations.token_management", "TokenManagement"),
        "utilities": ("workiva._operations.utilities", "Utilities"),
        "api_health": ("workiva._operations.api_health", "ApiHealth"),
    }

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *,
        region: Region = Region.EU,
        timeout: Optional[float] = None,
        config: Optional[SDKConfig] = None,
        client: Optional[httpx.Client] = None,
        async_client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        if config is None:
            config = SDKConfig(
                region=region,
                timeout_s=timeout,
            )

        self._base_client = BaseClient(
            client_id=client_id,
            client_secret=client_secret,
            config=config,
            client=client,
            async_client=async_client,
        )
        self._config = config

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

    def wait(self, response: Any) -> OperationPoller:
        """Create an :class:`OperationPoller` from an HTTP 202 response.

        Extracts the operation ID from the ``Location`` header and the
        initial polling interval from the ``Retry-After`` header.

        Args:
            response: An httpx.Response or any object with a ``headers`` dict
                      (for backwards compatibility with generated responses).

        Returns:
            An :class:`OperationPoller` ready for ``.result()`` or
            ``.result_async()``.
        """
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
