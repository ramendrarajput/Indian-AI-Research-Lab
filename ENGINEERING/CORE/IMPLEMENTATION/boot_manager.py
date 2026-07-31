"""
===============================================================================
Project BRAHMA
Boot Manager

File:
    boot_manager.py

Purpose:
    Orchestrates complete Runtime Boot and Shutdown.

Description:
    BootManager is responsible for coordinating the complete runtime
    lifecycle.

    Responsibilities:

        • Build Runtime
        • Execute Startup Sequence
        • Start Runtime Kernel
        • Shutdown Runtime

    BootManager NEVER creates components directly.

    Component creation belongs to RuntimeBuilder.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

import logging

from .runtime_builder import RuntimeBuilder
from .startup_sequence import StartupSequence
from .shutdown_sequence import ShutdownSequence

logger = logging.getLogger(__name__)


class BootManager:
    """
    BRAHMA Runtime Boot Manager.

    Coordinates the complete runtime lifecycle.
    """

    def __init__(self) -> None:

        self.context = None

    # =========================================================================
    # Public API
    # =========================================================================

    def boot(self) -> None:
        """
        Boot the BRAHMA Runtime.
        """

        logger.info("=" * 80)
        logger.info("PROJECT BRAHMA Runtime Boot")
        logger.info("=" * 80)

        # ---------------------------------------------------------------------
        # Build Runtime
        # ---------------------------------------------------------------------

        self.context = RuntimeBuilder().build()

        # ---------------------------------------------------------------------
        # Startup
        # ---------------------------------------------------------------------

        StartupSequence(self.context).execute()

        # ---------------------------------------------------------------------
        # Start Runtime Kernel
        # ---------------------------------------------------------------------

        self._start_runtime()

        logger.info("BRAHMA Runtime is now operational.")

    # =========================================================================

    def shutdown(self) -> None:
        """
        Shutdown BRAHMA Runtime.
        """

        if self.context is None:

            logger.warning("Runtime not initialized.")

            return

        logger.info("=" * 80)
        logger.info("PROJECT BRAHMA Runtime Shutdown")
        logger.info("=" * 80)

        ShutdownSequence(self.context).execute()

        logger.info("BRAHMA Runtime stopped successfully.")

    # =========================================================================

    def _start_runtime(self) -> None:
        """
        Start Runtime Kernel.
        """

        kernel = self.context.runtime_kernel

        if kernel is None:

            logger.warning("Runtime Kernel not available.")

            return

        kernel.start()

    # =========================================================================

    @property
    def runtime(self):
        """
        Return Runtime Context.
        """

        return self.context