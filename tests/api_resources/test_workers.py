# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brainbase import Brainbase, AsyncBrainbase

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Brainbase) -> None:
        worker = client.workers.create(
            name="name",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Brainbase) -> None:
        worker = client.workers.create(
            name="name",
            description="description",
            status="status",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Brainbase) -> None:
        response = client.workers.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Brainbase) -> None:
        with client.workers.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Brainbase) -> None:
        worker = client.workers.retrieve(
            "id",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Brainbase) -> None:
        response = client.workers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Brainbase) -> None:
        with client.workers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Brainbase) -> None:
        worker = client.workers.list()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Brainbase) -> None:
        response = client.workers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Brainbase) -> None:
        with client.workers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_id(self, client: Brainbase) -> None:
        worker = client.workers.create_id(
            id="id",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_id_with_all_params(self, client: Brainbase) -> None:
        worker = client.workers.create_id(
            id="id",
            description="description",
            name="name",
            status="status",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_id(self, client: Brainbase) -> None:
        response = client.workers.with_raw_response.create_id(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_id(self, client: Brainbase) -> None:
        with client.workers.with_streaming_response.create_id(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_id(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.with_raw_response.create_id(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_id(self, client: Brainbase) -> None:
        worker = client.workers.delete_id(
            "id",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_id(self, client: Brainbase) -> None:
        response = client.workers.with_raw_response.delete_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_id(self, client: Brainbase) -> None:
        with client.workers.with_streaming_response.delete_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_id(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.with_raw_response.delete_id(
                "",
            )


class TestAsyncWorkers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncBrainbase) -> None:
        worker = await async_client.workers.create(
            name="name",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrainbase) -> None:
        worker = await async_client.workers.create(
            name="name",
            description="description",
            status="status",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrainbase) -> None:
        worker = await async_client.workers.retrieve(
            "id",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBrainbase) -> None:
        worker = await async_client.workers.list()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_id(self, async_client: AsyncBrainbase) -> None:
        worker = await async_client.workers.create_id(
            id="id",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_id_with_all_params(self, async_client: AsyncBrainbase) -> None:
        worker = await async_client.workers.create_id(
            id="id",
            description="description",
            name="name",
            status="status",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_id(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.with_raw_response.create_id(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_id(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.with_streaming_response.create_id(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_id(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.with_raw_response.create_id(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_id(self, async_client: AsyncBrainbase) -> None:
        worker = await async_client.workers.delete_id(
            "id",
        )
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_id(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.with_raw_response.delete_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert worker is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_id(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.with_streaming_response.delete_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_id(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.with_raw_response.delete_id(
                "",
            )
