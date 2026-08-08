"""
PROJECT BRAHMA
Long Term Memory

Stores permanent knowledge.
"""

from __future__ import annotations

from ENGINEERING.MEMORY.memory_record import MemoryRecord
from ENGINEERING.MEMORY.sqlite_storage import SQLiteMemoryStorage

class LongTermMemory:

    def __init__(self):

        self._records: list[MemoryRecord] = []
        self.storage = SQLiteMemoryStorage()

    # -------------------------------------------------

    def add(
        self,
        record: MemoryRecord,
    ):

        self._records.append(record)

        self.storage.save(record)
        
    # -------------------------------------------------
    # Load Persistent Memories
    # -------------------------------------------------

    def load(self, records: list[MemoryRecord]):

        self._records.extend(records)

    # -------------------------------------------------    

    def get(self, index: int):

        return self._records[index]

    # -------------------------------------------------

    def all(self):

        return self._records

    # -------------------------------------------------

    def clear(self):

        self._records.clear()

    # -------------------------------------------------

    def size(self):

        return len(self._records)

    # -------------------------------------------------

    def summary(self):

        return {

            "records": len(self._records),

        }

    #-------------------------------------------------

    def recall(
        self,
        query: str,
    ):

        return self.storage.search(query)