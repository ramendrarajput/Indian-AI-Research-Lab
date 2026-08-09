"""
PROJECT BRAHMA
Long Term Memory

Stores permanent knowledge.
"""

from __future__ import annotations

from ENGINEERING.MEMORY.memory_record import MemoryRecord
from ENGINEERING.MEMORY.sqlite_storage import SQLiteMemoryStorage


class LongTermMemory:
    """
    Permanent memory layer of Project BRAHMA.

    Responsibilities
    ----------------
    • Maintain long-term MemoryRecord objects.
    • Load persistent memories during startup.
    • Persist newly promoted memories.
    • Update existing memories.
    • Recall memories through the storage layer.

    Storage ownership
    -----------------
    LongTermMemory owns the persistent storage backend.

    MemoryEngine should not directly save long-term records.
    """

    # ==========================================================
    # Initialization
    # ==========================================================

    def __init__(self):

        self._records: list[MemoryRecord] = []

        self.storage = SQLiteMemoryStorage()

    # ==========================================================
    # Add Memory
    # ==========================================================

    def add(
        self,
        record: MemoryRecord,
    ) -> MemoryRecord:
        """
        Add a memory to Long-Term Memory and persist it.
        """

        if not isinstance(record, MemoryRecord):

            raise TypeError(
                "record must be a MemoryRecord"
            )

        # ------------------------------------------------------
        # Avoid duplicate in-memory records
        # ------------------------------------------------------

        existing_index = self._find_index(record.uid)

        if existing_index is None:

            self._records.append(record)

        else:

            self._records[existing_index] = record

        # ------------------------------------------------------
        # Persist
        # ------------------------------------------------------

        self.storage.save(record)

        return record

    # ==========================================================
    # Load Persistent Memories
    # ==========================================================

    def load(
        self,
        records: list[MemoryRecord],
    ):
        """
        Load persistent memories into the in-memory collection.
        """

        for record in records:

            if not isinstance(record, MemoryRecord):

                continue

            existing_index = self._find_index(record.uid)

            if existing_index is None:

                self._records.append(record)

            else:

                self._records[existing_index] = record

        return self._records

    # ==========================================================
    # Find Memory By UID
    # ==========================================================

    def _find_index(
        self,
        uid: str,
    ):
        """
        Return the in-memory index of a memory UID.
        """

        for index, record in enumerate(self._records):

            if record.uid == uid:

                return index

        return None

    # ==========================================================
    # Get Memory
    # ==========================================================

    def get(
        self,
        index: int,
    ):

        return self._records[index]

    # ==========================================================
    # Get Memory By UID
    # ==========================================================

    def get_by_uid(
        self,
        uid: str,
    ):
        """
        Return a long-term memory by UID.
        """

        index = self._find_index(uid)

        if index is None:

            return None

        return self._records[index]

    # ==========================================================
    # All Memories
    # ==========================================================

    def all(self):

        return self._records

    # ==========================================================
    # Update Memory
    # ==========================================================

    def update(
        self,
        record: MemoryRecord,
    ):
        """
        Update an existing Long-Term Memory.

        The UID remains the identity of the memory.

        The updated record replaces the old in-memory record
        and is persisted through the storage layer.
        """

        if not isinstance(record, MemoryRecord):

            raise TypeError(
                "record must be a MemoryRecord"
            )

        index = self._find_index(record.uid)

        if index is None:

            return None

        self._records[index] = record

        self.storage.save(record)

        return record

    # ==========================================================
    # Clear In-Memory Long-Term Memory
    # ==========================================================

    def clear(self):

        self._records.clear()

    # ==========================================================
    # Size
    # ==========================================================

    def size(self):

        return len(self._records)

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self):

        return {

            "records": len(self._records),

        }

    # ==========================================================
    # Recall
    # ==========================================================

    def recall(
        self,
        query: str,
    ):

        return self.storage.search(query)