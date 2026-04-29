---
name: Cognee Status
description: Checks the health and content of the Cognee memory system.
---

# Cognee Status Workflow

Diagnostics for the memory layer.

## Execution Steps

1. **Check System Health**:
   ```powershell
   uv run python scripts/cognee/status.py
   ```

2. **Manage Pruning (If needed)**:
   If a dataset is stale or needs reset:
   ```powershell
   uv run python scripts/cognee/forget.py --dataset "MasterPrompts"
   ```

## Best Practices
- Run this before starting a major indexing operation.
- Use this to verify that your session context was successfully stored.
