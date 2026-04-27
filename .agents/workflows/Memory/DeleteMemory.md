---
name: DeleteMemory
description: Workflow for archiving or removing stale/incorrect memories.
---

# /DeleteMemory Workflow

Use this workflow to clean up the memory bank. Prefer archiving over permanent deletion.

## 🔄 Sequence

### 1. Verification
- Use `grep` to ensure no active tasks or files depend on this memory.
- **Thinking Mode**: Use `sequentialthinking` to confirm that the memory is truly obsolete or incorrect.

### 2. Archive
- Move the file from its current location to `docs/memory/archive/`.
- Append `[ARCHIVED]` to the filename or add a note inside.

### 3. De-indexing
- Remove the entry from `docs/memory/index.md`.
