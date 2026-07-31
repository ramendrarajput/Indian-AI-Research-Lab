"""
===============================================================================
Project BRAHMA
Universal Agent

File:
    universal_agent.py

Purpose:
    Canonical implementation of the Universal Cognitive Agent.

Description:
    UniversalAgent represents the fundamental implementation of
    intelligence inside Project BRAHMA.

    The UniversalAgent is completely independent of

        • AI Models
        • LLM Providers
        • Frameworks
        • APIs
        • Runtime Implementations

    Intelligence emerges through the interaction of independent
    cognitive modules.

    UniversalAgent itself performs no reasoning.

    It coordinates cognition.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .agent_identity import AgentIdentity
from .agent_context import AgentContext
from .agent_objective import AgentObjective
from .agent_capability import AgentCapability
from .agent_memory import AgentMemory

from .agent_reasoner import AgentReasoner
from .agent_planner import AgentPlanner
from .agent_executor import AgentExecutor
from .agent_reflection import AgentReflection
from .agent_learning import AgentLearning

from .cognitive_protocol import CognitiveProtocol


# =============================================================================
# Universal Agent
# =============================================================================

@dataclass(slots=True)
class UniversalAgent(CognitiveProtocol):
    """
    Canonical Cognitive Agent.

    UniversalAgent does not implement intelligence.

    UniversalAgent coordinates independent cognitive modules.

    Every implementation inside Project BRAHMA eventually inherits
    from this class.
    """

    # -------------------------------------------------------------------------
    # Identity
    # -------------------------------------------------------------------------

    identity: AgentIdentity

    # -------------------------------------------------------------------------
    # Runtime Context
    # -------------------------------------------------------------------------

    context: AgentContext

    # -------------------------------------------------------------------------
    # Objective
    # -------------------------------------------------------------------------

    objective: AgentObjective

    # -------------------------------------------------------------------------
    # Capability
    # -------------------------------------------------------------------------

    capability: AgentCapability

    # -------------------------------------------------------------------------
    # Runtime Memory
    # -------------------------------------------------------------------------

    memory: AgentMemory

    # -------------------------------------------------------------------------
    # Cognitive Modules
    # -------------------------------------------------------------------------

    reasoner: AgentReasoner | None = field(default=None)

    planner: AgentPlanner | None = field(default=None)

    executor: AgentExecutor | None = field(default=None)

    reflection: AgentReflection | None = field(default=None)

    learning: AgentLearning | None = field(default=None)

    # -------------------------------------------------------------------------
    # Runtime Metadata
    # -------------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # =========================================================================
    # Construction
    # =========================================================================

    def __post_init__(self) -> None:
        """
        Synchronize Context with Runtime Components.
        """

        self.context.memory = self.memory

        self.context.reasoner = self.reasoner

        self.context.planner = self.planner

        self.context.executor = self.executor

    # =========================================================================
    # Registration API
    # =========================================================================

    def set_reasoner(
        self,
        reasoner: AgentReasoner,
    ) -> None:

        self.reasoner = reasoner

        self.context.reasoner = reasoner

    # -------------------------------------------------------------------------

    def set_planner(
        self,
        planner: AgentPlanner,
    ) -> None:

        self.planner = planner

        self.context.planner = planner

    # -------------------------------------------------------------------------

    def set_executor(
        self,
        executor: AgentExecutor,
    ) -> None:

        self.executor = executor

        self.context.executor = executor

        # -------------------------------------------------------------------------

    def set_reflection(
        self,
        reflection: AgentReflection,
    ) -> None:
        """
        Register Reflection module.
        """

        self.reflection = reflection

    # -------------------------------------------------------------------------

    def set_learning(
        self,
        learning: AgentLearning,
    ) -> None:
        """
        Register Learning module.
        """

        self.learning = learning

    # =========================================================================
    # Metadata API
    # =========================================================================

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store runtime metadata.
        """

        self.metadata[key] = value

    # -------------------------------------------------------------------------

    def get_metadata(
        self,
        key: str,
        default=None,
    ):
        """
        Retrieve runtime metadata.
        """

        return self.metadata.get(
            key,
            default,
        )

    # -------------------------------------------------------------------------

    def clear_metadata(self) -> None:
        """
        Remove all temporary metadata.
        """

        self.metadata.clear()

    # =========================================================================
    # Validation
    # =========================================================================

    def validate(self) -> None:
        """
        Validate mandatory components.

        Raises
        ------
        RuntimeError
            If any mandatory cognitive component is missing.
        """

        if self.reasoner is None:
            raise RuntimeError("Reasoner is not registered.")

        if self.planner is None:
            raise RuntimeError("Planner is not registered.")

        if self.executor is None:
            raise RuntimeError("Executor is not registered.")

        if self.reflection is None:
            raise RuntimeError("Reflection is not registered.")

        if self.learning is None:
            raise RuntimeError("Learning is not registered.")

    # =========================================================================
    # Health Check
    # =========================================================================

    @property
    def is_ready(self) -> bool:
        """
        Returns True when all cognitive modules are available.
        """

        return all(
            (
                self.reasoner,
                self.planner,
                self.executor,
                self.reflection,
                self.learning,
            )
        )

    # -------------------------------------------------------------------------

    def health_check(self) -> dict:
        """
        Runtime health report.
        """

        return {

            "identity": self.identity.fullname,

            "ready": self.is_ready,

            "reasoner": self.reasoner is not None,

            "planner": self.planner is not None,

            "executor": self.executor is not None,

            "reflection": self.reflection is not None,

            "learning": self.learning is not None,
        }    

        # =========================================================================
    # Cognitive Pipeline
    # =========================================================================

    def observe(
        self,
        observation: Any,
    ) -> Any:
        """
        Receive an observation.

        Future versions may normalize sensory inputs,
        perform preprocessing, or attach timestamps.

        Current implementation returns the observation unchanged.
        """

        return observation

    # -------------------------------------------------------------------------

    def understand(
        self,
        observation: Any,
    ):
        """
        Produce understanding through reasoning.
        """

        self.validate()

        return self.reasoner.reason(

            observation=observation,

            context=self.context,

            objective=self.objective,

            memory=self.memory,
        )

    # -------------------------------------------------------------------------

    def plan(
        self,
        reasoning,
    ):
        """
        Produce an execution plan.
        """

        self.validate()

        return self.planner.plan(

            objective=self.objective,

            understanding=reasoning,

            context=self.context,

            capability=self.capability,
        )

    # -------------------------------------------------------------------------

    def execute(
        self,
        plan,
    ):
        """
        Execute the generated plan.
        """

        self.validate()

        return self.executor.execute(

            plan=plan,

            context=self.context,
        )

    # -------------------------------------------------------------------------

    def reflect(
        self,
        plan,
        execution,
    ):
        """
        Reflect upon execution.
        """

        self.validate()

        return self.reflection.reflect(

            objective=self.objective,

            plan=plan,

            execution=execution,

            context=self.context,
        )

    # -------------------------------------------------------------------------

    def learn(
        self,
        reflection,
    ):
        """
        Learn from reflection.
        """

        self.validate()

        return self.learning.learn(

            reflection=reflection,

            memory=self.memory,

            context=self.context,
        )

    # =========================================================================
    # Complete Cognitive Cycle
    # =========================================================================

    def run(
        self,
        observation: Any,
    ) -> dict[str, Any]:
        """
        Execute one complete cognitive cycle.

            Observation
                    ↓
            Reasoning
                    ↓
            Planning
                    ↓
            Execution
                    ↓
            Reflection
                    ↓
            Learning
        """

        # -------------------------------------------------------------
        # Observation
        # -------------------------------------------------------------

        observation = self.observe(observation)

        # -------------------------------------------------------------
        # Reasoning
        # -------------------------------------------------------------

        reasoning = self.understand(observation)

        # -------------------------------------------------------------
        # Planning
        # -------------------------------------------------------------

        planning = self.plan(reasoning)

        # -------------------------------------------------------------
        # Execution
        # -------------------------------------------------------------

        execution = self.execute(planning)

        # -------------------------------------------------------------
        # Reflection
        # -------------------------------------------------------------

        reflection = self.reflect(

            planning,

            execution,
        )

        # -------------------------------------------------------------
        # Learning
        # -------------------------------------------------------------

        learning = self.learn(reflection)

        # -------------------------------------------------------------

        return {

            "reasoning": reasoning,

            "planning": planning,

            "execution": execution,

            "reflection": reflection,

            "learning": learning,
        }

        # =========================================================================
    # Runtime Synchronization
    # =========================================================================

    def synchronize_context(self) -> None:
        """
        Synchronize runtime components with AgentContext.

        This method should be called whenever runtime components
        are replaced or injected.
        """

        self.context.memory = self.memory

        self.context.reasoner = self.reasoner

        self.context.planner = self.planner

        self.context.executor = self.executor

    # -------------------------------------------------------------------------

    def refresh(self) -> None:
        """
        Refresh runtime state.

        Updates timestamp and synchronizes runtime references.
        """

        self.context.update_timestamp()

        self.synchronize_context()

    # =========================================================================
    # Objective Management
    # =========================================================================

    def set_objective(
        self,
        objective: AgentObjective,
    ) -> None:
        """
        Replace the current objective.
        """

        self.objective = objective

    # -------------------------------------------------------------------------

    def activate_objective(self) -> None:
        """
        Activate the current objective.
        """

        self.objective.activate()

    # -------------------------------------------------------------------------

    def complete_objective(self) -> None:
        """
        Mark the current objective as completed.
        """

        self.objective.complete()

    # -------------------------------------------------------------------------

    def fail_objective(self) -> None:
        """
        Mark the current objective as failed.
        """

        self.objective.fail()

    # =========================================================================
    # Lifecycle Hooks
    # =========================================================================

    def on_initialize(self) -> None:
        """
        Runtime initialization hook.

        Override in subclasses when required.
        """

        self.refresh()

    # -------------------------------------------------------------------------

    def on_before_run(
        self,
        observation: Any,
    ) -> None:
        """
        Hook executed immediately before the cognitive cycle.
        """

        self.refresh()

    # -------------------------------------------------------------------------

    def on_after_run(
        self,
        result: dict[str, Any],
    ) -> None:
        """
        Hook executed immediately after the cognitive cycle.
        """

        self.refresh()

    # =========================================================================
    # Statistics
    # =========================================================================

    def statistics(self) -> dict[str, Any]:
        """
        Runtime statistics for the Agent.
        """

        return {

            "identity": self.identity.to_dict(),

            "context": self.context.to_dict(),

            "objective": self.objective.to_dict(),

            "ready": self.is_ready,

            "memory_type": self.memory.memory_type,

            "memory_records": self.memory.size(),

            "metadata": dict(self.metadata),
        }

    # =========================================================================
    # Serialization
    # =========================================================================

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the Agent.

        Heavy runtime objects are intentionally omitted.
        """

        return {

            "identity": self.identity.to_dict(),

            "context": self.context.to_dict(),

            "objective": self.objective.to_dict(),

            "capability": self.capability.to_dict(),

            "ready": self.is_ready,

            "metadata": dict(self.metadata),
        }

        # =========================================================================
    # Convenience Properties
    # =========================================================================

    @property
    def uid(self) -> str:
        """
        Shortcut to Agent Identity UID.
        """

        return self.identity.uid

    # -------------------------------------------------------------------------

    @property
    def name(self) -> str:
        """
        Shortcut to Agent name.
        """

        return self.identity.name

    # -------------------------------------------------------------------------

    @property
    def version(self) -> str:
        """
        Shortcut to Agent version.
        """

        return self.identity.version

    # -------------------------------------------------------------------------

    @property
    def fullname(self) -> str:
        """
        Human-readable Agent identifier.
        """

        return self.identity.fullname

    # -------------------------------------------------------------------------

    @property
    def category(self):
        """
        Shortcut to Agent category.
        """

        return self.identity.category

    # =========================================================================
    # Lifecycle
    # =========================================================================

    def reset(self) -> None:
        """
        Reset temporary runtime state.

        Permanent identity is preserved.
        """

        self.clear_metadata()

        self.context.clear_metadata()

        self.refresh()

    # -------------------------------------------------------------------------

    def clone(self):
        """
        Placeholder for future cloning support.

        Runtime-specific implementations may override this method.
        """

        raise NotImplementedError(
            "Agent cloning is not implemented."
        )

    # =========================================================================
    # Representation
    # =========================================================================

    def __str__(self) -> str:

        return self.fullname

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            "UniversalAgent("
            f"name='{self.name}', "
            f"version='{self.version}', "
            f"ready={self.is_ready})"
        )