# RiskEvents

Types:

```python
from clarative.types import RiskEventRetrieveResponse, RiskEventListResponse
```

Methods:

- <code title="get /v1/risk-events/{urn}">client.risk_events.<a href="./src/clarative/resources/risk_events.py">retrieve</a>(urn) -> <a href="./src/clarative/types/risk_event_retrieve_response.py">RiskEventRetrieveResponse</a></code>
- <code title="get /v1/risk-events">client.risk_events.<a href="./src/clarative/resources/risk_events.py">list</a>(\*\*<a href="src/clarative/types/risk_event_list_params.py">params</a>) -> <a href="./src/clarative/types/risk_event_list_response.py">RiskEventListResponse</a></code>

# Slas

Types:

```python
from clarative.types import (
    SlaRetrieveResponse,
    SlaListResponse,
    SlaGetUptimeMetricsResponse,
    SlaListDataSourcesResponse,
    SlaListViolationsResponse,
    SlaRetrieveViolationResponse,
)
```

Methods:

- <code title="get /v1/slas/{urn}">client.slas.<a href="./src/clarative/resources/slas.py">retrieve</a>(urn) -> <a href="./src/clarative/types/sla_retrieve_response.py">SlaRetrieveResponse</a></code>
- <code title="get /v1/slas">client.slas.<a href="./src/clarative/resources/slas.py">list</a>() -> <a href="./src/clarative/types/sla_list_response.py">SlaListResponse</a></code>
- <code title="get /v1/slas/{sla_urn}/data-sources/{data_source_urn}/uptime-metrics">client.slas.<a href="./src/clarative/resources/slas.py">get_uptime_metrics</a>(data_source_urn, \*, sla_urn, \*\*<a href="src/clarative/types/sla_get_uptime_metrics_params.py">params</a>) -> <a href="./src/clarative/types/sla_get_uptime_metrics_response.py">SlaGetUptimeMetricsResponse</a></code>
- <code title="get /v1/slas/{sla_urn}/data-sources">client.slas.<a href="./src/clarative/resources/slas.py">list_data_sources</a>(sla_urn) -> <a href="./src/clarative/types/sla_list_data_sources_response.py">SlaListDataSourcesResponse</a></code>
- <code title="get /v1/slas/{sla_urn}/violations">client.slas.<a href="./src/clarative/resources/slas.py">list_violations</a>(sla_urn, \*\*<a href="src/clarative/types/sla_list_violations_params.py">params</a>) -> <a href="./src/clarative/types/sla_list_violations_response.py">SlaListViolationsResponse</a></code>
- <code title="get /v1/slas/{sla_urn}/violations/{violation_urn}">client.slas.<a href="./src/clarative/resources/slas.py">retrieve_violation</a>(violation_urn, \*, sla_urn) -> <a href="./src/clarative/types/sla_retrieve_violation_response.py">SlaRetrieveViolationResponse</a></code>

# Vendors

Types:

```python
from clarative.types import VendorRetrieveResponse, VendorListResponse
```

Methods:

- <code title="get /v1/vendors/{urn}">client.vendors.<a href="./src/clarative/resources/vendors.py">retrieve</a>(urn) -> <a href="./src/clarative/types/vendor_retrieve_response.py">VendorRetrieveResponse</a></code>
- <code title="get /v1/vendors">client.vendors.<a href="./src/clarative/resources/vendors.py">list</a>() -> <a href="./src/clarative/types/vendor_list_response.py">VendorListResponse</a></code>
