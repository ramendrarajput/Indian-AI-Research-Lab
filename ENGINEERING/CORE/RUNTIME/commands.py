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

from datetime import datetime
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

    print("services")

    print("status")

    print("labs")

    print("agent")

    print("memory")

    print("registry")

    print("context")

    print("scheduler")

    print("plugins")

    print("config")

    print("version")

    print("health")

    print("uptime")

    print("consolidate")

    print("history")
    
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
# Services
# ==========================================================

def cmd_services():

    from ENGINEERING.CORE.RUNTIME.context import runtime_context
    print()
    print("Services")
    print("----------------------------")
    for service in runtime_context.registry.list_services(): #summary():
        print(f"✓ {service}")
    print()
    print("Pending")
    print("----------------------------")

    pending = [

        "universal_agent",

        "scheduler",

        "laboratory_manager",

        "provider_manager",

        "model_manager",

        "event_bus",

        "event_history",

        "logger",

        "runtime_context",

        "runtime_registry",

        "runtime_state",

        "memory_engine",

    ]

    registered = set(runtime_context.registry.list_services())

    for item in pending:

        if item not in registered:

            print(f"• {item}")

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

#===========================================================
#Consolidate
#===========================================================

def cmd_consolidate():

    #runtime_memory.consolidate()
    from ENGINEERING.CORE.RUNTIME.context import runtime_context

    runtime_context.memory.consolidate()

    print()

    print("Memory consolidated.")

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
# Scheduler
# ==========================================================

def cmd_scheduler():

    print()

    print("Scheduler")

    print("----------------------------")

    print()

    print("Scheduler not initialized.")

    print()

    print()

# ==========================================================
# Plugins
# ==========================================================

def cmd_plugins():

    print()

    print("Plugins")

    print("----------------------------")

    print()

    print("Plugin Manager not initialized.")

    print()

# ==========================================================
# Registry
# ==========================================================

def cmd_registry():

    print()

    print("Registry")

    print("----------------------------")

    print()

    print("Registry Viewer not implemented.")

    print()

# ==========================================================
# Context
# ==========================================================

def cmd_context():

    print()

    print("Context")

    print("----------------------------")

    print()

    print("Runtime Context Viewer not implemented.")

    print()
                    
# ==========================================================
# History
# ==========================================================

def cmd_history():

    print()

    print("History")

    print("----------------------------")

    print()

    print("History Viewer not implemented.")

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
# Memory Update
# ==========================================================

def cmd_memory_update(
    uid: str,
    *content_parts,
):

    from ENGINEERING.CORE.RUNTIME.context import runtime_context

    content = " ".join(content_parts)

    memory_engine = runtime_context.memory

    if memory_engine is None:

        print()
        print("Memory Engine not initialized.")
        print()

        return

    record = memory_engine.get_long_term_by_uid(uid)

    if record is None:

        print()
        print(f'No long-term memory found for UID "{uid}".')
        print()

        return

    print()
    print("## Memory Update")
    print()

    print("Before")
    print("----------------------------------------------")
    print("UID        :", record.uid)
    print("Content    :", record.content)
    print("Importance :", record.importance)
    print()

    record.content = content

    updated = memory_engine.update_memory(record)

    if updated is None:

        print("Memory update failed.")
        print()

        return

    print("After")
    print("----------------------------------------------")
    print("UID        :", updated.uid)
    print("Content    :", updated.content)
    print("Importance :", updated.importance)
    print()

    print("Memory updated and persisted.")
    print()

# ==========================================================
# Memory
# ==========================================================

def cmd_memory():

    from ENGINEERING.CORE.RUNTIME.context import runtime_context

    print()
    print("Memory Engine")
    print("----------------------------")
    print()

    memory = runtime_context.memory

    if memory is None:

        print("Memory Engine not initialized.")
        return

    print("Status")
    print("------")
    print("READY")
    print()

    print("Memory Components")
    print("-----------------")

    print(
        f"Working Memory   : {memory.working.summary()['records']} records"
    )
    print()

    print("Recent Working Memory")

    print("----------------------------")

    records = memory.recall_working()

    if not records:

        print("No memories.")

    else:

        for record in records[-5:]:

            print(f"- {record.content}")

    print(
        f"Session Memory   : {memory.session.summary()['records']} records"
    )

    print(
        f"Long-Term Memory : {memory.long_term.summary()['records']} records"
    )

    print()

    total = (
        memory.working.size()
        + memory.session.size()
        + memory.long_term.size()
    )

    print("Statistics")
    print("----------")

    print(f"Total Records : {total}")

    print()

    print("Persistence")
    print("-----------")
    print("Disabled")
    print()

    print("Embeddings")
    print("----------")
    print("Disabled")
    print()

    print("Vector Database")
    print("---------------")
    print("Disabled")
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

    #runtime_kernel.stop()
    runtime_instance.shutdown()
    
    raise SystemExit

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
# Version
# ==========================================================

