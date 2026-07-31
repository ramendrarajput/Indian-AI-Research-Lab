"""
===============================================================================
Project BRAHMA
Agent Capability

File:
    agent_capability.py

Purpose:
    Defines what an Agent is capable of doing.

Description:
    Capability represents an abstract intelligent ability.

    Capability is NOT a tool.

    Capability is NOT an implementation.

    A Capability may be fulfilled by one or more concrete tools,
    models, APIs, services, or algorithms.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


# =============================================================================
# Capability Category
# =============================================================================

class CapabilityCategory(str, Enum):
    """
    High-level capability classification.
    """

    PERCEPTION = "perception"

    REASONING = "reasoning"

    PLANNING = "planning"

    EXECUTION = "execution"

    MEMORY = "memory"

    COMMUNICATION = "communication"

    KNOWLEDGE = "knowledge"

    COMPUTATION = "computation"

    OBSERVATION = "observation"

    LEARNING = "learning"

    CUSTOM = "custom"


# =============================================================================
# Capability
# =============================================================================

@dataclass(slots=True)
class AgentCapability:
    """
    Represents one abstract capability of an Agent.
    """

    # -------------------------------------------------------------------------

    uid: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------

    name: str = ""

    # -------------------------------------------------------------------------

    description: str = ""

    # -------------------------------------------------------------------------

    category: CapabilityCategory = CapabilityCategory.CUSTOM

    # -------------------------------------------------------------------------
    # Whether this capability is currently available.
    # -------------------------------------------------------------------------

    enabled: bool = True

    # -------------------------------------------------------------------------
    # Optional implementation reference.
    #
    # Example:
    #
    #   Search Capability
    #          ↓
    #   DuckDuckGo Tool
    #
    # This keeps Capability independent from implementation.
    # -------------------------------------------------------------------------

    implementation: Any = None

    # -------------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # =========================================================================

    def enable(self) -> None:

        self.enabled = True

    # -------------------------------------------------------------------------

    def disable(self) -> None:

        self.enabled = False

    # =========================================================================

    @property
    def is_available(self) -> bool:

        return self.enabled

    # =========================================================================

    def set_metadata(self, key: str, value: Any) -> None:

        self.metadata[key] = value

    # -------------------------------------------------------------------------

    def get_metadata(self, key: str, default=None):

        return self.metadata.get(key, default)

    # =========================================================================

    def supports(self, capability_name: str) -> bool:
        """
        Compare capability names.

        Comparison is case-insensitive.
        """

        return self.name.lower() == capability_name.lower()

    # =========================================================================

    def to_dict(self) -> dict:

        return {
            "uid": self.uid,
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "enabled": self.enabled,
            "metadata": self.metadata,
        }

    # =========================================================================

    def __str__(self) -> str:

        state = "Enabled" if self.enabled else "Disabled"

        return f"{self.name} ({state})"