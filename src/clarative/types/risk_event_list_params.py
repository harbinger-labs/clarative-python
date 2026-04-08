# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RiskEventListParams"]


class RiskEventListParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter events created on or after this ISO-8601 timestamp"""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter events created before this ISO-8601 timestamp"""

    review_statuses: Optional[List[Literal["PENDING", "VERIFYING", "APPLICABLE", "NOT_APPLICABLE"]]]
    """Filter events by review status (PENDING, VERIFYING, APPLICABLE, NOT_APPLICABLE)"""

    risk_threshold: Optional[Literal["UNASSIGNED", "NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"]]
    """Filter events by minimum risk level"""

    vendor_urn: Optional[str]
    """A vendor's unique identifier"""
