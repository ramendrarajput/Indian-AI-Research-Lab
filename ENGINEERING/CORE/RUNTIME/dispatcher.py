"""
PROJECT BRAHMA
Universal Runtime Dispatcher

Author:
    Ramendra Singh Rajput

Description
-----------
The Dispatcher is responsible for routing runtime commands
to the appropriate handler.

The Console never executes business logic directly.

All runtime interactions flow through the Dispatcher.

Future Responsibilities
-----------------------
• Universal Agent Routing
• Laboratory Routing
• Runtime Commands
• Plugin Routing
• Event Dispatch
"""

from __future__ import annotations

from typing import Callable


#from ENGINEERING.CORE.EVENTBUS.event_type import EventType
#from ENGINEERING.CORE.EVENTBUS.publisher import EventPublisher
#class RuntimeDispatcher(EventPublisher):
class RuntimeDispatcher:
    """
    Universal Runtime Dispatcher.
    """


    def __init__(self):

        #super().__init__("runtime.dispatcher")

        self._commands: dict[str, Callable] = {}

    # --------------------------------------------------

    def register(
        self,
        command: str,
        handler: Callable,
    ) -> None:
        """
        Register command handler.
        """

        self._commands[command.lower()] = handler

    # --------------------------------------------------

    def unregister(
        self,
        command: str,
    ) -> None:

        self._commands.pop(command.lower(), None)

    # --------------------------------------------------

    def dispatch(
        self,
        command: str,
        *args,
        **kwargs,
    ):

        command = command.lower()

        handler = self._commands.get(command)

        if handler is None:

            #self.publish(

            #    EventType.UNKNOWN_COMMAND,
     
            #    payload={

            #      "command": command,

            #    },

            #)

            return self.unknown(command)

        return handler(*args, **kwargs)

    # --------------------------------------------------

    def commands(self):

        return sorted(self._commands.keys())

    # --------------------------------------------------

    @staticmethod
    def unknown(command: str):

        print()

        print(f'Unknown command "{command}"')

        print("Type 'help' to see available commands.")

        print()


#
# Global Dispatcher
#

runtime_dispatcher = RuntimeDispatcher()