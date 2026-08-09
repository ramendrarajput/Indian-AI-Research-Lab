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

    # def search(
    #     self,
    #     query: str,
    # ):

    #     rows = self.cursor.execute(

    #         """
    #         SELECT *

    #         FROM memories

    #         WHERE

    #             content LIKE ?

    #             OR category LIKE ?

    #             OR source LIKE ?

    #         ORDER BY

    #         importance DESC,

    #         timestamp DESC
    #         """,

    #         (
    #             f"%{query}%",
    #             f"%{query}%",
    #             f"%{query}%",

    #         ),

    #     ).fetchall()

    #     memories = []

    #     for row in rows:

    #         memories.append(

    #             MemoryRecord(

    #                 uid=row["uid"],

    #                 timestamp=datetime.fromisoformat(row["timestamp"]),

    #                 #category=row["category"],
    #                 category=MemoryType(row["category"]),

    #                 source=row["source"],

    #                 content=row["content"],

    #                 importance=row["importance"],

    #                 tags=json.loads(row["tags"]),

    #                 payload=json.loads(row["payload"]),

    #                 metadata=json.loads(row["metadata"]),

    #             )

    #         )

    #     return memories

    # ==========================================================
    # Search Memory
    # ==========================================================

    # def search(
    #     self,
    #     query: str,
    # ):

    #     query = query.strip().lower()

    #     if not query:
    #         return []

    #     rows = self.cursor.execute(
    #         """
    #         SELECT *
    #         FROM memories
    #         """
    #     ).fetchall()

    #     scored_memories = []

    #     query_tokens = set(query.split())

    #     for row in rows:

    #         content = (row["content"] or "").lower()
    #         category = (row["category"] or "").lower()
    #         source = (row["source"] or "").lower()

    #         tags = json.loads(row["tags"] or "[]")

    #         tags = [
    #             str(tag).lower()
    #             for tag in tags
    #         ]

    #         score = 0.0

    #         # --------------------------------------------------
    #         # Content Match
    #         # --------------------------------------------------

    #         if query == content:
    #             score += 100

    #         elif query in content:
    #             score += 50

    #         # --------------------------------------------------
    #         # Token Match
    #         # --------------------------------------------------

    #         content_tokens = set(content.split())

    #         matched_tokens = query_tokens.intersection(
    #             content_tokens
    #         )

    #         score += len(matched_tokens) * 10

    #         # --------------------------------------------------
    #         # Tag Match
    #         # --------------------------------------------------

    #         for token in query_tokens:

    #             if token in tags:
    #                 score += 25

    #         # --------------------------------------------------
    #         # Category Match
    #         # --------------------------------------------------

    #         if query in category:
    #             score += 20

    #         # --------------------------------------------------
    #         # Source Match
    #         # --------------------------------------------------

    #         if query in source:
    #             score += 15

    #         # --------------------------------------------------
    #         # Importance
    #         # --------------------------------------------------

    #         score += float(row["importance"] or 0)

    #         # --------------------------------------------------
    #         # Only Relevant Memories
    #         # --------------------------------------------------

    #         if score <= 0:
    #             continue

    #         memory = MemoryRecord(

    #             uid=row["uid"],

    #             timestamp=datetime.fromisoformat(
    #                 row["timestamp"]
    #             ),

    #             category=MemoryType(row["category"]),

    #             source=row["source"],

    #             content=row["content"],

    #             importance=row["importance"],

    #             tags=json.loads(
    #                 row["tags"] or "[]"
    #             ),

    #             payload=json.loads(
    #                 row["payload"] or "{}"
    #             ),

    #             metadata=json.loads(
    #                 row["metadata"] or "{}"
    #             ),

    #         )

    #         scored_memories.append(
    #             (score, memory)
    #         )

    #     # ------------------------------------------------------
    #     # Rank Memories
    #     # ------------------------------------------------------

    #     scored_memories.sort(
    #         key=lambda item: (
    #             item[0],
    #             item[1].timestamp,
    #         ),
    #         reverse=True,
    #     )

    #     return [
    #         memory
    #         for score, memory
    #         in scored_memories
    #     ]

    # ==========================================================
    # Search Memory
    # ==========================================================

    def search(
        self,
        query: str,
    ):

        query = query.strip().lower()

        if not query:
            return []

        rows = self.cursor.execute(
            """
            SELECT *
            FROM memories
            """
        ).fetchall()

        scored_memories = []

        query_tokens = set(query.split())

        for row in rows:

            content = (row["content"] or "").lower()
            category = (row["category"] or "").lower()
            source = (row["source"] or "").lower()

            tags = json.loads(
                row["tags"] or "[]"
            )

            tags = [
                str(tag).lower()
                for tag in tags
            ]

            content_tokens = set(
                content.split()
            )

            # ==================================================
            # Relevance
            # ==================================================

            relevant = False

            # Exact content match
            if query == content:

                relevant = True

            # Query appears inside content
            elif query in content:

                relevant = True

            # At least one query token appears in content
            elif query_tokens.intersection(
                content_tokens
            ):

                relevant = True

            # Query token appears in tags
            elif any(
                token in tags
                for token in query_tokens
            ):

                relevant = True

            # Query appears in category
            elif query in category:

                relevant = True

            # Query appears in source
            elif query in source:

                relevant = True

            # Ignore completely unrelated memories
            if not relevant:

                continue

            # ==================================================
            # Relevance Score
            # ==================================================

            score = 0.0

            # --------------------------------------------------
            # Exact Content Match
            # --------------------------------------------------

            if query == content:

                score += 100

            # --------------------------------------------------
            # Phrase Match
            # --------------------------------------------------

            elif query in content:

                score += 50

            # --------------------------------------------------
            # Token Match
            # --------------------------------------------------

            matched_tokens = query_tokens.intersection(
                content_tokens
            )

            score += (
                len(matched_tokens) * 10
            )

            # --------------------------------------------------
            # Tag Match
            # --------------------------------------------------

            for token in query_tokens:

                if token in tags:

                    score += 25

            # --------------------------------------------------
            # Category Match
            # --------------------------------------------------

            if query in category:

                score += 20

            # --------------------------------------------------
            # Source Match
            # --------------------------------------------------

            if query in source:

                score += 15

            # --------------------------------------------------
            # Importance Bonus
            # --------------------------------------------------

            score += float(
                row["importance"] or 0
            )

            # ==================================================
            # Build Memory Record
            # ==================================================

            memory = MemoryRecord(

                uid=row["uid"],

                timestamp=datetime.fromisoformat(
                    row["timestamp"]
                ),

                category=MemoryType(
                    row["category"]
                ),

                source=row["source"],

                content=row["content"],

                importance=row["importance"],

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

            scored_memories.append(
                (
                    score,
                    memory,
                )
            )

        # ======================================================
        # Rank Memories
        # ======================================================

        scored_memories.sort(

            key=lambda item: (
                item[0],
                item[1].importance,
                item[1].timestamp,
            ),

            reverse=True,
        )

        # ======================================================
        # Return Ranked Memories
        # ======================================================

        return [
            memory
            for score, memory
            in scored_memories
        ]

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