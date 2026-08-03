"""
PROJECT BRAHMA
Universal Runtime Context

Author:
    Ramendra Singh Rajput

Description
-----------
The Runtime Context is the single source of truth for the
entire BRAHMA Runtime.

Every subsystem receives the same RuntimeContext instance.

The Runtime Context stores runtime-wide objects such as:

• Runtime State
• Logger
• Registry
• Kernel
• Configuration
• Environment
• Metadata

No runtime component should create duplicate global objects.

Philosophy
----------
One Runtime

↓

One Context

↓

One Truth
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from ENGINEERING.CORE.RUNTIME.state import RuntimeStatus, runtime_state
from ENGINEERING.CORE.RUNTIME.logger import logger


@dataclass(slots=True)
class RuntimeContext:
    """
    Universal Runtime Context.

    Shared across the complete BRAHMA Runtime.
    """

    # -------------------------------------------------------
    # Runtime Information
    # -------------------------------------------------------

    version: str = "0.2"

    runtime_name: str = "Project BRAHMA"

    boot_time: datetime = field(default_factory=datetime.now)

    # -------------------------------------------------------
    # Runtime Services
    # -------------------------------------------------------

    state: RuntimeStatus = field(default_factory=lambda: runtime_state)

    logger: Any = field(default_factory=lambda: logger)

    # -------------------------------------------------------
    # Runtime Components
    # -------------------------------------------------------

    registry: Any = None

    kernel: Any = None

    settings: Any = None

    environment: Any = None

    event_bus: Any = None

    event_history: Any = None

    # -------------------------------------------------------
    # Future Runtime Objects
    # -------------------------------------------------------

    universal_agent: Any = None

    memory: Any = None

    event_bus: Any = None

    scheduler: Any = None

    # -------------------------------------------------------
    # Laboratory Runtime
    # -------------------------------------------------------

    loaded_labs: dict[str, Any] = field(default_factory=dict)

    # -------------------------------------------------------
    # Runtime Metadata
    # -------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # -------------------------------------------------------
    # Utility Methods
    # -------------------------------------------------------

    def register_lab(self, name: str, lab: Any) -> None:
        """
        Register a laboratory.
        """
        self.loaded_labs[name] = lab

    def get_lab(self, name: str) -> Any:
        """
        Retrieve a registered laboratory.
        """
        return self.loaded_labs.get(name)

    def has_lab(self, name: str) -> bool:
        """
        Check whether a laboratory is loaded.
        """
        return name in self.loaded_labs

    def uptime(self):
        """
        Runtime uptime.
        """
        return datetime.now() - self.boot_time


#
# Global Runtime Context
#

runtime_context = RuntimeContext()