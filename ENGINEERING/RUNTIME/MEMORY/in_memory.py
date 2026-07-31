"""
===============================================================================
Project BRAHMA
In-Memory Runtime Memory

File:
    in_memory.py

Purpose:
    Default Runtime Memory implementation used during development
    and Project BRAHMA v0.1 boot.

Description:
    Implements AgentMemory using an in-process dictionary.

    Characteristics

        • Fast
        • Lightweight
        • No external dependency
        • Runtime Scoped
        • Easily replaceable

    This implementation is intentionally simple.

    Future implementations may include

        • RedisMemory
        • VectorMemory
        • GraphMemory
        • HybridMemory

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

from typing import Any

from ...AGENTS.CORE.agent_memory import AgentMemory


# =============================================================================
# In-Memory Implementation
# =============================================================================

class InMemory(AgentMemory):
    """
    Default runtime memory.

    Stores information in a Python dictionary.

    Lifetime:

        Runtime only.
    """

    # -------------------------------------------------------------------------

    def __init__(self) -> None:

        self._storage: dict[str, Any] = {}

    # =========================================================================
    # Write Operations
    # =========================================================================

    def store(
        self,
        key: str,
        value: Any,
    ) -> None:

        self._storage[key] = value

    # -------------------------------------------------------------------------

    def update(
        self,
        key: str,
        value: Any,
    ) -> None:

        self._storage[key] = value

    # -------------------------------------------------------------------------

    def delete(
        self,
        key: str,
    ) -> None:

        self._storage.pop(key, None)

    # =========================================================================
    # Read Operations
    # =========================================================================

    def retrieve(
        self,
        key: str,
    ) -> Any:

        return self._storage.get(key)

    # -------------------------------------------------------------------------

    def exists(
        self,
        key: str,
    ) -> bool:

        return key in self._storage

    # =========================================================================
    # Search
    # =========================================================================

    def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[Any]:
        """
        Simple keyword search.

        Future implementations may perform

            • Vector Search
            • Semantic Search
            • Hybrid Search
        """

        query = query.lower()

        results = []

        for key, value in self._storage.items():

            if query in key.lower():

                results.append(value)

                continue

            if query in str(value).lower():

                results.append(value)

            if len(results) >= limit:

                break

        return results

    # =========================================================================
    # Management
    # =========================================================================

    def clear(self) -> None:

        self._storage.clear()

    # -------------------------------------------------------------------------

    def size(self) -> int:

        return len(self._storage)

    # -------------------------------------------------------------------------

    def statistics(self) -> dict:

        return {
            "memory_type": self.memory_type,
            "storage_backend": "Python Dictionary",
            "total_records": len(self._storage),
        }

    # =========================================================================

    @property
    def memory_type(self) -> str:

        return "InMemory"

    # =========================================================================

    def keys(self):

        return list(self._storage.keys())

    # -------------------------------------------------------------------------

    def values(self):

        return list(self._storage.values())

    # -------------------------------------------------------------------------

    def items(self):

        return list(self._storage.items())

    # =========================================================================

    def __len__(self) -> int:

        return len(self._storage)

    # -------------------------------------------------------------------------

    def __contains__(self, key: str) -> bool:

        return key in self._storage

    # -------------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            "InMemory("
            f"records={len(self._storage)})"
        )