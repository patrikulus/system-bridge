# generated by datamodel-codegen:
#   filename:  display.json

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class Display(BaseModel):
    """
    Display
    """

    class Config:
        extra = Extra.allow

    last_updated: dict[str, float] = Field(..., description="Last updated")
