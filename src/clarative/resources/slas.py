# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import sla_list_violations_params, sla_get_uptime_metrics_params
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
from ..types.sla_list_response import SlaListResponse
from ..types.sla_retrieve_response import SlaRetrieveResponse
from ..types.sla_list_violations_response import SlaListViolationsResponse
from ..types.sla_list_data_sources_response import SlaListDataSourcesResponse
from ..types.sla_get_uptime_metrics_response import SlaGetUptimeMetricsResponse
from ..types.sla_retrieve_violation_response import SlaRetrieveViolationResponse

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
            path_template("/v1/slas/{urn}", urn=urn),
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
        """List all SLAs, sorted by name alphabetically (case-insensitive)"""
        return self._get(
            "/v1/slas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListResponse,
        )

    def get_uptime_metrics(
        self,
        data_source_urn: str,
        *,
        sla_urn: str,
        end: str,
        start: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaGetUptimeMetricsResponse:
        """
        Get uptime metrics for an SLA data source

        Args:
          end: Year and month landing within the last SLA evaluation period to include in the
              result, in the format YYYY-MM

          start: Year and month landing within the first SLA evaluation period to include in the
              result, in the format YYYY-MM

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        if not data_source_urn:
            raise ValueError(f"Expected a non-empty value for `data_source_urn` but received {data_source_urn!r}")
        return self._get(
            path_template(
                "/v1/slas/{sla_urn}/data-sources/{data_source_urn}/uptime-metrics",
                sla_urn=sla_urn,
                data_source_urn=data_source_urn,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    sla_get_uptime_metrics_params.SlaGetUptimeMetricsParams,
                ),
            ),
            cast_to=SlaGetUptimeMetricsResponse,
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
        """List all data sources for an SLA.

        There is never more than one status page
        source, and the monitor data sources are sorted alphabetically by name
        (case-insensitive).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        return self._get(
            path_template("/v1/slas/{sla_urn}/data-sources", sla_urn=sla_urn),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListDataSourcesResponse,
        )

    def list_violations(
        self,
        sla_urn: str,
        *,
        data_source_urn: Optional[str] | Omit = omit,
        end_month: Optional[str] | Omit = omit,
        start_month: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaListViolationsResponse:
        """
        List all violations for an SLA, sorted first by timestamp (oldest first) and
        second by total downtime (longest first).

        Args:
          data_source_urn: An SLA data source's unique identifier

          end_month: Year and month landing within the last SLA evaluation period to include in the
              result, in the format YYYY-MM. Defaults to the current time.

          start_month: Year and month landing within the first SLA evaluation period to include in the
              result, in the format YYYY-MM. Defaults to 2024-01.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        return self._get(
            path_template("/v1/slas/{sla_urn}/violations", sla_urn=sla_urn),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "data_source_urn": data_source_urn,
                        "end_month": end_month,
                        "start_month": start_month,
                    },
                    sla_list_violations_params.SlaListViolationsParams,
                ),
            ),
            cast_to=SlaListViolationsResponse,
        )

    def retrieve_violation(
        self,
        violation_urn: str,
        *,
        sla_urn: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaRetrieveViolationResponse:
        """
        Get details on a specific SLA violation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        if not violation_urn:
            raise ValueError(f"Expected a non-empty value for `violation_urn` but received {violation_urn!r}")
        return self._get(
            path_template(
                "/v1/slas/{sla_urn}/violations/{violation_urn}", sla_urn=sla_urn, violation_urn=violation_urn
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaRetrieveViolationResponse,
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
            path_template("/v1/slas/{urn}", urn=urn),
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
        """List all SLAs, sorted by name alphabetically (case-insensitive)"""
        return await self._get(
            "/v1/slas",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListResponse,
        )

    async def get_uptime_metrics(
        self,
        data_source_urn: str,
        *,
        sla_urn: str,
        end: str,
        start: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaGetUptimeMetricsResponse:
        """
        Get uptime metrics for an SLA data source

        Args:
          end: Year and month landing within the last SLA evaluation period to include in the
              result, in the format YYYY-MM

          start: Year and month landing within the first SLA evaluation period to include in the
              result, in the format YYYY-MM

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        if not data_source_urn:
            raise ValueError(f"Expected a non-empty value for `data_source_urn` but received {data_source_urn!r}")
        return await self._get(
            path_template(
                "/v1/slas/{sla_urn}/data-sources/{data_source_urn}/uptime-metrics",
                sla_urn=sla_urn,
                data_source_urn=data_source_urn,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    sla_get_uptime_metrics_params.SlaGetUptimeMetricsParams,
                ),
            ),
            cast_to=SlaGetUptimeMetricsResponse,
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
        """List all data sources for an SLA.

        There is never more than one status page
        source, and the monitor data sources are sorted alphabetically by name
        (case-insensitive).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        return await self._get(
            path_template("/v1/slas/{sla_urn}/data-sources", sla_urn=sla_urn),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaListDataSourcesResponse,
        )

    async def list_violations(
        self,
        sla_urn: str,
        *,
        data_source_urn: Optional[str] | Omit = omit,
        end_month: Optional[str] | Omit = omit,
        start_month: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaListViolationsResponse:
        """
        List all violations for an SLA, sorted first by timestamp (oldest first) and
        second by total downtime (longest first).

        Args:
          data_source_urn: An SLA data source's unique identifier

          end_month: Year and month landing within the last SLA evaluation period to include in the
              result, in the format YYYY-MM. Defaults to the current time.

          start_month: Year and month landing within the first SLA evaluation period to include in the
              result, in the format YYYY-MM. Defaults to 2024-01.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        return await self._get(
            path_template("/v1/slas/{sla_urn}/violations", sla_urn=sla_urn),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "data_source_urn": data_source_urn,
                        "end_month": end_month,
                        "start_month": start_month,
                    },
                    sla_list_violations_params.SlaListViolationsParams,
                ),
            ),
            cast_to=SlaListViolationsResponse,
        )

    async def retrieve_violation(
        self,
        violation_urn: str,
        *,
        sla_urn: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlaRetrieveViolationResponse:
        """
        Get details on a specific SLA violation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sla_urn:
            raise ValueError(f"Expected a non-empty value for `sla_urn` but received {sla_urn!r}")
        if not violation_urn:
            raise ValueError(f"Expected a non-empty value for `violation_urn` but received {violation_urn!r}")
        return await self._get(
            path_template(
                "/v1/slas/{sla_urn}/violations/{violation_urn}", sla_urn=sla_urn, violation_urn=violation_urn
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlaRetrieveViolationResponse,
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
        self.get_uptime_metrics = to_raw_response_wrapper(
            slas.get_uptime_metrics,
        )
        self.list_data_sources = to_raw_response_wrapper(
            slas.list_data_sources,
        )
        self.list_violations = to_raw_response_wrapper(
            slas.list_violations,
        )
        self.retrieve_violation = to_raw_response_wrapper(
            slas.retrieve_violation,
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
        self.get_uptime_metrics = async_to_raw_response_wrapper(
            slas.get_uptime_metrics,
        )
        self.list_data_sources = async_to_raw_response_wrapper(
            slas.list_data_sources,
        )
        self.list_violations = async_to_raw_response_wrapper(
            slas.list_violations,
        )
        self.retrieve_violation = async_to_raw_response_wrapper(
            slas.retrieve_violation,
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
        self.get_uptime_metrics = to_streamed_response_wrapper(
            slas.get_uptime_metrics,
        )
        self.list_data_sources = to_streamed_response_wrapper(
            slas.list_data_sources,
        )
        self.list_violations = to_streamed_response_wrapper(
            slas.list_violations,
        )
        self.retrieve_violation = to_streamed_response_wrapper(
            slas.retrieve_violation,
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
        self.get_uptime_metrics = async_to_streamed_response_wrapper(
            slas.get_uptime_metrics,
        )
        self.list_data_sources = async_to_streamed_response_wrapper(
            slas.list_data_sources,
        )
        self.list_violations = async_to_streamed_response_wrapper(
            slas.list_violations,
        )
        self.retrieve_violation = async_to_streamed_response_wrapper(
            slas.retrieve_violation,
        )
