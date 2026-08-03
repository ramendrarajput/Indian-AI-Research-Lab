"""
PROJECT BRAHMA
Universal Event Publisher

Author
------
Ramendra Singh Rajput

Description
-----------
Base Publisher used throughout Project BRAHMA.

A Publisher never knows who receives an event.

It only creates Events and forwards them to the
Universal Event Bus.

Examples
--------
Runtime Publisher

Kernel Publisher

Memory Publisher

Universal Agent Publisher

Laboratory Publisher

Future
------
• Batch Publishing
• Async Publishing
• Remote Publishing
"""

from __future__ import annotations

from typing import Any

from ENGINEERING.CORE.EVENTBUS.event import Event
from ENGINEERING.CORE.EVENTBUS.event_type import EventType


class EventPublisher:
    """
    Base class for all Event Publishers.
    """

    def __init__(self, source: str):

        self._source = source

        #
        # Will be injected later
        #
        self._event_bus = None

    # ==========================================================
    # Properties
    # ==========================================================

    @property
    def source(self) -> str:

        return self._source

    # ==========================================================
    # Event Bus
    # ==========================================================

    def attach_bus(self, event_bus) -> None:
        """
        Attach the Universal Event Bus.
        """

        self._event_bus = event_bus

    # ==========================================================
    # Publish
    # ==========================================================

    def publish(
        self,
        event_type: EventType,
        payload: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """
        Publish an event to the Event Bus.
        """

        if self._event_bus is None:

            raise RuntimeError(
                "Event Bus not attached to publisher."
            )

        event = Event(

            event_type=event_type.value,

            source=self.source,

            payload=payload or {},

            metadata=metadata or {},

        )

        self._event_bus.publish(event)

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"(source='{self.source}')"
        )