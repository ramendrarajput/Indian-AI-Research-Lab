# PROJECT BRAHMA — DEPENDENCY MODEL

> *"The direction of dependency determines the stability of the architecture."*

**Project BRAHMA**
**Core Dependency Architecture**

---

# Purpose

This document defines the official **Dependency Model** of Project BRAHMA.

Its purpose is to establish permanent rules governing how engineering components may depend upon one another.

The Dependency Model protects the architecture from becoming tightly coupled, unstable, and difficult to evolve.

Every engineering dependency must comply with the rules defined in this document.

---

# Scope

This document governs dependencies between:

* Engineering Layers
* Domains
* Modules
* Components
* Services
* Agents
* Applications
* Future Laboratories
* Plugins

It applies to the entire Project BRAHMA ecosystem.

---

# Why Dependency Rules Exist

Without dependency rules:

* modules become tightly coupled,
* circular references appear,
* testing becomes difficult,
* replacement becomes expensive,
* architecture gradually collapses.

Stable dependency direction is the foundation of long-term engineering.

---

# Core Principle

Project BRAHMA follows one immutable architectural rule:

> **Dependencies always point toward greater stability.**

Higher-level systems depend on lower-level foundations.

Lower-level foundations never depend on higher-level implementations.

---

# Dependency Hierarchy

The permanent dependency hierarchy is:

```text
Applications
        │
        ▼
Pages
        │
        ▼
User Interface
        │
        ▼
Agents
        │
        ▼
Services
        │
        ▼
Core
        │
        ▼
Kernel
```

Every dependency must follow this direction.

---

# Dependency Direction

The architecture follows a single direction:

```text
Higher Abstraction

↓

Lower Abstraction

↓

Permanent Foundation
```

Reverse dependencies are prohibited.

---

# Allowed Layer Dependencies

## Applications

Applications may depend upon:

* Pages
* UI
* Agents
* Services

Applications must never depend directly upon:

* Providers
* Infrastructure
* Kernel

---

## Pages

Pages may depend upon:

* UI
* Agents
* Services

Pages must never contain business logic.

---

## User Interface

The UI may depend upon:

* Agents
* Services
* Core Interfaces

The UI must never depend upon:

* AI Providers
* Databases
* Infrastructure
* Kernel implementation

---

## Agents

Agents may depend upon:

* Services
* Core
* Contracts
* Interfaces

Agents must never depend upon:

* Pages
* UI
* Applications

Agents reason.

They do not render interfaces.

---

## Services

Services may depend upon:

* Core
* Contracts
* Interfaces
* Registries

Services must never depend upon:

* Agents
* Pages
* UI
* Applications

Services execute engineering capabilities.

They do not coordinate user interaction.

---

## Core

Core may depend upon:

* Kernel
* Standard Library
* Approved third-party libraries

Core must never depend upon:

* Services
* Agents
* Applications
* UI
* Pages

Core remains implementation-independent.

---

## Kernel

Kernel depends upon nothing inside Project BRAHMA.

The Kernel is the architectural root.

---

# Infrastructure Dependencies

Infrastructure exists beside the runtime architecture.

Engineering components may use infrastructure through stable abstractions.

No engineering module should directly depend upon infrastructure implementation.

Examples:

Allowed:

```text
Service

↓

Storage Contract

↓

Infrastructure
```

Not allowed:

```text
Service

↓

AWS SDK
```

---

# Provider Dependencies

Providers are implementation details.

Only the AI Gateway communicates with providers.

```text
Agent

↓

Service

↓

Core

↓

AI Gateway

↓

Provider
```

Direct provider access is prohibited.

---

# Tool Dependencies

Tools perform engineering operations.

Tools may depend upon:

* Core
* Utilities
* Approved Libraries

Tools should never depend upon:

* Applications
* UI
* Pages

---

# Utility Dependencies

Utilities may depend upon:

* Standard Library

Utilities should remain almost dependency-free.

Utilities should never depend upon:

* Services
* Agents
* Applications

