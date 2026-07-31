"""
===============================================================================
Project BRAHMA
Agent Planner

File:
    agent_planner.py

Purpose:
    Defines the abstract planning interface used by every BRAHMA Agent.

Description:
    Planning transforms understanding into an executable plan.

    A Planner never performs execution.

    It only decides:

        • What should be done
        • In what order
        • Under which constraints

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
# Planning Status
# =============================================================================

class PlanningStatus(str, Enum):

    CREATED = "created"

    READY = "ready"

    FAILED = "failed"


# =============================================================================
# Plan Step
# =============================================================================

@dataclass(slots=True)
class PlanStep:
    """
    Represents one executable step inside a plan.
    """

    step_id: str = field(default_factory=lambda: str(uuid4()))

    title: str = ""

    description: str = ""

    capability: str = ""

    expected_output: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)


# =============================================================================
# Planning Result
# =============================================================================

@dataclass(slots=True)
class PlanningResult:
    """
    Output produced by the Planner.
    """

    uid: str = field(default_factory=lambda: str(uuid4()))

    status: PlanningStatus = PlanningStatus.CREATED

    objective: Any = None

    understanding: Any = None

    steps: list[PlanStep] = field(default_factory=list)

    assumptions: list[str] = field(default_factory=list)

    constraints: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # -------------------------------------------------------------------------

    def add_step(self, step: PlanStep) -> None:

        self.steps.append(step)

    # -------------------------------------------------------------------------

    def add_assumption(self, text: str) -> None:

        self.assumptions.append(text)

    # -------------------------------------------------------------------------

    def add_constraint(self, text: str) -> None:

        self.constraints.append(text)

    # -------------------------------------------------------------------------

    @property
    def total_steps(self) -> int:

        return len(self.steps)

    # -------------------------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "uid": self.uid,
            "status": self.status.value,
            "steps": [step.__dict__ for step in self.steps],
            "assumptions": self.assumptions,
            "constraints": self.constraints,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }


# =============================================================================
# Planner Interface
# =============================================================================

class AgentPlanner(ABC):
    """
    Abstract planning interface.

    Every planning engine must inherit this class.
    """

    # -------------------------------------------------------------------------

    @abstractmethod
    def plan(
        self,
        *,
        objective: Any,
        understanding: Any,
        context: Any = None,
        capability: Any = None,
    ) -> PlanningResult:
        """
        Generate an execution plan.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def revise(
        self,
        plan: PlanningResult,
        feedback: Any,
    ) -> PlanningResult:
        """
        Revise an existing plan.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def validate(
        self,
        plan: PlanningResult,
    ) -> bool:
        """
        Validate structural consistency of a plan.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def planner_name(self) -> str:
        """
        Human-readable planner name.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def planning_strategy(self) -> str:
        """
        Examples:

            sequential
            hierarchical
            tree-search
            graph
            reactive
            hybrid
        """

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(planner={self.planner_name})"
        )