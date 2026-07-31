"""
===============================================================================
Project BRAHMA
Runtime Kernel

File:
    runtime_kernel.py

Purpose:
    Initializes, manages and shuts down the BRAHMA Runtime.

Description:
    RuntimeKernel is the central operating component of Project BRAHMA.

    Responsibilities

        • Boot Runtime
        • Create RuntimeContext
        • Initialize Memory
        • Initialize Runtime Components
        • Register Agents
        • Shutdown Runtime

    RuntimeKernel NEVER performs cognition.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum

from .runtime_context import RuntimeContext


# =============================================================================
# Runtime State
# =============================================================================

class RuntimeState(str, Enum):

    CREATED = "created"

    INITIALIZING = "initializing"

    READY = "ready"

    RUNNING = "running"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"


# =============================================================================
# Runtime Kernel
# =============================================================================

class RuntimeKernel:
    """
    Central Runtime Controller.
    """

    # ---------------------------------------------------------------------

    def __init__(self) -> None:

        self.context = RuntimeContext()

        self.state = RuntimeState.CREATED

        self.boot_time = None

    # =========================================================================
    # Boot
    # =========================================================================

    def boot(self) -> RuntimeContext:
        """
        Boot Project BRAHMA Runtime.
        """

        self.state = RuntimeState.INITIALIZING

        self.boot_time = datetime.now(timezone.utc)

        # -------------------------------------------------------------
        # Initialize Runtime Components
        # -------------------------------------------------------------

        self.initialize_memory()

        self.initialize_registry()

        self.initialize_scheduler()

        self.initialize_coordinator()

        self.initialize_monitor()

        self.initialize_history()

        self.initialize_security()

        self.initialize_logger()

        # -------------------------------------------------------------

        self.state = RuntimeState.READY

        return self.context

    # =========================================================================
    # Component Initialization
    # =========================================================================

    def initialize_memory(self):

        # Already created by RuntimeContext

        return self.context.memory

    # ---------------------------------------------------------------------

    def initialize_registry(self):

        return self.context.registry

    # ---------------------------------------------------------------------

    def initialize_scheduler(self):

        return self.context.scheduler

    # ---------------------------------------------------------------------

    def initialize_coordinator(self):

        return self.context.coordinator

    # ---------------------------------------------------------------------

    def initialize_monitor(self):

        return self.context.monitor

    # ---------------------------------------------------------------------

    def initialize_history(self):

        return self.context.history

    # ---------------------------------------------------------------------

    def initialize_security(self):

        return self.context.security

    # ---------------------------------------------------------------------

    def initialize_logger(self):

        return self.context.logger

    # =========================================================================
    # Runtime Lifecycle
    # =========================================================================

    def start(self) -> None:

        if self.state != RuntimeState.READY:

            raise RuntimeError(
                "Runtime must be READY before start()."
            )

        self.state = RuntimeState.RUNNING

    # ---------------------------------------------------------------------

    def stop(self) -> None:

        self.state = RuntimeState.STOPPING

        self.context.clear()

        self.state = RuntimeState.STOPPED

    # =========================================================================
    # Agent Registration
    # =========================================================================

    def register_agent(self, agent) -> None:

        self.context.register_agent(agent)

    # ---------------------------------------------------------------------

    def unregister_agent(self, agent_uid: str) -> None:

        self.context.unregister_agent(agent_uid)

    # =========================================================================
    # Information
    # =========================================================================

    @property
    def is_ready(self) -> bool:

        return self.state == RuntimeState.READY

    # ---------------------------------------------------------------------

    @property
    def is_running(self) -> bool:

        return self.state == RuntimeState.RUNNING

    # ---------------------------------------------------------------------

    def statistics(self) -> dict:

        return {

            "state": self.state.value,

            "boot_time": (
                self.boot_time.isoformat()
                if self.boot_time
                else None
            ),

            "runtime": self.context.statistics(),
        }

    # =========================================================================

    def __repr__(self) -> str:

        return (
            "RuntimeKernel("
            f"state={self.state.value})"
        )