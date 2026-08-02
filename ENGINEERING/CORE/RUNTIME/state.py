"""
PROJECT BRAHMA
Runtime State Management

Author:
    Ramendra Singh Rajput

Description:
    Defines the global runtime state for the BRAHMA Universal Runtime.

The Runtime State represents the current lifecycle stage of the system.

Boot
↓
Initialization
↓
Kernel Loading
↓
Runtime Ready
↓
Shutdown

Every runtime component reads this state instead of maintaining
its own independent status.
"""

from __future__ import annotations

from enum import Enum, auto


class RuntimeState(Enum):
    """
    Universal Runtime Lifecycle States.
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


class RuntimeStatus:
    """
    Stores the current runtime status.

    A single shared object should be used across the runtime.
    """

    def __init__(self):
        self._state = RuntimeState.CREATED

    @property
    def state(self) -> RuntimeState:
        return self._state

    def set(self, state: RuntimeState) -> None:
        self._state = state

    def is_ready(self) -> bool:
        return self._state == RuntimeState.READY

    def is_running(self) -> bool:
        return self._state == RuntimeState.RUNNING

    def is_failed(self) -> bool:
        return self._state == RuntimeState.FAILED

    def reset(self) -> None:
        self._state = RuntimeState.CREATED

    def __str__(self) -> str:
        return self._state.name


#
# Global Runtime State
#

runtime_state = RuntimeStatus()