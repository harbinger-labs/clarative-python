# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "SlaRetrieveResponse",
    "SlaDetails",
    "SlaDetailsAPIUptimeSlaDetails",
    "SlaDetailsAPIUptimeSlaDetailsTier",
    "SlaDetailsAPITimeUnderSlaDetails",
    "SlaDetailsAPITimeUnderSlaDetailsTier",
]


class SlaDetailsAPIUptimeSlaDetailsTier(BaseModel):
    availability_percentage: float
    """
    The availability percentage threshold for the tier, modeled as a float between 0
    and 1 (e.g. 0.999 is 99.9% availability)
    """

    credit_unit: str
    """The unit of the credit value (e.g. PERCENT or DAY)"""

    credit_value: float
    """The credit value for the tier (e.g. 0.5 for 50% credit)"""


class SlaDetailsAPIUptimeSlaDetails(BaseModel):
    measurement_period_unit: str
    """The duration unit of the measurement interval (e.g. DAY, MONTH, QUARTER, YEAR)"""

    measurement_period_value: int
    """The number of measurement period units (e.g. 1 for a single calendar quarter)"""

    tiers: List[SlaDetailsAPIUptimeSlaDetailsTier]
    """The credit tiers of the SLA, ordered by availability percentage"""

    sla_type: Optional[Literal["UPTIME"]] = None
    """The type of SLA"""


class SlaDetailsAPITimeUnderSlaDetailsTier(BaseModel):
    availability_percentage: float
    """
    The availability percentage threshold for the tier, modeled as a float between 0
    and 1 (e.g. 0.999 is 99.9% availability)
    """

    credit_unit: str
    """The unit of the credit value (e.g. PERCENT, DAY, or HOUR)"""

    credit_value: float
    """The credit value for the tier (e.g. 0.5 for 50% credit)"""

    per_unit: str
    """The 'per' unit for the time under calculation (e.g. PERCENT or HOUR)"""

    per_value: float
    """The 'per' value for the time under calculation (e.g.

    5% per each 1% below threshold)
    """


class SlaDetailsAPITimeUnderSlaDetails(BaseModel):
    measurement_period_unit: str
    """The duration unit of the measurement interval (e.g. MONTH, QUARTER)"""

    measurement_period_value: int
    """The number of measurement period units (e.g. 1 for a single calendar quarter)"""

    tiers: List[SlaDetailsAPITimeUnderSlaDetailsTier]
    """The credit tiers of the SLA, ordered by availability percentage"""

    sla_type: Optional[Literal["TIME_UNDER"]] = None
    """The type of SLA"""


SlaDetails: TypeAlias = Annotated[
    Union[SlaDetailsAPIUptimeSlaDetails, SlaDetailsAPITimeUnderSlaDetails, None], PropertyInfo(discriminator="sla_type")
]


class SlaRetrieveResponse(BaseModel):
    description: str
    """A description of the SLA"""

    name: str
    """The name of the SLA"""

    urn: str
    """A unique identifier for the SLA"""

    vendor_urn: str
    """A unique identifier for the vendor associated with the SLA"""

    sla_details: Optional[SlaDetails] = None
    """The SLA tier configuration details, including type and credit tiers.

    Null if the SLA does not have incident-based tier rules configured.
    """
