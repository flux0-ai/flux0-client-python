"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class RetrieveSessionRequestTypedDict(TypedDict):
    session_id: str
    r"""Unique identifier of the session"""


class RetrieveSessionRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique identifier of the session"""
