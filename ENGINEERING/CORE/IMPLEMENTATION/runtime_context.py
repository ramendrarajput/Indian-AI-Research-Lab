"""
===============================================================================
Project BRAHMA
Runtime Context

File:
    runtime_context.py

Purpose:
    Defines the central Runtime Context shared across the entire BRAHMA Runtime.

Description:
    RuntimeContext is the execution universe of Project BRAHMA.

    Every runtime component receives the same RuntimeContext instance.

    It contains runtime state, registries, configuration,
    services, event bus, memory engine and runtime metadata.

Author:
    Project BRAHMA

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class RuntimeMetadata:
    """
    Immutable runtime metadata.
    """

    runtime_name: str = "BRAHMA Runtime"

    runtime_version: str = "1.0.0"

    started_at: datetime = field(default_factory=datetime.utcnow)

    session_id: str = ""


# =============================================================================


@dataclass(slots=True)
class RuntimeContext:
    """
    Global execution context of Project BRAHMA.

    Every component receives RuntimeContext.

    Components must never communicate using globals.

    They communicate through RuntimeContext.
    """

    # -------------------------------------------------------------------------
    # Runtime Identity
    # -------------------------------------------------------------------------

    metadata: RuntimeMetadata = field(default_factory=RuntimeMetadata)

    # -------------------------------------------------------------------------
    # Configuration
    # -------------------------------------------------------------------------

    configuration: Any = None

    # -------------------------------------------------------------------------
    # Registries
    # -------------------------------------------------------------------------

    service_registry: Any = None

    tool_registry: Any = None

    provider_registry: Any = None

    agent_registry: Any = None

    workflow_registry: Any = None

    plugin_registry: Any = None

    # -------------------------------------------------------------------------
    # Runtime Infrastructure
    # -------------------------------------------------------------------------

    event_bus: Any = None

    lifecycle_manager: Any = None

    runtime_kernel: Any = None

    scheduler: Any = None

    cache: Any = None

    # -------------------------------------------------------------------------
    # Memory
    # -------------------------------------------------------------------------

    memory_manager: Any = None

    # -------------------------------------------------------------------------
    # Observability
    # -------------------------------------------------------------------------

    logger: Any = None

    metrics: Any = None

    tracer: Any = None

    # -------------------------------------------------------------------------
    # Security
    # -------------------------------------------------------------------------

    security_manager: Any = None

    # -------------------------------------------------------------------------
    # Storage
    # -------------------------------------------------------------------------

    storage_manager: Any = None

    # -------------------------------------------------------------------------
    # Internal Runtime State
    # -------------------------------------------------------------------------

    state: dict[str, Any] = field(default_factory=dict)

    # -------------------------------------------------------------------------
    # Shared Runtime Objects
    # -------------------------------------------------------------------------

    shared_objects: dict[str, Any] = field(default_factory=dict)

    # =========================================================================
    # State Management
    # =========================================================================

    def set_state(self, key: str, value: Any) -> None:
        """
        Store runtime state.
        """

        self.state[key] = value

    # -------------------------------------------------------------------------

    def get_state(self, key: str, default: Any = None) -> Any:
        """
        Retrieve runtime state.
        """

        return self.state.get(key, default)

    # =========================================================================
    # Shared Objects
    # =========================================================================

    def register(self, name: str, obj: Any) -> None:
        """
        Register shared runtime object.
        """

        self.shared_objects[name] = obj

    # -------------------------------------------------------------------------

    def resolve(self, name: str) -> Any:
        """
        Resolve shared runtime object.
        """

        return self.shared_objects.get(name)

    # =========================================================================

    def clear(self) -> None:
        """
        Clear runtime state.

        Used during shutdown.
        """

        self.state.clear()

        self.shared_objects.clear()