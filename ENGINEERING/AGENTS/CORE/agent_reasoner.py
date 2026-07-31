"""
===============================================================================
Project BRAHMA
Agent Reasoner

File:
    agent_reasoner.py

Purpose:
    Defines the abstract reasoning interface used by every BRAHMA Agent.

Description:
    Reasoning is independent of any AI model.

    LLMs are only one possible implementation of reasoning.

    Every reasoning engine inside Project BRAHMA must inherit this
    interface.

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
# Reasoning Status
# =============================================================================

class ReasoningStatus(str, Enum):

    CREATED = "created"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"


# =============================================================================
# Reasoning Result
# =============================================================================

@dataclass(slots=True)
class ReasoningResult:
    """
    Output produced by a reasoning engine.

    This object is model-independent.
    """

    uid: str = field(default_factory=lambda: str(uuid4()))

    status: ReasoningStatus = ReasoningStatus.CREATED

    understanding: Any = None

    confidence: float = 1.0

    evidence: list[Any] = field(default_factory=list)

    assumptions: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # -------------------------------------------------------------------------

    def add_evidence(self, item: Any) -> None:

        self.evidence.append(item)

    # -------------------------------------------------------------------------

    def add_assumption(self, text: str) -> None:

        self.assumptions.append(text)

    # -------------------------------------------------------------------------

    @property
    def succeeded(self) -> bool:

        return self.status == ReasoningStatus.COMPLETED

    # -------------------------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "uid": self.uid,
            "status": self.status.value,
            "confidence": self.confidence,
            "evidence": self.evidence,
            "assumptions": self.assumptions,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }


# =============================================================================
# Agent Reasoner Interface
# =============================================================================

class AgentReasoner(ABC):
    """
    Abstract reasoning interface.

    Every reasoning implementation
    (LLM, Symbolic AI, Rule Engine, Hybrid AI, etc.)
    must inherit this interface.
    """

    # -------------------------------------------------------------------------

    @abstractmethod
    def reason(
        self,
        observation: Any,
        *,
        context: Any = None,
        objective: Any = None,
        memory: Any = None,
    ) -> ReasoningResult:
        """
        Transform knowledge into understanding.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def explain(
        self,
        result: ReasoningResult,
    ) -> str:
        """
        Explain why the reasoning reached its conclusion.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def validate(
        self,
        result: ReasoningResult,
    ) -> bool:
        """
        Validate internal consistency of the reasoning result.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def engine_name(self) -> str:
        """
        Human-readable reasoning engine.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def reasoning_type(self) -> str:
        """
        Examples:

            symbolic
            neural
            probabilistic
            hybrid
            logical
        """

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(engine={self.engine_name})"
        )