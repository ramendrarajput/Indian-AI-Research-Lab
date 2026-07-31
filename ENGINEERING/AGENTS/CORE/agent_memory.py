"""
===============================================================================
Project BRAHMA
Agent Memory Interface

File:
    agent_memory.py

Purpose:
    Defines the abstract memory interface used by every BRAHMA Agent.

Description:
    Memory is NOT owned by an Agent.

    Memory belongs to the Runtime.

    Agents interact with Memory through this interface.

    Different Runtime implementations may provide:

        • Working Memory
        • Episodic Memory
        • Semantic Memory
        • Long-Term Memory
        • Vector Memory
        • Graph Memory
        • Hybrid Memory

    The Agent never depends upon a specific implementation.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


# =============================================================================
# Memory Interface
# =============================================================================

class AgentMemory(ABC):
    """
    Abstract memory interface.

    Every Runtime Memory implementation must inherit this class.
    """

    # -------------------------------------------------------------------------
    # Write Operations
    # -------------------------------------------------------------------------

    @abstractmethod
    def store(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store information.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def update(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Update existing information.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def delete(
        self,
        key: str,
    ) -> None:
        """
        Remove stored information.
        """

    # -------------------------------------------------------------------------
    # Read Operations
    # -------------------------------------------------------------------------

    @abstractmethod
    def retrieve(
        self,
        key: str,
    ) -> Any:
        """
        Retrieve stored information.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def exists(
        self,
        key: str,
    ) -> bool:
        """
        Determine whether information exists.
        """

    # -------------------------------------------------------------------------
    # Search Operations
    # -------------------------------------------------------------------------

    @abstractmethod
    def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[Any]:
        """
        Semantic or keyword search.

        Runtime implementation decides search strategy.
        """

    # -------------------------------------------------------------------------
    # Memory Management
    # -------------------------------------------------------------------------

    @abstractmethod
    def clear(self) -> None:
        """
        Remove all stored information.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def size(self) -> int:
        """
        Number of stored records.
        """

    # -------------------------------------------------------------------------

    @abstractmethod
    def statistics(self) -> dict:
        """
        Return memory statistics.

        Example:

            total_records
            memory_type
            storage_backend
            vector_dimension
            etc.
        """

    # -------------------------------------------------------------------------

    @property
    @abstractmethod
    def memory_type(self) -> str:
        """
        Human-readable memory implementation.
        """

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(type={self.memory_type})"
        )