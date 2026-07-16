# Project BRAHMA

## Changelog

All notable changes to Project BRAHMA are documented in this file.

The format is inspired by Keep a Changelog and Semantic Versioning.

# Changelog

All notable changes to **Project BRAHMA (Indian AI Research Lab)** will be documented in this file.

This project follows a structured architecture-first development approach.

---

## [Unreleased]

### Planned

- Complete app.py modularization
- Move remaining AI services into `core/`
- Separate business logic from UI
- Production service layer
- Docker support
- REST API
- CI/CD Pipeline

---

## [2026-07]

### Added

- Modular Calculator Agent
- Modular Email Agent
- Standalone Text Agent UI
- Standalone Image Agent UI
- Standalone Audio Agent UI
- Standalone Video Agent UI
- Production Memory Manager (`core/memory.py`)
- QA Pipeline module (`core/pipeline.py`)

### Changed

- Refactored Multi-Agent Chain into standalone UI modules.
- Refactored AI Chat to use production-style memory architecture.
- Moved Research Agent out of `app.py`.
- Moved Arxiv Agent out of `app.py`.
- Moved QA Pipeline initialization into `core/pipeline.py`.
- Simplified routing inside `app.py`.
- Reduced business logic inside UI files.

### Architecture

Project structure now follows:

```
app.py
│
├── agents/
├── core/
├── prompts/
├── ui/
│   └── pages/
├── docs/
└── assets/
```

Architecture principles:

- UI contains only presentation logic.
- Agents contain business logic.
- Core contains reusable services.
- Prompts remain centralized.
- app.py acts only as the application router.

---

## Authors

Developer

Ramendra Singh Rajput

Project

Project BRAHMA (Indian AI Research Lab)

Started as a personal AI Operating System project focused on modular,
production-ready Agentic AI architecture.