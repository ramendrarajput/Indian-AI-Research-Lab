"""
===============================================================================
Project BRAHMA
Gemini Configuration

File:
    gemini_configuration.py

Purpose:
    Central configuration for every Google Gemini implementation
    inside Project BRAHMA.

Description:
    This module acts as the single source of truth for all Gemini
    runtime parameters.

    No implementation should hardcode provider settings.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


# =============================================================================
# Supported Gemini Models
# =============================================================================

class GeminiModel(str, Enum):
    """
    Official Gemini models supported by Project BRAHMA.
    """

    FLASH = "gemini-2.5-flash"

    FLASH_LITE = "gemini-2.5-flash-lite"

    PRO = "gemini-2.5-pro"


# =============================================================================
# Retry Policy
# =============================================================================

@dataclass(slots=True)
class RetryPolicy:

    max_attempts: int = 3

    retry_delay_seconds: float = 2.0

    exponential_backoff: bool = True


# =============================================================================
# Safety Policy
# =============================================================================

@dataclass(slots=True)
class SafetyPolicy:

    enabled: bool = True

    allow_code_generation: bool = True

    allow_reasoning: bool = True

    allow_tool_execution: bool = True


# =============================================================================
# Generation Parameters
# =============================================================================

@dataclass(slots=True)
class GenerationParameters:

    temperature: float = 0.2

    top_p: float = 0.95

    top_k: int = 40

    max_output_tokens: int = 8192

    candidate_count: int = 1


# =============================================================================
# Gemini Configuration
# =============================================================================

@dataclass(slots=True)
class GeminiConfiguration:
    """
    Complete runtime configuration for Gemini.
    """

    # ---------------------------------------------------------------------
    # Model
    # ---------------------------------------------------------------------

    default_model: GeminiModel = GeminiModel.FLASH

    # ---------------------------------------------------------------------
    # Runtime
    # ---------------------------------------------------------------------

    timeout_seconds: int = 120

    thinking_budget: int | None = None

    streaming_enabled: bool = True

    # ---------------------------------------------------------------------
    # Policies
    # ---------------------------------------------------------------------

    retry: RetryPolicy = field(default_factory=RetryPolicy)

    safety: SafetyPolicy = field(default_factory=SafetyPolicy)

    generation: GenerationParameters = field(
        default_factory=GenerationParameters
    )

    # ---------------------------------------------------------------------
    # Future extension
    # ---------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # =========================================================================

    def set_model(
        self,
        model: GeminiModel,
    ) -> None:

        self.default_model = model

    # -------------------------------------------------------------------------

    def update_temperature(
        self,
        value: float,
    ) -> None:

        self.generation.temperature = value

    # -------------------------------------------------------------------------

    def update_max_tokens(
        self,
        value: int,
    ) -> None:

        self.generation.max_output_tokens = value

    # -------------------------------------------------------------------------

    def enable_streaming(self) -> None:

        self.streaming_enabled = True

    # -------------------------------------------------------------------------

    def disable_streaming(self) -> None:

        self.streaming_enabled = False

    # -------------------------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "model": self.default_model.value,
            "timeout_seconds": self.timeout_seconds,
            "thinking_budget": self.thinking_budget,
            "streaming_enabled": self.streaming_enabled,
            "generation": vars(self.generation),
            "retry": vars(self.retry),
            "safety": vars(self.safety),
            "metadata": self.metadata,
        }


# =============================================================================
# Default Configuration
# =============================================================================

DEFAULT_GEMINI_CONFIGURATION = GeminiConfiguration()