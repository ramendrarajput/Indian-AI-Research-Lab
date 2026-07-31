"""
===============================================================================
Project BRAHMA
Cognitive Protocol

File:
    cognitive_protocol.py

Purpose:
    Defines the canonical cognitive interface implemented by every
    BRAHMA Agent.

Description:
    CognitiveProtocol specifies the complete intelligence lifecycle.

        Observe
            ↓
        Understand
            ↓
        Plan
            ↓
        Execute
            ↓
        Reflect
            ↓
        Learn

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


# =============================================================================
# Cognitive Protocol
# =============================================================================

class CognitiveProtocol(ABC):
    """
    Canonical cognitive interface.

    Every intelligent Agent inside Project BRAHMA follows this
    protocol.
    """

    # =========================================================================
    # Cognitive Pipeline
    # =========================================================================

    @abstractmethod
    def observe(
        self,
        observation: Any,
    ) -> Any:
        """
        Receive an observation.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def understand(
        self,
        observation: Any,
    ):
        """
        Produce understanding.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def plan(
        self,
        reasoning,
    ):
        """
        Produce an execution plan.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def execute(
        self,
        plan,
    ):
        """
        Execute the generated plan.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def reflect(
        self,
        plan,
        execution,
    ):
        """
        Reflect on execution.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def learn(
        self,
        reflection,
    ):
        """
        Learn from reflection.
        """

    # =========================================================================

    @abstractmethod
    def run(
        self,
        observation: Any,
    ):
        """
        Execute one complete cognitive cycle.
        """