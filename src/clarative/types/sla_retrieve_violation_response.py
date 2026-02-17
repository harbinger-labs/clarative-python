# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "SlaRetrieveViolationResponse",
    "DataSource",
    "DataSourceAPIStatusPageSlaDataSource",
    "DataSourceAPIMonitorSlaDataSource",
    "DowntimeEvent",
    "EvaluationPeriod",
    "EvaluationPeriodEndMonth",
    "EvaluationPeriodStartMonth",
    "Sla",
    "Vendor",
]


class DataSourceAPIStatusPageSlaDataSource(BaseModel):
    excluded_product_tags: List[str]
    """A list of incident tags that are excluded from the SLA's calculations"""

    included_product_tags: List[str]
    """A list of incident tags that are included in the SLA's calculations"""

    urn: str
    """A unique identifier for the data source"""

    data_source_type: Optional[Literal["STATUS_PAGE"]] = None
    """The type of the data source"""


class DataSourceAPIMonitorSlaDataSource(BaseModel):
    description: Optional[str] = None
    """The monitor's description"""

    name: str
    """The monitor's display name"""

    urn: str
    """A unique identifier for the data source"""

    data_source_type: Optional[Literal["MONITOR"]] = None
    """The type of the data source"""


DataSource: TypeAlias = Union[DataSourceAPIStatusPageSlaDataSource, DataSourceAPIMonitorSlaDataSource]


class DowntimeEvent(BaseModel):
    duration_hours: float
    """The duration of the downtime event in hours"""

    end_time: datetime
    """The end time of the downtime event"""

    name: str
    """The display name of the downtime event"""

    start_time: datetime
    """The start time of the downtime event"""


class EvaluationPeriodEndMonth(BaseModel):
    """The month in which the SLA violation ended. Null if the violation is ongoing."""

    month: int
    """The month number (1-12)"""

    year: int
    """The year of the month"""


class EvaluationPeriodStartMonth(BaseModel):
    """The month in which the SLA violation started"""

    month: int
    """The month number (1-12)"""

    year: int
    """The year of the month"""


class EvaluationPeriod(BaseModel):
    """The evaluation period during which the SLA violation occurred.

    The length of the period is determined by the SLA's configured evaluation window (for example: monthly or quarterly).
    """

    end_month: EvaluationPeriodEndMonth
    """The month in which the SLA violation ended. Null if the violation is ongoing."""

    start_month: EvaluationPeriodStartMonth
    """The month in which the SLA violation started"""


class Sla(BaseModel):
    """The SLA that was violated"""

    description: str
    """A description of the SLA"""

    name: str
    """The name of the SLA"""

    urn: str
    """A unique identifier for the SLA"""

    vendor_urn: str
    """A unique identifier for the vendor associated with the SLA"""


class Vendor(BaseModel):
    """The vendor responsible for the violation"""

    created_at: datetime
    """An ISO-8601-formatted timestamp representing when the vendor was created (UTC)"""

    description: Optional[str] = None
    """The vendor's description"""

    name: str
    """The vendor's display name"""

    urn: str
    """A unique identifier for the vendor"""


class SlaRetrieveViolationResponse(BaseModel):
    allowable_downtime_hours: float
    """
    The total number of allowable downtime hours during the evaluation period, as
    defined by the SLA's terms
    """

    data_source: DataSource
    """The data source used to determine the violation."""

    data_source_type: Literal["STATUS_PAGE", "MONITOR"]
    """The type of data source used to determine the violation."""

    downtime_events: List[DowntimeEvent]
    """
    A list of downtime events that occurred during the evaluation period and
    contributed to the SLA violation
    """

    downtime_hours: float
    """The total number of downtime hours during the evaluation period"""

    evaluation_period: EvaluationPeriod
    """The evaluation period during which the SLA violation occurred.

    The length of the period is determined by the SLA's configured evaluation window
    (for example: monthly or quarterly).
    """

    sla: Sla
    """The SLA that was violated"""

    uptime_percentage: float
    """The percentage of uptime during the evaluation period"""

    urn: str
    """A unique identifier composed of the SLA URN and the evaluation period"""

    vendor: Vendor
    """The vendor responsible for the violation"""
