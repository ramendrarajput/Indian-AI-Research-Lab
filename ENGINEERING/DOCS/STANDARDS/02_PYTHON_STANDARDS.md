# PROJECT BRAHMA — PYTHON STANDARDS

> *"Programming languages evolve.
> Readable code endures."*

**— Project BRAHMA**

---

# PURPOSE

This document defines the Python engineering standards used throughout Project BRAHMA.

Its objective is to ensure that every Python module developed within the project remains:

* readable,
* maintainable,
* scalable,
* testable,
* production-ready,
* and understandable by future contributors.

Python code should reflect engineering discipline rather than individual coding style.

---

# PHILOSOPHY

Python is currently the primary implementation language of Project BRAHMA.

It is selected because of:

* readability,
* scientific ecosystem,
* AI ecosystem,
* rapid development,
* long-term community support.

However,

Project BRAHMA is **not Python-dependent**.

Python is an implementation language.

Project BRAHMA is an engineering architecture.

---

# PYTHON VERSION

Current supported version:

```text
Python 3.12+
```

Every module should remain compatible with the officially supported project version.

---

# PEP COMPLIANCE

All code should follow:

* PEP 8
* PEP 257
* PEP 484 (Type Hints)

Unless architectural requirements justify an exception.

---

# FILE NAMING

Use lowercase with underscores.

Correct

```text
chat_service.py
image_agent.py
knowledge_graph.py
document_parser.py
```

Avoid

```text
ChatService.py
ImageAgent.py
New File.py
abc.py
```

File names should describe responsibility.

---

# MODULE RESPONSIBILITY

One module.

One responsibility.

Avoid "utility dumping."

Incorrect

```text
utils.py
helper.py
misc.py
common.py
```

Preferred

```text
json_utils.py
image_utils.py
pdf_parser.py
audio_converter.py
```

---

# CLASS NAMING

Use PascalCase.

```python
ResearchAgent

VisionAnalyzer

KnowledgeGraph

FinanceService
```

Classes represent objects or services.

---

# FUNCTION NAMING

Use snake_case.

```python
generate_summary()

load_document()

create_embedding()

process_audio()
```

Function names should describe actions.

---

# VARIABLE NAMING

Variables should describe meaning.

Good

```python
user_question

conversation_history

embedding_vector

research_document
```

Avoid

```python
a

temp

x

abc

data1
```

Meaningful names reduce documentation requirements.

---

# CONSTANTS

Use uppercase.

```python
MAX_RETRIES

DEFAULT_MODEL

API_TIMEOUT

VECTOR_DIMENSION
```

---

# TYPE HINTS

Public functions should use type hints whenever practical.

Example

```python
def search_documents(query: str) -> list[str]:
    ...
```

Type hints improve:

* readability,
* editor support,
* static analysis,
* long-term maintenance.

---

# DOCSTRINGS

Public modules, classes, and functions should contain descriptive docstrings.

Example

```python
def load_pdf(path: str):
    """
    Load a PDF document and return extracted text.
    """
```

Docstrings should explain:

* purpose,
* parameters,
* return values,
* important behavior.

---

# IMPORT STANDARDS

Import order:

```text
Standard Library

↓

Third-party Libraries

↓

Project Modules
```

Example

```python
import os
from pathlib import Path

import streamlit as st
import numpy as np

from ENGINEERING.CORE.ai import chat
```

Avoid wildcard imports.

```python
from module import *
```

---

# FUNCTION DESIGN

Functions should:

* perform one task,
* avoid hidden side effects,
* return predictable results.

Recommended length:

30–50 lines.

Large functions should be decomposed.

---

# CLASS DESIGN

Classes should follow the Single Responsibility Principle.

Avoid "God Classes."

Prefer composition over inheritance whenever possible.

---

# ERROR HANDLING

Never suppress exceptions.

Incorrect

```python
try:
    ...
except:
    pass
```

Preferred

```python
try:
    ...
except Exception as error:
    logger.exception(error)
```

Errors should be:

* logged,
* understandable,
* actionable.

---

# LOGGING

Use the logging framework.

Avoid production use of:

```python
print()
```

Preferred

```python
logger.info()

logger.warning()

logger.error()

logger.exception()
```

Logs should explain events rather than merely announce execution.

---

# COMMENTS

Write comments only when they explain intent.

Avoid comments that describe obvious code.

Bad

```python
# Increment i

i += 1
```

Better

```python
# Retry because the provider may temporarily rate-limit requests.
```

---

# FILE SIZE

Preferred:

300–500 lines.

Files larger than approximately 700 lines should be reviewed for modularization.

---

# DEPENDENCY MANAGEMENT

Project dependencies belong in:

```text
requirements.txt

or

pyproject.toml
```

Avoid unnecessary libraries.

Every dependency should have a documented purpose.

---

# CONFIGURATION

Configuration values should never be hardcoded.

Use:

```text
.env

config/

environment variables
```

---

# PATH MANAGEMENT

Always use:

```python
from pathlib import Path
```

Avoid manually concatenating paths.

Correct

```python
BASE_DIR / "DATA"
```

---

# SECURITY

Never commit:

* API keys
* passwords
* tokens
* credentials

Only commit:

```text
.env.example
```

---

# TESTABILITY

Functions should be deterministic whenever practical.

Avoid tightly coupling logic with UI.

Pure functions are preferred.

---

# PERFORMANCE

Optimize only after measurement.

Avoid:

* premature optimization,
* unnecessary loops,
* repeated API requests,
* repeated file loading.

Cache expensive operations when appropriate.

---

# ASYNCHRONOUS CODE

Use asynchronous programming only when it clearly improves scalability or responsiveness.

Avoid unnecessary complexity.

---

# PROJECT IMPORTS

Always import through the project package.

Correct

```python
from ENGINEERING.CORE.ai import chat
```

Avoid relative imports that depend on execution location.

---

# ENGINEERING PRINCIPLE

Readable code is more valuable than clever code.

Future contributors should understand the purpose of every module without reading its entire implementation.

Python code should communicate intent before implementation.

---

# FINAL PRINCIPLE

Python is the current language.

Engineering is the permanent discipline.

Project BRAHMA values engineers who write software that remains understandable years after it was created.

---

*"Good Python code solves today's problem.

Great Python code remains understandable tomorrow."*

**Project BRAHMA**
