# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SlaGetUptimeMetricsParams"]


class SlaGetUptimeMetricsParams(TypedDict, total=False):
    sla_urn: Required[str]

    end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """ISO-formatted datetime for the end of the evaluation period (e.g.

    2024-01-31, 2024-01-31T23:59:59Z)
    """

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """ISO-formatted datetime for the start of the evaluation period (e.g.

    2024-01-01, 2024-01-15T08:00:00Z)
    """
