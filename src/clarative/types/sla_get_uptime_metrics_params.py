# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SlaGetUptimeMetricsParams"]


class SlaGetUptimeMetricsParams(TypedDict, total=False):
    sla_urn: Required[str]

    end: Required[str]
    """
    Year and month landing within the last SLA evaluation period to include in the
    result, in the format YYYY-MM
    """

    start: Required[str]
    """
    Year and month landing within the first SLA evaluation period to include in the
    result, in the format YYYY-MM
    """
