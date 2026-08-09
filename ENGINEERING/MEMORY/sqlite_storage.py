"""
PROJECT BRAHMA

SQLite Memory Storage

Persistent storage backend for the Universal Memory Engine.
"""

from __future__ import annotations

import json
import sqlite3

from datetime import datetime
from pathlib import Path

from ENGINEERING.MEMORY.memory_record import MemoryRecord
from ENGINEERING.MEMORY.memory_type import MemoryType

from .storage import MemoryStorage


class SQLiteMemoryStorage(MemoryStorage):
    """
    SQLite-backed persistent memory storage.

    Responsibilities
    ----------------
    • Create the memory database.
    • Persist MemoryRecord objects.
    • Load persistent memories.
    • Search persistent memories.
    • Replace existing records using UID.
    • Provide controlled database cleanup.

    The storage layer knows nothing about Working Memory,
    Session Memory, or Runtime lifecycle.

    It only manages persistence.
    """

    # ==========================================================
    # Initialization
    # ==========================================================

    def __init__(
        self,
        database: str | Path = "memory.db",
    ):

        self.database = Path(database)

        self.connection = sqlite3.connect(
            self.database
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self._create_tables()

    # ==========================================================
    # Save / Insert / Replace
    # ==========================================================

    def save(
        self,
        record: MemoryRecord,
    ) -> None:
        """
        Persist a MemoryRecord.

        UID is the primary identity of a memory.

        If the UID already exists, the existing database
        record is replaced.
        """

        if not isinstance(record, MemoryRecord):

            raise TypeError(
                "record must be a MemoryRecord"
            )

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

                ?, ?, ?, ?, ?, ?, ?, ?, ?

            )
            """,
            (
                record.uid,
                record.timestamp.isoformat(),
                record.category.value
                if isinstance(record.category, MemoryType)
                else str(record.category),
                record.source,
                record.content,
                record.importance,
                json.dumps(record.tags),
                json.dumps(record.payload),
                json.dumps(record.metadata),
            ),
        )

        self.connection.commit()

    # ==========================================================
    # Load All Memories
    # ==========================================================

    def load_all(self) -> list[MemoryRecord]:
        """
        Load all persistent memories.

        Important memories are returned first,
        followed by newer memories.
        """

        rows = self.cursor.execute(
            """
            SELECT *
            FROM memories
            ORDER BY importance DESC, timestamp DESC
            """
        ).fetchall()

        return [
            self._row_to_memory(row)
            for row in rows
        ]

    # ==========================================================
    # Search Memory
    # ==========================================================

    def search(
        self,
        query: str,
    ) -> list[MemoryRecord]:
        """
        Search persistent memories.

        Current search scope:

        • content
        • category
        • source

        Results are ordered by importance and timestamp.
        """

        query = query.strip()

        if not query:

            return []

        pattern = f"%{query}%"

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
                pattern,
                pattern,
                pattern,
            ),
        ).fetchall()

        return [
            self._row_to_memory(row)
            for row in rows
        ]

    # ==========================================================
    # Delete All Memories
    # ==========================================================

    def clear(self) -> None:
        """
        Permanently delete all persistent memories.

        This operation is intentionally explicit.
        """

        self.cursor.execute(
            """
            DELETE FROM memories
            """
        )

        self.connection.commit()

    # ==========================================================
    # Close Storage
    # ==========================================================

    def close(self) -> None:
        """
        Close the SQLite connection.
        """

        if self.connection:

            self.connection.close()

    # ==========================================================
    # Context Manager
    # ==========================================================

    def __enter__(self):

        return self

    # ----------------------------------------------------------

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):

        self.close()

    # ==========================================================
    # Row → MemoryRecord
    # ==========================================================

    @staticmethod
    def _row_to_memory(
        row: sqlite3.Row,
    ) -> MemoryRecord:
        """
        Convert a SQLite row into MemoryRecord.
        """

        return MemoryRecord(

            uid=row["uid"],

            timestamp=datetime.fromisoformat(
                row["timestamp"]
            ),

            category=MemoryType(
                row["category"]
            ),

            source=row["source"],

            content=row["content"],

            importance=float(
                row["importance"] or 0.0
            ),

            tags=json.loads(
                row["tags"] or "[]"
            ),

            payload=json.loads(
                row["payload"] or "{}"
            ),

            metadata=json.loads(
                row["metadata"] or "{}"
            ),

        )

    # ==========================================================
    # Create Database
    # ==========================================================

    def _create_tables(self) -> None:
        """
        Create the persistent memory table if it does not exist.
        """

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