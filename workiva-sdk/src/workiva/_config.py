"""SDK configuration dataclass."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Optional

from workiva._constants import Region


@dataclass(frozen=True)
class RetryConfig:
    """Retry configuration with exponential backoff."""

    initial_interval_ms: int = 500
    max_interval_ms: int = 30_000
    exponent: float = 1.5
    max_elapsed_ms: int = 120_000
    retry_connection_errors: bool = True
    status_codes: tuple[int, ...] = (429, 500, 502, 503, 504)


DEFAULT_RETRY = RetryConfig()


@dataclass
class SDKConfig:
    """Configuration for the Workiva SDK client.

    All fields are resolved at construction time so downstream code never
    needs to call ``get_server_details()``.
    """

    region: Region = Region.EU
    timeout_s: Optional[float] = None
    retry: RetryConfig = field(default_factory=lambda: DEFAULT_RETRY)
    logger: logging.Logger = field(default_factory=lambda: logging.getLogger("workiva"))
