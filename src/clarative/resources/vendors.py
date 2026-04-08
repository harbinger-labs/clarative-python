# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import vendor_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.vendor_list_response import VendorListResponse
from ..types.vendor_retrieve_response import VendorRetrieveResponse

__all__ = ["VendorsResource", "AsyncVendorsResource"]


class VendorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VendorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#accessing-raw-response-data-eg-headers
        """
        return VendorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VendorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#with_streaming_response
        """
        return VendorsResourceWithStreamingResponse(self)

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
    ) -> VendorRetrieveResponse:
        """
        Fetch in-depth information about a single vendor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not urn:
            raise ValueError(f"Expected a non-empty value for `urn` but received {urn!r}")
        return self._get(
            path_template("/v1/vendors/{urn}", urn=urn),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorRetrieveResponse,
        )

    def list(
        self,
        *,
        lifecycle_stage: Optional[Literal["INITIAL_ASSESSMENT", "ONBOARDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VendorListResponse:
        """
        List all vendors, sorted by name alphabetically (case-insensitive)

        Args:
          lifecycle_stage: Filter vendors by lifecycle stage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/vendors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"lifecycle_stage": lifecycle_stage}, vendor_list_params.VendorListParams),
            ),
            cast_to=VendorListResponse,
        )


class AsyncVendorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVendorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVendorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVendorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#with_streaming_response
        """
        return AsyncVendorsResourceWithStreamingResponse(self)

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
    ) -> VendorRetrieveResponse:
        """
        Fetch in-depth information about a single vendor

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not urn:
            raise ValueError(f"Expected a non-empty value for `urn` but received {urn!r}")
        return await self._get(
            path_template("/v1/vendors/{urn}", urn=urn),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VendorRetrieveResponse,
        )

    async def list(
        self,
        *,
        lifecycle_stage: Optional[Literal["INITIAL_ASSESSMENT", "ONBOARDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VendorListResponse:
        """
        List all vendors, sorted by name alphabetically (case-insensitive)

        Args:
          lifecycle_stage: Filter vendors by lifecycle stage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/vendors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"lifecycle_stage": lifecycle_stage}, vendor_list_params.VendorListParams
                ),
            ),
            cast_to=VendorListResponse,
        )


class VendorsResourceWithRawResponse:
    def __init__(self, vendors: VendorsResource) -> None:
        self._vendors = vendors

        self.retrieve = to_raw_response_wrapper(
            vendors.retrieve,
        )
        self.list = to_raw_response_wrapper(
            vendors.list,
        )


class AsyncVendorsResourceWithRawResponse:
    def __init__(self, vendors: AsyncVendorsResource) -> None:
        self._vendors = vendors

        self.retrieve = async_to_raw_response_wrapper(
            vendors.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            vendors.list,
        )


class VendorsResourceWithStreamingResponse:
    def __init__(self, vendors: VendorsResource) -> None:
        self._vendors = vendors

        self.retrieve = to_streamed_response_wrapper(
            vendors.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            vendors.list,
        )


class AsyncVendorsResourceWithStreamingResponse:
    def __init__(self, vendors: AsyncVendorsResource) -> None:
        self._vendors = vendors

        self.retrieve = async_to_streamed_response_wrapper(
            vendors.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            vendors.list,
        )
