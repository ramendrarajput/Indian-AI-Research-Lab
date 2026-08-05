"""
PROJECT BRAHMA
Universal Memory Record

Author
------
Ramendra Singh Rajput

Description
-----------
Atomic Memory Object of Project BRAHMA.

Everything remembered by BRAHMA
is stored as a MemoryRecord.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime

from uuid import uuid4

@dataclass(slots=True)
class MemoryRecord:

    uid: str = field(default_factory=lambda: str(uuid4()))

timestamp: datetime = field(default_factory=datetime.now)

source: str = ""

memory_type: str = ""

importance: int = 1

tags: list[str] = field(default_factory=list)

payload: dict = field(default_factory=dict)

def __repr__(self):

    return (

        f"MemoryRecord("

        f"{self.memory_type}, "

        f"{self.source}, "

        f"{self.timestamp:%H:%M:%S})"

    )

