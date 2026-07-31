"""
===============================================================================
Project BRAHMA

File:
    main.py

Purpose:
    Official Bootloader of Project BRAHMA.

Description:
    This file is the single entry point of the entire BRAHMA Runtime.

    Responsibilities

        • Load Environment
        • Initialize Logging
        • Initialize Gemini Client
        • Initialize Runtime
        • Initialize Memory
        • Initialize Orchestrator
        • Boot Universal Agent
        • Execute Cognitive Cycle

Author:
    Project BRAHMA
===============================================================================
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from google import genai

# =============================================================================
# Runtime
# =============================================================================

from .RUNTIME.MEMORY.in_memory import InMemory

from .RUNTIME.runtime_context import RuntimeContext

from .RUNTIME.runtime_kernel import RuntimeKernel

from .RUNTIME.runtime import Runtime

from .RUNTIME.runtime_services import RuntimeServices
# =============================================================================
# Orchestration
# =============================================================================

from .AGENTS.ORCHESTRATION.orchestrator import Orchestrator

# =============================================================================
# Boot Banner
# =============================================================================

BOOT_BANNER = r"""

==============================================================

                PROJECT BRAHMA

      Universal Artificial Intelligence Runtime

==============================================================

"""


# =============================================================================
# Project Root
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent

ENV_FILE = PROJECT_ROOT / ".env"


# =============================================================================
# Logging
# =============================================================================

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",
)

LOGGER = logging.getLogger("BRAHMA")


# =============================================================================
# Environment
# =============================================================================
from pathlib import Path
from dotenv import load_dotenv
import logging

LOGGER = logging.getLogger(__name__)

def load_environment() -> None:
    """
    Load .env from multiple possible locations.

    Search order:
        1. Current working directory
        2. ENGINEERING/.env
        3. Project Root/.env
    """

    current = Path(__file__).resolve()

    candidates = [
        Path.cwd() / ".env",
        current.parent / ".env",
        current.parent.parent / ".env",
    ]

    for env_file in candidates:

        if env_file.exists():

            load_dotenv(env_file)

            LOGGER.info(".env loaded from: %s", env_file)

            return

    LOGGER.warning(".env file not found.")

#def load_environment() -> None:
#    """
#    Load .env configuration.
#    """

#    if ENV_FILE.exists():

#        load_dotenv(ENV_FILE)

#        LOGGER.info("Environment loaded.")

#    else:

#        LOGGER.warning(".env file not found.")


# =============================================================================
# Gemini Client
# =============================================================================

def create_gemini_client() -> genai.Client:
    """
    Create Google Gemini Client.
    """

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:

        raise RuntimeError(

            "GOOGLE_API_KEY was not found in environment."
        )

    LOGGER.info("Creating Gemini Client...")

    return genai.Client(

        api_key=api_key,
    )


# =============================================================================
# Boot Sequence
# =============================================================================

def boot():
    """
    Complete boot sequence (Part-2).

    Initializes:

        • Gemini Client
        • Memory
        • Runtime Context
        • Runtime Kernel
        • Runtime
        • Orchestrator
    """

    print(BOOT_BANNER)

    LOGGER.info("Boot sequence started.")

    # -------------------------------------------------------------
    # Environment
    # -------------------------------------------------------------

    load_environment()

    # -------------------------------------------------------------
    # Gemini Client
    # -------------------------------------------------------------

    client = create_gemini_client()

    LOGGER.info("Gemini Client initialized.")

    # -------------------------------------------------------------
    # Memory
    # -------------------------------------------------------------

    memory = InMemory()

    LOGGER.info("Memory initialized.")

    # -------------------------------------------------------------
    # Runtime Context
    # -------------------------------------------------------------

    runtime_context = RuntimeContext()

    runtime_context.memory = memory

    LOGGER.info("Runtime Context initialized.")

    # -------------------------------------------------------------
    # Runtime Kernel
    # -------------------------------------------------------------

    kernel = RuntimeKernel()

    LOGGER.info("Runtime Kernel initialized.")

    # -------------------------------------------------------------
    # Runtime
    # -------------------------------------------------------------

    runtime = Runtime()

    runtime.boot()

    kernel = runtime.kernel

    runtime_context = runtime.context

    # -------------------------------------------------------------
    # Orchestrator
    # -------------------------------------------------------------

    orchestrator = runtime.orchestrator

    LOGGER.info("Orchestrator initialized.")

    # -------------------------------------------------------------
    # Runtime References
    # -------------------------------------------------------------

    runtime_context.runtime = runtime

    runtime_context.orchestrator = orchestrator

    # -------------------------------------------------------------
    # Boot Summary
    # -------------------------------------------------------------

    LOGGER.info("Runtime successfully booted.")

    return {

        "client": client,

        "memory": memory,

        "runtime_context": runtime_context,

        "kernel": kernel,

        "runtime": runtime,

        "orchestrator": orchestrator,
    }

# =============================================================================
# Agent Construction
# =============================================================================

from .AGENTS.IMPLEMENTATIONS.GEMINI.gemini_agent import GeminiAgent


# =============================================================================
# Build Agent
# =============================================================================

