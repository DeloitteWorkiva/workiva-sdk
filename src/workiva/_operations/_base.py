"""Base namespace class for generated operation modules."""

from __future__ import annotations

from typing import TYPE_CHECKING

from workiva._constants import _API

if TYPE_CHECKING:
    from workiva._client import BaseClient


class BaseNamespace:
    """Base class for API namespace groups (Files, Chains, Wdata, etc.)."""

    _api: _API = _API.PLATFORM

    def __init__(self, client: "BaseClient") -> None:
        self._client = client
