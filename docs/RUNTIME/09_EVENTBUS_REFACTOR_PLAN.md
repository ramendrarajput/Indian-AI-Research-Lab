# PROJECT BRAHMA

# EVENT BUS INTEGRATION PLAN

Document ID
-----------
09_EVENTBUS_REFACTOR_PLAN

Version
-------
v0.2

Author
------
Ramendra Singh Rajput

Status
------
PLANNED

---

# Objective

Integrate the Universal Event Bus into the BRAHMA Runtime
without introducing circular imports, hidden dependencies,
or unstable boot behaviour.

This document defines the exact integration sequence.

No step should be skipped.

---

# Current Runtime

Current Boot Sequence

brahma.py

↓

startup.py

↓

boot.py

↓

kernel.py

↓

console.py

↓

dispatcher.py

↓

commands.py

Runtime successfully boots.

This state must remain stable after every integration step.

---

# Current EventBus

Completed

✓ event.py

✓ event_type.py

✓ subscriber.py

✓ publisher.py

✓ event_bus.py

✓ history.py

✓ handlers.py

✓ exceptions.py

Pending

□ README.md

---

# Integration Philosophy

Current

Component

↓

Component

↓

Component

Future

Publisher

↓

EventBus

↓

Subscribers

Runtime components must never communicate directly.

Everything should eventually flow through the Event Bus.

---

# PHASE 1

Runtime Foundation

Goal

Import EventBus into Runtime safely.

Checklist

□ Import runtime_event_bus into boot.py

□ Import runtime_event_history where required

□ Runtime still boots

STOP

Run

python brahma.py

Boot must succeed before continuing.

---

# PHASE 2

Kernel Events

Goal

Kernel becomes first publisher.

Events

KERNEL_START

KERNEL_READY

KERNEL_STOP

Checklist

□ RuntimeKernel inherits EventPublisher

□ attach_bus()

□ publish(KERNEL_START)

□ publish(KERNEL_READY)

□ publish(KERNEL_STOP)

STOP

Run Runtime again.

No regressions allowed.

---

# PHASE 3

Runtime Events

Events

RUNTIME_BOOT

RUNTIME_READY

RUNTIME_STOP

Checklist

□ boot_runtime()

□ startup_runtime()

□ shutdown_runtime()

All publish events.

STOP

Boot Runtime.

Verify.

---

# PHASE 4

Console Events

Events

COMMAND_RECEIVED

UNKNOWN_COMMAND

Checklist

□ Console publishes entered command

□ Unknown commands generate events

STOP

Manual testing.

---

# PHASE 5

Dispatcher Events

Goal

Dispatcher becomes event aware.

Checklist

□ Publish before dispatch

□ Publish unknown command

□ Publish dispatch completed

STOP

Boot Runtime.

---

# PHASE 6

Logging Handler

Goal

Automatic Runtime Logging

Checklist

□ Register LoggingEventHandler

□ Verify events appear in runtime.log

STOP

Test.

---

# PHASE 7

History Integration

Goal

Event Replay Foundation

Checklist

□ Every published event stored

□ Verify history size grows

□ Verify history queries

STOP

Test.

---

# PHASE 8

Subscriber Registration

Goal

Automatic Runtime Registration

Checklist

□ Kernel subscriber

□ Runtime subscriber

□ Console subscriber

STOP

Verify.

---

# PHASE 9

Diagnostics

Goal

Runtime Inspection

Commands

events

history

subscribers

publishers

statistics

Checklist

□ Runtime Console commands

STOP

Verify.

---

# PHASE 10

Documentation

README.md

Architecture Diagram

Developer Guide

Examples

Future Roadmap

---

# Testing Rules

Every phase must satisfy

□ Imports successful

□ No circular imports

□ Runtime boots

□ Runtime commands work

□ Runtime exits cleanly

Only then continue.

---

# Never Do

Never integrate multiple phases together.

Never continue if Runtime fails.

Never ignore circular imports.

Never publish events before EventBus exists.

---

# Success Criteria

At completion

brahma.py

↓

startup.py

↓

boot.py

↓

kernel.py

↓

EventBus

↓

Logging

↓

History

↓

Subscribers

↓

Console

↓

Dispatcher

↓

Commands

Everything boots successfully.

No circular imports.

No runtime failures.

Universal Event Bus operational.

---

# Milestone

M2

Universal Event Bus

Status

READY TO START

---

# Progress Tracker

## Phase 1 — EventBus Foundation

- [x] event.py
- [x] event_type.py
- [x] subscriber.py
- [x] publisher.py
- [x] event_bus.py
- [x] history.py
- [x] handlers.py
- [x] exceptions.py
- [x] Runtime integration completed
- [x] Runtime boot successful

---

## Phase 2 — Kernel Event Publisher

- [x] RuntimeKernel inherits EventPublisher
- [x] Kernel attached to EventBus
- [x] KERNEL_START publish added
- [x] KERNEL_READY publish added
- [x] KERNEL_STOP publish added
- [ ] Logging Handler registration
- [ ] First live event test

---

## Phase 3 — Runtime Events

