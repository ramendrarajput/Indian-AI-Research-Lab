"""
PROJECT BRAHMA
Memory Storage

Persistent Storage Layer
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .memory_record import MemoryRecord


class MemoryStorage(ABC):
    """
    Abstract storage backend.

    Every persistent memory backend
    must implement this interface.
    """

    @abstractmethod
    def save(self, record: MemoryRecord) -> None:
        ...

    @abstractmethod
    def load_all(self) -> list[MemoryRecord]:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...