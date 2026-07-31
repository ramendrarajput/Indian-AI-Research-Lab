"""
===============================================================================
Project BRAHMA
Orchestration State

File:
    orchestration_state.py

Purpose:
    Defines the universal cognitive state machine used by the
    Project BRAHMA orchestration engine.

Description:
    Every orchestration workflow exists in exactly one state.

    The orchestrator transitions between these states while
    coordinating cognitive agents.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime


# =============================================================================
# Cognitive State Enumeration
# =============================================================================

class OrchestrationState(Enum):
    """
    Universal orchestration lifecycle.
    """

    # -------------------------------------------------------------------------
    # Lifecycle
    # -------------------------------------------------------------------------

    CREATED = auto()

    INITIALIZED = auto()

    READY = auto()

    # -------------------------------------------------------------------------
    # Cognitive Pipeline
    # -------------------------------------------------------------------------

    OBSERVING = auto()

    REASONING = auto()

    PLANNING = auto()

    EXECUTING = auto()

    REFLECTING = auto()

    LEARNING = auto()

    # -------------------------------------------------------------------------
    # Coordination
    # -------------------------------------------------------------------------

    ROUTING = auto()

    SYNCHRONIZING = auto()

    WAITING = auto()

    # -------------------------------------------------------------------------
    # Completion
    # -------------------------------------------------------------------------

    COMPLETED = auto()

    FAILED = auto()

    CANCELLED = auto()

    RECOVERING = auto()


# =============================================================================
# State Record
# =============================================================================

@dataclass(slots=True)
class StateRecord:
    """
    Represents one state transition.
    """

    state: OrchestrationState

    timestamp: datetime

    description: str = ""


# =============================================================================
# State Machine
# =============================================================================

class OrchestrationStateMachine:
    """
    Maintains the current orchestration state.
    """

    def __init__(self) -> None:

        self._current_state = OrchestrationState.CREATED

        self._history: list[StateRecord] = [
            StateRecord(
                state=self._current_state,
                timestamp=datetime.utcnow(),
                description="Orchestration created",
            )
        ]

    # =========================================================================

    @property
    def current_state(self) -> OrchestrationState:

        return self._current_state

    # =========================================================================

    @property
    def history(self) -> tuple[StateRecord, ...]:

        return tuple(self._history)

    # =========================================================================

    def transition_to(
        self,
        state: OrchestrationState,
        description: str = "",
    ) -> None:
        """
        Transition orchestration to a new state.
        """

        self._current_state = state

        self._history.append(

            StateRecord(

                state=state,

                timestamp=datetime.utcnow(),

                description=description,
            )
        )

    # =========================================================================

    def reset(self) -> None:
        """
        Reset orchestration lifecycle.
        """

        self._current_state = OrchestrationState.CREATED

        self._history.clear()

        self._history.append(

            StateRecord(

                state=self._current_state,

                timestamp=datetime.utcnow(),

                description="State machine reset",
            )
        )

    # =========================================================================

    def is_terminal(self) -> bool:
        """
        Returns True if orchestration has finished.
        """

        return self._current_state in {

            OrchestrationState.COMPLETED,

            OrchestrationState.CANCELLED,

            OrchestrationState.FAILED,
        }

    # =========================================================================

    def __repr__(self) -> str:

        return (
            f"OrchestrationStateMachine("
            f"state={self._current_state.name})"
        )