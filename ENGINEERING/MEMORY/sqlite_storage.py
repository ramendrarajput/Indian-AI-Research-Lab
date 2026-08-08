"""
PROJECT BRAHMA

SQLite Memory Storage
"""

from __future__ import annotations
import sqlite3
from pathlib import Path

from ENGINEERING.MEMORY.memory_type import MemoryType
from .storage import MemoryStorage
import json
from .memory_record import MemoryRecord
from datetime import datetime


class SQLiteMemoryStorage(MemoryStorage):

    def __init__(self):

        self.database = Path("memory.db")

        self.connection = sqlite3.connect(self.database)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self._create_tables()

    def save(
        self,
        record: MemoryRecord,
    ):

        self.cursor.execute(

            """
            INSERT OR REPLACE INTO memories(

                uid,
                timestamp,
                category,
                source,
                content,
                importance,
                tags,
                payload,
                metadata

            )

            VALUES(

                ?,?,?,?,?,?,?,?,?

            )

            """,

            (

                record.uid,

                record.timestamp.isoformat(),

                record.category,

                record.source,

                record.content,

                record.importance,

                json.dumps(record.tags),

                json.dumps(record.payload),

                json.dumps(record.metadata),

            ),

        )

        self.connection.commit()

    def load_all(self):

        rows = self.cursor.execute(
            """
            SELECT *
            FROM memories
            ORDER BY importance DESC, timestamp DESC
            """
        ).fetchall()

        memories = []

        for row in rows:

            memories.append(
                MemoryRecord(
                    uid=row["uid"],
                    timestamp=datetime.fromisoformat(row["timestamp"]),
                    category=MemoryType(row["category"]),
                    source=row["source"],
                    content=row["content"],
                    importance=row["importance"],
                    tags=json.loads(row["tags"] or "[]"),
                    payload=json.loads(row["payload"] or "{}"),
                    metadata=json.loads(row["metadata"] or "{}"),
                )
            )

        return memories
    
    def clear(self):

        raise NotImplementedError

    # ==========================================================
    # Search Memory
    # ==========================================================

    def search(
        self,
        query: str,
    ):

        rows = self.cursor.execute(

            """
            SELECT *

            FROM memories

            WHERE

                content LIKE ?

                OR category LIKE ?

                OR source LIKE ?

            ORDER BY

            importance DESC,

            timestamp DESC
            """,

            (
                f"%{query}%",
                f"%{query}%",
                f"%{query}%",

            ),

        ).fetchall()

        memories = []

        for row in rows:

            memories.append(

                MemoryRecord(

                    uid=row["uid"],

                    timestamp=datetime.fromisoformat(row["timestamp"]),

                    #category=row["category"],
                    category=MemoryType(row["category"]),

                    source=row["source"],

                    content=row["content"],

                    importance=row["importance"],

                    tags=json.loads(row["tags"]),

                    payload=json.loads(row["payload"]),

                    metadata=json.loads(row["metadata"]),

                )

            )

        return memories

    # ==========================================================
    # Create Database
    # ==========================================================

    def _create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memories(

                uid TEXT PRIMARY KEY,

                timestamp TEXT,

                category TEXT,

                source TEXT,

                content TEXT,

                importance REAL,

                tags TEXT,

                payload TEXT,

                metadata TEXT

            )
            """
        )

        self.connection.commit()