"""
PROJECT BRAHMA
Universal Event Bus Exceptions

Author
------
Ramendra Singh Rajput

Description
-----------
Custom exception hierarchy for the BRAHMA Universal Event Bus.

Every EventBus related error should inherit from
EventBusError.

Future
------
• Distributed Runtime Errors
• Network Event Errors
• Serialization Errors
• Security Exceptions
"""

from __future__ import annotations


# ==========================================================
# Base Exception
# ==========================================================

class EventBusError(Exception):
    """
    Base exception for the Universal Event Bus.
    """
    pass


# ==========================================================
# Registration Errors
# ==========================================================

class SubscriberAlreadyRegistered(EventBusError):
    """
    Raised when attempting to register the same subscriber twice.
    """
    pass


class SubscriberNotFound(EventBusError):
    """
    Raised when attempting to remove a subscriber
    that is not registered.
    """
    pass


# ==========================================================
# Publisher Errors
# ==========================================================

class EventBusNotAttached(EventBusError):
    """
    Raised when a Publisher tries to publish an event
    without an attached Event Bus.
    """
    pass


# ==========================================================
# Event Errors
# ==========================================================

class InvalidEvent(EventBusError):
    """
    Raised when an invalid Event object is supplied.
    """
    pass


class UnknownEventType(EventBusError):
    """
    Raised when an unknown EventType is encountered.
    """
    pass


# ==========================================================
# Dispatch Errors
# ==========================================================

class EventDispatchError(EventBusError):
    """
    Raised when an Event cannot be dispatched.
    """
    pass


class EventHandlerError(EventBusError):
    """
    Raised when a subscriber fails while handling an event.
    """
    pass


# ==========================================================
# History Errors
# ==========================================================

class EventHistoryError(EventBusError):
    """
    Raised for Event History related failures.
    """
    pass