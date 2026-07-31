"""
===============================================================================
Project BRAHMA
Gemini Learning

File:
    gemini_learning.py

Purpose:
    Google Gemini implementation of the Universal AgentLearning.

Description:
    GeminiLearning transforms reflection into reusable knowledge.

            ReflectionResult
                    ↓
            Prompt Adapter
                    ↓
            Google Gemini
                    ↓
            Response Adapter
                    ↓
            LearningResult

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from google import genai

from ...CORE.agent_learning import (
    AgentLearning,
    LearningResult,
)

from ...CORE.agent_reflection import ReflectionResult

from .gemini_configuration import GeminiConfiguration
from .gemini_prompt_adapter import GeminiPromptAdapter
from .gemini_response_adapter import GeminiResponseAdapter


# =============================================================================
# Gemini Learning
# =============================================================================

class GeminiLearning(AgentLearning):
    """
    Google Gemini implementation of AgentLearning.
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
    def learning_engine(self) -> str:

        return "Gemini Learning"

    # -------------------------------------------------------------------------

    @property
    def learning_strategy(self) -> str:

        return "llm"

    # =========================================================================

    def learn(
        self,
        *,
        reflection: ReflectionResult,
        memory=None,
        context=None,
    ) -> LearningResult:
        """
        Transform reflection into reusable knowledge.
        """

        prompt = self.prompt_adapter.build_learning_prompt(

            reflection=reflection,
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

        return self.response_adapter.to_learning(
            gemini_response
        )

    # =========================================================================

    def validate(
        self,
        learning: LearningResult,
    ) -> bool:

        return learning is not None

    # =========================================================================
    # Apply Learning
    # =========================================================================

    def apply(
        self,
        learning: LearningResult,
        *,
        memory=None,
    ) -> bool:
        """
        Apply learned knowledge.

        MVP implementation.
        """

        return True