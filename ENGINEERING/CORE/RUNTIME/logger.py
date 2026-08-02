"""
PROJECT BRAHMA
Universal Runtime Logger

Author:
    Ramendra Singh Rajput

Description
-----------
Central logging system for the BRAHMA Runtime.

Every runtime component uses this logger.

Responsibilities
----------------
• Boot Logs
• Runtime Logs
• Kernel Logs
• Service Logs
• Laboratory Logs
• Exception Logs

Future
------
• UI Log Streaming
• Remote Logging
• Distributed Runtime Logs
"""

from __future__ import annotations

import logging
from pathlib import Path


# -------------------------------------------------------------------
# Log Directory
# -------------------------------------------------------------------

LOG_DIRECTORY = Path("ENGINEERING/LOGS")
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "runtime.log"


# -------------------------------------------------------------------
# Logger
# -------------------------------------------------------------------

LOGGER_NAME = "BRAHMA_RUNTIME"

logger = logging.getLogger(LOGGER_NAME)


if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    #
    # Console
    #

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    #
    # File
    #

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    #
    # Register
    #

    logger.addHandler(console_handler)

    logger.addHandler(file_handler)

    logger.propagate = False


# -------------------------------------------------------------------
# Runtime Log API
# -------------------------------------------------------------------

def runtime(message: str) -> None:
    logger.info(f"[RUNTIME] {message}")


def boot(message: str) -> None:
    logger.info(f"[BOOT] {message}")

# -------------------------------------------------------------------
# Startup Logs
# -------------------------------------------------------------------

def startup(message: str) -> None:
    logger.info(f"[STARTUP] {message}")

def kernel(message: str) -> None:
    logger.info(f"[KERNEL] {message}")


def service(message: str) -> None:
    logger.info(f"[SERVICE] {message}")


def lab(message: str) -> None:
    logger.info(f"[LAB] {message}")


def warning(message: str) -> None:
    logger.warning(message)


def error(message: str) -> None:
    logger.error(message)


def critical(message: str) -> None:
    logger.critical(message)