---
name: Cognee Index
description: Performs a full workspace indexing using Cognee's temporal/incremental engine.
---

# Cognee Workspace Indexing Workflow

This workflow ensures the entire codebase is indexed into the Cognee Knowledge Graph. It uses the `temporal_cognify` engine to track changes over time.

## Prerequisites
- `uv` installed and configured.
- `cognee` package installed.

## Execution Steps

1. **Verify Environment**:
   Ensure `.cogneeignore` or `.git` exists in the root.

2. **Run Indexer**:
   Execute the root-aware indexer script.
   ```powershell
   uv run python scripts/cognee/indexer.py
   ```

3. **Verify Status**:
   Check if the dataset was created and items processed.
   ```powershell
   uv run python scripts/cognee/status.py
   ```

## Best Practices
- Run this workflow after significant refactors.
- Use `lefthook` to automate this on every git commit for "Always-Synced" memory.
