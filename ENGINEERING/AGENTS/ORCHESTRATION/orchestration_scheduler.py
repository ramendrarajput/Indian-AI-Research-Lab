"""
===============================================================================
Project BRAHMA
Orchestration Scheduler

File:
    orchestration_scheduler.py

Purpose:
    Determines WHEN and IN WHAT ORDER cognitive agents execute.

Description:
    The Scheduler never selects agents.

    The Router selects agents.

    The Scheduler schedules execution.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Iterable


# =============================================================================
# Execution Mode
# =============================================================================

class ExecutionMode(Enum):
    """
    Supported scheduling modes.
    """

    SEQUENTIAL = auto()

    PARALLEL = auto()

    DEPENDENCY = auto()


# =============================================================================
# Scheduled Task
# =============================================================================

@dataclass(slots=True)
class ScheduledTask:
    """
    Represents one scheduled execution task.
    """

    agent_name: str

    priority: int = 0

    dependencies: list[str] = field(default_factory=list)


# =============================================================================
# Execution Schedule
# =============================================================================

@dataclass(slots=True)
class ExecutionSchedule:
    """
    Ordered execution schedule.
    """

    mode: ExecutionMode

    tasks: list[ScheduledTask]


# =============================================================================
# Scheduler
# =============================================================================

class OrchestrationScheduler:
    """
    Universal cognitive scheduler.
    """

    # ---------------------------------------------------------------------

    def sequential(
        self,
        agents: Iterable[str],
    ) -> ExecutionSchedule:
        """
        Schedule agents sequentially.
        """

        tasks = [

            ScheduledTask(
                agent_name=name,
                priority=index,
            )

            for index, name in enumerate(agents)

        ]

        return ExecutionSchedule(

            mode=ExecutionMode.SEQUENTIAL,

            tasks=tasks,
        )

    # ---------------------------------------------------------------------

    def parallel(
        self,
        agents: Iterable[str],
    ) -> ExecutionSchedule:
        """
        Schedule agents for parallel execution.
        """

        tasks = [

            ScheduledTask(
                agent_name=name,
                priority=0,
            )

            for name in agents

        ]

        return ExecutionSchedule(

            mode=ExecutionMode.PARALLEL,

            tasks=tasks,
        )

    # ---------------------------------------------------------------------

    def dependency(
        self,
        tasks: Iterable[ScheduledTask],
    ) -> ExecutionSchedule:
        """
        Dependency-aware schedule.
        """

        return ExecutionSchedule(

            mode=ExecutionMode.DEPENDENCY,

            tasks=list(tasks),
        )

    # =========================================================================

    def sort_by_priority(
        self,
        schedule: ExecutionSchedule,
    ) -> ExecutionSchedule:
        """
        Sort tasks by priority.
        """

        schedule.tasks.sort(

            key=lambda task: task.priority

        )

        return schedule

    # =========================================================================

    def validate(
        self,
        schedule: ExecutionSchedule,
    ) -> bool:
        """
        Basic schedule validation.
        """

        names = {

            task.agent_name

            for task in schedule.tasks

        }

        for task in schedule.tasks:

            for dependency in task.dependencies:

                if dependency not in names:

                    return False

        return True

    # =========================================================================

    def __repr__(self) -> str:

        return "OrchestrationScheduler()"