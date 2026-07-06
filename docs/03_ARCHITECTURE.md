# Project BRAHMA Architecture

> Production-ready architecture for a scalable, modular, provider-independent AI Research Platform.

---

# Overview

Project BRAHMA follows a layered architecture.

Each layer has a single responsibility.

Higher layers depend only on lower layers.

Lower layers never depend on higher layers.

---

# Architecture Diagram

```
                User

                  │

                  ▼

          Streamlit UI Layer

                  │

                  ▼

          Services Layer

                  │

                  ▼

          AI Gateway (core)

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

  AI Providers         Local Models

        │                   │

        └─────────┬─────────┘

                  ▼

              AI Models
```

---

# Project Structure

```
Project BRAHMA/

│

├── app.py

│

├── agents/

├── assets/

├── config/

├── core/

│      ├── ai.py

│      ├── registry.py

│      └── providers/

│

├── services/

├── prompts/

├── tools/

├── ui/

├── data/

├── logs/

├── docs/

├── tests/

└── requirements.txt
```

---

# Layer Responsibilities

## UI Layer

Responsible for:

- User Interface
- Navigation
- Widgets
- File Upload
- User Input
- Display Output

Never contains business logic.

---

## Services Layer

Responsible for:

- Business Logic
- Data Processing
- Workflow
- Validation
- AI Orchestration

Services communicate with Core.

---

## Core Layer

Responsible for:

- AI Gateway
- Provider Registry
- Model Selection
- Provider Switching

The rest of the application never directly calls providers.

---

## Provider Layer

Responsible for interacting with external AI providers.

Example:

Gemini

OpenAI

Claude

Ollama

DeepSeek

Every provider implements a common interface.

---

## Agent Layer

Responsible for autonomous AI systems.

Examples:

Research Agent

Finance Agent

Health Agent

Image Agent

Philosophy Agent

Music Agent

Recruitment Agent

Each agent focuses on a single domain.

---

## Prompt Layer

Stores reusable prompts.

Prompts must never be hardcoded inside business logic.

---

## Tools Layer

Responsible for external integrations.

Examples:

DuckDuckGo

Wikipedia

Arxiv

Google Search

Finance APIs

PDF Processing

OCR

---

## Data Layer

Stores:

Knowledge Base

Embeddings

FAISS Index

Documents

Datasets

Temporary Files

---

# AI Gateway

Every AI request passes through:

```
core/ai.py
```

No other module should directly call providers.

Example:

```
UI

↓

Service

↓

core.ai

↓

Provider

↓

Model
```

---

# Provider Registry

The provider registry selects the active AI provider.

Supported providers:

Gemini

OpenAI

Claude

Ollama

DeepSeek

Future providers can be added without changing application logic.

---

# Dependency Rules

Allowed:

UI

↓

Services

↓

Core

↓

Providers

Not Allowed:

Providers

↓

UI

Services

↓

UI

Core

↓

UI

Agents

↓

UI

---

# Folder Responsibilities

## agents/

Domain-specific AI agents.

---

## config/

Application configuration.

Models

Environment Variables

Constants

Settings

---

## core/

AI Gateway

Provider Registry

Provider Implementations

---

## services/

Business Logic

Workflow

AI Orchestration

---

## prompts/

Prompt Templates

System Prompts

Agent Prompts

---

## tools/

External APIs

Search Tools

Utilities

OCR

PDF

Web

---

## ui/

Sidebar

Navigation

Pages

Widgets

Themes

---

## assets/

Images

Icons

Videos

Static Files

---

## data/

Knowledge Base

Embeddings

Datasets

FAISS

---

## logs/

Application Logs

Debug Logs

Audit Logs

---

## docs/

Project Documentation

---

## tests/

Unit Tests

Integration Tests

Regression Tests

---

# Coding Flow

User

↓

UI

↓

Service

↓

Core AI

↓

Provider

↓

Model

↓

Response

↓

UI

---

# Design Principles

- Modular
- Scalable
- Maintainable
- Testable
- Provider Independent
- Secure
- Reusable
- Production Ready

---

# Future Expansion

The architecture is designed to support:

- Multi-Agent AI
- MCP
- RAG
- Voice AI
- Vision AI
- Robotics
- AI Automation
- Fine-tuning
- Local LLMs
- Distributed AI Systems

without changing the existing architecture.

---

# Final Architecture Principle

Every module should have a single responsibility.

Every dependency should move inward.

Every provider should be replaceable.

Every feature should be modular.

Project BRAHMA should evolve by adding modules, not by rewriting the architecture.