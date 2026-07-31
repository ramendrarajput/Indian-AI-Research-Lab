# PROJECT BRAHMA — CODE REVIEW GUIDELINES

> *"Every review is an opportunity to improve the project, not to criticize the engineer."*

**— Project BRAHMA**

---

# PURPOSE

This document defines the code review guidelines followed throughout Project BRAHMA.

Code review ensures that every contribution improves the project's:

* architecture,
* quality,
* maintainability,
* security,
* documentation,
* and long-term stability.

Code review is a collaborative engineering activity.

It is not an approval ceremony.

---

# REVIEW PHILOSOPHY

Project BRAHMA follows one fundamental principle:

> **Review the code. Respect the contributor.**

Every review should improve:

* the implementation,
* the architecture,
* the documentation,
* and the engineer.

---

# REVIEW OBJECTIVES

Code review exists to verify:

* correctness,
* architectural consistency,
* readability,
* maintainability,
* security,
* documentation,
* testing,
* long-term sustainability.

---

# REVIEW HIERARCHY

Every review should follow the same order.

```text id="tzk3e8"
Architecture

↓

Documentation

↓

Engineering Standards

↓

Implementation

↓

Testing

↓

Performance

↓

Style
```

Architecture always takes priority over formatting.

---

# ARCHITECTURE REVIEW

Verify that the change:

* respects the Master Architecture,
* follows dependency direction,
* preserves module boundaries,
* introduces no unnecessary coupling,
* avoids architectural shortcuts.

Architecture should never be weakened for convenience.

---

# DOCUMENTATION REVIEW

Confirm that:

* new features are documented,
* READMEs remain accurate,
* important decisions are recorded,
* public interfaces are explained.

Undocumented functionality is considered incomplete.

---

# ENGINEERING STANDARDS REVIEW

Verify compliance with:

* Engineering Standards
* Python Standards
* Documentation Standards
* Security Standards

Engineering discipline should remain consistent throughout the project.

---

# READABILITY REVIEW

Ask:

* Can another engineer understand this code?
* Are names meaningful?
* Is the logic obvious?
* Is unnecessary complexity avoided?

Readable software is preferred over clever software.

---

# RESPONSIBILITY REVIEW

Verify that every module has a clear responsibility.

Avoid:

* God classes
* God functions
* Mixed responsibilities

One module should solve one primary problem.

---

# SECURITY REVIEW

Review for:

* hardcoded secrets,
* unsafe input handling,
* authentication issues,
* authorization issues,
* dependency risks,
* sensitive logging.

Security concerns should be resolved before merging.

---

# TESTING REVIEW

Confirm that:

* appropriate tests exist,
* regression risks are considered,
* existing tests remain valid,
* important workflows are verified.

Testing increases confidence in future development.

---

# PERFORMANCE REVIEW

Consider:

* unnecessary API calls,
* repeated computation,
* excessive memory usage,
* inefficient algorithms.

Optimize only where justified.

Correctness always comes first.

---

# DEPENDENCY REVIEW

Before approving new dependencies verify:

* purpose,
* maintenance,
* security,
* architectural necessity.

Avoid unnecessary external packages.

---

# ERROR HANDLING REVIEW

Confirm that:

* exceptions are handled appropriately,
* meaningful logging exists,
* failures remain understandable,
* silent failures are avoided.

---

# USER EXPERIENCE REVIEW

For UI changes verify:

* clarity,
* consistency,
* accessibility,
* expected behavior.

Engineering includes user experience.

---

# RESEARCH REVIEW

For research-related contributions verify:

* observations remain distinguishable from hypotheses,
* assumptions are documented,
* scientific reasoning is preserved,
* conclusions are reproducible.

Research integrity is a review responsibility.

---

# REVIEW COMMUNICATION

Review comments should be:

* respectful,
* constructive,
* specific,
* technically justified.

Avoid personal criticism.

Discuss the implementation—not the individual.

---

# APPROVAL CRITERIA

A contribution should generally satisfy:

✓ Architecture respected

✓ Documentation updated

✓ Tests completed

✓ Security reviewed

✓ Naming consistent

✓ No unnecessary complexity

✓ Engineering Standards followed

✓ Code understandable

---

# WHEN TO REQUEST CHANGES

Request changes when:

* architecture is violated,
* documentation is missing,
* security risks exist,
* functionality is incorrect,
* code is unnecessarily complex,
* important tests are absent.

Feedback should explain the reasoning.

---

# WHEN TO APPROVE

Approve when:

* engineering quality is acceptable,
* architectural principles are preserved,
* remaining issues are minor,
* documentation is complete,
* implementation improves the project.

Perfection is not required.

Engineering judgment is.

---

# POST-REVIEW RESPONSIBILITY

After approval ensure that:

* comments are resolved,
* documentation remains current,
* Decision Log is updated if required,
* architecture has not unintentionally changed.

---

# WHAT SHOULD NEVER HAPPEN

Code review should never:

* approve known architectural violations,
* ignore security concerns,
* merge undocumented features,
* approve broken functionality,
* become personal criticism,
* prioritize style over architecture.

---

# REVIEW CHECKLIST

Before approving verify:

✓ Architecture preserved

✓ Documentation updated

✓ Standards followed

✓ Tests passed

✓ Security reviewed

✓ Dependencies justified

✓ Logging appropriate

✓ Error handling complete

✓ Readability acceptable

✓ Long-term maintainability improved

---

# CONTINUOUS IMPROVEMENT

Code review itself should evolve.

As Project BRAHMA grows, review practices should improve through:

* documented experience,
* engineering lessons,
* research insights,
* architectural evolution.

---

# FINAL PRINCIPLE

A successful review is not measured by the number of comments.

It is measured by whether the project becomes stronger after the review.

Every approved contribution should leave Project BRAHMA in a better state than before.

---

*"Great engineers write good software.

Great reviews build great engineers."*

**Project BRAHMA**
