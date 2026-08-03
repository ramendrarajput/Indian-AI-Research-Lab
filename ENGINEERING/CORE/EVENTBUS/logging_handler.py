"""
PROJECT BRAHMA
Universal Event Logging Handler

Author
------
Ramendra Singh Rajput

Description
-----------
Consumes Runtime Events and writes them into the Runtime Logger.

Responsibilities
----------------
• Subscribe to Runtime Events
• Convert Events into Runtime Logs
• Provide the first Event Consumer

Future
------
• UI Event Stream
• Telemetry
• Distributed Logging
• Remote Monitoring
"""

from __future__ import annotations

from ENGINEERING.CORE.EVENTBUS.event import Event
from ENGINEERING.CORE.EVENTBUS.event_type import EventType
from ENGINEERING.CORE.EVENTBUS.subscriber import EventSubscriber

from ENGINEERING.CORE.RUNTIME.logger import logger


# ==========================================================
# Runtime Logging Handler
# ==========================================================

class RuntimeLoggingHandler(EventSubscriber):
    """
    Logs every Runtime Event.
    """

    def __init__(self):

        super().__init__("runtime.logging")

    # ------------------------------------------------------

    def handle_event(self, event: Event) -> None:
        """
        Receive an event from the EventBus.
        """

        logger.info(
            "[EVENT] %-20s -> %s",
            event.source,
            event.event_type,
        )


#
# Global Logging Handler
#

runtime_logging_handler = RuntimeLoggingHandler()


# ==========================================================
# Registration Helper
# ==========================================================

def register_logging_handler(event_bus) -> None:
    """
    Register Runtime Logging Handler.
    """

    #
    # Kernel Events
    #

    event_bus.subscribe(
        EventType.KERNEL_START,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.KERNEL_READY,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.KERNEL_STOP,
        runtime_logging_handler,
    )

    event_bus.subscribe(
            EventType.KERNEL_ERROR,
            runtime_logging_handler,
        )

    #
    # Runtime Events
    #

    event_bus.subscribe(
        EventType.RUNTIME_BOOT,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.RUNTIME_READY,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.RUNTIME_STOP,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.RUNTIME_START,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.RUNTIME_RESTART,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.RUNTIME_ERROR,
        runtime_logging_handler,
    )

    event_bus.subscribe(
        EventType.COMMAND_RECEIVED.value,
        runtime_logging_handler,
 )