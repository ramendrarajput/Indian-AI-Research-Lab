"""
===============================================================================
Project BRAHMA
Orchestration Coordinator

File:
    orchestration_coordinator.py

Purpose:
    Coordinates multiple cognitive agents during orchestration.

Description:
    The Coordinator is responsible for executing scheduled agents,
    collecting their outputs, and maintaining a unified orchestration
    context.

    The Coordinator never performs cognition.

    It coordinates cognition.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .orchestration_context import OrchestrationContext
from .orchestration_scheduler import (
    ExecutionSchedule,
    ExecutionMode,
)


# =============================================================================
# Agent Result
# =============================================================================

@dataclass(slots=True)
class AgentExecutionResult:
    """
    Result produced by a single cognitive agent.
    """

    agent_name: str

    success: bool

    output: Any = None

    error: str | None = None


# =============================================================================
# Coordination Result
# =============================================================================

@dataclass(slots=True)
class CoordinationResult:
    """
    Complete orchestration output.
    """

    success: bool

    results: list[AgentExecutionResult] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)


# =============================================================================
# Orchestration Coordinator
# =============================================================================

class OrchestrationCoordinator:
    """
    Coordinates execution of multiple cognitive agents.
    """

    # ---------------------------------------------------------------------

    def execute(
        self,
        *,
        schedule: ExecutionSchedule,
        registry,
        context: OrchestrationContext,
    ) -> CoordinationResult:
        """
        Execute all scheduled agents.
        """

        result = CoordinationResult(success=True)

        if schedule.mode == ExecutionMode.SEQUENTIAL:

            for task in schedule.tasks:

                execution = self._execute_agent(

                    task.agent_name,

                    registry,

                    context,
                )

                result.results.append(execution)

                if not execution.success:

                    result.success = False

        elif schedule.mode == ExecutionMode.PARALLEL:

            #
            # Current implementation executes sequentially.
            #
            # Future implementation may use:
            #
            # asyncio
            # threading
            # multiprocessing
            # distributed execution
            #

            for task in schedule.tasks:

                execution = self._execute_agent(

                    task.agent_name,

                    registry,

                    context,
                )

                result.results.append(execution)

                if not execution.success:

                    result.success = False

        elif schedule.mode == ExecutionMode.DEPENDENCY:

            #
            # Future dependency graph execution.
            #

            for task in schedule.tasks:

                execution = self._execute_agent(

                    task.agent_name,

                    registry,

                    context,
                )

                result.results.append(execution)

                if not execution.success:

                    result.success = False

        result.metadata["execution_mode"] = schedule.mode.name

        result.metadata["agents"] = len(result.results)

        return result

    # =========================================================================

    def _execute_agent(
        self,
        agent_name: str,
        registry,
        context: OrchestrationContext,
    ) -> AgentExecutionResult:
        """
        Execute one registered agent.
        """

        agent = registry.get(agent_name)

        if agent is None:

            return AgentExecutionResult(

                agent_name=agent_name,

                success=False,

                error="Agent not registered.",
            )

        context.activate_agent(agent_name)

        try:

            #
            # Universal execution entry point.
            #
            output = agent.run(context)

            context.complete_agent(agent_name)

            return AgentExecutionResult(

                agent_name=agent_name,

                success=True,

                output=output,
            )

        except Exception as exc:

            context.fail_agent(agent_name)

            return AgentExecutionResult(

                agent_name=agent_name,

                success=False,

                error=str(exc),
            )

    # =========================================================================

    def merge_results(
        self,
        coordination: CoordinationResult,
    ) -> dict[str, Any]:
        """
        Merge all successful outputs into one structure.
        """

        merged = {}

        for result in coordination.results:

            if result.success:

                merged[result.agent_name] = result.output

        return merged

    # =========================================================================

    def __repr__(self) -> str:

        return "OrchestrationCoordinator()"