"""
===============================================================================
Project BRAHMA
Orchestration Context

File:
    orchestration_context.py

Purpose:
    Defines the shared cognitive context used by the orchestration
    engine while coordinating multiple agents.

Description:
    The orchestration context represents the complete working memory
    of an active orchestration session.

    It is intentionally provider-independent and technology-independent.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


# =============================================================================
# Orchestration Context
# =============================================================================

@dataclass(slots=True)
class OrchestrationContext:
    """
    Shared cognitive context for an orchestration session.
    """

    # -------------------------------------------------------------------------
    # Identity
    # -------------------------------------------------------------------------

    session_id: str = field(default_factory=lambda: str(uuid4()))

    orchestration_id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # Observation
    # -------------------------------------------------------------------------

    observation: Any = None

    objective: Any = None

    # -------------------------------------------------------------------------
    # Cognitive Results
    # -------------------------------------------------------------------------

    reasoning = None

    planning = None

    execution = None

    reflection = None

    learning = None

    # -------------------------------------------------------------------------
    # Knowledge
    # -------------------------------------------------------------------------

    memory: Any = None

    knowledge: Any = None

    # -------------------------------------------------------------------------
    # Agent Information
    # -------------------------------------------------------------------------

    active_agents: list[str] = field(default_factory=list)

    completed_agents: list[str] = field(default_factory=list)

    failed_agents: list[str] = field(default_factory=list)

    # -------------------------------------------------------------------------
    # Runtime Information
    # -------------------------------------------------------------------------

    environment: dict[str, Any] = field(default_factory=dict)

    constraints: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    # =========================================================================
    # Agent Tracking
    # =========================================================================

    def activate_agent(
        self,
        agent_name: str,
    ) -> None:

        if agent_name not in self.active_agents:
            self.active_agents.append(agent_name)

    # -------------------------------------------------------------------------

    def complete_agent(
        self,
        agent_name: str,
    ) -> None:

        if agent_name in self.active_agents:
            self.active_agents.remove(agent_name)

        if agent_name not in self.completed_agents:
            self.completed_agents.append(agent_name)

    # -------------------------------------------------------------------------

    def fail_agent(
        self,
        agent_name: str,
    ) -> None:

        if agent_name in self.active_agents:
            self.active_agents.remove(agent_name)

        if agent_name not in self.failed_agents:
            self.failed_agents.append(agent_name)

    # =========================================================================
    # Environment
    # =========================================================================

    def set_environment(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.environment[key] = value

    # -------------------------------------------------------------------------

    def get_environment(
        self,
        key: str,
        default: Any = None,
    ) -> Any:

        return self.environment.get(key, default)

    # =========================================================================
    # Constraints
    # =========================================================================

    def set_constraint(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.constraints[key] = value

    # -------------------------------------------------------------------------

    def get_constraint(
        self,
        key: str,
        default: Any = None,
    ) -> Any:

        return self.constraints.get(key, default)

    # =========================================================================
    # Metadata
    # =========================================================================

    def update_metadata(
        self,
        **kwargs: Any,
    ) -> None:

        self.metadata.update(kwargs)

    # =========================================================================

    def clear(self) -> None:
        """
        Reset runtime information while preserving identity.
        """

        self.observation = None
        self.objective = None

        self.reasoning = None
        self.planning = None
        self.execution = None
        self.reflection = None
        self.learning = None

        self.memory = None
        self.knowledge = None

        self.active_agents.clear()
        self.completed_agents.clear()
        self.failed_agents.clear()

        self.environment.clear()
        self.constraints.clear()
        self.metadata.clear()

    # =========================================================================

    def __repr__(self) -> str:

        return (
            "OrchestrationContext("
            f"session='{self.session_id}', "
            f"active_agents={len(self.active_agents)}, "
            f"completed_agents={len(self.completed_agents)}, "
            f"failed_agents={len(self.failed_agents)})"
        )