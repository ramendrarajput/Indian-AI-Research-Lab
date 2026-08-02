"""
PROJECT BRAHMA
Universal Runtime State

Author
------
Ramendra Singh Rajput

Description
-----------
Defines the global lifecycle state of the Project BRAHMA Runtime.

Every runtime component must read and update the same RuntimeState.

There is exactly ONE runtime lifecycle.

Runtime Lifecycle

CREATED
    ↓
BOOTING
    ↓
INITIALIZING
    ↓
LOADING_KERNEL
    ↓
LOADING_SERVICES
    ↓
LOADING_LABS
    ↓
READY
    ↓
RUNNING
    ↓
PAUSED
    ↓
STOPPING
    ↓
STOPPED

If any fatal error occurs

FAILED

Philosophy
----------
One Runtime

↓

One State

↓

One Truth
"""

from __future__ import annotations

from enum import Enum, auto


# ==========================================================
# Runtime Lifecycle
# ==========================================================

class RuntimeState(Enum):
    """
    Universal Runtime Lifecycle.
    """

    CREATED = auto()

    BOOTING = auto()

    INITIALIZING = auto()

    LOADING_KERNEL = auto()

    LOADING_SERVICES = auto()

    LOADING_LABS = auto()

    READY = auto()

    RUNNING = auto()

    PAUSED = auto()

    STOPPING = auto()

    STOPPED = auto()

    FAILED = auto()


# ==========================================================
# Runtime State Manager
# ==========================================================

class RuntimeStatus:
    """
    Global Runtime State Manager.

    Every runtime module shares the same instance.
    """

    def __init__(self):

        self._state = RuntimeState.CREATED

    # ------------------------------------------------------

    @property
    def state(self) -> RuntimeState:

        return self._state

    # ------------------------------------------------------

    def get(self) -> RuntimeState:

        return self._state

    # ------------------------------------------------------

    def set(self, state: RuntimeState) -> None:

        self._state = state

    # ------------------------------------------------------
    # State Checks
    # ------------------------------------------------------

    def is_created(self) -> bool:

        return self._state == RuntimeState.CREATED

    def is_booting(self) -> bool:

        return self._state == RuntimeState.BOOTING

    def is_initializing(self) -> bool:

        return self._state == RuntimeState.INITIALIZING

    def is_loading_kernel(self) -> bool:

        return self._state == RuntimeState.LOADING_KERNEL

    def is_loading_services(self) -> bool:

        return self._state == RuntimeState.LOADING_SERVICES

    def is_loading_labs(self) -> bool:

        return self._state == RuntimeState.LOADING_LABS

    def is_ready(self) -> bool:

        return self._state == RuntimeState.READY

    def is_running(self) -> bool:

        return self._state == RuntimeState.RUNNING

    def is_paused(self) -> bool:

        return self._state == RuntimeState.PAUSED

    def is_stopping(self) -> bool:

        return self._state == RuntimeState.STOPPING

    def is_stopped(self) -> bool:

        return self._state == RuntimeState.STOPPED

    def is_failed(self) -> bool:

        return self._state == RuntimeState.FAILED

    # ------------------------------------------------------

    def reset(self) -> None:

        self._state = RuntimeState.CREATED

    # ------------------------------------------------------

    def __str__(self):

        return self._state.name


# ==========================================================
# Global Runtime State
# ==========================================================

runtime_state = RuntimeStatus()