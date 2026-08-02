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


class RuntimeConsole:
    """
    Thin Runtime Console.

    Console only accepts user input and forwards it
    to the Dispatcher.
    """

    def __init__(self):

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

        runtime_dispatcher.dispatch(command)

    # =====================================================

    def shutdown(self):

        runtime("Runtime Console Stopped.")

        self.running = False


#
# Global Console
#

runtime_console = RuntimeConsole()