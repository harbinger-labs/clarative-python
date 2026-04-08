# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VendorRetrieveResponse", "Metadata"]


class Metadata(BaseModel):
    name: str
    """The name of the metadata field"""

    type: Literal["TEXT", "SELECT", "MULTI_SELECT"]
    """The type of the metadata field"""

    urn: str
    """A unique identifier for the metadata field"""

    value: Optional[object] = None
    """The value of the metadata field"""


class VendorRetrieveResponse(BaseModel):
    created_at: datetime
    """An ISO-8601-formatted timestamp representing when the vendor was created (UTC)"""

    description: Optional[str] = None
    """The vendor's description"""

    lifecycle_stage: Literal["INITIAL_ASSESSMENT", "ONBOARDED"]
    """The vendor's current lifecycle stage"""

    name: str
    """The vendor's display name"""

    urn: str
    """A unique identifier for the vendor"""

    metadata: Optional[List[Metadata]] = None
    """A list of custom metadata fields associated with the vendor"""
