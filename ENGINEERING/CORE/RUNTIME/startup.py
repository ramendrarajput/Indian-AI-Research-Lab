"""
PROJECT BRAHMA
Universal Runtime Startup

Author:
    Ramendra Singh Rajput

Description
-----------
The Startup Manager is responsible for orchestrating the
complete Runtime startup sequence.

Responsibilities
----------------
• Execute Runtime Boot
• Start Runtime Kernel
• Validate Runtime
• Return Runtime Context

Philosophy
----------
Boot creates the Runtime.

Kernel keeps the Runtime alive.

Startup connects them together.
"""

from __future__ import annotations

from ENGINEERING.CORE.RUNTIME.boot import (
    boot_runtime,
    runtime_summary,
)

from ENGINEERING.CORE.RUNTIME.kernel import (
    runtime_kernel,
)

from ENGINEERING.CORE.RUNTIME.logger import startup


# ==========================================================
# Runtime Startup
# ==========================================================

def startup_runtime():
    """
    Start the complete Project BRAHMA Runtime.
    """

    startup("Starting Project BRAHMA Runtime...")

    #
    # Boot Runtime
    #

    context = boot_runtime()

    #
    # Start Kernel
    #

    runtime_kernel.start()

    startup("Project BRAHMA Runtime Successfully Started.")

    return context


# ==========================================================
# Runtime Shutdown
# ==========================================================

def shutdown_runtime():
    """
    Shutdown Project BRAHMA Runtime.
    """

    startup("Stopping Project BRAHMA Runtime...")

    runtime_kernel.stop()

    startup("Runtime Shutdown Completed.")


# ==========================================================
# Runtime Restart
# ==========================================================

def restart_runtime():
    """
    Restart Runtime.
    """

    startup("Restarting Project BRAHMA Runtime...")

    shutdown_runtime()

    startup_runtime()


# ==========================================================
# Runtime Health
# ==========================================================

def runtime_health():
    """
    Runtime health information.
    """

    return {

        "kernel_running": runtime_kernel.is_running(),

        "runtime_summary": runtime_summary(),

        "kernel_summary": runtime_kernel.runtime_status(),

    }