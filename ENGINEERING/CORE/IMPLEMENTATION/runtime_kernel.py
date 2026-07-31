"""
===============================================================================
Project BRAHMA
Runtime Kernel

File:
    runtime_kernel.py

Purpose:
    Controls the lifecycle of the BRAHMA Runtime.

Description:
    RuntimeKernel is the execution heart of Project BRAHMA.

    It is responsible for:

        • Runtime State
        • Runtime Loop
        • Tick Execution
        • Pause / Resume
        • Shutdown

    RuntimeKernel NEVER contains business logic.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

import logging
from enum import Enum, auto

from .runtime_context import RuntimeContext

logger = logging.getLogger(__name__)


# =============================================================================
# Runtime States
# =============================================================================

class RuntimeState(Enum):
    """
    Runtime lifecycle states.
    """

    CREATED = auto()

    INITIALIZED = auto()

    RUNNING = auto()

    PAUSED = auto()

    STOPPED = auto()

    SHUTDOWN = auto()


# =============================================================================
# Runtime Kernel
# =============================================================================

class RuntimeKernel:
    """
    BRAHMA Runtime Kernel.

    The kernel owns the runtime execution loop.

    It does not execute AI.

    It executes the runtime itself.
    """

    def __init__(self, context: RuntimeContext):

        self.context = context

        self.state = RuntimeState.CREATED

        self.running = False

        self.tick_count = 0

    # =========================================================================

    def initialize(self) -> None:
        """
        Initialize Runtime.
        """

        logger.info("Initializing Runtime Kernel...")

        self.state = RuntimeState.INITIALIZED

    # =========================================================================

    def start(self) -> None:
        """
        Start Runtime.
        """

        logger.info("Starting Runtime Kernel...")

        self.running = True

        self.state = RuntimeState.RUNNING

    # =========================================================================

    def pause(self) -> None:
        """
        Pause Runtime.
        """

        logger.info("Pausing Runtime...")

        self.state = RuntimeState.PAUSED

    # =========================================================================

    def resume(self) -> None:
        """
        Resume Runtime.
        """

        logger.info("Resuming Runtime...")

        self.state = RuntimeState.RUNNING

    # =========================================================================

    def tick(self) -> None:
        """
        Execute one Runtime Tick.

        Future versions will execute:

            Scheduler

            Event Queue

            Workflow Queue

            Agent Queue

            Monitoring

        No business logic belongs here.
        """

        if self.state != RuntimeState.RUNNING:
            return

        self.tick_count += 1

        logger.debug(f"Runtime Tick {self.tick_count}")

    # =========================================================================

    def stop(self) -> None:
        """
        Stop Runtime.
        """

        logger.info("Stopping Runtime...")

        self.running = False

        self.state = RuntimeState.STOPPED

    # =========================================================================

    def shutdown(self) -> None:
        """
        Shutdown Runtime.
        """

        logger.info("Shutting down Runtime...")

        self.running = False

        self.state = RuntimeState.SHUTDOWN

    # =========================================================================

    @property
    def is_running(self) -> bool:
        """
        Runtime running state.
        """

        return self.state == RuntimeState.RUNNING

    # =========================================================================

    @property
    def current_state(self) -> RuntimeState:
        """
        Current Runtime State.
        """

        return self.state