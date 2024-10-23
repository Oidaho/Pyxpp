---
name: New issue
about: A task template that contains everything you need to complete the task within
  this repository.
title: New task
labels: ''
assignees: ''

---

### Recommendations for the task completion process
  - Use [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) for a quick code editor
  - Create a separate branch to work on your task
  - When naming commits, specify the issue id to which it belongs: `Added some files (#1)`
  - Before creating a PR, make sure that all the `pytest` tests for your task pass
  - When creating a PR, assign @Oidaho as a reviewer
  
### {Short Task description}

{Broad task description}

**Target file:** `project/file/path/here.py`
**Target function\class:** `some_function`

#### List of implementation tasks:
  - make smt
  - paint walls
  - eat pizza

### Testing information

**Tests startup command:** `pytest -k ClassName`
**Tests count:** `5`
