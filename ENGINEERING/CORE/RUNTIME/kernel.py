"""
PROJECT BRAHMA
Universal Runtime Kernel

Author
------
Ramendra Singh Rajput

Description
-----------
The Runtime Kernel is the execution engine of Project BRAHMA.

Unlike boot.py (which initializes the runtime),
the Kernel manages the lifecycle of the running Runtime.

Responsibilities
----------------
• Start Runtime
• Stop Runtime
• Restart Runtime
• Runtime Health
• Runtime Coordination

Future Responsibilities
-----------------------
• Laboratory Lifecycle
• Universal Agent Lifecycle
• Event Bus
• Memory Engine
• Scheduler
"""

from __future__ import annotations

from ENGINEERING.CORE.RUNTIME.context import runtime_context
from ENGINEERING.CORE.RUNTIME.logger import kernel
from ENGINEERING.CORE.RUNTIME.state import (
    RuntimeState,
    runtime_state,
)


# ==========================================================
# Runtime Kernel
# ==========================================================

class RuntimeKernel:
    """
    Universal Runtime Kernel.

    The Kernel controls the Runtime lifecycle.
    """

    def __init__(self):
        pass

    # ======================================================

    def start(self):

        if runtime_state.is_running():

            kernel("Runtime Kernel already running.")

            return

        runtime_state.set(RuntimeState.LOADING_KERNEL)

        kernel("Loading Runtime Kernel...")

        #
        # Future
        #
        # Initialize Scheduler
        # Initialize Event Bus
        # Initialize Memory
        # Initialize Universal Agent
        #

        runtime_state.set(RuntimeState.RUNNING)

        kernel("Runtime Kernel Started.")

    # ======================================================

    def stop(self):

        if runtime_state.is_stopped():

            kernel("Runtime Kernel already stopped.")

            return

        runtime_state.set(RuntimeState.STOPPING)

        kernel("Stopping Runtime Kernel...")

        #
        # Future
        #
        # Shutdown Services
        # Flush Memory
        # Save Session
        # Unload Labs
        #

        runtime_state.set(RuntimeState.STOPPED)

        kernel("Runtime Kernel Stopped.")

    # ======================================================

    def restart(self):

        kernel("Restarting Runtime Kernel...")

        self.stop()

        self.start()

    # ======================================================

    def pause(self):

        runtime_state.set(RuntimeState.PAUSED)

        kernel("Runtime Paused.")

    # ======================================================

    def resume(self):

        runtime_state.set(RuntimeState.RUNNING)

        kernel("Runtime Resumed.")

    # ======================================================

    def fail(self):

        runtime_state.set(RuntimeState.FAILED)

        kernel("Runtime Failure Detected.")

    # ======================================================

    def is_running(self) -> bool:

        return runtime_state.is_running()

    # ======================================================

    def runtime_status(self):

        return {

            "runtime": runtime_context.runtime_name,

            "version": runtime_context.version,

            "state": runtime_state.state.name,

            "boot_time": runtime_context.boot_time,

            "loaded_labs": len(runtime_context.loaded_labs),

            "services": runtime_context.registry.summary()
            if runtime_context.registry
            else {},

        }


#
# Global Runtime Kernel
#

runtime_kernel = RuntimeKernel()