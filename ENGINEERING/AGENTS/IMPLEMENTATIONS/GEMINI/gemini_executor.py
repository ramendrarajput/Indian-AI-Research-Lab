"""
===============================================================================
Project BRAHMA
Gemini Executor

File:
    gemini_executor.py

Purpose:
    Google Gemini implementation of the Universal AgentExecutor.

Description:
    GeminiExecutor coordinates execution of an existing plan.

        PlanningResult
                ↓
        Prompt Adapter
                ↓
        Google Gemini
                ↓
        Response Adapter
                ↓
        ExecutionResult

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from google import genai

from ...CORE.agent_executor import (
    AgentExecutor,
    ExecutionResult,
)

from ...CORE.agent_planner import PlanningResult

from .gemini_configuration import GeminiConfiguration
from .gemini_prompt_adapter import GeminiPromptAdapter
from .gemini_response_adapter import GeminiResponseAdapter


# =============================================================================
# Gemini Executor
# =============================================================================

class GeminiExecutor(AgentExecutor):
    """
    Google Gemini implementation of AgentExecutor.
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
    def executor_name(self) -> str:

        return "Gemini Executor"

    # -------------------------------------------------------------------------

    @property
    def execution_strategy(self) -> str:

        return "llm"

    # =========================================================================

    def execute(
        self,
        *,
        plan: PlanningResult,
        context=None,
    ) -> ExecutionResult:
        """
        Execute a previously generated plan.
        """

        prompt = self.prompt_adapter.build_custom_prompt(

            system=(
                "Execute the supplied plan.\n"
                "Follow the ordered steps.\n"
                "Report execution results clearly."
            ),

            user=str(plan),
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

        return self.response_adapter.to_execution(
            gemini_response
        )

    # =========================================================================

    def validate(
        self,
        execution: ExecutionResult,
    ) -> bool:

        return execution is not None

    # =========================================================================
    # Executor Information
    # =========================================================================

    @property
    def execution_backend(self) -> str:
        return "gemini"


    # =========================================================================
    # Execute Single Step
    # =========================================================================

    def execute_step(
        self,
        step,
        *,
        context=None,
    ):
        """
        Execute one plan step.

        MVP implementation.
        """

        return self.execute(
            plan=step,
            context=context,
        )


    # =========================================================================
    # Cancel Execution
    # =========================================================================

    def cancel(
        self,
        execution_id: str,
    ) -> bool:
        """
        Cancel execution.

        MVP implementation.
        """

        return True