---

# Plugin Dependencies

Plugins communicate through contracts.

Plugins must never directly access internal implementation details.

Correct:

```text
Plugin

↓

Interface

↓

Core
```

Incorrect:

```text
Plugin

↓

Internal Class
```

---

# Laboratory Dependencies

Every future laboratory follows the same architecture.

Example:

```text
AI Lab

↓

Services

↓

Core

↓

Kernel
```

The laboratory should never redefine architectural layers.

---

# Cross-Domain Communication

Domains communicate only through:

* Contracts
* Interfaces
* Events
* Registries

Direct internal coupling between domains is discouraged.

---

# Dependency Inversion Principle

High-level policy must never depend upon low-level implementation.

Instead:

High-level modules define interfaces.

Low-level modules implement those interfaces.

Example:

```text
Chat Service

↓

Chat Provider Interface

↓

Gemini Provider

OpenAI Provider

Claude Provider
```

The service depends on the interface—not on the provider.

---

# Circular Dependencies

Circular dependencies are prohibited.

Example:

```text
Service A

↓

Service B

↓

Service A
```

This is an architectural violation.

If circular dependencies appear:

* redesign responsibilities,
* introduce an interface,
* extract shared functionality into Core.

Never solve circular dependencies with shortcuts.

---

# Shared Dependencies

Shared functionality belongs in Core.

If multiple modules require identical behavior:

Bad:

```text
Agent

↓

Utility Copy

Service

↓

Utility Copy
```

Good:

```text
Agent

↓

Core

↓

Shared Utility

↓

Service
```

---

# External Libraries

External libraries should enter the architecture through controlled boundaries.

Applications should not directly expose third-party APIs throughout the codebase.

Adapters or gateways should isolate external dependencies.

---

# Dependency Stability Rule

The lower the layer:

* the fewer dependencies it should have,
* the slower it should change,
* the greater its stability.

Example:

| Layer        | Stability |
| ------------ | --------- |
| Applications | Low       |
| Pages        | Medium    |
| UI           | Medium    |
| Agents       | High      |
| Services     | Higher    |
| Core         | Very High |
| Kernel       | Maximum   |

---

# Architectural Violations

Examples of violations:

❌ UI importing AI Provider SDK.

❌ Service importing Streamlit.

❌ Core importing Application code.

❌ Agent modifying UI directly.

❌ Kernel referencing Services.

Each of these breaks architectural independence.

---

# Dependency Review Checklist

Before introducing a dependency, verify:

✓ Does it point inward?

✓ Does it increase coupling?

✓ Can the implementation be replaced later?

✓ Does it violate any architectural boundary?

✓ Can an interface remove this dependency?

Only after these questions are satisfied should the dependency be introduced.

---

# Relationship with Previous Documents

This document extends:

* 01_ARCHITECTURE_PHILOSOPHY.md
* 02_ARCHITECTURAL_VOCABULARY.md
* 03_STRUCTURAL_LAYER_MODEL.md
* 04_EXECUTION_LAYER_MODEL.md

---

# Foundation for Future Documents

This Dependency Model becomes the basis for:

* Contracts
* Interfaces
* Kernel
* AI Gateway
* Provider Architecture
* Registry System
* Event System
* Plugin System
* Dependency Injection
* Module Design

No future engineering document should contradict this dependency model.

---

# Long-Term Vision

As Project BRAHMA grows into hundreds of modules and multiple scientific laboratories, dependency complexity will naturally increase.

The Dependency Model exists to ensure that architectural complexity does **not** grow at the same rate.

New capabilities should increase functionality—not architectural entropy.

---

# Final Principle

Architecture remains stable because dependencies remain disciplined.

Every dependency is an engineering decision.

Every engineering decision either strengthens or weakens the architecture.

Project BRAHMA therefore treats dependency direction as a constitutional rule rather than an implementation preference.

---

*"Stable dependencies create stable systems.

Stable systems create sustainable engineering."*

**Project BRAHMA**
**Core Dependency Model**
