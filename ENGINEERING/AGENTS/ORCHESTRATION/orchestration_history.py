"""
===============================================================================
Project BRAHMA
Orchestration History

File:
    orchestration_history.py

Purpose:
    Maintains the immutable execution history of orchestration sessions.

Description:
    History represents what actually happened during orchestration.

    Unlike runtime context, history is never modified after recording.

    It forms the long-term evidence base for:

        • Reflection
        • Learning
        • Benchmarking
        • Auditing
        • Scientific reproducibility

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


# =============================================================================
# History Record
# =============================================================================

@dataclass(slots=True, frozen=True)
class HistoryRecord:
    """
    Immutable orchestration history record.
    """

    history_id: str

    session_id: str

    timestamp: datetime

    state: str

    objective: Any

    observation: Any

    participating_agents: tuple[str, ...]

    successful_agents: tuple[str, ...]

    failed_agents: tuple[str, ...]

    execution_time: float | None

    metadata: dict[str, Any]


# =============================================================================
# Orchestration History
# =============================================================================

class OrchestrationHistory:
    """
    Long-term immutable orchestration history.
    """

    # -------------------------------------------------------------------------

    def __init__(self) -> None:

        self._records: list[HistoryRecord] = []

    # =========================================================================
    # Recording
    # =========================================================================

    def record(
        self,
        *,
        session_id: str,
        state: str,
        objective: Any,
        observation: Any,
        participating_agents: list[str],
        successful_agents: list[str],
        failed_agents: list[str],
        execution_time: float | None,
        metadata: dict[str, Any] | None = None,
    ) -> HistoryRecord:
        """
        Record one orchestration execution.
        """

        history = HistoryRecord(

            history_id=str(uuid4()),

            session_id=session_id,

            timestamp=datetime.utcnow(),

            state=state,

            objective=objective,

            observation=observation,

            participating_agents=tuple(participating_agents),

            successful_agents=tuple(successful_agents),

            failed_agents=tuple(failed_agents),

            execution_time=execution_time,

            metadata=dict(metadata or {}),
        )

        self._records.append(history)

        return history

    # =========================================================================
    # Query
    # =========================================================================

    def all(self) -> tuple[HistoryRecord, ...]:

        return tuple(self._records)

    # -------------------------------------------------------------------------

    def latest(self) -> HistoryRecord | None:

        if not self._records:
            return None

        return self._records[-1]

    # -------------------------------------------------------------------------

    def by_session(
        self,
        session_id: str,
    ) -> tuple[HistoryRecord, ...]:

        return tuple(

            record

            for record in self._records

            if record.session_id == session_id

        )

    # =========================================================================
    # Statistics
    # =========================================================================

    @property
    def total_records(self) -> int:

        return len(self._records)

    # -------------------------------------------------------------------------

    @property
    def successful_records(self) -> int:

        return sum(

            1

            for record in self._records

            if len(record.failed_agents) == 0

        )

    # -------------------------------------------------------------------------

    @property
    def failed_records(self) -> int:

        return self.total_records - self.successful_records

    # =========================================================================
    # Maintenance
    # =========================================================================

    def clear(self) -> None:
        """
        Clear stored history.

        Intended primarily for testing.
        """

        self._records.clear()

    # =========================================================================

    def __len__(self) -> int:

        return len(self._records)

    # -------------------------------------------------------------------------

    def __iter__(self):

        return iter(self._records)

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            "OrchestrationHistory("
            f"records={len(self._records)})"
        )