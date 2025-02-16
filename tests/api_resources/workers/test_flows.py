# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brainbase import Brainbase, AsyncBrainbase
from tests.utils import assert_matches_type
from brainbase.types.workers import (
    FlowListResponse,
    FlowCreateResponse,
    FlowUpdateResponse,
    FlowRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Brainbase) -> None:
        flow = client.workers.flows.create(
            worker_id="workerId",
            code="code",
            name="name",
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Brainbase) -> None:
        flow = client.workers.flows.create(
            worker_id="workerId",
            code="code",
            name="name",
            label="label",
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Brainbase) -> None:
        response = client.workers.flows.with_raw_response.create(
            worker_id="workerId",
            code="code",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Brainbase) -> None:
        with client.workers.flows.with_streaming_response.create(
            worker_id="workerId",
            code="code",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowCreateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.flows.with_raw_response.create(
                worker_id="",
                code="code",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Brainbase) -> None:
        flow = client.workers.flows.retrieve(
            flow_id="flowId",
            worker_id="workerId",
        )
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Brainbase) -> None:
        response = client.workers.flows.with_raw_response.retrieve(
            flow_id="flowId",
            worker_id="workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Brainbase) -> None:
        with client.workers.flows.with_streaming_response.retrieve(
            flow_id="flowId",
            worker_id="workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.flows.with_raw_response.retrieve(
                flow_id="flowId",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.workers.flows.with_raw_response.retrieve(
                flow_id="",
                worker_id="workerId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Brainbase) -> None:
        flow = client.workers.flows.update(
            flow_id="flowId",
            worker_id="workerId",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Brainbase) -> None:
        flow = client.workers.flows.update(
            flow_id="flowId",
            worker_id="workerId",
            code="code",
            label="label",
            name="name",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Brainbase) -> None:
        response = client.workers.flows.with_raw_response.update(
            flow_id="flowId",
            worker_id="workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Brainbase) -> None:
        with client.workers.flows.with_streaming_response.update(
            flow_id="flowId",
            worker_id="workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.flows.with_raw_response.update(
                flow_id="flowId",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.workers.flows.with_raw_response.update(
                flow_id="",
                worker_id="workerId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Brainbase) -> None:
        flow = client.workers.flows.list(
            "workerId",
        )
        assert_matches_type(FlowListResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Brainbase) -> None:
        response = client.workers.flows.with_raw_response.list(
            "workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert_matches_type(FlowListResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Brainbase) -> None:
        with client.workers.flows.with_streaming_response.list(
            "workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert_matches_type(FlowListResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.flows.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Brainbase) -> None:
        flow = client.workers.flows.delete(
            flow_id="flowId",
            worker_id="workerId",
        )
        assert flow is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Brainbase) -> None:
        response = client.workers.flows.with_raw_response.delete(
            flow_id="flowId",
            worker_id="workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = response.parse()
        assert flow is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Brainbase) -> None:
        with client.workers.flows.with_streaming_response.delete(
            flow_id="flowId",
            worker_id="workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = response.parse()
            assert flow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Brainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.flows.with_raw_response.delete(
                flow_id="flowId",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.workers.flows.with_raw_response.delete(
                flow_id="",
                worker_id="workerId",
            )


class TestAsyncFlows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncBrainbase) -> None:
        flow = await async_client.workers.flows.create(
            worker_id="workerId",
            code="code",
            name="name",
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBrainbase) -> None:
        flow = await async_client.workers.flows.create(
            worker_id="workerId",
            code="code",
            name="name",
            label="label",
        )
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.flows.with_raw_response.create(
            worker_id="workerId",
            code="code",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowCreateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.flows.with_streaming_response.create(
            worker_id="workerId",
            code="code",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowCreateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.flows.with_raw_response.create(
                worker_id="",
                code="code",
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrainbase) -> None:
        flow = await async_client.workers.flows.retrieve(
            flow_id="flowId",
            worker_id="workerId",
        )
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.flows.with_raw_response.retrieve(
            flow_id="flowId",
            worker_id="workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.flows.with_streaming_response.retrieve(
            flow_id="flowId",
            worker_id="workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowRetrieveResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.flows.with_raw_response.retrieve(
                flow_id="flowId",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.workers.flows.with_raw_response.retrieve(
                flow_id="",
                worker_id="workerId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncBrainbase) -> None:
        flow = await async_client.workers.flows.update(
            flow_id="flowId",
            worker_id="workerId",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBrainbase) -> None:
        flow = await async_client.workers.flows.update(
            flow_id="flowId",
            worker_id="workerId",
            code="code",
            label="label",
            name="name",
        )
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.flows.with_raw_response.update(
            flow_id="flowId",
            worker_id="workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowUpdateResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.flows.with_streaming_response.update(
            flow_id="flowId",
            worker_id="workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowUpdateResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.flows.with_raw_response.update(
                flow_id="flowId",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.workers.flows.with_raw_response.update(
                flow_id="",
                worker_id="workerId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBrainbase) -> None:
        flow = await async_client.workers.flows.list(
            "workerId",
        )
        assert_matches_type(FlowListResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.flows.with_raw_response.list(
            "workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert_matches_type(FlowListResponse, flow, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.flows.with_streaming_response.list(
            "workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert_matches_type(FlowListResponse, flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.flows.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncBrainbase) -> None:
        flow = await async_client.workers.flows.delete(
            flow_id="flowId",
            worker_id="workerId",
        )
        assert flow is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBrainbase) -> None:
        response = await async_client.workers.flows.with_raw_response.delete(
            flow_id="flowId",
            worker_id="workerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow = await response.parse()
        assert flow is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBrainbase) -> None:
        async with async_client.workers.flows.with_streaming_response.delete(
            flow_id="flowId",
            worker_id="workerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow = await response.parse()
            assert flow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBrainbase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.flows.with_raw_response.delete(
                flow_id="flowId",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.workers.flows.with_raw_response.delete(
                flow_id="",
                worker_id="workerId",
            )
