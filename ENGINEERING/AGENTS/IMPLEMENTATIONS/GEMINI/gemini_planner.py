"""
===============================================================================
Project BRAHMA
Gemini Planner

File:
    gemini_planner.py

Purpose:
    Google Gemini implementation of the Universal AgentPlanner.

Description:
    GeminiPlanner transforms understanding into an executable plan.

        ReasoningResult
                ↓
        Prompt Adapter
                ↓
        Google Gemini
                ↓
        Response Adapter
                ↓
        PlanningResult

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from google import genai

from ...CORE.agent_planner import (
    AgentPlanner,
    PlanningResult,
)

from ...CORE.agent_reasoner import ReasoningResult

from .gemini_configuration import GeminiConfiguration
from .gemini_prompt_adapter import GeminiPromptAdapter
from .gemini_response_adapter import GeminiResponseAdapter


# =============================================================================
# Gemini Planner
# =============================================================================

class GeminiPlanner(AgentPlanner):
    """
    Google Gemini implementation of AgentPlanner.
    """

    # -------------------------------------------------------------------------

    def __init__(
        self,
        client: genai.Client,
        configuration: GeminiConfiguration,
    ) -> None:

        self.client = client

        self.configuration = configuration

        self.prompt_adapter = GeminiPromptAdapter()

        self.response_adapter = GeminiResponseAdapter()

    # =========================================================================

    @property
    def planner_name(self) -> str:

        return "Gemini Planner"

    # -------------------------------------------------------------------------

    @property
    def planning_strategy(self) -> str:

        return "llm"

    # =========================================================================

    def plan(
        self,
        *,
        objective,
        understanding: ReasoningResult,
        context=None,
        capability=None,
    ) -> PlanningResult:
        """
        Generate an execution plan.
        """

        prompt = self.prompt_adapter.build_planning_prompt(
            objective=objective,
            understanding=understanding,
        )

        response = self.client.models.generate_content(
            model=self.configuration.default_model.value,

            contents=prompt.user,

            config={
                "system_instruction": prompt.system,

                "temperature":
                    self.configuration.generation.temperature,

                "top_p":
                    self.configuration.generation.top_p,

                "top_k":
                    self.configuration.generation.top_k,

                "max_output_tokens":
                    self.configuration.generation.max_output_tokens,
            },
        )

        gemini_response = self.response_adapter.extract_text(
            response
        )

        return self.response_adapter.to_plan(
            gemini_response
        )

    # =========================================================================

    def validate(
        self,
        plan: PlanningResult,
    ) -> bool:

        return plan is not None

    # =========================================================================
    # Planner Information
    # =========================================================================

    @property
    def planner_name(self) -> str:
        return "Gemini Planner"


    @property
    def planning_strategy(self) -> str:
        return "llm-sequential"


    # =========================================================================
    # Plan Revision
    # =========================================================================

    def revise(
        self,
        plan: PlanningResult,
        feedback,
    ) -> PlanningResult:
        """
        Revise an existing plan.

        फिलहाल MVP implementation।
        बाद में feedback के आधार पर Gemini से नया plan बनवाएँगे।
        """

        return plan


    # =========================================================================
    # Validation
    # =========================================================================

    def validate(
        self,
        plan: PlanningResult,
    ) -> bool:

        return (
            plan is not None
            and len(plan.steps) > 0
        )