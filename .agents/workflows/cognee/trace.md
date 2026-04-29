---
name: Cognee Trace
description: Records an AgentTrace (Lesson Learned) into the permanent Knowledge Graph.
---

# Cognee Trace Workflow

Use this workflow at the end of a task or when a significant technical insight is discovered. This ensures the lesson is preserved for future agents.

## Parameters
- `lesson`: The insight or pattern discovered.
- `category`: (architecture, bug, setup, logic).
- `session`: (Optional) The Bead ID.

## Execution Steps

1. **Record Lesson**:
   ```powershell
   uv run python scripts/cognee/trace.py "Lesson description here" --category "architecture" --session "{{BEAD_ID}}"
   ```

2. **Verify Record**:
   (Optional) Check status to see the new item in the dataset.
   ```powershell
   uv run python scripts/cognee/status.py
   ```

## Best Practices
- Keep lessons concise but descriptive.
- Include the "Why" and "How" in the lesson text.
- This workflow should be part of every session wrap-up.
