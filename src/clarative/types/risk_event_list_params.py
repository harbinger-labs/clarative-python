# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RiskEventListParams"]


class RiskEventListParams(TypedDict, total=False):
    risk_threshold: Optional[Literal["UNASSIGNED", "NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"]]
    """Filter events by minimum risk level"""

    vendor_urn: Optional[str]
    """A vendor's unique identifier"""
