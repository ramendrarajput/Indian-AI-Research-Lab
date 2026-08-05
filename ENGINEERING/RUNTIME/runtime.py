"""
===============================================================================
Project BRAHMA
Runtime

File:
    runtime.py

Purpose:
    Public Runtime interface for Project BRAHMA.

Description:
    Runtime represents the complete execution environment of
    Project BRAHMA.

    It coordinates

        • Runtime Kernel
        • Runtime Context
        • Orchestrator
        • Agents

    Runtime is the primary entry point for every application.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from typing import Any
from venv import logger

from ENGINEERING.CORE.RUNTIME.logger import runtime
from ENGINEERING.MEMORY.memory_engine import runtime_memory
from ENGINEERING.CORE.RUNTIME.context import runtime_context
from .runtime_kernel import RuntimeKernel
from ..AGENTS.ORCHESTRATION.orchestrator import Orchestrator


# =============================================================================
# Runtime
# =============================================================================

class Runtime:
    """
    Public execution environment.

    This class owns the complete lifecycle of Project BRAHMA.
    """

    # -------------------------------------------------------------------------

    def __init__(self) -> None:

        self.kernel = RuntimeKernel()

        self.context = runtime_context 

        self.context.memory = runtime_memory

    # =========================================================================
    # Boot
    # =========================================================================

    def boot(self):
        """
        Boot Project BRAHMA.
        """

        context = self.kernel.boot()

        self.context = context

        self.kernel.context = context

        return context

    # =========================================================================
    # Start Runtime
    # =========================================================================

    def start(self):
        """
        Start runtime execution.
        """

        self.kernel.start()

    # =========================================================================
    # Stop Runtime
    # =========================================================================

    def shutdown(self):
        """
        Shutdown Runtime.
        """
        self.kernel.stop()
        runtime("Project BRAHMA Runtime Shutdown Complete.")

    # =========================================================================
    # Agent Registration
    # =========================================================================

    def register_agent(self, agent):
        """
        Register an Agent with the Runtime.
        """

        self.kernel.register_agent(agent)

    # -------------------------------------------------------------------------

    def unregister_agent(self, agent_uid: str):

        self.kernel.unregister_agent(agent_uid)

    # =========================================================================
    # Execution
    # =========================================================================

    def execute(
        self,
        *,
        agent,
        observation: Any,
        objective: Any,
    ):
        """
        Execute one complete cognitive cycle.
        """

        if not self.kernel.is_running:

            raise RuntimeError(
                "Runtime must be started before execution."
            )

        self.orchestrator.initialize(

            observation=observation,

            objective=objective,
        )

        self.orchestrator.context.memory = self.context.memory

        return self.orchestrator.execute_pipeline(agent)

    # =========================================================================
    # Information
    # =========================================================================

    @property
    def statistics(self):

        return self.kernel.statistics()

    # -------------------------------------------------------------------------

    @property
    def is_ready(self):

        return self.kernel.is_ready

    # -------------------------------------------------------------------------

    @property
    def is_running(self):

        return self.kernel.is_running

    # =========================================================================

    def __repr__(self):

        return (
            "Runtime("
            f"ready={self.is_ready}, "
            f"running={self.is_running})"
        )


# Global Runtime

runtime_instance = Runtime()

