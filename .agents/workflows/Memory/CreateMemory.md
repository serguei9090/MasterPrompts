---
name: CreateMemory
description: Workflow for distilling new knowledge into the long-term memory bank.
---

# /CreateMemory Workflow

Use this workflow to persist new architectural decisions, patterns, or lessons learned.

## 🔄 Sequence

### 1. Context Analysis
- Review the current task completion state.
- Identify the core "Why" and "How" of the implementation.
- **Thinking Mode**: Invoke `sequentialthinking` to determine the most appropriate memory category (`decisions`, `entities`, `patterns`, `lessons`, `sessions`).

### 2. Drafting
- Create a new `.md` file in the selected `docs/memory/` subfolder.
- Follow the "AI-Optimized" format:
  - Concise title.
  - Context/Rationale.
  - Implementation details/Bullet points.
  - Related files/TODOs.

### 3. Indexing
- Open `docs/memory/index.md`.
- Append the new memory entry with a brief summary.

### 4. Verification
- Run a grep check to ensure no conflicting memories exist.
- If conflicts are found, pivot to `/ModifyMemory`.
