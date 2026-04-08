# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["VendorListParams"]


class VendorListParams(TypedDict, total=False):
    lifecycle_stage: Optional[Literal["INITIAL_ASSESSMENT", "ONBOARDED"]]
    """Filter vendors by lifecycle stage"""
