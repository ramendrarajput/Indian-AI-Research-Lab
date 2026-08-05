"""
PROJECT BRAHMA
Working Memory

Author
------
Ramendra Singh Rajput

Description
-----------
Short-term Runtime Memory.

Stores active runtime memories.

Future
------
• Conversation Context

• Active Tasks

• Agent Thoughts

• Runtime State
"""

from __future__ import annotations

from ENGINEERING.MEMORY.memory_record import MemoryRecord

class WorkingMemory:

    def __init__(self):

        self._records: list[MemoryRecord] = []

    def add(

        self,

        record: MemoryRecord,

    ):

        self._records.append(record)

    def recent(

        self,

        count: int = 10,

    ):

        return self._records[-count:]

    def size(self):

        return len(self._records)

    def clear(self):

        self._records.clear()

    def all(self):

        return self._records

    def summary(self):

        return {

            "records": self.size()

        }

    def __repr__(self):

        return (

            f"WorkingMemory("

            f"records={self.size()})"

        )

    