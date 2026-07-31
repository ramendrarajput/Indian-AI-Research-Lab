"""
===============================================================================
Project BRAHMA
Orchestration Router

File:
    orchestration_router.py

Purpose:
    Responsible for selecting the most appropriate cognitive agent
    for a given task.

Description:
    The router never executes agents.

    It only decides WHICH agent should execute.

    Routing decisions are capability-based rather than
    implementation-based.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional, Protocol


# =============================================================================
# Routing Request
# =============================================================================

@dataclass(slots=True)
class RoutingRequest:
    """
    Represents a routing decision request.
    """

    objective: object

    observation: object

    required_capabilities: tuple[str, ...] = ()

    preferred_agent: str | None = None


# =============================================================================
# Routable Agent Protocol
# =============================================================================

class RoutableAgent(Protocol):

    @property
    def implementation_name(self) -> str:
        ...

    @property
    def capability_names(self) -> tuple[str, ...]:
        ...


# =============================================================================
# Orchestration Router
# =============================================================================

class OrchestrationRouter:
    """
    Capability-based agent router.
    """

    # ---------------------------------------------------------------------

    def route(
        self,
        request: RoutingRequest,
        agents: Iterable[RoutableAgent],
    ) -> Optional[RoutableAgent]:
        """
        Select the most appropriate agent.
        """

        # -------------------------------------------------------------
        # Explicit Preference
        # -------------------------------------------------------------

        if request.preferred_agent:

            for agent in agents:

                if (
                    agent.implementation_name
                    == request.preferred_agent
                ):
                    return agent

        # -------------------------------------------------------------
        # Capability Matching
        # -------------------------------------------------------------

        required = set(request.required_capabilities)

        best_agent = None

        best_score = -1

        for agent in agents:

            available = set(agent.capability_names)

            score = len(
                required.intersection(
                    available
                )
            )

            if score > best_score:

                best_score = score

                best_agent = agent

        return best_agent

    # =========================================================================

    def supports(
        self,
        capability: str,
        agent: RoutableAgent,
    ) -> bool:

        return capability in agent.capability_names

    # =========================================================================

    def capability_score(
        self,
        capabilities: Iterable[str],
        agent: RoutableAgent,
    ) -> int:

        requested = set(capabilities)

        available = set(agent.capability_names)

        return len(
            requested.intersection(
                available
            )
        )

    # =========================================================================

    def __repr__(self) -> str:

        return "OrchestrationRouter()"