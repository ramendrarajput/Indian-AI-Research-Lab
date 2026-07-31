"""
===============================================================================
Project BRAHMA
Universal Agent

Version:
    2.0

Purpose:
    Defines the canonical public interface to the Project BRAHMA
    Cognitive Operating System.

Description:
    UniversalAgent never performs cognition.

    It is a façade.

    All cognition is delegated to the Orchestration Layer.

Architecture

    Application
            │
            ▼
    UniversalAgent
            │
            ▼
      Orchestrator
            │
            ▼
    Cognitive Ecosystem

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .agent_identity import AgentIdentity
from .agent_context import AgentContext
from .agent_objective import AgentObjective
from .agent_capability import AgentCapability
from .agent_memory import AgentMemory

from .ORCHESTRATION.orchestrator import Orchestrator


# =============================================================================
# Universal Agent
# =============================================================================

@dataclass(slots=True)
class UniversalAgent:
    """
    Universal Cognitive Interface.

    The UniversalAgent owns metadata.

    The Orchestrator owns cognition.
    """

    identity: AgentIdentity

    context: AgentContext

    objective: AgentObjective

    capability: AgentCapability

    memory: AgentMemory

    orchestrator: Orchestrator

    # =========================================================================
    # Initialization
    # =========================================================================

    def initialize(
        self,
        *,
        observation: Any,
        objective: Any,
    ) -> None:
        """
        Initialize one cognitive session.
        """

        self.orchestrator.initialize(

            observation=observation,

            objective=objective,
        )

    # =========================================================================
    # Public Execution Interface
    # =========================================================================

    def run(
        self,
        observation: Any,
    ) -> Any:
        """
        Execute one complete cognitive cycle.

        The UniversalAgent performs no reasoning.

        It delegates everything to the Orchestrator.
        """

        # -------------------------------------------------------------
        # Initialize Runtime
        # -------------------------------------------------------------

        self.initialize(

            observation=observation,

            objective=self.objective,
        )

        # -------------------------------------------------------------
        # Delegate Complete Cognition
        # -------------------------------------------------------------

        result = self.orchestrator.execute_pipeline(

            agent=self
        )

        return result

    # =========================================================================
    # Delegation Layer
    #
    # These methods are intentionally thin wrappers.
    #
    # They delegate to implementation-specific behaviour.
    #
    # GeminiAgent
    # ClaudeAgent
    # OpenAIAgent
    # PhysicsAgent
    #
    # override these methods.
    # =========================================================================

    def reason(
        self,
        **kwargs,
    ):
        raise NotImplementedError()

    # -------------------------------------------------------------------------

    def plan(
        self,
        **kwargs,
    ):
        raise NotImplementedError()

    # -------------------------------------------------------------------------

    def execute(
        self,
        **kwargs,
    ):
        raise NotImplementedError()

    # -------------------------------------------------------------------------

    def reflect(
        self,
        **kwargs,
    ):
        raise NotImplementedError()

    # -------------------------------------------------------------------------

    def learn(
        self,
        **kwargs,
    ):
        raise NotImplementedError()

    # =========================================================================
    # Health
    # =========================================================================

    @property
    def implementation_name(self) -> str:
        """
        Returns implementation identity.

        Override inside implementation agents.
        """

        return "UniversalAgent"

    # -------------------------------------------------------------------------

    @property
    def capability_names(self) -> tuple[str, ...]:
        """
        Returns available capabilities.

        Override inside implementation agents.
        """

        return tuple()

    # =========================================================================

    def shutdown(self) -> None:
        """
        Shutdown cognitive session.

        Future versions may release resources here.
        """

        pass

    # =========================================================================

    def __repr__(self) -> str:

        return (
            "UniversalAgent("
            f"{self.identity.fullname})"
        )