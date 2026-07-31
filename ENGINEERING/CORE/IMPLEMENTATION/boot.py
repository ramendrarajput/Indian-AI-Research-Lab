"""
===============================================================================
Project BRAHMA
Runtime Entry Point

File:
    boot.py

Purpose:
    Public entry point for the BRAHMA Runtime.

Description:
    This module is intentionally minimal.

    Responsibilities:

        • Configure Logging
        • Create BootManager
        • Boot Runtime
        • Handle Fatal Errors
        • Ensure Graceful Shutdown

    All runtime orchestration belongs to BootManager.

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

import logging
import sys

from .boot_manager import BootManager


# =============================================================================
# Logging
# =============================================================================

def configure_logging() -> None:
    """
    Configure runtime logging.

    NOTE:
        Future versions may replace this with the
        Observability subsystem.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


# =============================================================================
# Runtime Entry
# =============================================================================

def main() -> int:
    """
    Start the BRAHMA Runtime.

    Returns
    -------
    int
        Process exit code.
    """

    configure_logging()

    logger = logging.getLogger(__name__)

    runtime = BootManager()

    try:

        runtime.boot()

        logger.info("BRAHMA Runtime started successfully.")

        #
        # NOTE
        #
        # Future Runtime Loop
        #
        # while runtime.runtime.lifecycle_manager.is_running():
        #
        #     runtime.runtime.runtime_kernel.tick()
        #
        #

        return 0

    except KeyboardInterrupt:

        logger.info("Shutdown requested by user.")

        runtime.shutdown()

        return 0

    except Exception:

        logger.exception("Fatal Runtime Error")

        runtime.shutdown()

        return 1


# =============================================================================

if __name__ == "__main__":

    sys.exit(main())