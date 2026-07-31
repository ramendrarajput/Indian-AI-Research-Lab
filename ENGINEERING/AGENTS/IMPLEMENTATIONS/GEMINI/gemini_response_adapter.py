"""
===============================================================================
Project BRAHMA
Gemini Response Adapter

File:
    gemini_response_adapter.py

Purpose:
    Converts Google Gemini responses into Project BRAHMA
    universal cognitive objects.

Description:
    UniversalAgent never consumes provider-specific responses.

    Every Gemini response is translated into standardized BRAHMA
    objects before entering the cognitive pipeline.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ...CORE.agent_reasoner import ReasoningResult
from ...CORE.agent_planner import PlanningResult
from ...CORE.agent_executor import (
    ExecutionResult,
    ExecutionStatus,
)
from ...CORE.agent_reflection import (
    ReflectionResult,
    ReflectionStatus,
)
from ...CORE.agent_learning import (
    LearningResult,
    LearningStatus,
)


# =============================================================================
# Raw Gemini Response
# =============================================================================

@dataclass(slots=True)
class GeminiResponse:
    """
    Provider-independent wrapper around a Gemini response.

    Only this adapter should understand provider-specific structure.
    """

    text: str

    raw: Any = None

    metadata: dict[str, Any] | None = None


# =============================================================================
# Gemini Response Adapter
# =============================================================================

class GeminiResponseAdapter:
    """
    Converts Gemini output into Project BRAHMA objects.
    """

    # -------------------------------------------------------------------------

    def to_reasoning(
        self,
        response: GeminiResponse,
    ) -> ReasoningResult:
        """
        Convert Gemini output into ReasoningResult.
        """

        result = ReasoningResult()

        #result.summary = response.text
        result.understanding = response.text
        result.status = result.status.COMPLETED
        result.metadata.update(response.metadata or {})

        return result

    # -------------------------------------------------------------------------

    def to_plan(
        self,
        response: GeminiResponse,
    ) -> PlanningResult:
        """
        Convert Gemini output into PlanningResult.
        """

        result = PlanningResult()

        result.status = result.status.READY

        result.metadata.update(response.metadata or {})

        result.metadata["raw_plan"] = response.text

        return result

    # -------------------------------------------------------------------------

    def to_execution(
        self,
        response: GeminiResponse,
    ) -> ExecutionResult:
        """
        Convert Gemini output into ExecutionResult.
        """

        result = ExecutionResult()

        result.status = ExecutionStatus.SUCCESS

        result.metadata.update(response.metadata or {})

        result.metadata["output"] = response.text

        return result

    # -------------------------------------------------------------------------

    def to_reflection(
        self,
        response: GeminiResponse,
    ) -> ReflectionResult:
        """
        Convert Gemini output into ReflectionResult.
        """

        result = ReflectionResult()

        result.status = ReflectionStatus.COMPLETED

        #result.summary = response.text

        result.metadata.update(response.metadata or {})

        return result

    # -------------------------------------------------------------------------

    def to_learning(
        self,
        response: GeminiResponse,
    ) -> LearningResult:
        """
        Convert Gemini output into LearningResult.
        """

        result = LearningResult()

        result.status = LearningStatus.APPLIED

        result.add_knowledge(response.text)

        result.metadata.update(response.metadata or {})

        return result

    # -------------------------------------------------------------------------

    def extract_text(
        self,
        raw_response: Any,
    ) -> GeminiResponse:
        """
        Extract provider text into a standardized GeminiResponse.

        This is the only method that should understand
        provider-specific response formats.
        """

        text = ""

        try:

            text = raw_response.text

        except AttributeError:

            text = str(raw_response)

        return GeminiResponse(
            text=text,
            raw=raw_response,
        )