"""
PROJECT BRAHMA
Universal Runtime Commands

Author
------
Ramendra Singh Rajput

Description
-----------
Built-in Runtime Commands.

This module contains command handlers only.

It does NOT know anything about the Console.

Architecture

Console
    ↓
Dispatcher
    ↓
Commands
"""

from __future__ import annotations

from ENGINEERING.CORE.RUNTIME.kernel import runtime_kernel
from ENGINEERING.CORE.RUNTIME.boot import runtime_summary


# ==========================================================
# HELP
# ==========================================================

def cmd_help():

    print()

    print("Available Commands")

    print("----------------------------")

    print()

    print("help")

    print("runtime")

    print("status")

    print("labs")

    print("agent")

    print("memory")

    print("clear")

    print("exit")

    print()


# ==========================================================
# Runtime Information
# ==========================================================

def cmd_runtime():

    info = runtime_summary()

    print()

    print("Runtime")

    print("----------------------------")

    print()

    print(f"Name      : {info['runtime']}")

    print(f"Version   : {info['version']}")

    print(f"State     : {info['state']}")

    print()

    print("Services")

    print("----------------------------")

    for service in info["services"]:

        print(f"• {service}")

    print()


# ==========================================================
# Runtime Status
# ==========================================================

def cmd_status():

    print()

    print("Kernel")

    print("----------------------------")

    print()

    if runtime_kernel.is_running():

        print("Status : RUNNING")

    else:

        print("Status : STOPPED")

    print()

# ==========================================================
# Events
# ==========================================================

def cmd_events():

    print()

    print("Events")

    print("----------------------------")

    print("Event command not implemented yet.")

    print()

# ==========================================================
# Laboratories
# ==========================================================

def cmd_labs():

    print()

    print("Laboratories")

    print("----------------------------")

    print()

    print("No laboratories registered.")

    print()


# ==========================================================
# Universal Agent
# ==========================================================

def cmd_agent():

    print()

    print("Universal Agent")

    print("----------------------------")

    print()

    print("Universal Agent not initialized.")

    print()


# ==========================================================
# Memory
# ==========================================================

def cmd_memory():

    print()

    print("Memory")

    print("----------------------------")

    print()

    print("Memory Engine not initialized.")

    print()


# ==========================================================
# Clear Screen
# ==========================================================

def cmd_clear():

    print("\n" * 100)


# ==========================================================
# Exit
# ==========================================================

from ENGINEERING.CORE.RUNTIME.kernel import runtime_kernel

def cmd_exit():

    print()
    print("Stopping Runtime...")
    print()

    runtime_kernel.stop()

    raise SystemExit

# ==========================================================
# Register Runtime Commands
# ==========================================================

def register_runtime_commands():
    from ENGINEERING.CORE.RUNTIME.dispatcher import runtime_dispatcher
    runtime_dispatcher.register("help", cmd_help)
    runtime_dispatcher.register("runtime", cmd_runtime)
    runtime_dispatcher.register("status", cmd_status)
    runtime_dispatcher.register("labs", cmd_labs)
    runtime_dispatcher.register("agent", cmd_agent)
    runtime_dispatcher.register("memory", cmd_memory)
    runtime_dispatcher.register("clear", cmd_clear)
    runtime_dispatcher.register("exit", cmd_exit)
    runtime_dispatcher.register("quit", cmd_exit)
    runtime_dispatcher.register("events", cmd_events)