- [ ] RUNTIME_BOOT
- [ ] RUNTIME_READY
- [ ] RUNTIME_SHUTDOWN

---

## Phase 4 — Console Events

- [ ] COMMAND_RECEIVED
- [ ] UNKNOWN_COMMAND

---

## Phase 5 — Dispatcher Events

- [ ] BEFORE_DISPATCH
- [ ] AFTER_DISPATCH

---

## Phase 6 — Diagnostics

- [ ] eventbus command
- [ ] events command
- [ ] history command
- [ ] subscribers command
- [ ] publishers command

---

## Final Verification

- [ ] Runtime boots
- [ ] No circular imports
- [ ] EventBus active
- [ ] Event history working
- [ ] Logging working
- [ ] Runtime stable

Phase 3

[x] Runtime Boot Event
[x] Runtime Ready Event
[x] Runtime Start Event
[x] Runtime Stop Event
[x] Runtime Restart Event
[x] Runtime Error Event

[x] Kernel Start Event
[x] Kernel Ready Event
[x] Kernel Stop Event
[x] Kernel Error Event


========================================
PHASE 1 – Core Infrastructure
========================================

[✓] Event
[✓] EventType
[✓] Publisher
[✓] Subscriber
[✓] EventBus
[✓] EventHistory
[✓] LoggingHandler

========================================
PHASE 2 – Runtime Integration
========================================

[✓] Runtime Boot
[✓] Runtime Ready
[✓] Kernel Start
[✓] Kernel Ready
[✓] Console Command
[✓] Unknown Command

========================================
PHASE 3 – Event Statistics
========================================

[✓] Statistics
[✓] Publish Counter
[✓] Event Summary

========================================
PHASE 4 – Runtime Commands
========================================

[✓] events (placeholder)
[ ] events stats
[ ] events last
[ ] events clear

========================================
M2 STATUS
========================================

🟢 STABLE

09_EVENTBUS_REFACTOR_CHECKLIST.md

PHASE 4

[✓] events
[ ] events last
[ ] events clear

M2 Progress

██████████████████████████░ 97%

#=================================UPDATE===================================
# UPDATE

# PROJECT BRAHMA

## Universal Event Bus Refactor Plan

**Document Version:** 2.0
**Current Milestone:** M2 Completed

---

# Objective

Build a Universal Event Bus capable of connecting every component of Project BRAHMA through a common event-driven architecture.

Every Runtime component, Laboratory, Universal Agent, Memory Engine and future AI module communicates only through events.

---

# M2 Goals (Completed)

## Runtime Integration

* [x] Universal Event Bus created
* [x] Universal Event History created
* [x] Event Publisher implemented
* [x] Runtime Boot events published
* [x] Runtime Ready events published
* [x] Runtime Kernel Start events published
* [x] Runtime Kernel Ready events published
* [x] Runtime Stop events published
* [x] Runtime Kernel Stop events published
* [x] Runtime Shutdown lifecycle completed

---

## Runtime Console Integration

* [x] Console publishes COMMAND_RECEIVED events
* [x] Unknown commands publish UNKNOWN_COMMAND events
* [x] Dispatcher integrated with Event Bus

---

## Event History

* [x] Event History storage
* [x] Event statistics
* [x] Event counters
* [x] Event source tracking
* [x] `events`
* [x] `events last`
* [x] `events clear`

---

## Runtime Lifecycle

Successfully implemented complete Runtime lifecycle.

```
BOOT
 ↓
READY
 ↓
KERNEL START
 ↓
RUNNING
 ↓
CONSOLE
 ↓
STOP
 ↓
SHUTDOWN
```

---

# M2 Result

Project BRAHMA now has a fully operational Runtime Event System.

Current Runtime components are synchronized through the Universal Event Bus.

This becomes the architectural backbone for every future module.

---

# M3 Goals

## Laboratory Manager

Planned Runtime Commands

* load <lab>
* unload <lab>
* reload <lab>
* labs
* lab info

---

## Runtime Registry

* Dynamic Laboratory Registration
* Runtime Discovery
* Dependency Management

---

## Laboratory Events

New Event Types

* LAB_LOADING
* LAB_LOADED
* LAB_UNLOADED
* LAB_FAILED

---

## Runtime Commands

```
BRAHMA > load finance

BRAHMA > load coding

BRAHMA > load physics

BRAHMA > unload finance

BRAHMA > labs
```

---

# Future Milestones

## M4

Universal Agent

## M5

Memory Engine

## M6

Offline LLM Integration

## M7

ChatGPT GUI Runtime Integration

```
app.py
     ↓
Project BRAHMA Runtime
     ↓
Universal Agent
     ↓
Laboratories
     ↓
Memory Engine
     ↓
Offline LLM
```

---

# Long-Term Vision

Project BRAHMA will evolve into a complete AI Operating System capable of running entirely offline.

The Runtime, Memory Engine, Event Bus, Laboratories, RAG System, Vector Database and future Local LLM will work together without requiring continuous internet connectivity.

This Event Bus is the foundation upon which the complete BRAHMA architecture will be built.


