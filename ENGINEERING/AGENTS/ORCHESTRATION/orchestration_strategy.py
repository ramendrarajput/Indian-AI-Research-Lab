"""
===============================================================================
Project BRAHMA
Orchestration Strategy

File:
    orchestration_strategy.py

Purpose:
    Defines the universal orchestration strategies used by
    Project BRAHMA.

Description:
    A strategy determines how multiple cognitive agents cooperate
    during an orchestration session.

    Strategies never perform orchestration.

    They define orchestration policy.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum, auto


# =============================================================================
# Strategy Types
# =============================================================================

class StrategyType(Enum):
    """
    Supported orchestration strategies.
    """

    SEQUENTIAL = auto()

    PARALLEL = auto()

    HIERARCHICAL = auto()

    DISTRIBUTED = auto()

    RECURSIVE = auto()

    ADAPTIVE = auto()


# =============================================================================
# Base Strategy
# =============================================================================

class OrchestrationStrategy(ABC):
    """
    Base class for every orchestration strategy.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def strategy_type(self) -> StrategyType:
        ...

    @abstractmethod
    def description(self) -> str:
        ...

    @abstractmethod
    def supports_parallel_execution(self) -> bool:
        ...

    @abstractmethod
    def supports_dynamic_agents(self) -> bool:
        ...


# =============================================================================
# Sequential Strategy
# =============================================================================

class SequentialStrategy(OrchestrationStrategy):

    @property
    def name(self) -> str:
        return "Sequential"

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.SEQUENTIAL

    def description(self) -> str:
        return (
            "Agents execute one after another. "
            "Each stage depends upon the previous stage."
        )

    def supports_parallel_execution(self) -> bool:
        return False

    def supports_dynamic_agents(self) -> bool:
        return False


# =============================================================================
# Parallel Strategy
# =============================================================================

class ParallelStrategy(OrchestrationStrategy):

    @property
    def name(self) -> str:
        return "Parallel"

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.PARALLEL

    def description(self) -> str:
        return (
            "Independent agents execute simultaneously."
        )

    def supports_parallel_execution(self) -> bool:
        return True

    def supports_dynamic_agents(self) -> bool:
        return False


# =============================================================================
# Hierarchical Strategy
# =============================================================================

class HierarchicalStrategy(OrchestrationStrategy):

    @property
    def name(self) -> str:
        return "Hierarchical"

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.HIERARCHICAL

    def description(self) -> str:
        return (
            "Coordinator delegates work to subordinate agents."
        )

    def supports_parallel_execution(self) -> bool:
        return True

    def supports_dynamic_agents(self) -> bool:
        return True


# =============================================================================
# Distributed Strategy
# =============================================================================

class DistributedStrategy(OrchestrationStrategy):

    @property
    def name(self) -> str:
        return "Distributed"

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.DISTRIBUTED

    def description(self) -> str:
        return (
            "Agents execute across multiple independent systems."
        )

    def supports_parallel_execution(self) -> bool:
        return True

    def supports_dynamic_agents(self) -> bool:
        return True


# =============================================================================
# Recursive Strategy
# =============================================================================

class RecursiveStrategy(OrchestrationStrategy):

    @property
    def name(self) -> str:
        return "Recursive"

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.RECURSIVE

    def description(self) -> str:
        return (
            "Agents may create and orchestrate additional agents."
        )

    def supports_parallel_execution(self) -> bool:
        return True

    def supports_dynamic_agents(self) -> bool:
        return True


# =============================================================================
# Adaptive Strategy
# =============================================================================

class AdaptiveStrategy(OrchestrationStrategy):

    @property
    def name(self) -> str:
        return "Adaptive"

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.ADAPTIVE

    def description(self) -> str:
        return (
            "The orchestration engine dynamically selects the most "
            "appropriate strategy according to runtime context."
        )

    def supports_parallel_execution(self) -> bool:
        return True

    def supports_dynamic_agents(self) -> bool:
        return True


# =============================================================================
# Default Strategy
# =============================================================================

DEFAULT_STRATEGY = AdaptiveStrategy()