"""
===============================================================================
Project BRAHMA
Gemini Prompt Adapter

File:
    gemini_prompt_adapter.py

Purpose:
    Converts Universal Cognitive Objects into Gemini-compatible prompts.

Description:
    UniversalAgent never communicates directly with Gemini.

    Communication always passes through this adapter.

    This keeps the Universal Cognitive Architecture independent of
    provider-specific prompt engineering.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


# =============================================================================
# Prompt Object
# =============================================================================

@dataclass(slots=True)
class GeminiPrompt:
    """
    Represents a provider-ready Gemini prompt.
    """

    system: str

    user: str

    metadata: dict[str, Any] | None = None


# =============================================================================
# Prompt Adapter
# =============================================================================

class GeminiPromptAdapter:
    """
    Translates UniversalAgent cognition into Gemini prompts.
    """

    # -------------------------------------------------------------------------

    def build_reasoning_prompt(
        self,
        *,
        observation: Any,
        objective: Any,
        context: Any = None,
        memory: Any = None,
    ) -> GeminiPrompt:
        """
        Build prompt for reasoning.
        """

        system = (
            "You are the reasoning engine of Project BRAHMA.\n"
            "Think carefully.\n"
            "Use available context.\n"
            "Do not hallucinate.\n"
            "Return structured reasoning."
        )

        user = (
            f"OBJECTIVE:\n{objective}\n\n"
            f"OBSERVATION:\n{observation}\n\n"
            f"CONTEXT:\n{context}\n\n"
            f"MEMORY:\n{memory}"
        )

        return GeminiPrompt(
            system=system,
            user=user,
        )

    # -------------------------------------------------------------------------

    def build_planning_prompt(
        self,
        *,
        understanding: Any,
        objective: Any,
    ) -> GeminiPrompt:
        """
        Build prompt for planning.
        """

        system = (
            "Generate an execution plan.\n"
            "Think step-by-step.\n"
            "Produce an ordered sequence of actions."
        )

        user = (
            f"OBJECTIVE:\n{objective}\n\n"
            f"UNDERSTANDING:\n{understanding}"
        )

        return GeminiPrompt(
            system=system,
            user=user,
        )

    # -------------------------------------------------------------------------

    def build_reflection_prompt(
        self,
        *,
        objective: Any,
        execution: Any,
    ) -> GeminiPrompt:
        """
        Build prompt for reflection.
        """

        system = (
            "Evaluate completed execution.\n"
            "Identify strengths.\n"
            "Identify weaknesses.\n"
            "Recommend improvements."
        )

        user = (
            f"OBJECTIVE:\n{objective}\n\n"
            f"EXECUTION:\n{execution}"
        )

        return GeminiPrompt(
            system=system,
            user=user,
        )

    # -------------------------------------------------------------------------

    def build_learning_prompt(
        self,
        *,
        reflection: Any,
    ) -> GeminiPrompt:
        """
        Build prompt for learning.
        """

        system = (
            "Transform reflection into reusable knowledge.\n"
            "Focus on long-term improvement."
        )

        user = (
            f"REFLECTION:\n{reflection}"
        )

        return GeminiPrompt(
            system=system,
            user=user,
        )

    # -------------------------------------------------------------------------

    def build_custom_prompt(
        self,
        *,
        system: str,
        user: str,
        metadata: dict[str, Any] | None = None,
    ) -> GeminiPrompt:
        """
        Build a custom prompt.
        """

        return GeminiPrompt(
            system=system,
            user=user,
            metadata=metadata,
        )