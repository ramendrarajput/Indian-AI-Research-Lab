"""
PROJECT BRAHMA
Universal Event History

Author
------
Ramendra Singh Rajput

Description
-----------
Stores the Runtime Event History.

Every event published through the Universal Event Bus
is recorded here.

Future
------
• Event Replay
• Event Persistence
• Runtime Diagnostics
• Distributed Synchronization
"""

from __future__ import annotations

from collections import deque
from typing import Iterable

from ENGINEERING.CORE.EVENTBUS.event import Event


class EventHistory:
    """
    Runtime Event History.
    """

    def __init__(
        self,
        max_events: int = 10000,
    ):

        self._events = deque(maxlen=max_events)

    # ======================================================
    # Add Event
    # ======================================================

    def add(
        self,
        event: Event,
    ) -> None:

        self._events.append(event)

    # ======================================================
    # Recent Events
    # ======================================================

    def recent(
        self,
        count: int = 10,
    ) -> list[Event]:

        return list(self._events)[-count:]

    # ======================================================
    # Find By Type
    # ======================================================

    def by_type(
        self,
        event_type: str,
    ) -> list[Event]:

        return [

            event

            for event in self._events

            if event.event_type == event_type

        ]

    # ======================================================
    # Find By Source
    # ======================================================

    def by_source(
        self,
        source: str,
    ) -> list[Event]:

        return [

            event

            for event in self._events

            if event.source == source

        ]

    # ======================================================
    # Iterator
    # ======================================================

    def all(self) -> Iterable[Event]:

        return iter(self._events)

    # ======================================================
    # Statistics
    # ======================================================

    def size(self) -> int:

        return len(self._events)

    # ======================================================
    # Clear
    # ======================================================

    def clear(self) -> None:

        self._events.clear()

    # ======================================================
    # Summary
    # ======================================================

    def summary(self):

        return {

            "events": len(self._events),

        }

    #=====================================================
    # History 
    #=====================================================
    
    #def last(self, count: int = 10):

    #    return self._history[-count:]

    # ======================================================
    # Last Events
    # ======================================================

    def last(
        self,
        count: int = 10,
    ) -> list[Event]:

        return list(self._events)[-count:]

    # ======================================================
    # Representation
    # ======================================================

    def __len__(self):

        return len(self._events)

    def __repr__(self):

        return (

            f"EventHistory("

            f"events={len(self._events)})"

        )


#
# Global Event History
#

runtime_event_history = EventHistory()