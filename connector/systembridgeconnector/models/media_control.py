# generated by datamodel-codegen:
#   filename:  media_control.json

from __future__ import annotations

from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel


class Action(Enum):
    play = "PLAY"
    pause = "PAUSE"
    stop = "STOP"
    previous = "PREVIOUS"
    next = "NEXT"
    seek = "SEEK"
    rewind = "REWIND"
    fastforward = "FASTFORWARD"
    shuffle = "SHUFFLE"
    repeat = "REPEAT"
    mute = "MUTE"
    volumedown = "VOLUMEDOWN"
    volumeup = "VOLUMEUP"


class MediaControl(BaseModel):
    """
    Media Control
    """

    action: Action
    value: Optional[Any] = None
