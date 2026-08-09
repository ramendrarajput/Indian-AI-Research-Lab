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

Future
------
• Working Memory
• Session Memory
• Long-Term Memory
• Vector Memory
• Knowledge Base
• Semantic Recall
• Reflection
"""
from __future__ import annotations

from ENGINEERING.CORE.RUNTIME.logger import runtime
from ENGINEERING.MEMORY.working_memory import WorkingMemory
from ENGINEERING.MEMORY.session_memory import SessionMemory
from ENGINEERING.MEMORY.memory_record import MemoryRecord
from ENGINEERING.MEMORY.long_term_memory import LongTermMemory
from ENGINEERING.MEMORY.memory_type import MemoryType
from .sqlite_storage import SQLiteMemoryStorage

class MemoryEngine:
    def __init__(self):

        self.working = WorkingMemory()
        self.long_term = LongTermMemory()

        self.session = SessionMemory()
        self.storage = SQLiteMemoryStorage()

        # =====================================================
        # Load Persistent Long-Term Memory
        # =====================================================

        records = self.storage.load_all()

        self.long_term.load(records)

        runtime("Long-Term Memory Loaded.")
    

    def remember(

        self,

        record: MemoryRecord,

    ):

        self.working.add(record)

        self.session.add(record)

    def recent(

        self,

        count: int = 10,

    ):

        return self.working.recent(count)

    def session_recent(

        self,

        count: int = 10,

    ):

        return self.session.recent(count)        

    def summary(self):

        return {

            "working": self.working.size(),

            "session": self.session.size(),

            "session_id": self.session.session_id,
 
        }

    def clear_working(self):

        self.working.clear()

    def clear_session(self):

        self.session.clear()

    def clear(self):

        self.clear_working()

        self.clear_session()

    def __repr__(self):

        return (

            "MemoryEngine("

            f"working={self.working.size()}, "

            f"session={self.session.size()})"

        )

    # ==========================================================
    # Store Memory
    # ==========================================================

    def remember(

        self,

        content: str,

        category: MemoryType = MemoryType.GENERAL,

        source: str = "runtime",

        importance: float = 0.0,

    ):

        record = MemoryRecord(

            category=category,

            source=source,

            content=content,

            importance=importance,

        )

        self.working.add(record)

        return record

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
    # Recall Long Term Memory
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

        records = self.long_term.all()

        for record in records:

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
            
            self.storage.save(record)

        self.session.clear()

    # ==========================================================
    # Promote All
    # ==========================================================

    def consolidate(self):

        self.promote_working_to_session()

        self.promote_session_to_long_term()

    # ==========================================================
    # Recall
    # ==========================================================

    def recall(
        self,
        query: str,
    ):

        return self.long_term.recall(query)    

            
runtime_memory = MemoryEngine()    