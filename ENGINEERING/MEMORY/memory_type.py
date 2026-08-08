"""
PROJECT BRAHMA

Memory Types

Universal Memory Classification
"""

from enum import Enum


class MemoryType(str, Enum):

    GENERAL = "general"

    USER = "user"

    SYSTEM = "system"

    OBSERVATION = "observation"

    KNOWLEDGE = "knowledge"

    DOCUMENT = "document"

    CHAT = "chat"

    TOOL = "tool"

    TASK = "task"

    GOAL = "goal"

    PLAN = "plan"

    REASONING = "reasoning"

    EXPERIENCE = "experience"