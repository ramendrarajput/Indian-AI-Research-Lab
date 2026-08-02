"""
PROJECT BRAHMA
Universal Runtime Boot Sequence

Author:
    Ramendra Singh Rajput

Description
-----------
Boot orchestrator for the BRAHMA Runtime.

Responsibilities
----------------
• Initialize Runtime
• Register Core Services
• Prepare Runtime Context
• Transition Runtime States
"""

from __future__ import annotations

from ENGINEERING.CORE.RUNTIME.context import runtime_context
from ENGINEERING.CORE.RUNTIME.logger import (
    boot,
    runtime,
)
from ENGINEERING.CORE.RUNTIME.registry import runtime_registry
from ENGINEERING.CORE.RUNTIME.state import (
    RuntimeStage,
    runtime_state,
)


# ==========================================================
# Runtime Boot
# ==========================================================

def boot_runtime():
    """
    Boot the Project BRAHMA Runtime.
    """

    # ------------------------------------------------------
    # BOOT START
    # ------------------------------------------------------

    runtime_state.set_stage(RuntimeStage.BOOTING)

    boot("Project BRAHMA Runtime Boot Started")

    # ------------------------------------------------------
    # Register Core Services
    # ------------------------------------------------------

    runtime_registry.register_service(
        "logger",
        runtime_context.logger,
    )

    runtime_registry.register_service(
        "runtime_state",
        runtime_context.state,
    )

    runtime_registry.register_service(
        "runtime_context",
        runtime_context,
    )

    runtime_registry.register_service(
        "runtime_registry",
        runtime_registry,
    )

    runtime_context.registry = runtime_registry

    boot("Core Runtime Services Registered")

    # ------------------------------------------------------
    # Runtime Ready
    # ------------------------------------------------------

    runtime_state.set_stage(RuntimeStage.READY)

    runtime("Project BRAHMA Runtime Ready")

    return runtime_context


# ==========================================================
# Runtime Summary
# ==========================================================

def runtime_summary():
    """
    Return Runtime Summary.
    """

    return {
        "runtime": runtime_context.runtime_name,
        "version": runtime_context.version,
        "boot_time": runtime_context.boot_time,
        "state": runtime_state.stage.name,
        "services": runtime_registry.list_services(),
        "labs": runtime_registry.list_labs(),
        "providers": runtime_registry.list_providers(),
    }