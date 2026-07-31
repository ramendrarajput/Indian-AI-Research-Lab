"""
===============================================================================
Project BRAHMA
Agent Objective

File:
    agent_objective.py

Purpose:
    Defines objectives that drive intelligent behavior.

Description:
    Objectives represent WHY an Agent acts.

    Identity answers:
        "Who am I?"

    Context answers:
        "Where am I?"

    Objective answers:
        "What am I trying to accomplish?"

    Objectives are dynamic and may evolve during execution.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


# =============================================================================
# Objective Status
# =============================================================================

class ObjectiveStatus(str, Enum):
    """
    Current lifecycle state of an objective.
    """

    CREATED = "created"

    ACTIVE = "active"

    PAUSED = "paused"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"


# =============================================================================
# Objective Priority
# =============================================================================

class ObjectivePriority(int, Enum):
    """
    Priority of an objective.
    """

    LOW = 10

    NORMAL = 50

    HIGH = 75

    CRITICAL = 100


# =============================================================================
# Agent Objective
# =============================================================================

@dataclass(slots=True)
class AgentObjective:
    """
    Represents a single goal pursued by an Agent.
    """

    # -------------------------------------------------------------------------
    # Permanent Identifier
    # -------------------------------------------------------------------------

    uid: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # Human Readable Title
    # -------------------------------------------------------------------------

    title: str = ""

    # -------------------------------------------------------------------------
    # Detailed Description
    # -------------------------------------------------------------------------

    description: str = ""

    # -------------------------------------------------------------------------
    # Status
    # -------------------------------------------------------------------------

    status: ObjectiveStatus = ObjectiveStatus.CREATED

    # -------------------------------------------------------------------------
    # Priority
    # -------------------------------------------------------------------------

    priority: ObjectivePriority = ObjectivePriority.NORMAL

    # -------------------------------------------------------------------------
    # Parent Objective
    # -------------------------------------------------------------------------

    parent_id: str | None = None

    # -------------------------------------------------------------------------
    # Success Criteria
    # -------------------------------------------------------------------------

    success_criteria: list[str] = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Constraints
    # -------------------------------------------------------------------------

    constraints: list[str] = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Metadata
    # -------------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # -------------------------------------------------------------------------
    # Creation Time
    # -------------------------------------------------------------------------

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # =========================================================================
    # State Management
    # =========================================================================

    def activate(self) -> None:

        self.status = ObjectiveStatus.ACTIVE

    # -------------------------------------------------------------------------

    def pause(self) -> None:

        self.status = ObjectiveStatus.PAUSED

    # -------------------------------------------------------------------------

    def complete(self) -> None:

        self.status = ObjectiveStatus.COMPLETED

    # -------------------------------------------------------------------------

    def fail(self) -> None:

        self.status = ObjectiveStatus.FAILED

    # -------------------------------------------------------------------------

    def cancel(self) -> None:

        self.status = ObjectiveStatus.CANCELLED

    # =========================================================================
    # Success Criteria
    # =========================================================================

    def add_success_criterion(self, criterion: str) -> None:

        self.success_criteria.append(criterion)

    # -------------------------------------------------------------------------

    def add_constraint(self, constraint: str) -> None:

        self.constraints.append(constraint)

    # =========================================================================
    # Metadata
    # =========================================================================

    def set_metadata(self, key: str, value: Any) -> None:

        self.metadata[key] = value

    # -------------------------------------------------------------------------

    def get_metadata(self, key: str, default=None):

        return self.metadata.get(key, default)

    # =========================================================================

    @property
    def is_active(self) -> bool:

        return self.status == ObjectiveStatus.ACTIVE

    # -------------------------------------------------------------------------

    @property
    def is_finished(self) -> bool:

        return self.status in (
            ObjectiveStatus.COMPLETED,
            ObjectiveStatus.FAILED,
            ObjectiveStatus.CANCELLED,
        )

    # =========================================================================

    def to_dict(self) -> dict:

        return {
            "uid": self.uid,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": int(self.priority),
            "parent_id": self.parent_id,
            "success_criteria": self.success_criteria,
            "constraints": self.constraints,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

    # =========================================================================

    def __str__(self) -> str:

        return f"{self.title} [{self.status.value}]"