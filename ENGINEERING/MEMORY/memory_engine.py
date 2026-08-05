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

from ENGINEERING.MEMORY.working_memory import WorkingMemory
from ENGINEERING.MEMORY.session_memory import SessionMemory
from ENGINEERING.MEMORY.memory_record import MemoryRecord

class MemoryEngine:
    def __init__(self):

        self.working = WorkingMemory()

        self.session = SessionMemory()

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

runtime_memory = MemoryEngine()    