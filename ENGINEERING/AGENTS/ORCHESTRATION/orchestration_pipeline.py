"""
===============================================================================
Project BRAHMA
Orchestration Pipeline

File:
    orchestration_pipeline.py

Purpose:
    Defines the universal cognitive execution pipeline for
    Project BRAHMA orchestration.

Description:
    A pipeline defines the ordered sequence of cognitive stages.

    Strategy decides HOW execution proceeds.

    Pipeline defines WHAT stages are executed.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto


# =============================================================================
# Pipeline Stages
# =============================================================================

class PipelineStage(Enum):
    """
    Universal cognitive pipeline.
    """

    OBSERVATION = auto()

    REASONING = auto()

    PLANNING = auto()

    EXECUTION = auto()

    REFLECTION = auto()

    LEARNING = auto()


# =============================================================================
# Pipeline Step
# =============================================================================

@dataclass(slots=True)
class PipelineStep:
    """
    One stage inside a cognitive pipeline.
    """

    stage: PipelineStage

    enabled: bool = True

    required: bool = True

    description: str = ""


# =============================================================================
# Orchestration Pipeline
# =============================================================================

@dataclass(slots=True)
class OrchestrationPipeline:
    """
    Ordered sequence of cognitive stages.
    """

    steps: list[PipelineStep] = field(default_factory=list)

    # -------------------------------------------------------------------------

    def add_step(
        self,
        step: PipelineStep,
    ) -> None:

        self.steps.append(step)

    # -------------------------------------------------------------------------

    def remove_step(
        self,
        stage: PipelineStage,
    ) -> None:

        self.steps = [
            step
            for step in self.steps
            if step.stage != stage
        ]

    # -------------------------------------------------------------------------

    def enable(
        self,
        stage: PipelineStage,
    ) -> None:

        for step in self.steps:

            if step.stage == stage:
                step.enabled = True

    # -------------------------------------------------------------------------

    def disable(
        self,
        stage: PipelineStage,
    ) -> None:

        for step in self.steps:

            if step.stage == stage:
                step.enabled = False

    # -------------------------------------------------------------------------

    def enabled_steps(
        self,
    ) -> tuple[PipelineStep, ...]:

        return tuple(

            step

            for step in self.steps

            if step.enabled

        )

    # -------------------------------------------------------------------------

    def __iter__(self):

        return iter(self.enabled_steps())

    # -------------------------------------------------------------------------

    def __len__(self):

        return len(self.enabled_steps())

    # -------------------------------------------------------------------------

    def __repr__(self):

        names = [

            step.stage.name

            for step in self.enabled_steps()

        ]

        return (
            f"OrchestrationPipeline("
            f"{' -> '.join(names)})"
        )


# =============================================================================
# Default Universal Pipeline
# =============================================================================

DEFAULT_PIPELINE = OrchestrationPipeline(

    steps=[

        PipelineStep(
            PipelineStage.OBSERVATION,
            description="Receive observation.",
        ),

        PipelineStep(
            PipelineStage.REASONING,
            description="Generate understanding.",
        ),

        PipelineStep(
            PipelineStage.PLANNING,
            description="Create execution plan.",
        ),

        PipelineStep(
            PipelineStage.EXECUTION,
            description="Execute planned actions.",
        ),

        PipelineStep(
            PipelineStage.REFLECTION,
            description="Evaluate execution.",
        ),

        PipelineStep(
            PipelineStage.LEARNING,
            description="Transform experience into knowledge.",
        ),

    ]

)