# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SlaListDataSourcesResponse", "MonitorDataSource", "StatusPageDataSource"]


class MonitorDataSource(BaseModel):
    description: Optional[str] = None
    """The monitor's description"""

    name: str
    """The monitor's display name"""

    urn: str
    """A unique identifier for the data source"""

    data_source_type: Optional[Literal["MONITOR"]] = None
    """The type of the data source"""


class StatusPageDataSource(BaseModel):
    """
    The SLA's data source for incidents pulled from vendor status pages, if applicable
    """

    excluded_product_tags: List[str]
    """A list of incident tags that are excluded from the SLA's calculations"""

    included_product_tags: List[str]
    """A list of incident tags that are included in the SLA's calculations"""

    urn: str
    """A unique identifier for the data source"""

    data_source_type: Optional[Literal["STATUS_PAGE"]] = None
    """The type of the data source"""


class SlaListDataSourcesResponse(BaseModel):
    monitor_data_sources: List[MonitorDataSource]
    """A list of any monitor data sources associated with the SLA"""

    sla_urn: str
    """A unique identifier for the SLA associated with this data source"""

    status_page_data_source: Optional[StatusPageDataSource] = None
    """
    The SLA's data source for incidents pulled from vendor status pages, if
    applicable
    """

    vendor_urn: str
    """A unique identifier for the vendor associated with this data source"""
