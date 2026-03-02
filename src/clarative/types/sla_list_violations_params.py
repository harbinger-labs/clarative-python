# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SlaListViolationsParams"]


class SlaListViolationsParams(TypedDict, total=False):
    data_source_urn: Optional[str]
    """An SLA data source's unique identifier"""

    end_month: Optional[str]
    """
    Year and month landing within the last SLA evaluation period to include in the
    result, in the format YYYY-MM. Defaults to the current time.
    """

    start_month: str
    """
    Year and month landing within the first SLA evaluation period to include in the
    result, in the format YYYY-MM. Defaults to 2024-01.
    """
