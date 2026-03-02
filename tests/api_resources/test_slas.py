# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clarative import Clarative, AsyncClarative
from tests.utils import assert_matches_type
from clarative.types import (
    SlaListResponse,
    SlaRetrieveResponse,
    SlaListViolationsResponse,
    SlaListDataSourcesResponse,
    SlaGetUptimeMetricsResponse,
    SlaRetrieveViolationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSlas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Clarative) -> None:
        sla = client.slas.retrieve(
            "urn",
        )
        assert_matches_type(SlaRetrieveResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Clarative) -> None:
        response = client.slas.with_raw_response.retrieve(
            "urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = response.parse()
        assert_matches_type(SlaRetrieveResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Clarative) -> None:
        with client.slas.with_streaming_response.retrieve(
            "urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = response.parse()
            assert_matches_type(SlaRetrieveResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Clarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `urn` but received ''"):
            client.slas.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Clarative) -> None:
        sla = client.slas.list()
        assert_matches_type(SlaListResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Clarative) -> None:
        response = client.slas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = response.parse()
        assert_matches_type(SlaListResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Clarative) -> None:
        with client.slas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = response.parse()
            assert_matches_type(SlaListResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_uptime_metrics(self, client: Clarative) -> None:
        sla = client.slas.get_uptime_metrics(
            data_source_urn="data_source_urn",
            sla_urn="sla_urn",
            end="end",
            start="start",
        )
        assert_matches_type(SlaGetUptimeMetricsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_uptime_metrics(self, client: Clarative) -> None:
        response = client.slas.with_raw_response.get_uptime_metrics(
            data_source_urn="data_source_urn",
            sla_urn="sla_urn",
            end="end",
            start="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = response.parse()
        assert_matches_type(SlaGetUptimeMetricsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_uptime_metrics(self, client: Clarative) -> None:
        with client.slas.with_streaming_response.get_uptime_metrics(
            data_source_urn="data_source_urn",
            sla_urn="sla_urn",
            end="end",
            start="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = response.parse()
            assert_matches_type(SlaGetUptimeMetricsResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_uptime_metrics(self, client: Clarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            client.slas.with_raw_response.get_uptime_metrics(
                data_source_urn="data_source_urn",
                sla_urn="",
                end="end",
                start="start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_urn` but received ''"):
            client.slas.with_raw_response.get_uptime_metrics(
                data_source_urn="",
                sla_urn="sla_urn",
                end="end",
                start="start",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_data_sources(self, client: Clarative) -> None:
        sla = client.slas.list_data_sources(
            "sla_urn",
        )
        assert_matches_type(SlaListDataSourcesResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_data_sources(self, client: Clarative) -> None:
        response = client.slas.with_raw_response.list_data_sources(
            "sla_urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = response.parse()
        assert_matches_type(SlaListDataSourcesResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_data_sources(self, client: Clarative) -> None:
        with client.slas.with_streaming_response.list_data_sources(
            "sla_urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = response.parse()
            assert_matches_type(SlaListDataSourcesResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_data_sources(self, client: Clarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            client.slas.with_raw_response.list_data_sources(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_violations(self, client: Clarative) -> None:
        sla = client.slas.list_violations(
            sla_urn="sla_urn",
        )
        assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_violations_with_all_params(self, client: Clarative) -> None:
        sla = client.slas.list_violations(
            sla_urn="sla_urn",
            data_source_urn="data_source_urn",
            end_month="end_month",
            start_month="start_month",
        )
        assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_violations(self, client: Clarative) -> None:
        response = client.slas.with_raw_response.list_violations(
            sla_urn="sla_urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = response.parse()
        assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_violations(self, client: Clarative) -> None:
        with client.slas.with_streaming_response.list_violations(
            sla_urn="sla_urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = response.parse()
            assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_violations(self, client: Clarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            client.slas.with_raw_response.list_violations(
                sla_urn="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_violation(self, client: Clarative) -> None:
        sla = client.slas.retrieve_violation(
            violation_urn="violation_urn",
            sla_urn="sla_urn",
        )
        assert_matches_type(SlaRetrieveViolationResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_violation(self, client: Clarative) -> None:
        response = client.slas.with_raw_response.retrieve_violation(
            violation_urn="violation_urn",
            sla_urn="sla_urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = response.parse()
        assert_matches_type(SlaRetrieveViolationResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_violation(self, client: Clarative) -> None:
        with client.slas.with_streaming_response.retrieve_violation(
            violation_urn="violation_urn",
            sla_urn="sla_urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = response.parse()
            assert_matches_type(SlaRetrieveViolationResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_violation(self, client: Clarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            client.slas.with_raw_response.retrieve_violation(
                violation_urn="violation_urn",
                sla_urn="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `violation_urn` but received ''"):
            client.slas.with_raw_response.retrieve_violation(
                violation_urn="",
                sla_urn="sla_urn",
            )


class TestAsyncSlas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClarative) -> None:
        sla = await async_client.slas.retrieve(
            "urn",
        )
        assert_matches_type(SlaRetrieveResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClarative) -> None:
        response = await async_client.slas.with_raw_response.retrieve(
            "urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = await response.parse()
        assert_matches_type(SlaRetrieveResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClarative) -> None:
        async with async_client.slas.with_streaming_response.retrieve(
            "urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = await response.parse()
            assert_matches_type(SlaRetrieveResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `urn` but received ''"):
            await async_client.slas.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncClarative) -> None:
        sla = await async_client.slas.list()
        assert_matches_type(SlaListResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncClarative) -> None:
        response = await async_client.slas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = await response.parse()
        assert_matches_type(SlaListResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncClarative) -> None:
        async with async_client.slas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = await response.parse()
            assert_matches_type(SlaListResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_uptime_metrics(self, async_client: AsyncClarative) -> None:
        sla = await async_client.slas.get_uptime_metrics(
            data_source_urn="data_source_urn",
            sla_urn="sla_urn",
            end="end",
            start="start",
        )
        assert_matches_type(SlaGetUptimeMetricsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_uptime_metrics(self, async_client: AsyncClarative) -> None:
        response = await async_client.slas.with_raw_response.get_uptime_metrics(
            data_source_urn="data_source_urn",
            sla_urn="sla_urn",
            end="end",
            start="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = await response.parse()
        assert_matches_type(SlaGetUptimeMetricsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_uptime_metrics(self, async_client: AsyncClarative) -> None:
        async with async_client.slas.with_streaming_response.get_uptime_metrics(
            data_source_urn="data_source_urn",
            sla_urn="sla_urn",
            end="end",
            start="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = await response.parse()
            assert_matches_type(SlaGetUptimeMetricsResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_uptime_metrics(self, async_client: AsyncClarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            await async_client.slas.with_raw_response.get_uptime_metrics(
                data_source_urn="data_source_urn",
                sla_urn="",
                end="end",
                start="start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_urn` but received ''"):
            await async_client.slas.with_raw_response.get_uptime_metrics(
                data_source_urn="",
                sla_urn="sla_urn",
                end="end",
                start="start",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_data_sources(self, async_client: AsyncClarative) -> None:
        sla = await async_client.slas.list_data_sources(
            "sla_urn",
        )
        assert_matches_type(SlaListDataSourcesResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_data_sources(self, async_client: AsyncClarative) -> None:
        response = await async_client.slas.with_raw_response.list_data_sources(
            "sla_urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = await response.parse()
        assert_matches_type(SlaListDataSourcesResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_data_sources(self, async_client: AsyncClarative) -> None:
        async with async_client.slas.with_streaming_response.list_data_sources(
            "sla_urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = await response.parse()
            assert_matches_type(SlaListDataSourcesResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_data_sources(self, async_client: AsyncClarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            await async_client.slas.with_raw_response.list_data_sources(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_violations(self, async_client: AsyncClarative) -> None:
        sla = await async_client.slas.list_violations(
            sla_urn="sla_urn",
        )
        assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_violations_with_all_params(self, async_client: AsyncClarative) -> None:
        sla = await async_client.slas.list_violations(
            sla_urn="sla_urn",
            data_source_urn="data_source_urn",
            end_month="end_month",
            start_month="start_month",
        )
        assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_violations(self, async_client: AsyncClarative) -> None:
        response = await async_client.slas.with_raw_response.list_violations(
            sla_urn="sla_urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = await response.parse()
        assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_violations(self, async_client: AsyncClarative) -> None:
        async with async_client.slas.with_streaming_response.list_violations(
            sla_urn="sla_urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = await response.parse()
            assert_matches_type(SlaListViolationsResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_violations(self, async_client: AsyncClarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            await async_client.slas.with_raw_response.list_violations(
                sla_urn="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_violation(self, async_client: AsyncClarative) -> None:
        sla = await async_client.slas.retrieve_violation(
            violation_urn="violation_urn",
            sla_urn="sla_urn",
        )
        assert_matches_type(SlaRetrieveViolationResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_violation(self, async_client: AsyncClarative) -> None:
        response = await async_client.slas.with_raw_response.retrieve_violation(
            violation_urn="violation_urn",
            sla_urn="sla_urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sla = await response.parse()
        assert_matches_type(SlaRetrieveViolationResponse, sla, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_violation(self, async_client: AsyncClarative) -> None:
        async with async_client.slas.with_streaming_response.retrieve_violation(
            violation_urn="violation_urn",
            sla_urn="sla_urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sla = await response.parse()
            assert_matches_type(SlaRetrieveViolationResponse, sla, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_violation(self, async_client: AsyncClarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sla_urn` but received ''"):
            await async_client.slas.with_raw_response.retrieve_violation(
                violation_urn="violation_urn",
                sla_urn="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `violation_urn` but received ''"):
            await async_client.slas.with_raw_response.retrieve_violation(
                violation_urn="",
                sla_urn="sla_urn",
            )
