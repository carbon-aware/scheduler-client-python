# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from carbonaware_scheduler import CarbonawareScheduler, AsyncCarbonawareScheduler
from carbonaware_scheduler.types import RegionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: CarbonawareScheduler) -> None:
        region = client.regions.list()
        assert_matches_type(RegionListResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: CarbonawareScheduler) -> None:
        response = client.regions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(RegionListResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: CarbonawareScheduler) -> None:
        with client.regions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(RegionListResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCarbonawareScheduler) -> None:
        region = await async_client.regions.list()
        assert_matches_type(RegionListResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCarbonawareScheduler) -> None:
        response = await async_client.regions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(RegionListResponse, region, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCarbonawareScheduler) -> None:
        async with async_client.regions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(RegionListResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True
