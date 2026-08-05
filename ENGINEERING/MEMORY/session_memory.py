"""
PROJECT BRAHMA
Session Memory

Author
------
Ramendra Singh Rajput

Description
-----------
Stores all Memory Records generated during one Runtime Session.

Future
------
• Session Restore

• Session Save

• Session Replay

• Conversation History

• Runtime Recovery
"""
from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from ENGINEERING.MEMORY.memory_record import MemoryRecord

class SessionMemory:

    def __init__(self):

        self.session_id = str(uuid4())

        self.created_at = datetime.now()

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

    def all(self):

        return self._records    

    def size(self):

        return len(self._records)

    def clear(self):

        self._records.clear()

    def summary(self):

        return {

            "session_id": self.session_id,

            "created_at": self.created_at,

            "records": self.size(),

        }    

    def __repr__(self):

        return (

            "SessionMemory("

            f"id={self.session_id}, "

            f"records={self.size()})"

        )

    