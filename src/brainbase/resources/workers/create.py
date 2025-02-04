# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workers import create_new_params

__all__ = ["CreateResource", "AsyncCreateResource"]


class CreateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CreateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-python-sdk#with_streaming_response
        """
        return CreateResourceWithStreamingResponse(self)

    def new(
        self,
        id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/workers/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                create_new_params.CreateNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCreateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCreateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-python-sdk#with_streaming_response
        """
        return AsyncCreateResourceWithStreamingResponse(self)

    async def new(
        self,
        id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/workers/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                create_new_params.CreateNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CreateResourceWithRawResponse:
    def __init__(self, create: CreateResource) -> None:
        self._create = create

        self.new = to_raw_response_wrapper(
            create.new,
        )


class AsyncCreateResourceWithRawResponse:
    def __init__(self, create: AsyncCreateResource) -> None:
        self._create = create

        self.new = async_to_raw_response_wrapper(
            create.new,
        )


class CreateResourceWithStreamingResponse:
    def __init__(self, create: CreateResource) -> None:
        self._create = create

        self.new = to_streamed_response_wrapper(
            create.new,
        )


class AsyncCreateResourceWithStreamingResponse:
    def __init__(self, create: AsyncCreateResource) -> None:
        self._create = create

        self.new = async_to_streamed_response_wrapper(
            create.new,
        )
