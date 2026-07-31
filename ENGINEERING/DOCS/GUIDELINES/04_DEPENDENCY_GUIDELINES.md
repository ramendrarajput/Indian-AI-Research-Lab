# PROJECT BRAHMA — DEPENDENCY GUIDELINES

> *"Every dependency is a long-term commitment.
> Choose dependencies with the same care as architectural decisions."*

**— Project BRAHMA**

---

# PURPOSE

This document defines the dependency management guidelines followed throughout Project BRAHMA.

Dependencies provide valuable functionality, but every external package also introduces:

* maintenance responsibility,
* security risk,
* compatibility challenges,
* operational complexity.

Project BRAHMA values architectural stability over dependency quantity.

---

# DEPENDENCY PHILOSOPHY

Project BRAHMA follows one fundamental principle:

> **Add dependencies only when they provide clear, long-term value.**

The best dependency is often the one that is not required.

---

# DEPENDENCY OBJECTIVES

Dependency management should ensure:

* Stability
* Security
* Maintainability
* Portability
* Reproducibility
* Long-term sustainability

---

# DEPENDENCY HIERARCHY

When solving a problem, always follow this order:

```text id="u1q2aw"
Python Standard Library

↓

Existing Project Module

↓

Internal Reusable Package

↓

Trusted Third-Party Library

↓

Custom Implementation
```

Avoid introducing external libraries before evaluating existing solutions.

---

# STANDARD LIBRARY FIRST

Always determine whether Python already provides the required functionality.

Examples:

* pathlib
* logging
* json
* sqlite3
* datetime
* asyncio
* typing

Prefer the standard library whenever practical.

---

# REUSE BEFORE INSTALL

Before adding a new package verify:

* Does Project BRAHMA already solve this problem?
* Can an existing internal module be reused?
* Can the functionality be generalized?

Avoid duplicate capabilities.

---

# DEPENDENCY EVALUATION

Every dependency should be evaluated before installation.

Questions to consider:

* Is the project actively maintained?
* Is it widely trusted?
* Is the documentation complete?
* Is the license acceptable?
* Is the project stable?
* Does it introduce unnecessary complexity?

Installation should never be the first solution.

---

# LONG-TERM SUPPORT

Prefer packages with:

* active maintainers,
* regular releases,
* strong community support,
* clear documentation,
* long-term stability.

Avoid abandoned or experimental libraries for production systems unless research explicitly requires them.

---

# SECURITY REVIEW

Every dependency should undergo a security review.

Verify:

* known vulnerabilities,
* supply-chain reputation,
* trusted source,
* secure release process.

Security is more important than convenience.

---

# LICENSE COMPATIBILITY

Every dependency should have a compatible license.

Document important licenses whenever required.

Avoid introducing legal uncertainty into the project.

---

# VERSION MANAGEMENT

Versions should remain predictable.

Avoid uncontrolled upgrades.

Use explicit version constraints where appropriate.

Dependencies should evolve deliberately rather than accidentally.

---

# OPTIONAL DEPENDENCIES

Large or specialized features should avoid forcing unnecessary installations.

Whenever practical, optional functionality should remain isolated.

Example:

```text id="i5g3bx"
Core AI

↓

Optional Image Generation

↓

Optional Video Processing
```

Users should install only what they need.

---

# DEVELOPMENT DEPENDENCIES

Development tools should remain separate from runtime dependencies.

Examples:

Development:

* linters
* formatters
* testing frameworks

Runtime:

* AI providers
* vector databases
* scientific libraries

Separate responsibilities improve deployment efficiency.

---

# DEPENDENCY DOCUMENTATION

Every significant dependency should have a documented purpose.

Future contributors should understand:

* why it exists,
* where it is used,
* whether alternatives were considered.

Undocumented dependencies increase technical debt.

---

# UNUSED DEPENDENCIES

Unused packages should be removed during maintenance.

Unused dependencies increase:

* attack surface,
* installation time,
* maintenance cost,
* deployment complexity.

Regular cleanup is encouraged.

---

# DEPENDENCY UPDATES

Update dependencies deliberately.

Before upgrading verify:

* compatibility,
* breaking changes,
* performance,
* documentation,
* existing tests.

Never upgrade production dependencies blindly.

---

# AI PROVIDERS

AI providers should remain replaceable.

Business logic should never depend directly on:

* OpenAI
* Google Gemini
* Anthropic
* Ollama
* DeepSeek
* future providers

Provider-specific implementations belong inside dedicated provider modules.

---

# LARGE FRAMEWORKS

Avoid adopting large frameworks when a lightweight solution is sufficient.

Frameworks should solve architectural problems—not create them.

---

# EXPERIMENTAL LIBRARIES

Experimental packages should remain isolated from production architecture.

Research may use experimental libraries.

Production systems should depend upon stable components.

---

# PYPROJECT.TOML

Project metadata and packaging configuration belong in:

```text id="lm9nfd"
pyproject.toml
```

This file serves as the authoritative package definition.

---

# REQUIREMENTS FILES

Dependencies should remain organized.

Examples:

```text id="0x9yur"
requirements.txt

requirements-dev.txt

requirements-research.txt
```

Separate runtime, development, and research requirements whenever practical.

---

# EDITABLE INSTALLATION

Development should prefer:

```bash id="9g4yia"
pip install -e .
```

Editable installation improves:

* stable imports,
* package management,
* developer experience.

Avoid modifying Python paths manually.

---

# DEPENDENCY AUDITS

Periodically review dependencies for:

* maintenance status,
* security,
* usage,
* necessity,
* replacement opportunities.

Dependency audits are part of long-term maintenance.

---

# WHAT SHOULD NEVER HAPPEN

Project BRAHMA should never:

* install packages without evaluation,
* depend upon abandoned libraries,
* duplicate existing functionality,
* keep unused dependencies,
* tightly couple architecture to one external provider.

---

# DEPENDENCY REVIEW CHECKLIST

Before adding a dependency verify:

✓ Clear purpose

✓ Active maintenance

✓ Trusted source

✓ Compatible license

✓ Security reviewed

✓ Existing alternatives evaluated

✓ Documentation updated

✓ Long-term value confirmed

---

# FINAL PRINCIPLE

Dependencies should strengthen the architecture—not control it.

Every installed package becomes part of the long-term engineering responsibility of Project BRAHMA.

Choose wisely.

Maintain responsibly.

Replace thoughtfully.

---

*"Architecture should own dependencies.

Dependencies should never own the architecture."*

**Project BRAHMA**
