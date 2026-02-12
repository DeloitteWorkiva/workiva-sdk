"""Unit tests: operation server ordering matches global SERVERS order.

Bug: Speakeasy reorders path-level servers during generation, placing US at
index 0 in ``*_OP_SERVERS`` lists.  The global ``SERVERS`` array has EU at
index 0.  Since ``server_idx`` applies to both, a mismatch means:

  - User selects EU (server_idx=0)
  - Global server → api.eu.wdesk.com ✓ (token issued for EU)
  - Wdata/Chains OP_SERVERS[0] → h.app.wdesk.com (US) ✗ → 401

``patch_sdk.py`` fixes this by reordering to EU=0, US=1, APAC=2.
These tests catch regressions after SDK regeneration.
"""

from __future__ import annotations

import pytest

from workiva import models
from workiva.sdkconfiguration import SERVERS


def _get_all_op_servers() -> list[tuple[str, list[str]]]:
    """Discover all *_OP_SERVERS lists exported from models."""
    result = []
    for name in dir(models):
        if name.endswith("_OP_SERVERS"):
            value = getattr(models, name)
            if isinstance(value, list) and len(value) == 3:
                result.append((name, value))
    return result


_ALL_OP_SERVERS = _get_all_op_servers()


class TestOperationServerOrder:
    """All ``*_OP_SERVERS`` lists must follow EU=0, US=1, APAC=2."""

    @pytest.mark.parametrize(
        "name,urls",
        _ALL_OP_SERVERS,
        ids=[name for name, _ in _ALL_OP_SERVERS],
    )
    def test_region_order_matches_global(self, name: str, urls: list[str]):
        """OP_SERVERS[i] region must match SERVERS[i] region."""
        assert ".eu." in urls[0], f"{name}[0] should be EU, got: {urls[0]}"
        assert ".app." in urls[1], f"{name}[1] should be US, got: {urls[1]}"
        assert ".apac." in urls[2], f"{name}[2] should be APAC, got: {urls[2]}"

    def test_global_servers_order(self):
        """Sanity: global SERVERS must be EU=0, US=1, APAC=2."""
        assert ".eu." in SERVERS[0], f"SERVERS[0] should be EU, got: {SERVERS[0]}"
        assert ".app." in SERVERS[1], f"SERVERS[1] should be US, got: {SERVERS[1]}"
        assert ".apac." in SERVERS[2], f"SERVERS[2] should be APAC, got: {SERVERS[2]}"

    def test_op_servers_exist(self):
        """There should be OP_SERVERS lists (guard against model restructuring)."""
        assert len(_ALL_OP_SERVERS) > 0, "No *_OP_SERVERS lists found in models"
