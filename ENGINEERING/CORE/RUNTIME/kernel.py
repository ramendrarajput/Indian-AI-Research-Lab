"""
PROJECT BRAHMA
Universal Runtime Kernel

Author:
    Ramendra Singh Rajput

Description
-----------
The Runtime Kernel is the central execution engine of
Project BRAHMA.

Unlike boot.py (which initializes the runtime),
the Kernel manages the lifecycle of the running runtime.

Responsibilities
----------------
• Start Runtime
• Stop Runtime
• Restart Runtime
• Runtime Health
• Runtime Coordination

Future Responsibilities
-----------------------
• Laboratory Management
• Universal Agent Lifecycle
• Scheduler
• Event Bus
• Memory Engine
"""

from __future__ import annotations

from enum import Enum, auto

from ENGINEERING.CORE.RUNTIME.context import runtime_context
from ENGINEERING.CORE.RUNTIME.logger import kernel
from ENGINEERING.CORE.RUNTIME.state import runtime_state


# ==========================================================
# Kernel State
# ==========================================================

class KernelStatus(Enum):
    """
    Runtime Kernel States.
    """

    STOPPED = auto()

    STARTING = auto()

    RUNNING = auto()

    STOPPING = auto()


# ==========================================================
# Runtime Kernel
# ==========================================================

class RuntimeKernel:
    """
    Universal Runtime Kernel.
    """

    def __init__(self):

        self.status = KernelStatus.STOPPED

    # ------------------------------------------------------

    def start(self):

        if self.status == KernelStatus.RUNNING:

            kernel("Kernel already running.")

            return

        self.status = KernelStatus.STARTING

        kernel("Starting Runtime Kernel...")

        # Future:
        #
        # initialize scheduler
        # initialize event bus
        # initialize memory
        # initialize universal agent
        #

        self.status = KernelStatus.RUNNING

        kernel("Runtime Kernel Started.")

    # ------------------------------------------------------

    def stop(self):

        if self.status == KernelStatus.STOPPED:

            kernel("Kernel already stopped.")

            return

        self.status = KernelStatus.STOPPING

        kernel("Stopping Runtime Kernel...")

        # Future:
        #
        # shutdown services
        # unload labs
        # flush memory
        #

        self.status = KernelStatus.STOPPED

        kernel("Runtime Kernel Stopped.")

    # ------------------------------------------------------

    def restart(self):

        kernel("Restarting Runtime Kernel...")

        self.stop()

        self.start()

    # ------------------------------------------------------

    def is_running(self) -> bool:

        return self.status == KernelStatus.RUNNING

    # ------------------------------------------------------

    def runtime_status(self):

        return {

            "kernel": self.status.name,

            "runtime": runtime_state.stage.name,

            "version": runtime_context.version,

            "runtime_name": runtime_context.runtime_name,

            "loaded_labs": len(runtime_context.loaded_labs),

        }


#
# Global Kernel
#

runtime_kernel = RuntimeKernel()