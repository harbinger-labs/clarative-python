# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["VendorListResponse", "VendorListResponseItem"]


class VendorListResponseItem(BaseModel):
    created_at: datetime
    """An ISO-8601-formatted timestamp representing when the vendor was created (UTC)"""

    description: Optional[str] = None
    """The vendor's description"""

    name: str
    """The vendor's display name"""

    urn: str
    """A unique identifier for the vendor"""

    domains: Optional[List[str]] = None
    """A list of domains associated with the vendor"""


VendorListResponse: TypeAlias = List[VendorListResponseItem]
