# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "SlaGetUptimeMetricsResponse",
    "SlaGetUptimeMetricsResponseItem",
    "SlaGetUptimeMetricsResponseItemDowntimeEvent",
    "SlaGetUptimeMetricsResponseItemTimeframe",
]


class SlaGetUptimeMetricsResponseItemDowntimeEvent(BaseModel):
    duration_hours: float
    """The duration of the downtime event in hours"""

    end_time: datetime
    """The end time of the downtime event"""

    name: str
    """The display name of the downtime event"""

    start_time: datetime
    """The start time of the downtime event"""


class SlaGetUptimeMetricsResponseItemTimeframe(BaseModel):
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


class SlaGetUptimeMetricsResponseItem(BaseModel):
    data_source_urn: str
    """The unique identifier of the data source"""

    downtime_events: List[SlaGetUptimeMetricsResponseItemDowntimeEvent]
    """A list of downtime events that occurred during the timeframe"""

    downtime_hours: float
    """The total number of downtime hours during the timeframe"""

    sla_urn: str
    """The unique identifier of the SLA"""

    timeframe: SlaGetUptimeMetricsResponseItemTimeframe
    """The timeframe for which the uptime metrics are calculated"""

    uptime_percentage: float
    """The percentage of uptime during the timeframe"""

    vendor_urn: str
    """The unique identifier of the vendor"""


SlaGetUptimeMetricsResponse: TypeAlias = List[SlaGetUptimeMetricsResponseItem]