def cmd_version():

    from ENGINEERING.CORE.RUNTIME.context import runtime_context

    print()
    print("BRAHMA Runtime")
    print("----------------------------")
    print()

    print(f"Version      : {runtime_context.version}")
    print(f"Runtime      : {runtime_context.runtime_name}")
    print("Mode         : Offline")
    print("Build        : Development")
    print("Architecture : Universal Runtime")
    print()
    
# ==========================================================
# Config
# ==========================================================

def cmd_config():

    print()

    print("Config")

    print("----------------------------")

    print()

    print("Config is not initialized")

    print()

# ==========================================================
# Health
# ==========================================================

def cmd_health():

    print()
    print("Runtime Health")
    print("----------------------------")
    print()

    print("✓ Kernel")
    print("✓ Event Bus")
    print("✓ Event History")
    print("✓ Runtime Registry")
    print("✓ Runtime Context")
    print("✓ Logger")
    print()

    print("Pending")
    print("----------------------------")
    print()

    print("○ Memory Engine")
    print("○ Universal Agent")
    print("○ Scheduler")
    print("○ Laboratories")
    print("○ Provider Manager")
    print()

# ==========================================================
# Uptime
# ==========================================================

def cmd_uptime():

    from ENGINEERING.CORE.RUNTIME.context import runtime_context

    uptime = datetime.now() - runtime_context.boot_time

    print()
    print("Runtime Uptime")
    print("----------------------------")
    print()

    print(str(uptime).split(".")[0])
    print()

# ==========================================================
# Memory Update
# ==========================================================

def cmd_memory_update(
    uid: str,
    *content_parts,
):

    from ENGINEERING.CORE.RUNTIME.context import runtime_context

    content = " ".join(content_parts)

    memory_engine = runtime_context.memory

    if memory_engine is None:

        print()
        print("Memory Engine not initialized.")
        print()

        return

    record = memory_engine.get_long_term_by_uid(uid)

    if record is None:

        print()
        print(f'No long-term memory found for UID "{uid}".')
        print()

        return

    print()
    print("## Memory Update")
    print()

    print("Before")
    print("----------------------------------------------")
    print(f"UID        : {record.uid}")
    print(f"Content    : {record.content}")
    print(f"Importance : {record.importance}")
    print()

    record.content = content

    updated = memory_engine.update_memory(record)

    if updated is None:

        print("Memory update failed.")
        print()

        return

    print("After")
    print("----------------------------------------------")
    print(f"UID        : {updated.uid}")
    print(f"Content    : {updated.content}")
    print(f"Importance : {updated.importance}")
    print()

    print("Memory updated and persisted.")
    print()
    
# ==========================================================
# Recall Memory
# ==========================================================

def cmd_recall(query: str = ""):

    from ENGINEERING.CORE.RUNTIME.context import runtime_context

    print()
    print("Memory Recall")
    print("----------------------------")
    print()

    if not query:

        print("Usage:")
        print("recall <query>")
        print()

        return

    memory_engine = runtime_context.memory

    if memory_engine is None:

        print("Memory Engine not initialized.")
        print()

        return

    records = memory_engine.recall(query)

    if not records:

        print(f'No memories found for "{query}".')
        print()

        return

    print(f'Results for "{query}"')
    print("----------------------------")
    print()

    for index, record in enumerate(records, start=1):

        print(f"{index}.")
        print()

        print(f"UID        : {record.uid}")
        print(f"Timestamp  : {record.timestamp}")
        print(f"Category   : {record.category}")
        print(f"Source     : {record.source}")
        print(f"Importance : {record.importance}")
        print(f"Content    : {record.content}")

        print()

        print("----------------------------")

    print()

# ==========================================================
# Providers
# ==========================================================

def cmd_providers():

    print()
    print("Providers")
    print("----------------------------")
    print()

    print("No providers loaded.")
    print()

    print("Future Providers")
    print("----------------------------")
    print()

    print("• OpenAI")
    print("• Gemini")
    print("• Anthropic")
    print("• Ollama")
    print("• BRAHMA Native")
    print()    

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
    runtime_dispatcher.register("recall", cmd_recall)
    runtime_dispatcher.register("memory update", cmd_memory_update)
    runtime_dispatcher.register("clear", cmd_clear)
    runtime_dispatcher.register("exit", cmd_exit)
    runtime_dispatcher.register("quit", cmd_exit)
    runtime_dispatcher.register("events", cmd_events)
    runtime_dispatcher.register("events last",cmd_events_last,)
    runtime_dispatcher.register("events clear",cmd_events_clear,)
    runtime_dispatcher.register("services", cmd_services)
    runtime_dispatcher.register("registry", cmd_registry)
    runtime_dispatcher.register("context", cmd_context)
    runtime_dispatcher.register("scheduler", cmd_scheduler)
    runtime_dispatcher.register("config", cmd_config)
    runtime_dispatcher.register("version", cmd_version)
    runtime_dispatcher.register("health", cmd_health)
    runtime_dispatcher.register("uptime", cmd_uptime)
    runtime_dispatcher.register("history", cmd_history)
    runtime_dispatcher.register("plugins", cmd_plugins)
    runtime_dispatcher.register("providers", cmd_providers)
    runtime_dispatcher.register("consolidate",cmd_consolidate,)
    