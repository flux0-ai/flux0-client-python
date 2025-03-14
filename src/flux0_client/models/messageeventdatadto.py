"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .contentpartdto import ContentPartDTO, ContentPartDTOTypedDict
from .reasoningpartdto import ReasoningPartDTO, ReasoningPartDTOTypedDict
from .toolpartdto import ToolPartDTO, ToolPartDTOTypedDict
from flux0_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from flux0_client.utils import get_discriminator, validate_const
import pydantic
from pydantic import Discriminator, Tag, model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, List, Literal, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


PartTypedDict = TypeAliasType(
    "PartTypedDict",
    Union[ContentPartDTOTypedDict, ReasoningPartDTOTypedDict, ToolPartDTOTypedDict],
)


Part = Annotated[
    Union[
        Annotated[ContentPartDTO, Tag("content")],
        Annotated[ReasoningPartDTO, Tag("reasoning")],
        Annotated[ToolPartDTO, Tag("tool_call")],
    ],
    Discriminator(lambda m: get_discriminator(m, "type", "type")),
]


class MessageEventDataDTOTypedDict(TypedDict):
    parts: List[PartTypedDict]
    type: Literal["message"]
    tags: NotRequired[Nullable[List[str]]]
    flagged: NotRequired[Nullable[bool]]
    participant: NotRequired[Nullable[Dict[str, str]]]


class MessageEventDataDTO(BaseModel):
    parts: List[Part]

    TYPE: Annotated[
        Annotated[Literal["message"], AfterValidator(validate_const("message"))],
        pydantic.Field(alias="type"),
    ] = "message"

    tags: OptionalNullable[List[str]] = UNSET

    flagged: OptionalNullable[bool] = UNSET

    participant: OptionalNullable[Dict[str, str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["tags", "flagged", "participant"]
        nullable_fields = ["tags", "flagged", "participant"]
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
