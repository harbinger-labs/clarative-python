# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SlaListResponse", "SlaListResponseItem"]


class SlaListResponseItem(BaseModel):
    description: str
    """A description of the SLA"""

    name: str
    """The name of the SLA"""

    urn: str
    """A unique identifier for the SLA"""

    vendor_urn: str
    """A unique identifier for the vendor associated with the SLA"""


SlaListResponse: TypeAlias = List[SlaListResponseItem]
