---
description: Workflow for initializing Cognee graph-based intelligence in a new or existing project.
---

# 🧠 Cognee Initialization Protocol

> **Assume Role:** `@architect` (System Setup)

This workflow establishes the **Cognee Intelligence Layer** for the project. It ensures that the knowledge graph is safely created without polluting the memory with binary or dependency files.

## Workflow: [Cognee Init]

### 1. [CHECK] - Prerequisites
- Verify that `cognee-cli` is installed via `uv` or pip.
- Verify that `scripts/cognee/indexer.py` exists in the repository. If not, use the `cognee-indexer` skill to generate it.
- Verify that `.cogneeignore` exists in the project root. If not, create a default one (ignoring `.venv`, `node_modules`, `dist`, `.cognee`, etc.).

### 2. [CONFIG] - Environment Setup
- Ensure `.env` contains the correct paths:
  ```env
  COGNEE_SKIP_CONNECTION_TEST=true
  SYSTEM_ROOT_DIRECTORY="./.cognee"
  DATA_ROOT_DIRECTORY="./.cognee"
  ```
- Ensure `.gitignore` includes `.cognee/`.

### 3. [HOOKS] - Continuous Integration
- Ensure `lefthook.yml` has the pre-commit hook configured for `cognee-index`:
  ```yaml
  pre-commit:
    commands:
      cognee-index:
        run: uv run python scripts/cognee/indexer.py {staged_files}
        glob: "*"
        skip: [merge, rebase]
  ```

### 4. [INDEX] - Initial Baseline
// turbo
- Execute the initial graph population (this will automatically create a dataset named after the project folder):
  ```bash
  uv run python scripts/cognee/indexer.py --full
  ```

### 5. [VERIFY] - Status Check
- Review the output of the indexing script.
- Ensure that no `node_modules` or `.venv` files were indexed.
- Output: "Cognee Baseline Initialization Complete for Dataset: [PROJECT_NAME]"
