# 📘 Project BRAHMA Rule Book

## Project Philosophy

This project follows a modular architecture.

Every module has a single responsibility.

Never place unrelated logic in the same file.

---

# Folder Responsibilities

## config/

Purpose

- Environment variables
- API Keys
- Global Constants
- Configuration

Never place

- UI
- AI logic
- Business logic

---

## core/

Purpose

Reusable engines used throughout the project.

Examples

- RAG
- PDF Utilities
- Vision
- TTS
- OCR
- Utilities

---

## core/cache.py

Purpose

Cache only heavyweight reusable resources.

Allowed

- Gemini Models
- FAISS
- Diffusers Pipelines
- Phi Agents
- Whisper
- YOLO

Rules

- Use only @st.cache_resource
- No business logic
- No UI
- Load → Cache → Return

Never place

- Prompts
- Embeddings
- PDF parsing
- User input
- Utility functions

---

## agents/

Purpose

Contains AI Agent definitions.

Examples

- Finance Agent
- Stock Agent
- Research Agent
- Medical Agent
- Music Agent

Each file should create only one agent.

---

## ui/

Purpose

Contains user interface only.

Rules

- No business logic
- No AI initialization
- No model loading

---

## ui/pages/

Purpose

Each page represents one feature.

Example

- ai_chat.py
- rag.py
- image_generation.py
- finance.py

---

## app.py

Purpose

Main application router.

Responsibilities

- Navigation
- Sidebar
- Routing pages

Never place

- AI logic
- Model initialization
- RAG
- PDF processing
- Long functions

---

# Naming Rules

Functions

✔ create_stock_agent()

✔ get_flash_model()

✔ load_vector_store()

Avoid

❌ test()

❌ abc()

❌ temp()

---

# Import Rules

Heavy resources

Always import from

core/cache.py

Business logic

Always import from

core/

Agents

Always import from

agents/

UI

Always import from

ui/pages/

---

# Golden Rule

If a file exceeds ~300 lines,
consider splitting it into smaller modules.

---

# Development Workflow

1. Create feature
2. Test
3. Refactor
4. Commit
5. Push

Never leave broken code in main branch.

---

Author

Ramendra Singh Rajput

Project

Indian AI Research Lab (Project BRAHMA)