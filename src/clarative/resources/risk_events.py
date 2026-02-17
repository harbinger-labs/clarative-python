# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import risk_event_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.risk_event_list_response import RiskEventListResponse
from ..types.risk_event_retrieve_response import RiskEventRetrieveResponse

__all__ = ["RiskEventsResource", "AsyncRiskEventsResource"]


class RiskEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RiskEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#accessing-raw-response-data-eg-headers
        """
        return RiskEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RiskEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#with_streaming_response
        """
        return RiskEventsResourceWithStreamingResponse(self)

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
    ) -> RiskEventRetrieveResponse:
        """
        Fetch in-depth information about a single risk event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not urn:
            raise ValueError(f"Expected a non-empty value for `urn` but received {urn!r}")
        return self._get(
            f"/v1/risk-events/{urn}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RiskEventRetrieveResponse,
        )

    def list(
        self,
        *,
        risk_threshold: Optional[Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]] | Omit = omit,
        vendor_urn: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RiskEventListResponse:
        """
        List all risk events with optional filters

        Args:
          risk_threshold: Filter events by minimum risk level

          vendor_urn: A vendor's unique identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/risk-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "risk_threshold": risk_threshold,
                        "vendor_urn": vendor_urn,
                    },
                    risk_event_list_params.RiskEventListParams,
                ),
            ),
            cast_to=RiskEventListResponse,
        )


class AsyncRiskEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRiskEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRiskEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRiskEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/harbinger-labs/clarative-python#with_streaming_response
        """
        return AsyncRiskEventsResourceWithStreamingResponse(self)

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
    ) -> RiskEventRetrieveResponse:
        """
        Fetch in-depth information about a single risk event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not urn:
            raise ValueError(f"Expected a non-empty value for `urn` but received {urn!r}")
        return await self._get(
            f"/v1/risk-events/{urn}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RiskEventRetrieveResponse,
        )

    async def list(
        self,
        *,
        risk_threshold: Optional[Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]] | Omit = omit,
        vendor_urn: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RiskEventListResponse:
        """
        List all risk events with optional filters

        Args:
          risk_threshold: Filter events by minimum risk level

          vendor_urn: A vendor's unique identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/risk-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "risk_threshold": risk_threshold,
                        "vendor_urn": vendor_urn,
                    },
                    risk_event_list_params.RiskEventListParams,
                ),
            ),
            cast_to=RiskEventListResponse,
        )


class RiskEventsResourceWithRawResponse:
    def __init__(self, risk_events: RiskEventsResource) -> None:
        self._risk_events = risk_events

        self.retrieve = to_raw_response_wrapper(
            risk_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            risk_events.list,
        )


class AsyncRiskEventsResourceWithRawResponse:
    def __init__(self, risk_events: AsyncRiskEventsResource) -> None:
        self._risk_events = risk_events

        self.retrieve = async_to_raw_response_wrapper(
            risk_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            risk_events.list,
        )


class RiskEventsResourceWithStreamingResponse:
    def __init__(self, risk_events: RiskEventsResource) -> None:
        self._risk_events = risk_events

        self.retrieve = to_streamed_response_wrapper(
            risk_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            risk_events.list,
        )


class AsyncRiskEventsResourceWithStreamingResponse:
    def __init__(self, risk_events: AsyncRiskEventsResource) -> None:
        self._risk_events = risk_events

        self.retrieve = async_to_streamed_response_wrapper(
            risk_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            risk_events.list,
        )
