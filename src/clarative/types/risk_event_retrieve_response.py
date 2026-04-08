# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RiskEventRetrieveResponse", "AIRiskLevelRecommendation", "Vendor"]


class AIRiskLevelRecommendation(BaseModel):
    """AI's risk level recommendation for this event, if available.

    AI recommendations are made automatically, shortly after a risk event is discovered.
    """

    explanation: str
    """The explanation for the AI's risk level recommendation"""

    recommended_risk_level: Literal["UNASSIGNED", "NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
    """The AI-recommended risk level for the event"""


class Vendor(BaseModel):
    """Details about the vendor associated with this risk event."""

    created_at: datetime
    """An ISO-8601-formatted timestamp representing when the vendor was created (UTC)"""

    description: Optional[str] = None
    """The vendor's description"""

    name: str
    """The vendor's display name"""

    urn: str
    """A unique identifier for the vendor"""


class RiskEventRetrieveResponse(BaseModel):
    ai_risk_level_recommendation: Optional[AIRiskLevelRecommendation] = None
    """AI's risk level recommendation for this event, if available.

    AI recommendations are made automatically, shortly after a risk event is
    discovered.
    """

    created_at: datetime
    """
    An ISO-8601-formatted timestamp representing when the risk event was created
    (UTC)
    """

    description: Optional[str] = None
    """The risk event's description"""

    name: str
    """The risk event's display name"""

    review_status: Literal["PENDING", "VERIFYING", "APPLICABLE", "NOT_APPLICABLE"]
    """
    The current review status of the risk event, representing where it is in the
    triage process.
    """

    risk_level: Literal["UNASSIGNED", "NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
    """The finalized, user-determined risk level for the event (if set)"""

    source_type: Literal["STATUS_PAGE", "MONITOR", "NEWS", "SEC_FILING"]
    """The type of the risk event"""

    url: Optional[str] = None
    """A URL with more information about the risk event"""

    urn: str
    """A unique identifier for the risk event"""

    vendor: Vendor
    """Details about the vendor associated with this risk event."""

    category_tags: Optional[List[str]] = None
    """Tags indicating the nature of the risk event."""
