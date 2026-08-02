# Runtime Refactor Plan

**Document Version:** 0.2  
**Project:** Project BRAHMA  
**Module:** Universal Runtime  
**Status:** Engineering Planning Document

---

# Objective

This document defines the Runtime Refactor Plan after completion of the
initial Runtime Architecture.

The goal is to transform the current Runtime into a fully modular,
dependency-clean, production-grade architecture while preserving the
existing functionality.

This document serves as the engineering blueprint for Runtime v0.2.

---

# Current Runtime Architecture

```
brahma.py
        │
        ▼
startup.py
        │
        ▼
boot.py
        │
        ▼
kernel.py
        │
        ▼
console.py
        │
        ▼
dispatcher.py
        │
        ▼
commands.py
```

---

# Foundation Layer (LOCKED)

The following files are considered Runtime Foundation.

They should remain stable.

```
ENGINEERING/
└── CORE/
    └── RUNTIME/
        state.py
        logger.py
        context.py
        registry.py
```

Status

✅ Approved

---

# Audit Summary

| Module | Status |
|----------|---------|
| state.py | ✅ Approved |
| logger.py | ✅ Approved |
| context.py | ✅ Approved |
| registry.py | ✅ Approved |
| dispatcher.py | ✅ Approved |
| commands.py | ⚠ Needs Refactor |
| boot.py | ⚠ Minor Refactor |
| kernel.py | ⚠ Needs Refactor |
| startup.py | ❌ Needs Refactor |
| console.py | ❌ Needs Refactor |
| brahma.py | ⚠ Wiring Update |

---

# Architecture Problems Identified

## 1. Circular Dependency

Current

```
Console

↓

Startup

↓

Commands

↓

Dispatcher

↓

Console
```

This violates clean architecture.

---

## 2. Responsibility Mixing

Console currently contains

- help
- runtime
- status
- labs
- memory
- agent

These already exist inside commands.py.

Business logic must never exist inside the Console.

---

## 3. Startup Responsibilities

startup.py currently

- Boots Runtime
- Starts Kernel
- Registers Commands

Startup should never register commands.

---

## 4. Runtime Lifecycle Duplication

Current

RuntimeState

```
CREATED
BOOTING
READY
RUNNING
STOPPED
FAILED
```

KernelStatus

```
STOPPED
STARTING
RUNNING
STOPPING
```

Two lifecycle systems exist.

Only one should exist.

---

## 5. Entry Point Wiring

Registration currently occurs inside Runtime modules.

Instead, Runtime wiring should only happen inside

```
brahma.py
```

---

# Target Runtime Architecture

```
                brahma.py
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
     startup     dispatcher    console
         │                       │
         ▼                       │
       boot                      │
         ▼                       │
      kernel                     │
         ▼                       │
     context                     │
         ▼                       │
     registry                    │
                                 │
                 commands ◄──────┘
```

---

# Refactor Phase A

## Dependency Cleanup

Tasks

- Remove command registration from startup.py
- Remove Runtime methods from console.py
- Console becomes Dispatcher-only
- Commands become Business Logic only

Expected Result

```
Console

↓

Dispatcher

↓

Commands
```

---

# Refactor Phase B

## Runtime Lifecycle

Tasks

Remove

```
KernelStatus
```

Kernel will instead use

```
RuntimeState
```

Single Runtime Lifecycle

```
CREATED

↓

BOOTING

↓

INITIALIZING

↓

LOADING_KERNEL

↓

LOADING_SERVICES

↓

LOADING_LABS

↓

READY

↓

RUNNING

↓

STOPPING

↓

STOPPED

↓

FAILED
```

---

# Refactor Phase C

## Runtime Entry Point

brahma.py becomes the only Runtime wiring module.

Flow

```
startup_runtime()

↓

register_runtime_commands()

↓

runtime_console.start()
```

---

# Future Runtime

After Refactor

```
Boot Screen

↓

Runtime Initialization

↓

Kernel Loading

↓

LAB Registry

↓

Universal Agent

↓

Project BRAHMA Home

↓

Universal Console

↓

Future UI
```

---

# Expected Benefits

- Zero circular imports
- Clean dependency graph
- Stable Runtime lifecycle
- Easier debugging
- Easier testing
- Future Agent integration
- Future GUI integration
- Runtime scalability

---

# Engineering Rule

During Runtime development

> Never fix architecture by adding imports.

Instead

> Move responsibilities to the correct layer.

---

# Runtime Engineering Philosophy

```
One Runtime

↓

One Context

↓

One Lifecycle

↓

One Dispatcher

↓

One Entry Point

↓

Universal Intelligence
```

---

**Status**

Runtime Audit Completed

Ready for Runtime Refactor Phase A