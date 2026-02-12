# Slas

Types:

```python
from clarative.types import SlaRetrieveResponse, SlaListResponse, SlaListDataSourcesResponse
```

Methods:

- <code title="get /v1/slas/{urn}">client.slas.<a href="./src/clarative/resources/slas.py">retrieve</a>(urn) -> <a href="./src/clarative/types/sla_retrieve_response.py">SlaRetrieveResponse</a></code>
- <code title="get /v1/slas">client.slas.<a href="./src/clarative/resources/slas.py">list</a>() -> <a href="./src/clarative/types/sla_list_response.py">SlaListResponse</a></code>
- <code title="get /v1/slas/{sla_urn}/data-sources">client.slas.<a href="./src/clarative/resources/slas.py">list_data_sources</a>(sla_urn) -> <a href="./src/clarative/types/sla_list_data_sources_response.py">SlaListDataSourcesResponse</a></code>

# Vendors

Types:

```python
from clarative.types import VendorRetrieveResponse, VendorListResponse
```

Methods:

- <code title="get /v1/vendors/{urn}">client.vendors.<a href="./src/clarative/resources/vendors.py">retrieve</a>(urn) -> <a href="./src/clarative/types/vendor_retrieve_response.py">VendorRetrieveResponse</a></code>
- <code title="get /v1/vendors">client.vendors.<a href="./src/clarative/resources/vendors.py">list</a>() -> <a href="./src/clarative/types/vendor_list_response.py">VendorListResponse</a></code>
