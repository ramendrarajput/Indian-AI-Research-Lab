"""
===============================================================================
Project BRAHMA
Lifecycle Manager

File:
    lifecycle_manager.py

Purpose:
    Controls the lifecycle of the BRAHMA Runtime.

Description:
    LifecycleManager is the single authority responsible for managing
    runtime states and validating state transitions.

Responsibilities:

    • Runtime lifecycle
    • State transitions
    • Transition validation
    • Runtime status inspection

This class NEVER executes runtime logic.

It only controls lifecycle.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from enum import Enum, auto
from typing import Final


# =============================================================================
# Runtime Lifecycle States
# =============================================================================

class RuntimeState(Enum):
    """
    Runtime lifecycle states.
    """

    CREATED = auto()

    INITIALIZED = auto()

    STARTING = auto()

    RUNNING = auto()

    PAUSED = auto()

    STOPPING = auto()

    STOPPED = auto()

    SHUTDOWN = auto()

    FAILED = auto()


# =============================================================================
# Lifecycle Manager
# =============================================================================

class LifecycleManager:
    """
    Controls runtime lifecycle.

    This class is the only component allowed
    to modify RuntimeState.
    """

    # -------------------------------------------------------------------------

    VALID_TRANSITIONS: Final = {

        RuntimeState.CREATED: {
            RuntimeState.INITIALIZED,
            RuntimeState.FAILED,
        },

        RuntimeState.INITIALIZED: {
            RuntimeState.STARTING,
            RuntimeState.FAILED,
        },

        RuntimeState.STARTING: {
            RuntimeState.RUNNING,
            RuntimeState.FAILED,
        },

        RuntimeState.RUNNING: {
            RuntimeState.PAUSED,
            RuntimeState.STOPPING,
            RuntimeState.FAILED,
        },

        RuntimeState.PAUSED: {
            RuntimeState.RUNNING,
            RuntimeState.STOPPING,
            RuntimeState.FAILED,
        },

        RuntimeState.STOPPING: {
            RuntimeState.STOPPED,
            RuntimeState.FAILED,
        },

        RuntimeState.STOPPED: {
            RuntimeState.SHUTDOWN,
        },

        RuntimeState.SHUTDOWN: set(),

        RuntimeState.FAILED: {
            RuntimeState.SHUTDOWN,
        },
    }

    # -------------------------------------------------------------------------

    def __init__(self) -> None:

        self._state = RuntimeState.CREATED

    # =========================================================================
    # Properties
    # =========================================================================

    @property
    def state(self) -> RuntimeState:
        """
        Current runtime state.
        """

        return self._state

    # -------------------------------------------------------------------------

    def is_running(self) -> bool:

        return self._state == RuntimeState.RUNNING

    # -------------------------------------------------------------------------

    def is_paused(self) -> bool:

        return self._state == RuntimeState.PAUSED

    # -------------------------------------------------------------------------

    def is_shutdown(self) -> bool:

        return self._state == RuntimeState.SHUTDOWN

    # =========================================================================
    # State Transition
    # =========================================================================

    def transition_to(self, new_state: RuntimeState) -> None:
        """
        Transition runtime to a new state.

        Raises
        ------
        RuntimeError
            If transition is invalid.
        """

        allowed = self.VALID_TRANSITIONS[self._state]

        if new_state not in allowed:

            raise RuntimeError(
                f"Invalid lifecycle transition "
                f"{self._state.name} -> {new_state.name}"
            )

        self._state = new_state

    # =========================================================================
    # Convenience Methods
    # =========================================================================

    def initialize(self) -> None:

        self.transition_to(RuntimeState.INITIALIZED)

    # -------------------------------------------------------------------------

    def start(self) -> None:

        self.transition_to(RuntimeState.STARTING)

    # -------------------------------------------------------------------------

    def running(self) -> None:

        self.transition_to(RuntimeState.RUNNING)

    # -------------------------------------------------------------------------

    def pause(self) -> None:

        self.transition_to(RuntimeState.PAUSED)

    # -------------------------------------------------------------------------

    def resume(self) -> None:

        self.transition_to(RuntimeState.RUNNING)

    # -------------------------------------------------------------------------

    def stop(self) -> None:

        self.transition_to(RuntimeState.STOPPING)

    # -------------------------------------------------------------------------

    def stopped(self) -> None:

        self.transition_to(RuntimeState.STOPPED)

    # -------------------------------------------------------------------------

    def shutdown(self) -> None:

        self.transition_to(RuntimeState.SHUTDOWN)

    # -------------------------------------------------------------------------

    def fail(self) -> None:

        self.transition_to(RuntimeState.FAILED)