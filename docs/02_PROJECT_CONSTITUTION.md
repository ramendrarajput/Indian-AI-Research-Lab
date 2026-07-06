# Project BRAHMA Constitution

> The permanent engineering principles that govern the design, development, and evolution of Project BRAHMA.

---

# Purpose

This constitution defines the non-negotiable rules that every contributor must follow while developing Project BRAHMA.

Every new feature, module, agent, provider, and service must comply with these principles.

---

# Rule 1 — Modular Architecture

Every component must have a single responsibility.

Large files should always be divided into smaller modules.

---

# Rule 2 — Separation of Concerns

Each folder has one responsibility only.

Example:

config/
Configuration only

core/
AI Providers and AI Gateway

agents/
AI Agents

services/
Business Logic

ui/
User Interface

prompts/
Prompt Engineering

tools/
External Integrations

data/
Knowledge Base

---

# Rule 3 — Provider Independence

No business logic should directly depend on any AI provider.

The application must be capable of switching between providers without changing business logic.

Supported providers may include:

- Gemini
- OpenAI
- Claude
- Ollama
- DeepSeek
- Future Providers

---

# Rule 4 — AI Gateway

Every AI request must pass through the AI Gateway.

The rest of the application must never directly call Gemini, OpenAI, or any provider SDK.

---

# Rule 5 — Single Responsibility Principle

Each file should perform only one task.

Avoid large files.

Preferred maximum file size:

300–500 lines.

---

# Rule 6 — Security First

Never commit:

- API Keys
- Passwords
- Secrets
- Tokens
- Credentials
- Private Certificates

Use:

.env

Only commit:

.env.example

---

# Rule 7 — Documentation First

Every major feature must be documented before implementation.

Documentation is part of the software.

---

# Rule 8 — Clean Code

Code must be:

- Readable
- Modular
- Reusable
- Maintainable
- Testable

Avoid duplicate code.

---

# Rule 9 — Git Workflow

Small commits only.

Every commit should represent one logical change.

Example:

feat:

fix:

refactor:

docs:

test:

style:

---

# Rule 10 — Testing

Every major feature should be tested before pushing to GitHub.

Broken code must never be pushed to the main branch.

---

# Rule 11 — Naming Convention

Use meaningful names.

Good:

chat_agent.py

vision_service.py

embedding.py

Bad:

abc.py

test2.py

newfile.py

---

# Rule 12 — Folder Independence

Each folder should remain independent.

Dependencies should always point inward.

Example:

UI

↓

Services

↓

Core

↓

Providers

Never reverse the dependency direction.

---

# Rule 13 — Backward Compatibility

Whenever possible, new features should not break existing functionality.

Refactoring should preserve public interfaces.

---

# Rule 14 — Scalability

Every design decision should support future expansion.

The architecture should accommodate:

- New AI Models
- New Providers
- New Agents
- New Services
- New User Interfaces

without requiring major redesign.

---

# Rule 15 — Open Source Quality

Every module should be written as if it will be reviewed by thousands of developers.

Maintain high standards of readability and professionalism.

---

# Engineering Philosophy

Think Long-Term.

Write Once.

Reuse Everywhere.

Keep It Simple.

Design Before Code.

Documentation Before Implementation.

Build for the Future.

---

# Final Principle

Project BRAHMA is not a collection of AI scripts.

It is a long-term AI Research Platform built with engineering discipline, modular architecture, and production-quality standards.