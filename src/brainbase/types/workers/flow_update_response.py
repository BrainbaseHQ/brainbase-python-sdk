# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowUpdateResponse"]


class FlowUpdateResponse(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    label: Optional[str] = None
