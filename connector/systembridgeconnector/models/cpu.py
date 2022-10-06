# generated by datamodel-codegen:
#   filename:  cpu.json

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class LastUpdated(BaseModel):
    """
    Last updated
    """

    class Config:
        extra = Extra.allow

    count: Optional[float] = None
    frequency_current: Optional[float] = None
    frequency_min: Optional[float] = None
    frequency_max: Optional[float] = None
    load_average: Optional[float] = None
    stats_ctx_switches: Optional[float] = None
    stats_interrupts: Optional[float] = None
    stats_soft_interrupts: Optional[float] = None
    stats_syscalls: Optional[float] = None
    temperature: Optional[float] = None
    times_user: Optional[float] = None
    times_system: Optional[float] = None
    times_idle: Optional[float] = None
    times_interrupt: Optional[float] = None
    times_dpc: Optional[float] = None
    times_percent_user: Optional[float] = None
    times_percent_system: Optional[float] = None
    times_percent_idle: Optional[float] = None
    times_percent_interrupt: Optional[float] = None
    times_percent_dpc: Optional[float] = None
    usage: Optional[float] = None
    voltage: Optional[float] = None


class Cpu(BaseModel):
    """
    CPU
    """

    class Config:
        extra = Extra.allow

    id: Optional[str] = Field(None, description="Event ID")
    count: Optional[int] = None
    frequency_current: Optional[float] = None
    frequency_min: Optional[float] = None
    frequency_max: Optional[float] = None
    load_average: Optional[float] = None
    stats_ctx_switches: Optional[int] = None
    stats_interrupts: Optional[int] = None
    stats_soft_interrupts: Optional[int] = None
    stats_syscalls: Optional[int] = None
    temperature: Optional[float] = None
    times_user: Optional[float] = None
    times_system: Optional[float] = None
    times_idle: Optional[float] = None
    times_interrupt: Optional[float] = None
    times_dpc: Optional[float] = None
    times_percent_user: Optional[float] = None
    times_percent_system: Optional[float] = None
    times_percent_idle: Optional[float] = None
    times_percent_interrupt: Optional[float] = None
    times_percent_dpc: Optional[float] = None
    usage: Optional[float] = None
    voltage: Optional[float] = None
    last_updated: Optional[LastUpdated] = Field(None, description="Last updated")
