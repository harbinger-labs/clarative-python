# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ClarativeError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import slas, vendors, risk_events
    from .resources.slas import SlasResource, AsyncSlasResource
    from .resources.vendors import VendorsResource, AsyncVendorsResource
    from .resources.risk_events import RiskEventsResource, AsyncRiskEventsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Clarative",
    "AsyncClarative",
    "Client",
    "AsyncClient",
]


class Clarative(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Clarative client instance.

        This automatically infers the `api_key` argument from the `CLARATIVE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CLARATIVE_API_KEY")
        if api_key is None:
            raise ClarativeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CLARATIVE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CLARATIVE_BASE_URL")
        if base_url is None:
            base_url = f"https://developer.clarative.ai"

        custom_headers_env = os.environ.get("CLARATIVE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def risk_events(self) -> RiskEventsResource:
        from .resources.risk_events import RiskEventsResource

        return RiskEventsResource(self)

    @cached_property
    def slas(self) -> SlasResource:
        from .resources.slas import SlasResource

        return SlasResource(self)

    @cached_property
    def vendors(self) -> VendorsResource:
        from .resources.vendors import VendorsResource

        return VendorsResource(self)

    @cached_property
    def with_raw_response(self) -> ClarativeWithRawResponse:
        return ClarativeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClarativeWithStreamedResponse:
        return ClarativeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._http_bearer if security.get("http_bearer", False) else {}),
        }

    @property
    def _http_bearer(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncClarative(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncClarative client instance.

        This automatically infers the `api_key` argument from the `CLARATIVE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CLARATIVE_API_KEY")
        if api_key is None:
            raise ClarativeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CLARATIVE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CLARATIVE_BASE_URL")
        if base_url is None:
            base_url = f"https://developer.clarative.ai"

        custom_headers_env = os.environ.get("CLARATIVE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def risk_events(self) -> AsyncRiskEventsResource:
        from .resources.risk_events import AsyncRiskEventsResource

        return AsyncRiskEventsResource(self)

    @cached_property
    def slas(self) -> AsyncSlasResource:
        from .resources.slas import AsyncSlasResource

        return AsyncSlasResource(self)

    @cached_property
    def vendors(self) -> AsyncVendorsResource:
        from .resources.vendors import AsyncVendorsResource

        return AsyncVendorsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncClarativeWithRawResponse:
        return AsyncClarativeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClarativeWithStreamedResponse:
        return AsyncClarativeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._http_bearer if security.get("http_bearer", False) else {}),
        }

    @property
    def _http_bearer(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ClarativeWithRawResponse:
    _client: Clarative

    def __init__(self, client: Clarative) -> None:
        self._client = client

    @cached_property
    def risk_events(self) -> risk_events.RiskEventsResourceWithRawResponse:
        from .resources.risk_events import RiskEventsResourceWithRawResponse

        return RiskEventsResourceWithRawResponse(self._client.risk_events)

    @cached_property
    def slas(self) -> slas.SlasResourceWithRawResponse:
        from .resources.slas import SlasResourceWithRawResponse

        return SlasResourceWithRawResponse(self._client.slas)

    @cached_property
    def vendors(self) -> vendors.VendorsResourceWithRawResponse:
        from .resources.vendors import VendorsResourceWithRawResponse

        return VendorsResourceWithRawResponse(self._client.vendors)


class AsyncClarativeWithRawResponse:
    _client: AsyncClarative

    def __init__(self, client: AsyncClarative) -> None:
        self._client = client

    @cached_property
    def risk_events(self) -> risk_events.AsyncRiskEventsResourceWithRawResponse:
        from .resources.risk_events import AsyncRiskEventsResourceWithRawResponse

        return AsyncRiskEventsResourceWithRawResponse(self._client.risk_events)

    @cached_property
    def slas(self) -> slas.AsyncSlasResourceWithRawResponse:
        from .resources.slas import AsyncSlasResourceWithRawResponse

        return AsyncSlasResourceWithRawResponse(self._client.slas)

    @cached_property
    def vendors(self) -> vendors.AsyncVendorsResourceWithRawResponse:
        from .resources.vendors import AsyncVendorsResourceWithRawResponse

        return AsyncVendorsResourceWithRawResponse(self._client.vendors)


class ClarativeWithStreamedResponse:
    _client: Clarative

    def __init__(self, client: Clarative) -> None:
        self._client = client

    @cached_property
    def risk_events(self) -> risk_events.RiskEventsResourceWithStreamingResponse:
        from .resources.risk_events import RiskEventsResourceWithStreamingResponse

        return RiskEventsResourceWithStreamingResponse(self._client.risk_events)

    @cached_property
    def slas(self) -> slas.SlasResourceWithStreamingResponse:
        from .resources.slas import SlasResourceWithStreamingResponse

        return SlasResourceWithStreamingResponse(self._client.slas)

    @cached_property
    def vendors(self) -> vendors.VendorsResourceWithStreamingResponse:
        from .resources.vendors import VendorsResourceWithStreamingResponse

        return VendorsResourceWithStreamingResponse(self._client.vendors)


class AsyncClarativeWithStreamedResponse:
    _client: AsyncClarative

    def __init__(self, client: AsyncClarative) -> None:
        self._client = client

    @cached_property
    def risk_events(self) -> risk_events.AsyncRiskEventsResourceWithStreamingResponse:
        from .resources.risk_events import AsyncRiskEventsResourceWithStreamingResponse

        return AsyncRiskEventsResourceWithStreamingResponse(self._client.risk_events)

    @cached_property
    def slas(self) -> slas.AsyncSlasResourceWithStreamingResponse:
        from .resources.slas import AsyncSlasResourceWithStreamingResponse

        return AsyncSlasResourceWithStreamingResponse(self._client.slas)

    @cached_property
    def vendors(self) -> vendors.AsyncVendorsResourceWithStreamingResponse:
        from .resources.vendors import AsyncVendorsResourceWithStreamingResponse

        return AsyncVendorsResourceWithStreamingResponse(self._client.vendors)


Client = Clarative

AsyncClient = AsyncClarative
