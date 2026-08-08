"""
PROJECT BRAHMA
Universal Runtime Boot Sequence

Author:
    Ramendra Singh Rajput

Description
-----------
Boot orchestrator for the BRAHMA Runtime.

Responsibilities
----------------
• Initialize Runtime
• Register Core Services
• Prepare Runtime Context
• Transition Runtime States
"""

from __future__ import annotations

from ENGINEERING.CORE.EVENTBUS.event import Event
from ENGINEERING.CORE.EVENTBUS.event_bus import runtime_event_bus
from ENGINEERING.CORE.EVENTBUS.history import runtime_event_history
from ENGINEERING.CORE.RUNTIME.context import runtime_context
from ENGINEERING.CORE.RUNTIME.logger import (
    boot,
    runtime,
)
from ENGINEERING.CORE.RUNTIME.registry import runtime_registry
from ENGINEERING.CORE.RUNTIME.state import (
    RuntimeState,
    runtime_state,
)
from ENGINEERING.CORE.RUNTIME.kernel import runtime_kernel
from ENGINEERING.CORE.EVENTBUS.logging_handler import register_logging_handler
from ENGINEERING.CORE.EVENTBUS.logging_handler import (
    register_logging_handler,
)
from ENGINEERING.CORE.RUNTIME.console import runtime_console
from ENGINEERING.CORE.EVENTBUS.event_type import EventType
from ENGINEERING.MEMORY.memory_engine import runtime_memory
from ENGINEERING.MEMORY.memory_type import MemoryType

# ==========================================================
# Runtime Boot
# ==========================================================

def boot_runtime():
    """
    Boot the Project BRAHMA Runtime.
    """

    # ------------------------------------------------------
    # BOOT START
    # ------------------------------------------------------

    runtime_state.set(RuntimeState.BOOTING)

    boot("Project BRAHMA Runtime Boot Started")

    runtime_event_bus.publish(

        Event(

            event_type=EventType.RUNTIME_BOOT.value,

            source="runtime.boot",

        )

    )

    # ------------------------------------------------------
    # Attach Global Registry to Runtime Context
    # ------------------------------------------------------

    runtime_context.registry = runtime_registry

    # ------------------------------------------------------
    # Register Core Services
    # ------------------------------------------------------

    runtime_registry.register_service(
        "logger",
        runtime_context.logger,
    )

    runtime_registry.register_service(
        "runtime_state",
        runtime_context.state,
    )

    runtime_registry.register_service(
        "runtime_context",
        runtime_context,
    )

    runtime_registry.register_service(
        "runtime_registry",
        runtime_registry,
    )

    runtime_registry.register_service(
    "event_bus",
    runtime_event_bus,
    )

    runtime_registry.register_service(
    "event_history",
    runtime_event_history,
   )

    runtime_registry.register_service(
        "memory_engine",
        runtime_memory,
       )
    runtime("Memory Engine Initialized.")

    #runtime_context.registry = runtime_registry
    runtime_context.event_bus = runtime_event_bus
    runtime_context.event_history = runtime_event_history

    runtime_kernel.attach_bus(
        runtime_event_bus,
    )

    runtime_console.attach_bus(
    runtime_event_bus,
    )

    register_logging_handler(
    runtime_event_bus,
    )

    boot("Core Runtime Services Registered")

    # ------------------------------------------------------
    # Runtime Ready
    # ------------------------------------------------------

    runtime_state.set(RuntimeState.READY)

    runtime("Project BRAHMA Runtime Ready")

    runtime_context.memory.remember(

        content="Project BRAHMA Runtime Boot Completed.",

        category=MemoryType.SYSTEM,

        source="runtime",

        importance=1.0,

    )
    
    runtime_event_bus.publish(

    Event(

        event_type=EventType.RUNTIME_READY.value,

        source="runtime.boot",

      )

  )
    return runtime_context


# ==========================================================
# Runtime Summary
# ==========================================================

def runtime_summary():
    """
    Return Runtime Summary.
    """

    return {
        "runtime": runtime_context.runtime_name,
        "version": runtime_context.version,
        "boot_time": runtime_context.boot_time,
        "state": runtime_state.state.name,
        "services": runtime_registry.list_services(),
        "labs": runtime_registry.list_labs(),
        "providers": runtime_registry.list_providers(),
        "event_bus": runtime_event_bus.summary(),
        "event_history": runtime_event_history.summary(),
    }