"""
===============================================================================
Project BRAHMA
Agent Identity

File:
    agent_identity.py

Purpose:
    Defines the immutable digital identity of every BRAHMA Agent.

Description:
    Identity is the first principle of intelligence.

    Every Agent inside Project BRAHMA possesses a permanent identity
    that remains stable throughout its lifetime.

    Identity is NOT runtime state.

    Identity is NOT memory.

    Identity is NOT context.

    Identity represents WHO the Agent is,
    not WHAT the Agent is currently doing.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4


# =============================================================================
# Agent Categories
# =============================================================================

class AgentCategory(str, Enum):
    """
    High-level Agent classification.
    """

    UNIVERSAL = "universal"

    RESEARCH = "research"

    SCIENTIFIC = "scientific"

    AI = "ai"

    PHYSICS = "physics"

    BIOLOGY = "biology"

    MATHEMATICS = "mathematics"

    ROBOTICS = "robotics"

    MEMORY = "memory"

    PLANNING = "planning"

    EXECUTION = "execution"

    CUSTOM = "custom"


# =============================================================================
# Agent Identity
# =============================================================================

@dataclass(frozen=True, slots=True)
class AgentIdentity:
    """
    Immutable identity of a BRAHMA Agent.

    This object uniquely identifies an Agent independently of:

        • Runtime
        • Framework
        • AI Model
        • Memory
        • Execution State

    Once created, identity never changes.
    """

    # -------------------------------------------------------------------------
    # Permanent Identifier
    # -------------------------------------------------------------------------

    uid: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # Human Readable Name
    # -------------------------------------------------------------------------

    name: str = "UnnamedAgent"

    # -------------------------------------------------------------------------
    # Agent Category
    # -------------------------------------------------------------------------

    category: AgentCategory = AgentCategory.UNIVERSAL

    # -------------------------------------------------------------------------
    # Version
    # -------------------------------------------------------------------------

    version: str = "1.0.0"

    # -------------------------------------------------------------------------
    # Creator
    # -------------------------------------------------------------------------

    creator: str = "Project BRAHMA"

    # -------------------------------------------------------------------------
    # Description
    # -------------------------------------------------------------------------

    description: str = ""

    # -------------------------------------------------------------------------
    # Creation Time
    # -------------------------------------------------------------------------

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # -------------------------------------------------------------------------
    # Optional Domain
    # -------------------------------------------------------------------------

    domain: str = ""

    # -------------------------------------------------------------------------
    # Optional Tags
    # -------------------------------------------------------------------------

    tags: tuple[str, ...] = ()

    # =========================================================================

    @property
    def fullname(self) -> str:
        """
        Human-readable identity string.
        """

        return f"{self.name} ({self.version})"

    # =========================================================================

    @property
    def is_universal(self) -> bool:
        """
        Returns True if this is a Universal Agent.
        """

        return self.category == AgentCategory.UNIVERSAL

    # =========================================================================

    def to_dict(self) -> dict:
        """
        Serialize identity.
        """

        return {
            "uid": self.uid,
            "name": self.name,
            "category": self.category.value,
            "version": self.version,
            "creator": self.creator,
            "description": self.description,
            "domain": self.domain,
            "tags": list(self.tags),
            "created_at": self.created_at.isoformat(),
        }

    # =========================================================================

    def __str__(self) -> str:

        return self.fullname