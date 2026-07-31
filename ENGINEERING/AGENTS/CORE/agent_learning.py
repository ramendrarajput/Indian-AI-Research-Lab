"""
===============================================================================
Project BRAHMA
Agent Learning

File:
    agent_learning.py

Purpose:
    Defines the learning interface used by every BRAHMA Agent.

Description:
    Learning transforms reflection into future improvement.

    Reflection answers:

        What happened?

    Learning answers:

        What should permanently change?

    Learning modifies future behaviour,
    not past execution.

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
# Learning Status
# =============================================================================

class LearningStatus(str, Enum):

    CREATED = "created"

    APPLIED = "applied"

    REJECTED = "rejected"

    FAILED = "failed"


# =============================================================================
# Learning Result
# =============================================================================

@dataclass(slots=True)
class LearningResult:
    """
    Represents knowledge extracted from experience.

    LearningResult is intended to improve future behaviour.
    """

    uid: str = field(default_factory=lambda: str(uuid4()))

    status: LearningStatus = LearningStatus.CREATED

    knowledge: list[str] = field(default_factory=list)

    improvements: list[str] = field(default_factory=list)

    updated_capabilities: list[str] = field(default_factory=list)

    updated_constraints: list[str] = field(default_factory=list)

    confidence: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # -------------------------------------------------------------------------

    def add_knowledge(self, text: str) -> None:

        self.knowledge.append(text)

    # -------------------------------------------------------------------------

    def add_improvement(self, text: str) -> None:

        self.improvements.append(text)

    # -------------------------------------------------------------------------

    def add_capability_update(self, text: str) -> None:

        self.updated_capabilities.append(text)

    # -------------------------------------------------------------------------

    def add_constraint_update(self, text: str) -> None:

        self.updated_constraints.append(text)

    # -------------------------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "uid": self.uid,
            "status": self.status.value,
            "knowledge": self.knowledge,
            "improvements": self.improvements,
            "updated_capabilities": self.updated_capabilities,
            "updated_constraints": self.updated_constraints,
            "confidence": self.confidence,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }


# =============================================================================
# Learning Interface
# =============================================================================

class AgentLearning(ABC):
    """
    Abstract learning interface.

    Every learning engine inside Project BRAHMA
    must inherit this interface.
    """

    # -------------------------------------------------------------------------

    @abstractmethod
    def learn(
        self,
        reflection: Any,
        *,
        memory: Any = None,
        context: Any = None,
    ) -> LearningResult:
        """
        Transform reflection into reusable knowledge.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def apply(
        self,
        learning: LearningResult,
    ) -> bool:
        """
        Apply learned improvements to the Agent or Runtime.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def validate(
        self,
        learning: LearningResult,
    ) -> bool:
        """
        Validate consistency of learned knowledge.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def learning_engine(self) -> str:
        """
        Human-readable learning engine.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def learning_strategy(self) -> str:
        """
        Examples:

            supervised
            reinforcement
            symbolic
            experiential
            hybrid
            evolutionary
        """

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(engine={self.learning_engine})"
        )