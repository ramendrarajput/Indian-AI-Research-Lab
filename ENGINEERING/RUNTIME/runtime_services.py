"""
===============================================================================
Project BRAHMA
Runtime Services

File:
    runtime_services.py

Purpose:
    Provides a unified service interface to the Runtime.

Description:
    RuntimeServices exposes all Runtime-managed components through a
    stable public API.

    The application should access Runtime resources through this class
    instead of directly navigating Runtime internals.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from .runtime_context import RuntimeContext


# =============================================================================
# Runtime Services
# =============================================================================

@dataclass(slots=True)
class RuntimeServices:
    """
    Public Runtime Service Locator.

    Wraps RuntimeContext and exposes commonly used services.
    """

    context: RuntimeContext

    # =========================================================================
    # Core Services
    # =========================================================================

    @property
    def memory(self):
        return self.context.memory

    # -------------------------------------------------------------------------

    @property
    def registry(self):
        return self.context.registry

    # -------------------------------------------------------------------------

    @property
    def scheduler(self):
        return self.context.scheduler

    # -------------------------------------------------------------------------

    @property
    def coordinator(self):
        return self.context.coordinator

    # -------------------------------------------------------------------------

    @property
    def orchestrator(self):
        return self.context.orchestrator

    # -------------------------------------------------------------------------

    @property
    def monitor(self):
        return self.context.monitor

    # -------------------------------------------------------------------------

    @property
    def history(self):
        return self.context.history

    # -------------------------------------------------------------------------

    @property
    def security(self):
        return self.context.security

    # =========================================================================
    # Agent Management
    # =========================================================================

    def register_agent(self, agent) -> None:
        """
        Register an agent with the Runtime Registry.
        """

        if self.registry is not None:
            self.registry.register(agent)

    # -------------------------------------------------------------------------

    def unregister_agent(self, agent) -> None:
        """
        Remove an agent from the Runtime Registry.
        """

        if self.registry is not None:
            self.registry.unregister(agent)

    # =========================================================================
    # Context Injection
    # =========================================================================

    def inject_into_agent(self, agent) -> None:
        """
        Inject Runtime-managed services into an AgentContext.
        """

        agent.context.runtime = self.context.runtime

        agent.context.memory = self.memory

        agent.context.registry = self.registry

        agent.context.scheduler = self.scheduler

        agent.context.coordinator = self.coordinator

        agent.context.orchestrator = self.orchestrator

        agent.context.monitor = self.monitor

        agent.context.history = self.history

        agent.context.security = self.security

    # =========================================================================
    # Diagnostics
    # =========================================================================

    def health(self) -> dict:
        """
        Runtime service availability.
        """

        return {
            "memory": self.memory is not None,
            "registry": self.registry is not None,
            "scheduler": self.scheduler is not None,
            "coordinator": self.coordinator is not None,
            "orchestrator": self.orchestrator is not None,
            "monitor": self.monitor is not None,
            "history": self.history is not None,
            "security": self.security is not None,
        }

    # =========================================================================

    def __repr__(self) -> str:

        healthy = sum(self.health().values())

        total = len(self.health())

        return (
            f"RuntimeServices("
            f"healthy={healthy}/{total})"
        )