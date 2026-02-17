# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clarative import Clarative, AsyncClarative
from tests.utils import assert_matches_type
from clarative.types import RiskEventListResponse, RiskEventRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRiskEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Clarative) -> None:
        risk_event = client.risk_events.retrieve(
            "urn",
        )
        assert_matches_type(RiskEventRetrieveResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Clarative) -> None:
        response = client.risk_events.with_raw_response.retrieve(
            "urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_event = response.parse()
        assert_matches_type(RiskEventRetrieveResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Clarative) -> None:
        with client.risk_events.with_streaming_response.retrieve(
            "urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_event = response.parse()
            assert_matches_type(RiskEventRetrieveResponse, risk_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Clarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `urn` but received ''"):
            client.risk_events.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Clarative) -> None:
        risk_event = client.risk_events.list()
        assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Clarative) -> None:
        risk_event = client.risk_events.list(
            risk_threshold="LOW",
            vendor_urn="vendor_urn",
        )
        assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Clarative) -> None:
        response = client.risk_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_event = response.parse()
        assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Clarative) -> None:
        with client.risk_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_event = response.parse()
            assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRiskEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncClarative) -> None:
        risk_event = await async_client.risk_events.retrieve(
            "urn",
        )
        assert_matches_type(RiskEventRetrieveResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncClarative) -> None:
        response = await async_client.risk_events.with_raw_response.retrieve(
            "urn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_event = await response.parse()
        assert_matches_type(RiskEventRetrieveResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncClarative) -> None:
        async with async_client.risk_events.with_streaming_response.retrieve(
            "urn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_event = await response.parse()
            assert_matches_type(RiskEventRetrieveResponse, risk_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncClarative) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `urn` but received ''"):
            await async_client.risk_events.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncClarative) -> None:
        risk_event = await async_client.risk_events.list()
        assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncClarative) -> None:
        risk_event = await async_client.risk_events.list(
            risk_threshold="LOW",
            vendor_urn="vendor_urn",
        )
        assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncClarative) -> None:
        response = await async_client.risk_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_event = await response.parse()
        assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncClarative) -> None:
        async with async_client.risk_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_event = await response.parse()
            assert_matches_type(RiskEventListResponse, risk_event, path=["response"])

        assert cast(Any, response.is_closed) is True
