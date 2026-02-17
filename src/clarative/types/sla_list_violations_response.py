# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "SlaListViolationsResponse",
    "SlaListViolationsResponseItem",
    "SlaListViolationsResponseItemEvaluationPeriod",
    "SlaListViolationsResponseItemEvaluationPeriodEndMonth",
    "SlaListViolationsResponseItemEvaluationPeriodStartMonth",
]


class SlaListViolationsResponseItemEvaluationPeriodEndMonth(BaseModel):
    """The month in which the SLA violation ended. Null if the violation is ongoing."""

    month: int
    """The month number (1-12)"""

    year: int
    """The year of the month"""


class SlaListViolationsResponseItemEvaluationPeriodStartMonth(BaseModel):
    """The month in which the SLA violation started"""

    month: int
    """The month number (1-12)"""

    year: int
    """The year of the month"""


class SlaListViolationsResponseItemEvaluationPeriod(BaseModel):
    """The evaluation period during which the SLA violation occurred.

    The length of the period is determined by the SLA's configured evaluation window (for example: monthly or quarterly).
    """

    end_month: SlaListViolationsResponseItemEvaluationPeriodEndMonth
    """The month in which the SLA violation ended. Null if the violation is ongoing."""

    start_month: SlaListViolationsResponseItemEvaluationPeriodStartMonth
    """The month in which the SLA violation started"""


class SlaListViolationsResponseItem(BaseModel):
    allowable_downtime_hours: float
    """
    The total number of allowable downtime hours during the evaluation period, as
    defined by the SLA's terms
    """

    data_source_type: Literal["STATUS_PAGE", "MONITOR"]
    """The type of data source used to determine the violation."""

    downtime_hours: float
    """The total number of downtime hours during the evaluation period"""

    evaluation_period: SlaListViolationsResponseItemEvaluationPeriod
    """The evaluation period during which the SLA violation occurred.

    The length of the period is determined by the SLA's configured evaluation window
    (for example: monthly or quarterly).
    """

    uptime_percentage: float
    """The percentage of uptime during the evaluation period"""

    urn: str
    """A unique identifier composed of the SLA URN and the evaluation period"""


SlaListViolationsResponse: TypeAlias = List[SlaListViolationsResponseItem]
