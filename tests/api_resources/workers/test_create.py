# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brainbase import Brainbase, AsyncBrainbase

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_new(self, client: Brainbase) -> None:
        create = client.workers.create.new(
            id="id",
        )
        assert create is None

    @pytest.mark.skip()
    @parametrize
    def test_method_new_with_all_params(self, client: Brainbase) -> None:
        create = client.workers.create.new(
            id="id",
            description="description",
            name="name",
            status="status",
        )
        assert create is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_new(self, client: Brainbase) -> None:
        response = client.workers.create.with_raw_response.new(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        create = response.parse()
        assert create is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_new(self, client: Brainbase) -> None:
        with client.workers.create.with_streaming_response.new(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            create = response.parse()
            assert create is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_new(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.create.with_raw_response.new(
                id="",
            )


class TestAsyncCreate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_new(self, async_client: AsyncBrainbase) -> None:
        create = await async_client.workers.create.new(
            id="id",
        )
        assert create is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_new_with_all_params(self, async_client: AsyncBrainbase) -> None:
        create = await async_client.workers.create.new(
            id="id",
            description="description",
            name="name",
            status="status",
        )
        assert create is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_new(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.create.with_raw_response.new(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        create = await response.parse()
        assert create is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_new(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.create.with_streaming_response.new(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            create = await response.parse()
            assert create is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_new(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.create.with_raw_response.new(
                id="",
            )
