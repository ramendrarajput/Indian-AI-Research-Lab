"""
PROJECT BRAHMA
Universal Event Handlers

Author
------
Ramendra Singh Rajput

Description
-----------
Default reusable Event Handlers for the
BRAHMA Universal Event Bus.

These handlers provide common functionality that
can be reused across Runtime components.

Future
------
• Runtime Logger Handler
• Audit Handler
• Event Replay Handler
• Metrics Handler
• Remote Event Handler
"""

from __future__ import annotations

from ENGINEERING.CORE.EVENTBUS.event import Event
from ENGINEERING.CORE.EVENTBUS.subscriber import EventSubscriber
from ENGINEERING.CORE.RUNTIME.logger import runtime


# ==========================================================
# Logging Handler
# ==========================================================

class LoggingEventHandler(EventSubscriber):
    """
    Logs every received event.
    """

    def __init__(self):

        super().__init__("LoggingHandler")

    def handle_event(
        self,
        event: Event,
    ) -> None:

        runtime(

            f"[EVENT] "

            f"{event.event_type} "

            f"from {event.source}"

        )


# ==========================================================
# Null Handler
# ==========================================================

class NullEventHandler(EventSubscriber):
    """
    Ignores all incoming events.

    Useful for testing.
    """

    def __init__(self):

        super().__init__("NullHandler")

    def handle_event(
        self,
        event: Event,
    ) -> None:

        pass


# ==========================================================
# Debug Handler
# ==========================================================

class DebugEventHandler(EventSubscriber):
    """
    Prints complete event information.
    """

    def __init__(self):

        super().__init__("DebugHandler")

    def handle_event(
        self,
        event: Event,
    ) -> None:

        print()

        print("========== EVENT ==========")

        print(event.to_dict())

        print("===========================")

        print()