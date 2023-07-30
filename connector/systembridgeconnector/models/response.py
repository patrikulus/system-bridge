# generated by datamodel-codegen:
#   filename:  response.json

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Extra, Field


class Response(BaseModel):
    """
    Response
    """

    class Config:
        extra = Extra.allow

    id: Optional[str] = Field(None, description="Message ID")
    type: str = Field(..., description="Type")
    subtype: Optional[str] = Field(None, description="Subtype")
    message: Optional[str] = Field(None, description="Message")
    module: Optional[str] = Field(None, description="Module")
    data: Optional[Any] = Field(None, description="Data")
