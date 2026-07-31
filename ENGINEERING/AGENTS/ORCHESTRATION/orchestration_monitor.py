"""
===============================================================================
Project BRAHMA
Orchestration Monitor

File:
    orchestration_monitor.py

Purpose:
    Provides runtime monitoring for the Project BRAHMA orchestration
    engine.

Description:
    The monitor observes the orchestration lifecycle without changing it.

    It measures:

        • execution state
        • execution time
        • running agents
        • completed agents
        • failures
        • orchestration health

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .orchestration_state import (
    OrchestrationStateMachine,
)

from .orchestration_context import (
    OrchestrationContext,
)


# =============================================================================
# Monitoring Snapshot
# =============================================================================

@dataclass(slots=True)
class MonitoringSnapshot:
    """
    Immutable orchestration snapshot.
    """

    timestamp: datetime

    current_state: str

    active_agents: tuple[str, ...]

    completed_agents: tuple[str, ...]

    failed_agents: tuple[str, ...]

    metadata: dict[str, Any]


# =============================================================================
# Performance Statistics
# =============================================================================

@dataclass(slots=True)
class PerformanceStatistics:
    """
    Runtime performance metrics.
    """

    started_at: datetime | None = None

    finished_at: datetime | None = None

    total_sessions: int = 0

    successful_sessions: int = 0

    failed_sessions: int = 0

    # -------------------------------------------------------------------------

    @property
    def execution_time_seconds(self) -> float | None:

        if self.started_at is None:
            return None

        if self.finished_at is None:
            return None

        return (
            self.finished_at - self.started_at
        ).total_seconds()


# =============================================================================
# Orchestration Monitor
# =============================================================================

class OrchestrationMonitor:
    """
    Runtime monitor for orchestration.
    """

    # -------------------------------------------------------------------------

    def __init__(self) -> None:

        self.statistics = PerformanceStatistics()

        self._snapshots: list[MonitoringSnapshot] = []

    # =========================================================================
    # Session Lifecycle
    # =========================================================================

    def session_started(self) -> None:

        self.statistics.started_at = datetime.utcnow()

        self.statistics.finished_at = None

        self.statistics.total_sessions += 1

    # -------------------------------------------------------------------------

    def session_completed(
        self,
        success: bool,
    ) -> None:

        self.statistics.finished_at = datetime.utcnow()

        if success:

            self.statistics.successful_sessions += 1

        else:

            self.statistics.failed_sessions += 1

    # =========================================================================
    # Snapshot
    # =========================================================================

    def capture(
        self,
        *,
        state: OrchestrationStateMachine,
        context: OrchestrationContext,
    ) -> MonitoringSnapshot:
        """
        Capture current orchestration state.
        """

        snapshot = MonitoringSnapshot(

            timestamp=datetime.utcnow(),

            current_state=state.current_state.name,

            active_agents=tuple(context.active_agents),

            completed_agents=tuple(context.completed_agents),

            failed_agents=tuple(context.failed_agents),

            metadata=dict(context.metadata),
        )

        self._snapshots.append(snapshot)

        return snapshot

    # =========================================================================
    # Health
    # =========================================================================

    def health(self) -> dict[str, Any]:
        """
        Return orchestration health summary.
        """

        return {

            "total_sessions":
                self.statistics.total_sessions,

            "successful_sessions":
                self.statistics.successful_sessions,

            "failed_sessions":
                self.statistics.failed_sessions,

            "execution_time":
                self.statistics.execution_time_seconds,

            "snapshots":
                len(self._snapshots),
        }

    # =========================================================================
    # History
    # =========================================================================

    @property
    def snapshots(
        self,
    ) -> tuple[MonitoringSnapshot, ...]:

        return tuple(self._snapshots)

    # =========================================================================

    def clear(self) -> None:

        self._snapshots.clear()

    # =========================================================================

    def __repr__(self) -> str:

        return (
            "OrchestrationMonitor("
            f"sessions={self.statistics.total_sessions}, "
            f"snapshots={len(self._snapshots)})"
        )