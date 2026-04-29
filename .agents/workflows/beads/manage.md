---
name: Beads Task Management
description: Standard workflow for managing tasks using the Beads (bd) protocol.
---

# Beads Task Management Workflow

This project uses `bd` (Beads) for issue tracking and roadmap management.

## Execution Steps

1. **List Available Work**:
   ```powershell
   bd ready
   ```

2. **Claim a Task**:
   ```powershell
   bd update {{BEAD_ID}} --claim
   ```

3. **Check Task Details**:
   ```powershell
   bd show {{BEAD_ID}}
   ```

4. **Complete Work**:
   Follow the session wrap-up in `AGENTS.md`.
   ```powershell
   bd close {{BEAD_ID}}
   ```

## Best Practices
- Never implement code without a corresponding Bead ID.
- Use `bd remember` for task-specific persistent knowledge.
