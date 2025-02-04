# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkerCreateIDParams"]


class WorkerCreateIDParams(TypedDict, total=False):
    description: str

    name: str

    status: str
