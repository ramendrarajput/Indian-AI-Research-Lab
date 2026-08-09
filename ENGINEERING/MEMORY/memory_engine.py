"""
PROJECT BRAHMA
Universal Memory Engine

Author
------
Ramendra Singh Rajput

Description
-----------
Central Memory Manager of Project BRAHMA.

Coordinates all Runtime Memories.

Memory Lifecycle
----------------
Working Memory
      ↓
Session Memory
      ↓
Long-Term Memory
      ↓
Persistent Storage

Future
------
• Vector Memory
• Semantic Recall
• Knowledge Base
• Reflection
• Learning
"""

from __future__ import annotations

from ENGINEERING.CORE.RUNTIME.logger import runtime

from ENGINEERING.MEMORY.working_memory import WorkingMemory
from ENGINEERING.MEMORY.session_memory import SessionMemory
from ENGINEERING.MEMORY.long_term_memory import LongTermMemory
from ENGINEERING.MEMORY.memory_record import MemoryRecord
from ENGINEERING.MEMORY.memory_type import MemoryType


class MemoryEngine:
    """
    Central coordinator of the BRAHMA Memory System.

    MemoryEngine does not directly own the persistent
    storage backend.

    LongTermMemory owns persistent memory storage.

    Memory lifecycle:

        remember()
            ↓
        Working Memory
            ↓
        Session Memory
            ↓
        Long-Term Memory
            ↓
        Persistent Storage
    """

    # ==========================================================
    # Initialization
    # ==========================================================

    def __init__(self):

        self.working = WorkingMemory()

        self.session = SessionMemory()

        self.long_term = LongTermMemory()

        # ------------------------------------------------------
        # Load Persistent Long-Term Memory
        # ------------------------------------------------------

        records = self.long_term.storage.load_all()

        self.long_term.load(records)

        runtime("Long-Term Memory Loaded.")

    # ==========================================================
    # Remember
    # ==========================================================

    def remember(
        self,
        content: str | MemoryRecord,
        category: MemoryType = MemoryType.GENERAL,
        source: str = "runtime",
        importance: float = 0.0,
    ) -> MemoryRecord:
        """
        Create or register a new memory.

        A new memory enters Working Memory first.

        MemoryRecord instances are accepted directly so existing
        Runtime integrations remain compatible.
        """

        # ------------------------------------------------------
        # Existing MemoryRecord
        # ------------------------------------------------------

        if isinstance(content, MemoryRecord):

            record = content

        # ------------------------------------------------------
        # Create New MemoryRecord
        # ------------------------------------------------------

        elif isinstance(content, str):

            record = MemoryRecord(

                category=category,

                source=source,

                content=content,

                importance=importance,

            )

        else:

            raise TypeError(
                "content must be a str or MemoryRecord"
            )

        # ------------------------------------------------------
        # Working Memory
        # ------------------------------------------------------

        self.working.add(record)

        return record

    # ==========================================================
    # Recent Working Memory
    # ==========================================================

    def recent(
        self,
        count: int = 10,
    ):

        return self.working.recent(count)

    # ==========================================================
    # Recent Session Memory
    # ==========================================================

    def session_recent(
        self,
        count: int = 10,
    ):

        return self.session.recent(count)

    # ==========================================================
    # Memory Summary
    # ==========================================================

    def summary(self):

        return {

            "working": self.working.size(),

            "session": self.session.size(),

            "long_term": self.long_term.size(),

            "session_id": self.session.session_id,

        }

    # ==========================================================
    # Clear Working Memory
    # ==========================================================

    def clear_working(self):

        self.working.clear()

    # ==========================================================
    # Clear Session Memory
    # ==========================================================

    def clear_session(self):

        self.session.clear()

    # ==========================================================
    # Clear Runtime Memory
    # ==========================================================

    def clear(self):

        self.clear_working()

        self.clear_session()

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self):

        return (

            "MemoryEngine("

            f"working={self.working.size()}, "

            f"session={self.session.size()}, "

            f"long_term={self.long_term.size()})"

        )

    # ==========================================================
    # Recall Working Memory
    # ==========================================================

    def recall_working(self):

        return self.working.all()

    # ==========================================================
    # Recall Session Memory
    # ==========================================================

    def recall_session(self):

        return self.session.all()

    # ==========================================================
    # Recall Long-Term Memory
    # ==========================================================

    def recall_long_term(self):

        return self.long_term.all()

    # ==========================================================
    # Update Long-Term Memory
    # ==========================================================

    def update_memory(
        self,
        record: MemoryRecord,
    ):

        return self.long_term.update(record)

    # ==========================================================
    # Find Long-Term Memory By UID
    # ==========================================================

    def get_long_term_by_uid(
        self,
        uid: str,
    ):

        for record in self.long_term.all():

            if record.uid == uid:

                return record

        return None

    # ==========================================================
    # Statistics
    # ==========================================================

    def statistics(self):

        return {

            "working": self.working.size(),

            "session": self.session.size(),

            "long_term": self.long_term.size(),

        }

    # ==========================================================
    # Promote Working → Session
    # ==========================================================

    def promote_working_to_session(self):

        records = self.working.all()

        for record in records:

            self.session.add(record)

        self.working.clear()

    # ==========================================================
    # Promote Session → Long-Term
    # ==========================================================

    def promote_session_to_long_term(self):

        records = self.session.all()

        for record in records:

            self.long_term.add(record)

        self.session.clear()

    # ==========================================================
    # Consolidate Memory
    # ==========================================================

    def consolidate(self):
        """
        Complete memory consolidation lifecycle.

        Working
            ↓
        Session
            ↓
        Long-Term
            ↓
        Persistent Storage
        """

        self.promote_working_to_session()

        self.promote_session_to_long_term()

    # ==========================================================
    # Recall Long-Term Memory
    # ==========================================================

    def recall(
        self,
        query: str,
    ):

        return self.long_term.recall(query)


# ==============================================================
# Global Runtime Memory Engine
# ==============================================================

runtime_memory = MemoryEngine()