def build_agent(
    *,
    client,
    services,
):
    """
    Construct the primary BRAHMA Agent.

    Runtime owns infrastructure.

    Agent owns cognition.

    RuntimeServices inject Runtime-managed resources into the Agent.
    """

    LOGGER.info("Constructing GeminiAgent...")

    # -------------------------------------------------------------------------
    # Create Agent
    # -------------------------------------------------------------------------

    agent = GeminiAgent(

        client=client,

        memory=services.memory,
    )

    LOGGER.info(

        "GeminiAgent created : %s",

        agent.fullname,
    )

    # -------------------------------------------------------------------------
    # Runtime Injection
    # -------------------------------------------------------------------------

    LOGGER.info(

        "Injecting Runtime Services..."
    )

    services.inject_into_agent(agent)

    LOGGER.info(

        "Runtime Services injected."
    )

    # -------------------------------------------------------------------------
    # Initialize Agent
    # -------------------------------------------------------------------------

    LOGGER.info(

        "Initializing Agent..."
    )

    agent.on_initialize()

    # -------------------------------------------------------------------------
    # Validation
    # -------------------------------------------------------------------------

    LOGGER.info(

        "Validating Agent..."
    )

    agent.validate()

    LOGGER.info(

        "Agent validation successful."
    )

    # -------------------------------------------------------------------------
    # Runtime Registration
    # -------------------------------------------------------------------------

    LOGGER.info(

        "Registering Agent..."
    )

    services.register_agent(agent)

    LOGGER.info(

        "Agent registered."
    )

    # -------------------------------------------------------------------------
    # Diagnostics
    # -------------------------------------------------------------------------

    LOGGER.info(

        "Agent Health : %s",

        agent.health_check(),
    )

    LOGGER.info(

        "Runtime Health : %s",

        services.health(),
    )

    return agent


# =============================================================================
# Runtime Startup
# =============================================================================

def initialize_runtime():

    boot_objects = boot()

    runtime = boot_objects["runtime"]

    client = boot_objects["client"]

    runtime_context = boot_objects["runtime_context"]

    # -------------------------------------------------------------
    # Runtime Services
    # -------------------------------------------------------------

    services = RuntimeServices(runtime_context)

    LOGGER.info("Runtime Services initialized.")

    # Runtime reference inject करो
    runtime_context.runtime = runtime

    # -------------------------------------------------------------
    # Build Gemini Agent
    # -------------------------------------------------------------

    agent = build_agent(

        client=client,

        services=services,
    )

    # -------------------------------------------------------------
    # Inject Runtime Services
    # -------------------------------------------------------------

    services.inject_into_agent(agent)

    # -------------------------------------------------------------
    # Register Agent
    # -------------------------------------------------------------

    runtime.register_agent(agent)

    LOGGER.info("Agent registered.")

    # -------------------------------------------------------------
    # Start Runtime
    # -------------------------------------------------------------

    LOGGER.info("Starting Runtime...")

    runtime.start()

    LOGGER.info("Runtime started successfully.")

    return {

        "runtime": runtime,

        "services": services,

        "agent": agent,
    }
# =============================================================================
# First Cognitive Cycle
# =============================================================================

def first_cognitive_cycle(agent):
    """
    Execute the very first Project BRAHMA cognitive cycle.

    This is the first moment where BRAHMA actually thinks.
    """

    LOGGER.info("=" * 80)
    LOGGER.info("FIRST COGNITIVE CYCLE")
    LOGGER.info("=" * 80)

    # -------------------------------------------------------------------------
    # First Observation
    # -------------------------------------------------------------------------

    observation = {

        "type": "system_boot",

        "message": (
            "Project BRAHMA Runtime initialized successfully. "
            "Perform system self-analysis."
        ),
    }

    LOGGER.info("Observation:")
    LOGGER.info(observation)

    # -------------------------------------------------------------------------
    # Cognitive Cycle
    # -------------------------------------------------------------------------

    result = agent.run(observation)

    # -------------------------------------------------------------------------
    # Display Results
    # -------------------------------------------------------------------------

    LOGGER.info("=" * 80)
    LOGGER.info("REASONING")
    LOGGER.info("=" * 80)
    LOGGER.info(result["reasoning"])

    LOGGER.info("=" * 80)
    LOGGER.info("PLANNING")
    LOGGER.info("=" * 80)
    LOGGER.info(result["planning"])

    LOGGER.info("=" * 80)
    LOGGER.info("EXECUTION")
    LOGGER.info("=" * 80)
    LOGGER.info(result["execution"])

    LOGGER.info("=" * 80)
    LOGGER.info("REFLECTION")
    LOGGER.info("=" * 80)
    LOGGER.info(result["reflection"])

    LOGGER.info("=" * 80)
    LOGGER.info("LEARNING")
    LOGGER.info("=" * 80)
    LOGGER.info(result["learning"])

    LOGGER.info("=" * 80)
    LOGGER.info("FIRST COGNITIVE CYCLE COMPLETED")
    LOGGER.info("=" * 80)

    return result


# =============================================================================
# Application Entry Point
# =============================================================================

def main():
    """
    Project BRAHMA Bootloader

        Boot Runtime
              ↓
        Build Agent
              ↓
        First Cognitive Cycle
    """

    try:

        system = initialize_runtime()

        runtime = system["runtime"]

        agent = system["agent"]

        first_cognitive_cycle(agent)

        LOGGER.info("")
        LOGGER.info("=" * 80)
        LOGGER.info("PROJECT BRAHMA BOOT SUCCESSFUL")
        LOGGER.info("=" * 80)

        return 0

    except Exception as ex:

        LOGGER.exception("PROJECT BRAHMA BOOT FAILED")

        raise


# =============================================================================

if __name__ == "__main__":

    raise SystemExit(main())
    
# =============================================================================
# Entry Point
# =============================================================================

def main() -> None:

    try:

        boot()

        LOGGER.info("Bootloader Part-1 completed successfully.")

    except Exception as ex:

        LOGGER.exception(

            "Boot failed."
        )

        sys.exit(1)


# =============================================================================

if __name__ == "__main__":

    main()