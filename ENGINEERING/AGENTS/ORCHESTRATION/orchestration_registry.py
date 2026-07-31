"""
===============================================================================
Project BRAHMA
Orchestration Registry

File:
    orchestration_registry.py

Purpose:
    Maintains the registry of all cognitive agents available to the
    Project BRAHMA orchestration engine.

Description:
    The registry acts as the discovery layer between the orchestrator
    and cognitive agents.

    The orchestrator never directly depends upon any implementation.

    Instead,

    it queries this registry.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from typing import Dict, Iterator, Optional


# =============================================================================
# Orchestration Registry
# =============================================================================

class OrchestrationRegistry:
    """
    Universal registry of cognitive agents.
    """

    # ---------------------------------------------------------------------

    def __init__(self) -> None:

        self._agents: Dict[str, object] = {}

    # =========================================================================
    # Registration
    # =========================================================================

    def register(
        self,
        name: str,
        agent: object,
    ) -> None:
        """
        Register a cognitive agent.
        """

        if name in self._agents:

            raise ValueError(
                f"Agent '{name}' is already registered."
            )

        self._agents[name] = agent

    # ---------------------------------------------------------------------

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove an agent from the registry.
        """

        self._agents.pop(name, None)

    # =========================================================================
    # Lookup
    # =========================================================================

    def get(
        self,
        name: str,
    ) -> Optional[object]:
        """
        Retrieve an agent by name.
        """

        return self._agents.get(name)

    # ---------------------------------------------------------------------

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._agents

    # =========================================================================
    # Discovery
    # =========================================================================

    def list_agents(self) -> tuple[str, ...]:
        """
        Return all registered agent names.
        """

        return tuple(sorted(self._agents.keys()))

    # ---------------------------------------------------------------------

    def count(self) -> int:

        return len(self._agents)

    # =========================================================================
    # Iteration
    # =========================================================================

    def __iter__(self) -> Iterator[tuple[str, object]]:

        return iter(self._agents.items())

    # =========================================================================
    # Maintenance
    # =========================================================================

    def clear(self) -> None:
        """
        Remove every registered agent.
        """

        self._agents.clear()

    # =========================================================================

    def __contains__(self, name: str) -> bool:

        return name in self._agents

    # ---------------------------------------------------------------------

    def __len__(self) -> int:

        return len(self._agents)

    # ---------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"OrchestrationRegistry("
            f"agents={len(self._agents)})"
        )


# =============================================================================
# Global Registry
# =============================================================================

GLOBAL_REGISTRY = OrchestrationRegistry()