# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["SlaGetUptimeMetricsResponse", "DowntimeEvent", "Metrics", "MetricsDeduplicated", "Timeframe"]


class DowntimeEvent(BaseModel):
    duration_hours: float
    """The duration of the downtime event in hours"""

    end_time: datetime
    """The end time of the downtime event"""

    name: str
    """The display name of the downtime event"""

    start_time: datetime
    """The start time of the downtime event"""


class Metrics(BaseModel):
    """The uptime metrics for the data source during the timeframe"""

    downtime_hours: float
    """The total number of downtime hours during the timeframe"""

    uptime_percentage: float
    """The percentage of uptime during the timeframe"""


class MetricsDeduplicated(BaseModel):
    """
    The uptime metrics for the data source during the timeframe, with overlapping windows of downtime (such as from different incidents that occurred simultaneously) counted only once
    """

    downtime_hours: float
    """The total number of downtime hours during the timeframe"""

    uptime_percentage: float
    """The percentage of uptime during the timeframe"""


class Timeframe(BaseModel):
    """The timeframe for which the uptime metrics are calculated"""

    end: datetime
    """
    The ISO-formatted end datetime of the timeframe for which the metrics are
    calculated
    """

    start: datetime
    """
    The ISO-formatted start datetime of the timeframe for which the metrics are
    calculated
    """


class SlaGetUptimeMetricsResponse(BaseModel):
    data_source_urn: str
    """The unique identifier of the data source"""

    downtime_events: List[DowntimeEvent]
    """A non-deduplicated list of downtime events that occurred during the timeframe"""

    metrics: Metrics
    """The uptime metrics for the data source during the timeframe"""

    metrics_deduplicated: MetricsDeduplicated
    """
    The uptime metrics for the data source during the timeframe, with overlapping
    windows of downtime (such as from different incidents that occurred
    simultaneously) counted only once
    """

    sla_urn: str
    """The unique identifier of the SLA"""

    timeframe: Timeframe
    """The timeframe for which the uptime metrics are calculated"""

    vendor_urn: str
    """The unique identifier of the vendor"""
