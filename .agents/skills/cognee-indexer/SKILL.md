---
name: cognee-indexer
description: Specialized skill for managing selective codebase indexing using Cognee and .cogneeignore. Use this to prevent knowledge graph pollution and to perform incremental memory updates.
---

# 🧠 Cognee selective Indexer Skill

This skill provides the standard operating procedure for indexing a project's codebase into the Cognee intelligence graph while strictly respecting the `.cogneeignore` and `.gitignore` boundaries.

## 🎯 When to Use
- During initial project setup (`/init` workflow) to establish baseline intelligence.
- When the user asks to "index the project" or "sync memory".
- When you need to force an update of specific files into Cognee.
- When Cognee is crashing due to indexing massive binary directories (like `node_modules` or `.venv`).

## ⚙️ Core Components

1.  **The `.cogneeignore` File**:
    - Always ensure a `.cogneeignore` file exists in the root.
    - It must include standard noisy directories: `node_modules/`, `.venv/`, `__pycache__/`, `dist/`, `build/`.
2.  **The `indexer.py` Script**:
    - Located at `scripts/cognee/indexer.py`.
    - This script automatically uses the **Project Root Folder Name** as the dataset name.
    - It supports a progress bar and error logging controlled by environment variables.

## 🚀 Execution Commands

### 1. Workspace Index
Run this command to walk the workspace and index it into a project-specific dataset:
```bash
uv run python scripts/cognee/indexer.py
```

### 2. Control Log Verbosity
Set `COGNEE_INDEX_LOG_LEVEL` in your `.env` to control the script's output:
- `INFO`: Shows a progress bar based on total files.
- `DEBUG`: Shows progress bar + lists each file being processed.
- `ERROR` (Default): Minimal output, logs errors to file.

## 📂 Error Logging
If any files fail to index, they are listed in:
`scripts/cognee/logs/errors.log`

## 🪝 Continuous Integration (Lefthook)
The repository can use `lefthook` to automatically index staged files.
- **Action**: It runs `uv run python scripts/cognee/indexer.py`, ensuring the knowledge graph stays isolated per project.

## ⚠️ Important Rules
- **NEVER** use `uv run cognee-cli remember .` directly. It bypasses the ignore logic.
- Always use the `scripts/cognee/indexer.py` script as the safe proxy to Cognee.
