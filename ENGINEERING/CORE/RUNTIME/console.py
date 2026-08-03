"""
PROJECT BRAHMA
Universal Runtime Console

Author:
    Ramendra Singh Rajput

Description
-----------
Thin interactive console for Project BRAHMA.

Responsibilities
----------------
• Read user input
• Forward commands to Dispatcher
• Handle Ctrl+C
• Stop console gracefully

The Console never executes business logic.

Architecture

User
   ↓
Console
   ↓
Dispatcher
   ↓
Commands
"""

from __future__ import annotations

from ENGINEERING.CORE.RUNTIME.dispatcher import runtime_dispatcher
from ENGINEERING.CORE.RUNTIME.logger import runtime

from ENGINEERING.CORE.EVENTBUS.publisher import EventPublisher
from ENGINEERING.CORE.EVENTBUS.event_type import EventType

class RuntimeConsole(EventPublisher):
#class RuntimeConsole:
    """
    Thin Runtime Console.

    Console only accepts user input and forwards it
    to the Dispatcher.
    """

    def __init__(self):

        super().__init__("runtime.console")

        self.running = True

    # =====================================================

    def start(self):

        runtime("Runtime Console Started.")

        print()
        print("══════════════════════════════════════════════")
        print("BRAHMA Runtime Console")
        print("Type 'help' to list commands.")
        print("══════════════════════════════════════════════")
        print()

        while self.running:

            try:

                command = input("BRAHMA > ").strip()

                if not command:
                    continue

                self.execute(command)

            except KeyboardInterrupt:

                print()
                print("Runtime Interrupted.")
                self.shutdown()

    # =====================================================
    
    def execute(self, command: str):

        self.publish(

        EventType.COMMAND_RECEIVED,

        payload={

            "command": command,

        },

    )

        runtime_dispatcher.dispatch(command)

    # =====================================================

    def shutdown(self):

        runtime("Runtime Console Stopped.")

        self.running = False


#
# Global Console
#

runtime_console = RuntimeConsole()