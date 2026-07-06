# Project BRAHMA Coding Standards

> Coding standards for building a clean, scalable, secure, and production-ready AI Research Platform.

---

# General Principles

Code should be:

- Simple
- Readable
- Modular
- Reusable
- Testable
- Maintainable

Always prefer clarity over cleverness.

---

# Python Version

Minimum Version

Python 3.12+

---

# File Naming

Use lowercase.

Use underscores.

Good

chat_service.py

image_agent.py

research_tool.py

embedding.py

Bad

ChatService.py

New File.py

abc.py

test2.py

---

# Folder Naming

Use lowercase only.

Good

agents/

services/

prompts/

providers/

Bad

Agent/

New Folder/

MyFiles/

---

# Variable Naming

Use descriptive names.

Good

user_question

image_path

response_text

Bad

a

x

temp

abc

---

# Function Naming

Use snake_case.

Good

generate_answer()

search_web()

create_embedding()

Bad

GenerateAnswer()

DoSearch()

ABC()

---

# Class Naming

Use PascalCase.

Good

ResearchAgent

ImageGenerator

FinanceService

---

# Constants

Use uppercase.

Good

MAX_RETRIES

DEFAULT_MODEL

API_TIMEOUT

---

# Imports

Standard Library

↓

Third Party

↓

Project Imports

Example

import os

import streamlit as st

from core.ai import chat

---

# Type Hints

Use type hints whenever practical.

Example

def generate_answer(question: str) -> str:

---

# Function Size

Maximum recommended:

30–50 lines

If a function becomes too large,

split it into smaller functions.

---

# File Size

Preferred:

300–500 lines

Avoid files larger than 700 lines.

---

# Comments

Write comments only when necessary.

Avoid obvious comments.

Bad

# Increment i

i += 1

Good

# Retry after API rate limit

---

# Docstrings

Public functions should have docstrings.

Example

def search_web(query: str):

    """
    Search the web and return relevant results.
    """

---

# Error Handling

Never ignore exceptions.

Bad

try:
    ...
except:
    pass

Good

try:
    ...
except Exception as e:
    logger.error(e)

---

# Logging

Use logging.

Avoid print() in production.

Good

logger.info()

logger.warning()

logger.error()

---

# Secrets

Never hardcode:

API Keys

Passwords

Tokens

Secrets

Use

.env

Only commit

.env.example

---

# AI Providers

Never directly call provider SDKs outside

core/providers/

Wrong

genai.GenerativeModel(...)

inside UI

Correct

core.ai.chat()

---

# Prompts

Never hardcode prompts.

Store them inside

prompts/

---

# Business Logic

Never place business logic inside:

app.py

sidebar.py

pages.py

Widgets

Business logic belongs inside:

services/

---

# UI Rules

UI should only:

Take Input

Display Output

Call Services

Nothing else.

---

# Agent Rules

Each agent should have one responsibility.

Examples

Research Agent

Finance Agent

Health Agent

Image Agent

---

# Git Commit Style

Use Conventional Commits.

Examples

feat:

fix:

refactor:

docs:

test:

style:

perf:

chore:

Examples

feat: add finance agent

fix: resolve image upload bug

docs: update architecture

refactor: modularize AI gateway

---

# Branch Strategy

main

Production-ready code only.

Future development branches may use:

feature/

bugfix/

hotfix/

---

# Testing

Every major feature should be tested before pushing.

Broken code should never reach main.

---

# Code Duplication

Avoid duplicate code.

If logic is reused,

move it into a reusable function or service.

---

# Dependency Rule

Dependencies always point inward.

UI

↓

Services

↓

Core

↓

Providers

Never reverse this direction.

---

# Performance

Avoid unnecessary API calls.

Reuse objects whenever possible.

Cache expensive operations when appropriate.

---

# Documentation

Every significant feature must include documentation.

Documentation is considered part of the implementation.

---

# Code Review Checklist

Before every commit, verify:

✓ Code runs successfully

✓ No API keys committed

✓ No duplicate logic

✓ Imports cleaned

✓ Functions are small

✓ Documentation updated

✓ Git status is clean

✓ Tests completed

---

# Engineering Philosophy

Design Before Code.

Write Clean Code.

Keep Functions Small.

Build Reusable Components.

Prefer Composition over Duplication.

Optimize for Maintainability.

Always Think Long-Term.