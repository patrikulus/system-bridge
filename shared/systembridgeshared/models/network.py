# generated by datamodel-codegen:
#   filename:  network.json

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class LastUpdated(BaseModel):
    """
    Last updated
    """

    class Config:
        extra = Extra.allow

    io_counters_bytes_sent: float
    io_counters_bytes_recv: float
    io_counters_packets_sent: float
    io_counters_packets_recv: float
    io_counters_errin: float
    io_counters_errout: float
    io_counters_dropin: float
    io_counters_dropout: float


class Network(BaseModel):
    """
    Network
    """

    class Config:
        extra = Extra.allow

    io_counters_bytes_sent: int
    io_counters_bytes_recv: int
    io_counters_packets_sent: int
    io_counters_packets_recv: int
    io_counters_errin: int
    io_counters_errout: int
    io_counters_dropin: int
    io_counters_dropout: int
    last_updated: LastUpdated = Field(..., description="Last updated")
