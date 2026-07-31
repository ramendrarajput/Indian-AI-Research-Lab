"""
===============================================================================
Project BRAHMA
Cognitive Protocol

File:
    cognitive_protocol.py

Purpose:
    Defines the universal cognitive interface implemented by every
    intelligent agent inside Project BRAHMA.

Description:
    The protocol establishes the minimum contract required for an
    implementation agent to participate in the BRAHMA Cognitive
    Operating System.

    Every implementation must expose the same cognitive lifecycle.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


# =============================================================================
# Cognitive Protocol
# =============================================================================

@runtime_checkable
class CognitiveProtocol(Protocol):
    """
    Universal cognitive interface.

    Every implementation agent must implement this protocol.
    """

    # -------------------------------------------------------------------------
    # Identity
    # -------------------------------------------------------------------------

    @property
    def implementation_name(self) -> str:
        ...

    # -------------------------------------------------------------------------

    @property
    def capability_names(self) -> tuple[str, ...]:
        ...

    # =========================================================================
    # Cognitive Lifecycle
    # =========================================================================

    def reason(
        self,
        *,
        observation: Any,
        context: Any,
        objective: Any,
        memory: Any,
    ) -> Any:
        """
        Produce understanding from observation.
        """
        ...

    # -------------------------------------------------------------------------

    def plan(
        self,
        *,
        reasoning: Any,
        context: Any,
        objective: Any,
        capability: Any,
    ) -> Any:
        """
        Produce an executable plan.
        """
        ...

    # -------------------------------------------------------------------------

    def execute(
        self,
        *,
        plan: Any,
        context: Any,
    ) -> Any:
        """
        Execute the generated plan.
        """
        ...

    # -------------------------------------------------------------------------

    def reflect(
        self,
        *,
        plan: Any,
        execution: Any,
        context: Any,
        objective: Any,
    ) -> Any:
        """
        Evaluate execution quality.
        """
        ...

    # -------------------------------------------------------------------------

    def learn(
        self,
        *,
        reflection: Any,
        context: Any,
        memory: Any,
    ) -> Any:
        """
        Convert reflection into long-term learning.
        """
        ...

    # =========================================================================

    def health_check(self) -> bool:
        """
        Verify implementation health.
        """
        ...