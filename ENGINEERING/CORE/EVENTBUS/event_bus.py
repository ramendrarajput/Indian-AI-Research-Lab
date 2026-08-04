"""
PROJECT BRAHMA
Universal Event Bus

Author
------
Ramendra Singh Rajput

Description
-----------
The Universal Event Bus is the communication backbone
of Project BRAHMA.

All Runtime components communicate through this Event Bus.

Publishers never know Subscribers.

Subscribers never know Publishers.

The Event Bus coordinates all communication.

Future
------
• Async Events

• Distributed Runtime

• Event Replay

• Event Persistence

• Priority Events
"""

from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict

from ENGINEERING.CORE.EVENTBUS.event import Event
from ENGINEERING.CORE.EVENTBUS.subscriber import EventSubscriber


class EventBus:
    """
    Universal Event Bus.
    """

    def __init__(self):

        #
        # event_type -> subscribers
        #

        self._subscribers: DefaultDict[
            str,
            list[EventSubscriber]
        ] = defaultdict(list)

        #
        # History (future replay support)
        #

        self._history: list[Event] = []

    # ==========================================================
    # Subscribe
    # ==========================================================

    def subscribe(
        self,
        event_type: str,
        subscriber: EventSubscriber,
    ) -> None:
        """
        Register subscriber.
        """

        if subscriber not in self._subscribers[event_type]:

            self._subscribers[event_type].append(
                subscriber
            )

    # ==========================================================
    # Unsubscribe
    # ==========================================================

    def unsubscribe(
        self,
        event_type: str,
        subscriber: EventSubscriber,
    ) -> None:
        """
        Remove subscriber.
        """

        if subscriber in self._subscribers[event_type]:

            self._subscribers[event_type].remove(
                subscriber
            )

    # ==========================================================
    # Publish
    # ==========================================================

    def publish(
        self,
        event: Event,
    ) -> None:
        """
        Publish event.
        """

        #
        # Store history
        #

        self._history.append(event)
        from ENGINEERING.CORE.EVENTBUS.history import runtime_event_history

        runtime_event_history.add(event)

        #
        # Notify subscribers
        #

        for subscriber in self._subscribers.get(
            event.event_type,
            [],
        ):

            subscriber.handle_event(event)

    # ==========================================================
    # Queries
    # ==========================================================

    def subscribers(
        self,
        event_type: str,
    ) -> list[EventSubscriber]:

        return list(
            self._subscribers.get(event_type, [])
        )

    def history(self) -> list[Event]:

        return list(self._history)

    def clear_history(self) -> None:

        self._history.clear()

    # ==========================================================
    # Statistics
    # ==========================================================

    def summary(self):

        event_counts = {}

        source_counts = {}

        for event in self._history:

            event_counts[event.event_type] = (
                event_counts.get(event.event_type, 0) + 1
            )

            source_counts[event.source] = (
                source_counts.get(event.source, 0) + 1
            )

        return {

            "registered_events": len(self._subscribers),

            "history_size": len(self._history),

            "subscriber_count": sum(
                len(x)
                for x in self._subscribers.values()
            ),

            "event_counts": event_counts,

            "source_counts": source_counts,

        }


    # ==========================================================
    # Statistics
    # ==========================================================

    def statistics(self):
     """
     Detailed Event Bus statistics.
     """

     return {

        "published_events":
            self._statistics["published_events"],

        "events_by_type":
            dict(self._statistics["events_by_type"]),

        "events_by_source":
            dict(self._statistics["events_by_source"]),

        "registered_events":
            len(self._subscribers),

        "subscriber_count":
            sum(
                len(v)
                for v in self._subscribers.values()
            ),

    }

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self):

        return (
            f"EventBus("
            f"events={len(self._subscribers)}, "
            f"history={len(self._history)})"
        )


#
# Global Event Bus
#

runtime_event_bus = EventBus()