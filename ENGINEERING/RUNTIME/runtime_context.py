"""
===============================================================================
Project BRAHMA
Runtime Context

File:
    runtime_context.py

Purpose:
    Defines the shared runtime execution context for Project BRAHMA.

Description:
    RuntimeContext represents the live execution environment of an
    active Project BRAHMA runtime.

    Unlike AgentContext, which belongs to a single Agent execution,
    RuntimeContext belongs to the Runtime itself.

    RuntimeContext manages shared runtime resources such as

        • Runtime Memory
        • Event Bus
        • Registry
        • Active Agents
        • Global Metadata
        • Runtime State

    Every Agent receives a reference to RuntimeContext through its
    AgentContext.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .MEMORY.in_memory import InMemory


# =============================================================================
# Runtime Context
# =============================================================================

@dataclass(slots=True)
class RuntimeContext:
    """
    Shared execution context for an active BRAHMA Runtime.
    """

    # -------------------------------------------------------------------------
    # Runtime Identification
    # -------------------------------------------------------------------------

    runtime_id: str = field(default_factory=lambda: str(uuid4()))

    runtime_name: str = "Project BRAHMA Runtime"

    runtime_version: str = "0.1"

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # -------------------------------------------------------------------------
    # Runtime Components
    # -------------------------------------------------------------------------

    memory: InMemory = field(default_factory=InMemory)

    event_bus: Any = None

    registry: Any = None

    scheduler: Any = None

    coordinator: Any = None

    monitor: Any = None

    history: Any = None

    security: Any = None

    logger: Any = None

    # -------------------------------------------------------------------------
    # Runtime References
    # -------------------------------------------------------------------------

    runtime: Any = None

    orchestrator: Any = None

    # -------------------------------------------------------------------------
    # Active Objects
    # -------------------------------------------------------------------------

    active_agents: dict[str, Any] = field(default_factory=dict)

    active_sessions: dict[str, Any] = field(default_factory=dict)

    active_tasks: dict[str, Any] = field(default_factory=dict)

    # -------------------------------------------------------------------------
    # Runtime Metadata
    # -------------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # =========================================================================
    # Agent Management
    # =========================================================================

    def register_agent(
        self,
        agent: Any,
    ) -> None:
        """
        Register an active agent.
        """

        identity = getattr(agent, "identity", None)

        if identity is None:
            raise ValueError(
                "Agent has no identity."
            )

        self.active_agents[identity.uid] = agent

    # -------------------------------------------------------------------------

    def unregister_agent(
        self,
        agent_uid: str,
    ) -> None:

        self.active_agents.pop(
            agent_uid,
            None,
        )

    # -------------------------------------------------------------------------

    def get_agent(
        self,
        agent_uid: str,
    ) -> Any:

        return self.active_agents.get(agent_uid)

    # =========================================================================
    # Session Management
    # =========================================================================

    def register_session(
        self,
        session_id: str,
        session: Any,
    ) -> None:

        self.active_sessions[session_id] = session

    # -------------------------------------------------------------------------

    def unregister_session(
        self,
        session_id: str,
    ) -> None:

        self.active_sessions.pop(
            session_id,
            None,
        )

    # =========================================================================
    # Task Management
    # =========================================================================

    def register_task(
        self,
        task_id: str,
        task: Any,
    ) -> None:

        self.active_tasks[task_id] = task

    # -------------------------------------------------------------------------

    def unregister_task(
        self,
        task_id: str,
    ) -> None:

        self.active_tasks.pop(
            task_id,
            None,
        )

    # =========================================================================
    # Metadata
    # =========================================================================

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.metadata[key] = value

    # -------------------------------------------------------------------------

    def get_metadata(
        self,
        key: str,
        default=None,
    ):

        return self.metadata.get(
            key,
            default,
        )

    # =========================================================================
    # Runtime Information
    # =========================================================================

    @property
    def total_agents(self) -> int:

        return len(self.active_agents)

    # -------------------------------------------------------------------------

    @property
    def total_sessions(self) -> int:

        return len(self.active_sessions)

    # -------------------------------------------------------------------------

    @property
    def total_tasks(self) -> int:

        return len(self.active_tasks)

    # =========================================================================

    def statistics(self) -> dict:
        """
        Runtime statistics.
        """

        return {
            "runtime_id": self.runtime_id,
            "runtime_name": self.runtime_name,
            "runtime_version": self.runtime_version,
            "created_at": self.created_at.isoformat(),
            "agents": self.total_agents,
            "sessions": self.total_sessions,
            "tasks": self.total_tasks,
            "memory": self.memory.statistics(),
        }

    # =========================================================================

    def clear(self) -> None:
        """
        Reset runtime.
        """

        self.memory.clear()

        self.active_agents.clear()

        self.active_sessions.clear()

        self.active_tasks.clear()

        self.metadata.clear()

    # =========================================================================

    def __repr__(self) -> str:

        return (
            "RuntimeContext("
            f"agents={self.total_agents}, "
            f"sessions={self.total_sessions}, "
            f"tasks={self.total_tasks})"
        )