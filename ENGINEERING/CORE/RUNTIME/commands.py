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

from ENGINEERING.CORE.EVENTBUS.event_type import EventType
from ENGINEERING.RUNTIME.runtime import runtime_instance
from ENGINEERING.CORE.RUNTIME.kernel import runtime_kernel
from ENGINEERING.CORE.RUNTIME.boot import runtime_summary
from ENGINEERING.CORE.EVENTBUS.history import runtime_event_history
from ENGINEERING.CORE.RUNTIME.kernel import runtime_kernel
from ENGINEERING.CORE.RUNTIME.dispatcher import runtime_dispatcher
    

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

    info = runtime_summary()

    bus = info["event_bus"]

    print()

    print("Event Bus")

    print("----------------------------")

    print()

    print(f"Published Events : {bus['history_size']}")

    print(f"Registered Types : {bus['registered_events']}")

    print(f"Subscribers      : {bus['subscriber_count']}")

    print()

    print("Event Counts")

    print("----------------------------")

    if not bus["event_counts"]:

        print("No events published.")

    else:

        for event_type, count in bus["event_counts"].items():

            print(f"{event_type:<25} {count}")

    print()

    print("Sources")

    print("----------------------------")

    if not bus["source_counts"]:

        print("No sources.")

    else:

        for source, count in bus["source_counts"].items():

            print(f"{source:<25} {count}")

    print()

# ==========================================================
# Last events
# ==========================================================

def cmd_events_last():

    print()
    print("Last Events")
    print("----------------------------")
    print()

    history = runtime_event_history.last()

    if not history:

        print("No events recorded.")
        print()
        return

    for event in history:

        print(
            f"{event.timestamp.strftime('%H:%M:%S')}  "
            f"{event.source:<20} "
            f"{event.event_type}"
        )

    print()

# ==========================================================
# Clear events
# ==========================================================

def cmd_events_clear():

    runtime_event_history.clear()

    print()

    print("Event history cleared.")

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
def cmd_exit():

    print()
    print("Stopping Runtime...")
    print()

    runtime_kernel.stop()
    runtime_instance.shutdown()
    
    raise SystemExit

# ==========================================================
# Register Runtime Commands
# ==========================================================

def register_runtime_commands():
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
    runtime_dispatcher.register("events last",cmd_events_last,)
    runtime_dispatcher.register("events clear",cmd_events_clear,)