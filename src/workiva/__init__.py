"""Workiva Python SDK — Unified client for Platform, Chains, and Wdata APIs.

Models can be imported from their respective submodules::

    from workiva.models.platform import File, Operation
    from workiva.models.chains import ChainResponse
    from workiva.models.wdata import TableDto
"""

from workiva._auth import TokenAcquisitionError
from workiva._constants import Region
from workiva._errors import (
    AuthenticationError,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    ServerError,
    WorkivaAPIError,
)
from workiva._version import __user_agent__, __version__
from workiva.client import Workiva
from workiva.exceptions import OperationCancelled, OperationFailed, OperationTimeout
from workiva.polling import OperationPoller

__all__ = [
    "__version__",
    "Workiva",
    "Region",
    "OperationPoller",
    "OperationFailed",
    "OperationCancelled",
    "OperationTimeout",
    "WorkivaAPIError",
    "AuthenticationError",
    "BadRequestError",
    "ForbiddenError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "ServerError",
    "TokenAcquisitionError",
]
