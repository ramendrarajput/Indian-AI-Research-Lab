"""
PROJECT BRAHMA

Runtime Metadata Persistence

Stores runtime lifecycle metadata such as:

• Last Boot
• Last Shutdown
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


# ==========================================================
# Runtime Metadata Manager
# ==========================================================

class RuntimeMetadata:

    def __init__(self):

        self.file = Path(__file__).parent / "runtime_metadata.json"

    # ------------------------------------------------------
    # Load
    # ------------------------------------------------------

    def load(self):

        if not self.file.exists():

            return {
                "last_boot": None,
                "last_shutdown": None,
            }

        try:

            with self.file.open(
                "r",
                encoding="utf-8",
            ) as file:

                return json.load(file)

        except (json.JSONDecodeError, OSError):

            return {
                "last_boot": None,
                "last_shutdown": None,
            }

    # ------------------------------------------------------
    # Save
    # ------------------------------------------------------

    def save(self, metadata):

        with self.file.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

    # ------------------------------------------------------
    # Last Boot
    # ------------------------------------------------------

    def record_boot(self):

        metadata = self.load()

        previous_boot = metadata.get("last_boot")

        metadata["last_boot"] = datetime.now().isoformat()

        self.save(metadata)

        return previous_boot

    # ------------------------------------------------------
    # Last Shutdown
    # ------------------------------------------------------

    def record_shutdown(self):

        metadata = self.load()

        metadata["last_shutdown"] = datetime.now().isoformat()

        self.save(metadata)


# ==========================================================
# Global Runtime Metadata
# ==========================================================

runtime_metadata = RuntimeMetadata()