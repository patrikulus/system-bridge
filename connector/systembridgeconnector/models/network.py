# generated by datamodel-codegen:
#   filename:  network.json

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class LastUpdated(BaseModel):
    """
    Last updated
    """

    io_counters_bytes_sent: Optional[float] = None
    io_counters_bytes_recv: Optional[float] = None
    io_counters_packets_sent: Optional[float] = None
    io_counters_packets_recv: Optional[float] = None
    io_counters_errin: Optional[float] = None
    io_counters_errout: Optional[float] = None
    io_counters_dropin: Optional[float] = None
    io_counters_dropout: Optional[float] = None


class Network(BaseModel):
    """
    Network
    """

    class Config:
        extra = Extra.allow

    id: Optional[str] = Field(None, description="Event ID")
    io_counters_bytes_sent: Optional[int] = None
    io_counters_bytes_recv: Optional[int] = None
    io_counters_packets_sent: Optional[int] = None
    io_counters_packets_recv: Optional[int] = None
    io_counters_errin: Optional[int] = None
    io_counters_errout: Optional[int] = None
    io_counters_dropin: Optional[int] = None
    io_counters_dropout: Optional[int] = None
    last_updated: Optional[LastUpdated] = Field(None, description="Last updated")
