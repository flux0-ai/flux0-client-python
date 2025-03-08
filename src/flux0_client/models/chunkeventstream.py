"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chunkeventdto import ChunkEventDTO, ChunkEventDTOTypedDict
from flux0_client.types import BaseModel
from flux0_client.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ChunkEventStreamTypedDict(TypedDict):
    data: ChunkEventDTOTypedDict
    event: Literal["chunk"]


class ChunkEventStream(BaseModel):
    data: ChunkEventDTO

    EVENT: Annotated[
        Annotated[Literal["chunk"], AfterValidator(validate_const("chunk"))],
        pydantic.Field(alias="event"),
    ] = "chunk"
