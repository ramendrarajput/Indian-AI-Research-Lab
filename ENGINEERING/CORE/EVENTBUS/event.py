"""
PROJECT BRAHMA
Universal Event

Author
------
Ramendra Singh Rajput

Description
-----------
Base Event object for the BRAHMA Universal Event Bus.

Every communication inside Project BRAHMA is represented
as an Event.

Examples
--------
RuntimeStarted

KernelStarted

MemoryReady

LabLoaded

AgentInitialized

UserCommand

Future
------
Distributed Runtime

Remote Event Bus

Event Replay

Event Persistence
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass(slots=True, frozen=True)
class Event:
    """
    Universal Runtime Event.
    """

    event_id: str = field(default_factory=lambda: str(uuid4()))

    event_type: str = ""

    source: str = ""

    payload: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(default_factory=datetime.utcnow)

    # --------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {

            "event_id": self.event_id,

            "event_type": self.event_type,

            "source": self.source,

            "payload": self.payload,

            "metadata": self.metadata,

            "timestamp": self.timestamp.isoformat(),

        }

    # --------------------------------------------------

    def __str__(self) -> str:

        return (
            f"Event("
            f"type={self.event_type}, "
            f"source={self.source})"
        )