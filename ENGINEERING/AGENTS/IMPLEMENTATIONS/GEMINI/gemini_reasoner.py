"""
===============================================================================
Project BRAHMA
Gemini Reasoner

File:
    gemini_reasoner.py

Purpose:
    Google Gemini implementation of the Universal AgentReasoner.

Description:
    GeminiReasoner coordinates the complete reasoning pipeline.

        Observation
            ↓
        Prompt Adapter
            ↓
        Gemini Model
            ↓
        Response Adapter
            ↓
        ReasoningResult

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from google import genai

from ...CORE.agent_reasoner import (
    AgentReasoner,
    ReasoningResult,
)

from .gemini_configuration import GeminiConfiguration
from .gemini_prompt_adapter import GeminiPromptAdapter
from .gemini_response_adapter import (
    GeminiResponseAdapter,
)


# =============================================================================
# Gemini Reasoner
# =============================================================================

class GeminiReasoner(AgentReasoner):
    """
    Google Gemini implementation of AgentReasoner.
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

    # =========================================================================
    # AgentReasoner Interface
    # =========================================================================

    @property
    def engine_name(self) -> str:
        """
        Human-readable reasoning engine.
        """
        return "Google Gemini"

    # -------------------------------------------------------------------------

    @property
    def reasoning_type(self) -> str:
        """
        Type of reasoning implementation.
        """
        return "neural"
    # =========================================================================

    def reason(
        self,
        *,
        observation,
        context=None,
        objective=None,
        memory=None,
    ) -> ReasoningResult:
        """
        Execute complete reasoning pipeline.
        """

        prompt = self.prompt_adapter.build_reasoning_prompt(
            observation=observation,
            context=context,
            objective=objective,
            memory=memory,
        )

        response = self.client.models.generate_content(
        model=self.configuration.default_model.value,
        contents=prompt.user,
        config=genai.types.GenerateContentConfig(
            system_instruction=prompt.system,
            temperature=self.configuration.generation.temperature,
            top_p=self.configuration.generation.top_p,
            top_k=self.configuration.generation.top_k,
            max_output_tokens=self.configuration.generation.max_output_tokens,
        ),
    )
        gemini_response = self.response_adapter.extract_text(
            response
        )

        return self.response_adapter.to_reasoning(
            gemini_response
        )

    # =========================================================================

    def validate(
        self,
        reasoning: ReasoningResult,
    ) -> bool:

        return reasoning is not None

    # =========================================================================

    def explain(
        self,
        result: ReasoningResult,
    ) -> str:
        """
        Explain the generated reasoning.
        """

        if result is None:
            return "No reasoning available."

        if result.understanding is None:
            return "Reasoning completed without explanation."

        return str(result.understanding)