---
name: UpdateMemory
description: Workflow for replacing an entire memory artifact with a more current version.
---

# /UpdateMemory Workflow

Use this workflow when a memory artifact is completely outdated and needs a full refresh.

## 🔄 Sequence

### 1. Identify Target
- Find the memory file in `docs/memory/` that needs updating.
- Verify its references and dependencies.

### 2. Replace Content
- Overwrite the file with the new distilled knowledge.
- Ensure the header date and context reflect the update.

### 3. Sync Index
- Update the summary in `docs/memory/index.md` if the core meaning has changed.

### 4. Validation
- Use `sequentialthinking` to verify that this update doesn't break architectural continuity documented in other memories.
