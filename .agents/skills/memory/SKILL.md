---
name: memory
description: Expert skill for managing the project's long-term memory bank. Use this to record architectural decisions, distilled session context, implementation patterns, and historical lessons in the `docs/memory/` directory.
---

# Memory Management Skill

This skill provides the mechanisms for maintaining a high-signal memory bank to assist AI agents in complex, long-running projects.

## 🎯 When to Use
- **After a Feature/Fix**: Distill the implementation logic and rationale.
- **When a Pattern Emerges**: Record the pattern to ensure future consistency.
- **Architectural Change**: Record the decision (ADR) and the "Why".
- **Pre-Task**: Search memory to avoid repeating mistakes or violating past decisions.

## 🛠️ Key Procedures

### 1. Memory Distillation (`/CreateMemory`)
Identify high-value context from the current session and write it to the appropriate subfolder in `docs/memory/`.
- `decisions/`: ADRs.
- `entities/`: Facts about tools/libs.
- `patterns/`: Code recipes.
- `lessons/`: Bug post-mortems.
- `sessions/`: Context summaries.

### 2. Memory Retrieval
Before starting a major refactor or design phase:
1. Grep `docs/memory/` for relevant keywords.
2. Read the `index.md` for a map of available context.
3. Use `sequentialthinking` to synthesize found memories into the current task plan.

### 3. Index Maintenance
Every time a file is added to `docs/memory/`, the `docs/memory/index.md` MUST be updated to include the new entry.

## 📂 Structure
- `docs/memory/decisions/`
- `docs/memory/entities/`
- `docs/memory/patterns/`
- `docs/memory/lessons/`
- `docs/memory/sessions/`
- `docs/memory/index.md`
