"""
===============================================================================
Project BRAHMA
Gemini Agent

File:
    gemini_agent.py

Purpose:
    Google Gemini implementation of the UniversalAgent.

Description:
    GeminiAgent provides the Google Gemini implementation of the
    Project BRAHMA UniversalAgent.

    UniversalAgent defines the cognitive architecture.

    GeminiAgent supplies Google Gemini based cognitive modules.

    Intelligence always remains inside UniversalAgent.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from google import genai

# =============================================================================
# Universal Agent
# =============================================================================

from ...CORE.universal_agent import UniversalAgent

# =============================================================================
# Core Objects
# =============================================================================

from ...CORE.agent_identity import (
    AgentIdentity,
    AgentCategory,
)

from ...CORE.agent_context import AgentContext

from ...CORE.agent_objective import AgentObjective

from ...CORE.agent_capability import (
    AgentCapability,
    CapabilityCategory,
)

from ...CORE.agent_memory import AgentMemory

# =============================================================================
# Gemini Configuration
# =============================================================================

from .gemini_configuration import GeminiConfiguration

# =============================================================================
# Gemini Cognitive Modules
# =============================================================================

from .gemini_reasoner import GeminiReasoner
from .gemini_planner import GeminiPlanner
from .gemini_executor import GeminiExecutor
from .gemini_reflection import GeminiReflection
from .gemini_learning import GeminiLearning


# =============================================================================
# Gemini Agent
# =============================================================================

class GeminiAgent(UniversalAgent):
    """
    Google Gemini implementation of UniversalAgent.

    UniversalAgent defines cognition.

    GeminiAgent provides Gemini implementations of
    all cognitive modules.
    """

    # -------------------------------------------------------------------------
    # Implementation Information
    # -------------------------------------------------------------------------

    IMPLEMENTATION_NAME = "Google Gemini"

    IMPLEMENTATION_VERSION = "2.0"

    PROVIDER = "Google"

    # -------------------------------------------------------------------------

    def __init__(
        self,
        *,
        client: genai.Client,
        memory: AgentMemory,
        configuration: GeminiConfiguration | None = None,
        identity: AgentIdentity | None = None,
        context: AgentContext | None = None,
        objective: AgentObjective | None = None,
        capability: AgentCapability | None = None,
    ) -> None:
        """
        Construct a Gemini-backed UniversalAgent.
        """

        # -------------------------------------------------------------
        # Gemini Runtime
        # -------------------------------------------------------------

        self.client = client

        self.configuration = (
            configuration
            if configuration is not None
            else GeminiConfiguration()
        )

        # -------------------------------------------------------------
        # Universal Agent Initialization
        # -------------------------------------------------------------

        super().__init__(

            identity=identity
            or AgentIdentity(

                name="GeminiAgent",

                category=AgentCategory.AI,

                description="Google Gemini Cognitive Agent",
            ),

            context=context
            or AgentContext(),

            objective=objective
            or AgentObjective(),

            capability=capability
            or AgentCapability(

                name="General Intelligence",

                category=CapabilityCategory.REASONING,

                description=(
                    "General reasoning capability powered "
                    "by Google Gemini."
                ),
            ),

            memory=memory,
        )

                # =============================================================
        # Create Gemini Cognitive Modules
        # =============================================================

        self.reasoner = GeminiReasoner(

            client=self.client,

            configuration=self.configuration,
        )

        # -------------------------------------------------------------

        self.planner = GeminiPlanner(

            client=self.client,

            configuration=self.configuration,
        )

        # -------------------------------------------------------------

        self.executor = GeminiExecutor(

            client=self.client,

            configuration=self.configuration,
        )

        # -------------------------------------------------------------

        self.reflection = GeminiReflection(

            client=self.client,

            configuration=self.configuration,
        )

        # -------------------------------------------------------------

        self.learning = GeminiLearning(

            client=self.client,

            configuration=self.configuration,
        )

        # =============================================================
        # Register Cognitive Modules
        # =============================================================

        self.set_reasoner(

            self.reasoner,
        )

        self.set_planner(

            self.planner,
        )

        self.set_executor(

            self.executor,
        )

        self.set_reflection(

            self.reflection,
        )

        self.set_learning(

            self.learning,
        )

        # =============================================================
        # Synchronize Runtime Context
        # =============================================================

        self.synchronize_context()

        # =============================================================
        # Validate Agent
        # =============================================================

        self.validate()

        # =============================================================
        # Runtime Initialization
        # =============================================================

        self.on_initialize()

        # =========================================================================
    # Provider Information
    # =========================================================================

    @property
    def implementation_name(self) -> str:
        """
        Human-readable implementation name.
        """

        return self.IMPLEMENTATION_NAME

    # -------------------------------------------------------------------------

    @property
    def implementation_version(self) -> str:
        """
        Current implementation version.
        """

        return self.IMPLEMENTATION_VERSION

    # -------------------------------------------------------------------------

    @property
    def provider_name(self) -> str:
        """
        AI provider name.
        """

        return self.PROVIDER

    # -------------------------------------------------------------------------

    @property
    def model_name(self) -> str:
        """
        Active Gemini model.
        """

        return str(self.configuration.default_model.value)

    # =========================================================================
    # Runtime Health
    # =========================================================================

    def health_check(self) -> bool:
        """
        Verify that the Gemini implementation is operational.
        """

        return all(

            (

                self.reasoner,

                self.planner,

                self.executor,

                self.reflection,

                self.learning,

                self.memory,
            )
        )

    # =========================================================================
    # Runtime Statistics
    # =========================================================================

    def statistics(self) -> dict:
        """
        Return implementation statistics.
        """

        base = super().statistics()

        base.update(

            {

                "implementation": self.implementation_name,

                "implementation_version": self.implementation_version,

                "provider": self.provider_name,

                "model": self.model_name,

                "healthy": self.health_check(),
            }
        )

        return base

    # =========================================================================
    # Runtime Refresh
    # =========================================================================

    def refresh(self) -> None:
        """
        Refresh runtime state.

        Future Gemini implementations may also refresh:

            • Model routing
            • Token limits
            • Rate limits
            • Runtime configuration
        """

        super().refresh()

    # =========================================================================
    # Validation
    # =========================================================================

    def validate(self) -> None:
        """
        Validate the Gemini implementation.
        """

        super().validate()

        if self.client is None:

            raise RuntimeError(

                "Gemini Client has not been initialized."
            )

        if self.configuration is None:

            raise RuntimeError(

                "Gemini Configuration has not been initialized."
            )    

        # =========================================================================
    # Serialization
    # =========================================================================

    def to_dict(self) -> dict:
        """
        Serialize the Gemini Agent.

        Heavy runtime objects (Gemini client, modules) are intentionally
        excluded from serialization.
        """

        data = super().to_dict()

        data.update(
            {
                "implementation": self.implementation_name,
                "implementation_version": self.implementation_version,
                "provider": self.provider_name,
                "model": self.model_name,
            }
        )

        return data

    # =========================================================================
    # Runtime Information
    # =========================================================================

    @property
    def runtime_information(self) -> dict:
        """
        Lightweight runtime information.
        """

        return {
            "implementation": self.implementation_name,
            "provider": self.provider_name,
            "model": self.model_name,
            "healthy": self.health_check(),
        }

    # =========================================================================
    # Debug Helpers
    # =========================================================================

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.identity.fullname} "
            f"[{self.provider_name} | {self.model_name}]"
        )

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:
        """
        Developer representation.
        """

        return (
            "GeminiAgent("
            f"name='{self.identity.name}', "
            f"model='{self.model_name}', "
            f"provider='{self.provider_name}', "
            f"healthy={self.health_check()})"
        )

    # =========================================================================
    # Lifecycle
    # =========================================================================

    def shutdown(self) -> None:
        """
        Gracefully shut down the Gemini Agent.

        Future implementations may release:

            • HTTP sessions
            • Streaming channels
            • Background workers
            • Tool connections
        """

        self.refresh()

    # =========================================================================
    # Boot Verification
    # =========================================================================

    def boot_check(self) -> bool:
        """
        Verify the agent is completely bootable.

        Returns:
            True if every required component is available.
        """

        try:

            self.validate()

            return self.health_check()

        except Exception:

            return False    