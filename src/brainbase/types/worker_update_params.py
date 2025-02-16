# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkerUpdateParams"]


class WorkerUpdateParams(TypedDict, total=False):
    description: str
    """Description of the worker"""

    name: str
    """Name of the worker"""
