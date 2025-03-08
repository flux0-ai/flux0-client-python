"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .eventsourcedto import EventSourceDTO
from .eventtypedto import EventTypeDTO
from flux0_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from flux0_client.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class ListSessionEventsRequestTypedDict(TypedDict):
    session_id: str
    r"""Unique identifier of the session"""
    min_offset: NotRequired[Nullable[int]]
    source: NotRequired[Nullable[EventSourceDTO]]
    r"""Source of the event within a session.

    Identifies who or what generated the event.
    """
    correlation_id: NotRequired[Nullable[str]]
    types: NotRequired[Nullable[List[EventTypeDTO]]]


class ListSessionEventsRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique identifier of the session"""

    min_offset: Annotated[
        OptionalNullable[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    source: Annotated[
        OptionalNullable[EventSourceDTO],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Source of the event within a session.

    Identifies who or what generated the event.
    """

    correlation_id: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    types: Annotated[
        OptionalNullable[List[EventTypeDTO]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["min_offset", "source", "correlation_id", "types"]
        nullable_fields = ["min_offset", "source", "correlation_id", "types"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
