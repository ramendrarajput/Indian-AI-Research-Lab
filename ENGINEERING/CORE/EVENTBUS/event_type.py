"""
PROJECT BRAHMA
Universal Event Types

Author
------
Ramendra Singh Rajput

Description
-----------
Defines all standard event types used throughout
Project BRAHMA.

Every event published on the Universal Event Bus must
use one of these event types.

Future
------
• Runtime Events
• Agent Events
• Laboratory Events
• Memory Events
• GUI Events
• Voice Events
• Distributed Events
"""

from __future__ import annotations

from enum import Enum


class EventType(str, Enum):
    """
    Universal BRAHMA Event Types.
    """

    # ======================================================
    # Runtime
    # ======================================================

    RUNTIME_BOOT = "runtime.boot"

    RUNTIME_READY = "runtime.ready"

    RUNTIME_START = "runtime.start"

    RUNTIME_STOP = "runtime.stop"

    RUNTIME_RESTART = "runtime.restart"

    RUNTIME_ERROR = "runtime.error"

    # ======================================================
    # Kernel
    # ======================================================

    KERNEL_START = "kernel.start"

    KERNEL_READY = "kernel.ready"

    KERNEL_STOP = "kernel.stop"

    KERNEL_ERROR = "kernel.error"

    # ======================================================
    # Console
    # ======================================================

    CONSOLE_STARTED = "console.started"

    COMMAND_RECEIVED = "console.command"

    UNKNOWN_COMMAND = "console.unknown"

    # ======================================================
    # Laboratories
    # ======================================================

    LAB_REGISTERED = "lab.registered"

    LAB_LOADED = "lab.loaded"

    LAB_UNLOADED = "lab.unloaded"

    # ======================================================
    # Universal Agent
    # ======================================================

    AGENT_INITIALIZED = "agent.initialized"

    AGENT_STARTED = "agent.started"

    AGENT_STOPPED = "agent.stopped"

    # ======================================================
    # Memory
    # ======================================================

    MEMORY_INITIALIZED = "memory.initialized"

    MEMORY_UPDATED = "memory.updated"

    MEMORY_SAVED = "memory.saved"

    MEMORY_LOADED = "memory.loaded"

    # ======================================================
    # Scheduler
    # ======================================================

    TASK_CREATED = "task.created"

    TASK_STARTED = "task.started"

    TASK_COMPLETED = "task.completed"

    TASK_FAILED = "task.failed"

    # ======================================================
    # Generic
    # ======================================================

    INFO = "system.info"

    WARNING = "system.warning"

    ERROR = "system.error"