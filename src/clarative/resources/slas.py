# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sla_list_response import SlaListResponse
from ..types.sla_retrieve_response import SlaRetrieveResponse
from ..types.sla_list_data_sources_response import SlaListDataSourcesResponse

__all__ = ["SlasResource", "AsyncSlasResource"]


class SlasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SlasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#accessing-raw-response-data-eg-headers
        """
        return SlasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#with_streaming_response
        """
        return SlasResourceWithStreamingResponse(self)

    def retrieve(
        self,
        urn: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaRetrieveResponse:
        """
        Fetch in-depth information about a single SLA

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not urn:
            raise ValueError(f"Expected a non-empty value for `urn` but received {urn!r}")
        return self._get(
            f"/v1/slas/{urn}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaListResponse:
        """List all SLAs"""
        return self._get(
            "/v1/slas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListResponse,
        )

    def list_data_sources(
        self,
        sla_urn: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaListDataSourcesResponse:
        """
        List all data sources for an SLA

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        return self._get(
            f"/v1/slas/{sla_urn}/data-sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListDataSourcesResponse,
        )


class AsyncSlasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSlasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSlasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#with_streaming_response
        """
        return AsyncSlasResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        urn: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaRetrieveResponse:
        """
        Fetch in-depth information about a single SLA

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not urn:
            raise ValueError(f"Expected a non-empty value for `urn` but received {urn!r}")
        return await self._get(
            f"/v1/slas/{urn}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaListResponse:
        """List all SLAs"""
        return await self._get(
            "/v1/slas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListResponse,
        )

    async def list_data_sources(
        self,
        sla_urn: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaListDataSourcesResponse:
        """
        List all data sources for an SLA

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        return await self._get(
            f"/v1/slas/{sla_urn}/data-sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListDataSourcesResponse,
        )


class SlasResourceWithRawResponse:
    def __init__(self, slas: SlasResource) -> None:
        self._slas = slas

        self.retrieve = to_raw_response_wrapper(
            slas.retrieve,
        )
        self.list = to_raw_response_wrapper(
            slas.list,
        )
        self.list_data_sources = to_raw_response_wrapper(
            slas.list_data_sources,
        )


class AsyncSlasResourceWithRawResponse:
    def __init__(self, slas: AsyncSlasResource) -> None:
        self._slas = slas

        self.retrieve = async_to_raw_response_wrapper(
            slas.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            slas.list,
        )
        self.list_data_sources = async_to_raw_response_wrapper(
            slas.list_data_sources,
        )


class SlasResourceWithStreamingResponse:
    def __init__(self, slas: SlasResource) -> None:
        self._slas = slas

        self.retrieve = to_streamed_response_wrapper(
            slas.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            slas.list,
        )
        self.list_data_sources = to_streamed_response_wrapper(
            slas.list_data_sources,
        )


class AsyncSlasResourceWithStreamingResponse:
    def __init__(self, slas: AsyncSlasResource) -> None:
        self._slas = slas

        self.retrieve = async_to_streamed_response_wrapper(
            slas.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            slas.list,
        )
        self.list_data_sources = async_to_streamed_response_wrapper(
            slas.list_data_sources,
        )
