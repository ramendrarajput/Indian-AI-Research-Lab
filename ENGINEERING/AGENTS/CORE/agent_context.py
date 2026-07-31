"""
===============================================================================
Project BRAHMA
Agent Context

File:
    agent_context.py

Purpose:
    Defines the runtime context within which an Agent exists.

Description:
    Context represents the current operating universe of an Agent.

    Unlike AgentIdentity, Context is mutable.

    Context changes continuously during execution.

    Context does NOT define who the Agent is.

    Context defines where, when, and under which conditions
    the Agent is currently operating.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


# =============================================================================
# Agent Context
# =============================================================================

@dataclass(slots=True)
class AgentContext:
    """
    Runtime operating context of an Agent.

    Context is dynamic.

    It evolves during execution.

    Every Agent receives a Context from the Runtime.
    """

    # -------------------------------------------------------------------------
    # Runtime Session
    # -------------------------------------------------------------------------

    session_id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # Runtime Identifier
    # -------------------------------------------------------------------------

    runtime_id: str = ""

    # -------------------------------------------------------------------------
    # Current Environment
    # -------------------------------------------------------------------------

    environment: str = "default"

    # -------------------------------------------------------------------------
    # Current Workspace
    # -------------------------------------------------------------------------

    workspace: str = ""

    # -------------------------------------------------------------------------
    # Active User
    # -------------------------------------------------------------------------

    user_id: str = ""

    # -------------------------------------------------------------------------
    # Active Task
    # -------------------------------------------------------------------------

    task_id: str = ""

    # -------------------------------------------------------------------------
    # Conversation
    # -------------------------------------------------------------------------

    conversation_id: str = ""

    # -------------------------------------------------------------------------
    # Current Timestamp
    # -------------------------------------------------------------------------

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # -------------------------------------------------------------------------
    # Shared Runtime Objects
    # -------------------------------------------------------------------------

    runtime: Any = None

    memory: Any = None

    planner: Any = None

    reasoner: Any = None

    executor: Any = None

    event_bus: Any = None

    storage: Any = None

    registry: Any = None

    observability: Any = None

    security: Any = None

    scheduler: Any = None

    coordinator: Any = None

    orchestrator: Any = None

    monitor: Any = None

    history: Any = None

    # -------------------------------------------------------------------------
    # Arbitrary Metadata
    # -------------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # =========================================================================
    # Context API
    # =========================================================================

    def update_timestamp(self) -> None:
        """
        Refresh execution timestamp.
        """

        self.timestamp = datetime.now(timezone.utc)

    # =========================================================================

    def set_metadata(self, key: str, value: Any) -> None:
        """
        Store metadata inside context.
        """

        self.metadata[key] = value

    # =========================================================================

    def get_metadata(self, key: str, default=None):
        """
        Read metadata.
        """

        return self.metadata.get(key, default)

    # =========================================================================

    def clear_metadata(self) -> None:
        """
        Remove all temporary metadata.
        """

        self.metadata.clear()

    # =========================================================================

    def to_dict(self) -> dict:
        """
        Serialize context.

        Heavy runtime objects are intentionally omitted.
        """

        return {
            "session_id": self.session_id,
            "runtime_id": self.runtime_id,
            "environment": self.environment,
            "workspace": self.workspace,
            "user_id": self.user_id,
            "task_id": self.task_id,
            "conversation_id": self.conversation_id,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata,
        }

    # =========================================================================

    def __str__(self) -> str:

        return (
            f"AgentContext("
            f"session={self.session_id}, "
            f"environment={self.environment})"
        )