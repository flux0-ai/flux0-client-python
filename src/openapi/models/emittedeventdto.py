"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .eventsourcedto import EventSourceDTO
from .eventtypedto import EventTypeDTO
from .messageeventdatadto import MessageEventDataDTO, MessageEventDataDTOTypedDict
from .statuseventdatadto import StatusEventDataDTO, StatusEventDataDTOTypedDict
from .tooleventdatadto import ToolEventDataDTO, ToolEventDataDTOTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from openapi.utils import get_discriminator
from pydantic import Discriminator, Tag, model_serializer
from typing import Any, Dict, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


DataTypedDict = TypeAliasType(
    "DataTypedDict",
    Union[
        ToolEventDataDTOTypedDict,
        StatusEventDataDTOTypedDict,
        MessageEventDataDTOTypedDict,
    ],
)


Data = Annotated[
    Union[
        Annotated[MessageEventDataDTO, Tag("message")],
        Annotated[StatusEventDataDTO, Tag("status")],
        Annotated[ToolEventDataDTO, Tag("tool_call_result")],
    ],
    Discriminator(lambda m: get_discriminator(m, "type", "type")),
]


class EmittedEventDTOTypedDict(TypedDict):
    id: str
    r"""Unique identifier for the event"""
    correlation_id: str
    r"""Identifier linking related events together"""
    type: EventTypeDTO
    r"""Type of event that occurred within a session.

    Represents different types of interactions that can occur within a conversation.
    """
    source: EventSourceDTO
    r"""Source of the event within a session.

    Identifies who or what generated the event.
    """
    data: DataTypedDict
    metadata: NotRequired[Nullable[Dict[str, Any]]]


class EmittedEventDTO(BaseModel):
    id: str
    r"""Unique identifier for the event"""

    correlation_id: str
    r"""Identifier linking related events together"""

    type: EventTypeDTO
    r"""Type of event that occurred within a session.

    Represents different types of interactions that can occur within a conversation.
    """

    source: EventSourceDTO
    r"""Source of the event within a session.

    Identifies who or what generated the event.
    """

    data: Data

    metadata: OptionalNullable[Dict[str, Any]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["metadata"]
        nullable_fields = ["metadata"]
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
