"""
===============================================================================
Project BRAHMA
Agent Reflection

File:
    agent_reflection.py

Purpose:
    Defines the reflection interface used by every BRAHMA Agent.

Description:
    Reflection evaluates completed execution.

    Reflection does NOT perform execution.

    Reflection does NOT create plans.

    Reflection answers:

        • What happened?
        • Was the objective achieved?
        • Why did it succeed?
        • Why did it fail?
        • What should improve?

    Reflection transforms execution into experience.

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
# Reflection Status
# =============================================================================

class ReflectionStatus(str, Enum):

    CREATED = "created"

    COMPLETED = "completed"

    FAILED = "failed"


# =============================================================================
# Reflection Result
# =============================================================================

@dataclass(slots=True)
class ReflectionResult:
    """
    Result produced after reflecting on execution.
    """

    uid: str = field(default_factory=lambda: str(uuid4()))

    status: ReflectionStatus = ReflectionStatus.CREATED

    success: bool = False

    score: float = 0.0

    summary: str = ""

    strengths: list[str] = field(default_factory=list)

    weaknesses: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)

    lessons: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # -------------------------------------------------------------------------

    def add_strength(self, text: str) -> None:

        self.strengths.append(text)

    # -------------------------------------------------------------------------

    def add_weakness(self, text: str) -> None:

        self.weaknesses.append(text)

    # -------------------------------------------------------------------------

    def add_recommendation(self, text: str) -> None:

        self.recommendations.append(text)

    # -------------------------------------------------------------------------

    def add_lesson(self, text: str) -> None:

        self.lessons.append(text)

    # -------------------------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "uid": self.uid,
            "status": self.status.value,
            "success": self.success,
            "score": self.score,
            "summary": self.summary,
            "strengths": self.strengths,
            "weaknesses": self.weaknesses,
            "recommendations": self.recommendations,
            "lessons": self.lessons,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }


# =============================================================================
# Reflection Interface
# =============================================================================

class AgentReflection(ABC):
    """
    Abstract reflection interface.

    Every reflection engine inside Project BRAHMA must inherit
    this interface.
    """

    # -------------------------------------------------------------------------

    @abstractmethod
    def reflect(
        self,
        *,
        objective: Any,
        plan: Any,
        execution: Any,
        context: Any = None,
    ) -> ReflectionResult:
        """
        Evaluate completed execution.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def summarize(
        self,
        reflection: ReflectionResult,
    ) -> str:
        """
        Produce a concise summary of reflection.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def validate(
        self,
        reflection: ReflectionResult,
    ) -> bool:
        """
        Validate reflection consistency.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def reflection_engine(self) -> str:
        """
        Human-readable reflection engine.
        """

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(engine={self.reflection_engine})"
        )