"""
===============================================================================
Project BRAHMA
Agent Executor

File:
    agent_executor.py

Purpose:
    Defines the execution interface used by every BRAHMA Agent.

Description:
    Execution transforms an approved plan into observable actions.

    The Executor never performs:

        • reasoning
        • planning
        • memory management

    It only executes.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


# =============================================================================
# Execution Status
# =============================================================================

class ExecutionStatus(str, Enum):

    CREATED = "created"

    RUNNING = "running"

    SUCCESS = "success"

    FAILED = "failed"

    CANCELLED = "cancelled"


# =============================================================================
# Execution Step Result
# =============================================================================

@dataclass(slots=True)
class ExecutionStepResult:
    """
    Result of one executed plan step.
    """

    step_id: str

    status: ExecutionStatus

    output: Any = None

    error: str = ""

    started_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    finished_at: datetime | None = None

    metadata: dict[str, Any] = field(default_factory=dict)


# =============================================================================
# Execution Result
# =============================================================================

@dataclass(slots=True)
class ExecutionResult:
    """
    Complete execution result.
    """

    uid: str = field(default_factory=lambda: str(uuid4()))

    status: ExecutionStatus = ExecutionStatus.CREATED

    outputs: list[ExecutionStepResult] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    started_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    finished_at: datetime | None = None

    # -------------------------------------------------------------------------

    def add_step_result(
        self,
        result: ExecutionStepResult,
    ) -> None:

        self.outputs.append(result)

    # -------------------------------------------------------------------------

    @property
    def successful_steps(self) -> int:

        return sum(
            1
            for step in self.outputs
            if step.status == ExecutionStatus.SUCCESS
        )

    # -------------------------------------------------------------------------

    @property
    def failed_steps(self) -> int:

        return sum(
            1
            for step in self.outputs
            if step.status == ExecutionStatus.FAILED
        )

    # -------------------------------------------------------------------------

    @property
    def total_steps(self) -> int:

        return len(self.outputs)

    # -------------------------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "uid": self.uid,
            "status": self.status.value,
            "steps": [
                {
                    "step_id": step.step_id,
                    "status": step.status.value,
                    "error": step.error,
                }
                for step in self.outputs
            ],
            "started_at": self.started_at.isoformat(),
            "finished_at": (
                self.finished_at.isoformat()
                if self.finished_at
                else None
            ),
            "metadata": self.metadata,
        }


# =============================================================================
# Executor Interface
# =============================================================================

class AgentExecutor(ABC):
    """
    Abstract execution interface.

    Every execution engine inside Project BRAHMA must inherit
    this interface.
    """

    # -------------------------------------------------------------------------

    @abstractmethod
    def execute(
        self,
        plan: Any,
        *,
        context: Any = None,
    ) -> ExecutionResult:
        """
        Execute an approved execution plan.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def execute_step(
        self,
        step: Any,
        *,
        context: Any = None,
    ) -> ExecutionStepResult:
        """
        Execute a single step.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def cancel(self) -> None:
        """
        Cancel the current execution.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def executor_name(self) -> str:
        """
        Human-readable executor name.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def execution_backend(self) -> str:
        """
        Examples

            local
            remote
            workflow
            robot
            cloud
            hybrid
        """

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(backend={self.execution_backend})"
        )