# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["VendorRetrieveResponse"]


class VendorRetrieveResponse(BaseModel):
    created_at: datetime
    """An ISO-8601-formatted timestamp representing when the vendor was created (UTC)"""

    description: Optional[str] = None
    """The vendor's description"""

    name: str
    """The vendor's display name"""

    urn: str
    """A unique identifier for the vendor"""
