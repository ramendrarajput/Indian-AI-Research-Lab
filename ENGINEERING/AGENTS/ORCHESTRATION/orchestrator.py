"""
===============================================================================
Project BRAHMA
Universal Orchestrator

File:
    orchestrator.py

Purpose:
    Central orchestration engine responsible for coordinating the
    complete cognitive lifecycle of Project BRAHMA.

Description:
    The Orchestrator never performs cognition.

    It coordinates cognition.

    It governs:

        • State
        • Context
        • Strategy
        • Pipeline
        • Agent Coordination

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from typing import Any

from .orchestration_state import (
    OrchestrationState,
    OrchestrationStateMachine,
)

from .orchestration_context import (
    OrchestrationContext,
)

from .orchestration_strategy import (
    OrchestrationStrategy,
    DEFAULT_STRATEGY,
)

from .orchestration_pipeline import (
    OrchestrationPipeline,
    DEFAULT_PIPELINE,
)


# =============================================================================
# Universal Orchestrator
# =============================================================================

class Orchestrator:
    """
    Universal Cognitive Orchestrator.

    Responsible for coordinating the complete intelligence pipeline.
    """

    # -------------------------------------------------------------------------

    def __init__(
        self,
        *,
        strategy: OrchestrationStrategy = DEFAULT_STRATEGY,
        pipeline: OrchestrationPipeline = DEFAULT_PIPELINE,
    ) -> None:

        self.state = OrchestrationStateMachine()

        self.context = OrchestrationContext()

        self.strategy = strategy

        self.pipeline = pipeline

    # =========================================================================
    # Lifecycle
    # =========================================================================

    def initialize(
        self,
        *,
        observation: Any,
        objective: Any,
    ) -> None:
        """
        Initialize a new orchestration session.
        """

        self.context.clear()

        self.context.observation = observation

        self.context.objective = objective

        self.state.transition_to(
            OrchestrationState.INITIALIZED,
            "Orchestration initialized.",
        )

    # =========================================================================
    # State Helpers
    # =========================================================================

    def transition(
        self,
        state: OrchestrationState,
        description: str = "",
    ) -> None:

        self.state.transition_to(
            state,
            description,
        )

    # =========================================================================
    # Cognitive Coordination
    # =========================================================================

    def execute_pipeline(
        self,
        agent,
    ):
        """
        Execute the configured cognitive pipeline.

        The supplied agent is expected to expose:

            reason()

            plan()

            execute()

            reflect()

            learn()
        """

        for step in self.pipeline:

            stage = step.stage

            # -------------------------------------------------------------
            # Observation
            # -------------------------------------------------------------

            if stage.name == "OBSERVATION":

                self.transition(
                    OrchestrationState.OBSERVING,
                    "Observation received.",
                )

            # -------------------------------------------------------------
            # Reasoning
            # -------------------------------------------------------------

            elif stage.name == "REASONING":

                self.transition(
                    OrchestrationState.REASONING,
                    "Reasoning started.",
                )

                self.context.reasoning = agent.reason(

                    observation=self.context.observation,

                    objective=self.context.objective,

                    context=self.context,

                    memory=self.context.memory,
                )

            # -------------------------------------------------------------
            # Planning
            # -------------------------------------------------------------

            elif stage.name == "PLANNING":

                self.transition(
                    OrchestrationState.PLANNING,
                    "Planning started.",
                )

                self.context.planning = agent.plan(

                    objective=self.context.objective,

                    understanding=self.context.reasoning,

                    context=self.context,
                )

            # -------------------------------------------------------------
            # Execution
            # -------------------------------------------------------------

            elif stage.name == "EXECUTION":

                self.transition(
                    OrchestrationState.EXECUTING,
                    "Execution started.",
                )

                self.context.execution = agent.execute(

                    plan=self.context.planning,

                    context=self.context,
                )

            # -------------------------------------------------------------
            # Reflection
            # -------------------------------------------------------------

            elif stage.name == "REFLECTION":

                self.transition(
                    OrchestrationState.REFLECTING,
                    "Reflection started.",
                )

                self.context.reflection = agent.reflect(

                    objective=self.context.objective,

                    execution=self.context.execution,
                )

            # -------------------------------------------------------------
            # Learning
            # -------------------------------------------------------------

            elif stage.name == "LEARNING":

                self.transition(
                    OrchestrationState.LEARNING,
                    "Learning started.",
                )

                self.context.learning = agent.learn(

                    reflection=self.context.reflection,
                )

        self.transition(

            OrchestrationState.COMPLETED,

            "Pipeline completed.",
        )

        return self.context

    # =========================================================================

    def reset(self) -> None:
        """
        Reset orchestrator.
        """

        self.state.reset()

        self.context.clear()

    # =========================================================================

    @property
    def current_state(self):

        return self.state.current_state

    # =========================================================================

    def __repr__(self):

        return (
            "Orchestrator("
            f"state={self.current_state.name}, "
            f"strategy={self.strategy.name})"
        )