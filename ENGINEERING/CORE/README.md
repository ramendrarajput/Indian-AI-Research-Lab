# PROJECT BRAHMA — CORE

> *"Every great system has a stable core.
> Everything else is allowed to evolve around it."*

**— Project BRAHMA**

---

# PURPOSE

The **CORE** domain is the architectural heart of Project BRAHMA.

It contains the fundamental abstractions, contracts, domain models, and orchestration logic upon which every other engineering domain depends.

CORE exists to ensure that the project remains:

* modular,
* maintainable,
* provider-independent,
* scalable,
* and stable over decades of continuous evolution.

CORE defines **how the system thinks**, not how it is displayed or deployed.

---

# MISSION

The mission of CORE is to provide a stable engineering foundation that remains independent of:

* user interfaces,
* AI providers,
* databases,
* operating systems,
* cloud platforms,
* external services,
* programming frameworks.

Everything may change.

CORE should remain.

---

# ARCHITECTURAL POSITION

```text
Applications

↓

Agents

↓

Services

↓

CORE

↓

Infrastructure

↓

External Providers
```

Every engineering domain ultimately depends upon CORE.

CORE should depend upon as little as possible.

---

# PHILOSOPHY

CORE is not a collection of utilities.

CORE is the **engineering brain** of Project BRAHMA.

It defines:

* rules,
* contracts,
* abstractions,
* orchestration,
* shared behaviors,
* architectural truth.

Implementation details belong elsewhere.

---

# CORE RESPONSIBILITIES

CORE owns responsibilities that are universal across the entire project.

Examples include:

* business rules,
* shared abstractions,
* domain models,
* interfaces,
* common contracts,
* event definitions,
* configuration contracts,
* lifecycle management,
* plugin contracts,
* runtime orchestration.

If a responsibility belongs to every engineering domain, it probably belongs inside CORE.

---

# WHAT BELONGS INSIDE CORE

Typical components include:

## Domain Models

Canonical representations of important concepts.

Example:

* Document
* Conversation
* Knowledge
* Agent
* Memory
* Task

---

## Interfaces

Public contracts used by other domains.

Examples:

* AI Interface
* Memory Interface
* Storage Interface
* Search Interface

Interfaces define behavior.

They never contain provider-specific implementation.

---

## Business Rules

Core decision-making logic.

Business rules should never exist inside:

* UI
* Infrastructure
* Applications

---

## Shared Contracts

Common request and response structures.

Shared data models.

Configuration schemas.

Validation contracts.

---

## Event Definitions

Project-wide events.

Examples:

* TaskStarted
* TaskCompleted
* DocumentIndexed
* AgentCreated

Events improve decoupling.

---

## Runtime Orchestration

The overall execution flow of Project BRAHMA.

CORE coordinates.

Other domains execute.

---

## Common Types

Project-wide:

* Enumerations
* Constants
* Identifiers
* Shared value objects

---

# WHAT DOES NOT BELONG INSIDE CORE

CORE should never contain:

* Streamlit code
* Web UI
* HTML
* CSS
* API provider SDKs
* Database queries
* Cloud deployment logic
* Hardware-specific code
* Temporary experiments
* Provider configuration
* Feature-specific application workflows

If a component depends on a specific technology, it probably does **not** belong inside CORE.

---

# DESIGN PRINCIPLES

## Stability First

CORE changes less frequently than any other engineering domain.

Architectural stability is more valuable than rapid modification.

---

## Framework Independence

CORE should not depend upon:

* Streamlit
* FastAPI
* Flask
* LangChain
* LangGraph
* OpenAI SDK
* Gemini SDK

Frameworks are replaceable.

CORE should remain reusable.

---

## Provider Independence

CORE communicates through abstractions.

It never communicates directly with providers.

Correct:

```python
chat()
```

Incorrect:

```python
OpenAI()

Gemini()

Anthropic()
```

Provider-specific implementations belong elsewhere.

---

## Minimal Dependencies

CORE should depend only upon packages that are:

* mature,
* essential,
* long-term,
* architecture-neutral.

Reducing dependencies improves stability.

---

## High Cohesion

Components inside CORE should be closely related.

Every module should contribute to the same architectural mission.

---

## Low Coupling

CORE should expose interfaces rather than implementation details.

Other domains should depend upon contracts, not internal code.

---

# DEPENDENCY RULES

Allowed:

```text
Applications

↓

Agents

↓

Services

↓

CORE
```

Not allowed:

```text
CORE

↓

Applications
```

Reverse dependencies are prohibited.

---

# DIRECTORY EVOLUTION

The internal organization of CORE may evolve over time.

Typical future areas may include:

```text
CORE/

contracts/

models/

interfaces/

events/

runtime/

configuration/

exceptions/

patterns/

plugins/

types/

utilities/
```

These directories should only be introduced when justified by architectural need.

---

# RELATIONSHIP WITH OTHER DOMAINS

## AI

Uses CORE interfaces.

CORE never depends upon AI implementations.

---

## SERVICES

Implements workflows using CORE.

---

## AGENTS

Build autonomous behavior upon CORE abstractions.

---

## INFRASTRUCTURE

Implements persistence and external communication.

CORE defines the contracts.

Infrastructure fulfills them.

---

## APPLICATIONS

Present CORE capabilities to users.

Applications never redefine CORE behavior.

---

# DOCUMENTATION

Every public component inside CORE should include:

* purpose,
* responsibility,
* public interfaces,
* expected behavior.

Undocumented architectural components are considered incomplete.

---

# TESTING

CORE requires the highest testing standards within Project BRAHMA.

Critical components should include:

* unit tests,
* contract tests,
* integration validation,
* regression tests.

Reliability of the entire project depends upon CORE correctness.

---

# LONG-TERM VISION

The CORE domain is expected to remain relevant throughout the lifetime of Project BRAHMA.

As technologies evolve, CORE should require minimal modification while allowing surrounding domains to adapt.

The goal is not to build software that works today.

The goal is to build an architectural foundation that remains useful for generations.

---

# FINAL PRINCIPLE

CORE is not the largest engineering domain.

It is the most stable one.

When uncertainty arises, ask one question:

> **"Is this responsibility fundamental to the entire project?"**

If the answer is yes, it belongs in CORE.

If not, it belongs elsewhere.

---

*"Frameworks evolve.

Providers change.

Applications come and go.

A well-designed core endures."*

**Project BRAHMA**
**Engineering Core Domain**
