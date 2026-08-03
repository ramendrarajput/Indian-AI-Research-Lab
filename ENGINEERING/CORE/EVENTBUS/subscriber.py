"""
PROJECT BRAHMA
Universal Event Subscriber

Author
------
Ramendra Singh Rajput

Description
-----------
Defines the base Subscriber interface for the
BRAHMA Universal Event Bus.

Every component that wishes to receive events
must inherit from EventSubscriber.

Examples
--------
Runtime Subscriber

Kernel Subscriber

Memory Subscriber

Universal Agent Subscriber

Laboratory Subscriber

Future
------
• Event Filters
• Priority Subscribers
• Async Subscribers
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from ENGINEERING.CORE.EVENTBUS.event import Event


class EventSubscriber(ABC):
    """
    Base class for all Runtime Event Subscribers.
    """

    def __init__(self, name: str):

        self._name = name

    # ==========================================================
    # Properties
    # ==========================================================

    @property
    def name(self) -> str:
        """
        Subscriber name.
        """
        return self._name

    # ==========================================================
    # Event Handler
    # ==========================================================

    @abstractmethod
    def handle_event(
        self,
        event: Event,
    ) -> None:
        """
        Handle an incoming event.

        Must be implemented by every subscriber.
        """
        raise NotImplementedError

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(name='{self.name}')"
        )