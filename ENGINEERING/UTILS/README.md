# PROJECT BRAHMA — UTILS

> *"Utilities should simplify engineering, not become engineering."*

**— Project BRAHMA**

---

# PURPOSE

The **UTILS** domain contains small, generic, reusable helper functions that support engineering code throughout Project BRAHMA.

Utilities improve readability, reduce duplication, and simplify implementation.

Utilities are supporting components.

They are **not** business components.

---

# MISSION

The mission of the UTILS domain is to provide lightweight helper functionality that can be safely reused across every engineering domain without introducing architectural coupling.

Utilities should reduce complexity.

They should never create complexity.

---

# ARCHITECTURAL POSITION

```text
Applications

↓

Agents

↓

Services

↓

Core

↓

Utilities
```

Utilities support all engineering layers.

They never define engineering behavior.

---

# PHILOSOPHY

Utilities exist to assist engineering.

They should never become the center of engineering.

If removing a utility changes business behavior, it probably does not belong inside UTILS.

---

# RESPONSIBILITIES

The UTILS domain owns generic helper functionality including:

* string manipulation,
* path handling,
* date and time formatting,
* hashing,
* identifier generation,
* serialization helpers,
* validation helpers,
* conversion helpers.

---

# WHAT BELONGS INSIDE UTILS

Examples include:

## String Helpers

* normalize_text()
* clean_whitespace()
* slugify()

---

## Date Helpers

* current_timestamp()
* format_datetime()
* parse_date()

---

## Path Helpers

* safe_join()
* normalize_path()
* relative_path()

---

## Identifier Helpers

* generate_uuid()
* random_identifier()

---

## Hash Helpers

* sha256_hash()
* md5_hash() *(only where appropriate)*
* checksum()

---

## Serialization Helpers

* safe_json_dump()
* safe_json_load()

---

## Validation Helpers

* is_email()
* is_valid_filename()
* sanitize_input()

---

## Formatting Helpers

* format_bytes()
* format_duration()
* format_number()

---

# WHAT DOES NOT BELONG INSIDE UTILS

The UTILS domain should never contain:

* AI workflows,
* business rules,
* database queries,
* service orchestration,
* reusable engineering tools,
* infrastructure management.

If the functionality solves an engineering problem rather than supporting code, it likely belongs in **TOOLS**, not **UTILS**.

---

# DESIGN PRINCIPLES

Every utility should be:

* small,
* deterministic,
* stateless,
* reusable,
* independently testable.

Utilities should have minimal dependencies.

---

# SINGLE RESPONSIBILITY

One utility.

One helper operation.

Examples:

Good

* normalize_path()
* sha256_hash()
* current_timestamp()

Avoid

* process_everything()
* helper.py with hundreds of unrelated functions

---

# DEPENDENCY RULES

Utilities may depend upon:

* Python Standard Library
* other utilities (when appropriate)

Utilities should avoid depending upon:

* Applications
* Services
* Agents
* Infrastructure

---

# TOOLS VS UTILS

Project BRAHMA intentionally separates these domains.

## TOOLS

Perform engineering operations.

Examples:

* PDF Parser
* OCR Wrapper
* Markdown Converter
* JSON Validator

---

## UTILS

Support engineering code.

Examples:

* UUID Generator
* Date Formatter
* String Cleaner
* Path Helper

Utilities assist.

Tools execute.

---

# TESTING

Every utility should include unit tests.

Utilities are reused extensively.

A defect in one utility may affect many engineering domains.

---

# DOCUMENTATION

Every public utility should document:

* purpose,
* parameters,
* return value,
* edge cases,
* examples (where appropriate).

---

# LONG-TERM VISION

The UTILS domain should remain intentionally small and disciplined.

It should never become a dumping ground for miscellaneous code.

As Project BRAHMA grows over decades, utilities should continue to represent only the smallest reusable building blocks of the engineering ecosystem.

---

# FINAL PRINCIPLE

Utilities should make engineering easier to read, easier to maintain, and easier to reuse.

If a utility becomes large enough to require its own architecture, it should graduate into a more appropriate engineering domain.

---

*"Utilities support engineering.

They should never replace engineering."*

**Project BRAHMA**
**Utilities Engineering Domain**
