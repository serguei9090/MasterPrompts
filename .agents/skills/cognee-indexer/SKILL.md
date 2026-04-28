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
2.  **The `cognee_indexer.py` Script**:
    - Located at `scripts/cognee_indexer.py`.
    - This script automatically uses the **Project Root Folder Name** as the dataset name.
    - It invokes `uv run cognee-cli remember <file> -d <project_name>`.

## 🚀 Execution Commands

### 1. Full Workspace Index (First Time / Rebuild)
Run this command to walk the entire workspace and index it into a project-specific dataset:
```bash
uv run python scripts/cognee_indexer.py --full
```

### 2. Incremental Index (Specific Files)
Run this command to index specific files (e.g., after an AutoCode surgical edit):
```bash
uv run python scripts/cognee_indexer.py path/to/file1.py path/to/file2.ts
```

### 3. Recall Context (Search)
When searching Cognee, always specify the dataset (the project folder name):
```bash
uv run cognee-cli recall "Your query" -d <project_name>
```

## 🪝 Continuous Integration (Lefthook)
The repository uses `lefthook` to automatically index staged files before committing.
- **Action**: It runs `uv run python scripts/cognee_indexer.py {staged_files}`, ensuring the knowledge graph stays isolated per project.

## ⚠️ Important Rules
- **NEVER** use `uv run cognee-cli remember .` directly. It bypasses the ignore logic and will crash the framework.
- Always use the `cognee_indexer.py` script as the safe proxy to Cognee.
