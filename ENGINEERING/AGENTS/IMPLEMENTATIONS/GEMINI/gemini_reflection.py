"""
===============================================================================
Project BRAHMA
Gemini Reflection

File:
    gemini_reflection.py

Purpose:
    Google Gemini implementation of the Universal AgentReflection.

Description:
    GeminiReflection evaluates completed execution and produces
    structured self-reflection.

        ExecutionResult
                ↓
        Prompt Adapter
                ↓
        Google Gemini
                ↓
        Response Adapter
                ↓
        ReflectionResult

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from google import genai

from ...CORE.agent_reflection import (
    AgentReflection,
    ReflectionResult,
)

from ...CORE.agent_executor import ExecutionResult

from .gemini_configuration import GeminiConfiguration
from .gemini_prompt_adapter import GeminiPromptAdapter
from .gemini_response_adapter import GeminiResponseAdapter


# =============================================================================
# Gemini Reflection
# =============================================================================

class GeminiReflection(AgentReflection):
    """
    Google Gemini implementation of AgentReflection.
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
    def reflection_engine(self) -> str:

        return "Gemini Reflection"

    # -------------------------------------------------------------------------

    @property
    def reflection_strategy(self) -> str:

        return "llm"

    # =========================================================================

    def reflect(
        self,
        *,
        observation=None,
        objective=None,
        plan=None,
        execution: ExecutionResult = None,
        context=None,
    ) -> ReflectionResult:
        """
        Evaluate completed execution.
        """

        prompt = self.prompt_adapter.build_reflection_prompt(

            objective=objective,

            execution=execution,
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

        return self.response_adapter.to_reflection(
            gemini_response
        )

    # =========================================================================

    def validate(
        self,
        reflection: ReflectionResult,
    ) -> bool:

        return reflection is not None

    # =========================================================================

    def summarize(
        self,
        reflection: ReflectionResult,
    ) -> str:
        """
        Return a short human-readable summary of reflection.
        """

        if reflection is None:
            return "No reflection available."

        if hasattr(reflection, "understanding"):
            return str(reflection.understanding)

        return str(reflection)