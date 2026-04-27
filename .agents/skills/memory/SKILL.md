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

## 🧠 The Hybrid Division of Labor

The project uses a Hybrid Memory Architecture to maximize speed and detail.

### 1. Beads (`bd`) - The Index & RAM
Beads is the single source of truth for **active tasks** and **atomic facts**. 
*   **Tasks & Issues:** Managed via `bd create`, `bd ready`.
*   **Atomic Facts:** Managed via `bd remember`. Use this for coding rules, file locations, and short tech stack constraints.
*   **Indexing:** If you write a long-form spec in `docs/memory/`, you MUST create a pointer in Beads so the next agent can find it: `bd remember "ARCHITECTURE [Feature X]: Full spec is at docs/memory/specs/x.md"`

### 2. `docs/memory/` - The Long-Form Hard Drive
Use this directory for large, formatted documentation that is too complex for a single database string.
*   **`docs/memory/architecture/`**: For Mermaid diagrams and system maps.
*   **`docs/memory/specs/`**: For deep API payloads, component trees, and DB schemas.
*   **`docs/memory/lessons/`**: For post-mortems and workflow adjustments.

### 2. Long-term Archive (`docs/memory/`)
For deep architectural decisions and stable patterns, continue to use the structured archive in `docs/memory/`.
- `decisions/`: ADRs.
- `entities/`: Facts about tools/libs.
- `patterns/`: Code recipes.
- `lessons/`: Bug post-mortems.

### 3. Memory Retrieval
Before starting any turn:
1. **Search Beads**: `bd search <keywords>` or `bd prime` to load active context.
2. **Scan Archive**: Grep `docs/memory/` for historical depth.
3. **Synthesis**: Use `sequentialthinking` to merge active beads with archived specs.


### 3. Index Maintenance
Every time a file is added to `docs/memory/`, the `docs/memory/index.md` MUST be updated to include the new entry.

## 📂 Structure
- `docs/memory/decisions/`
- `docs/memory/entities/`
- `docs/memory/patterns/`
- `docs/memory/lessons/`
- `docs/memory/sessions/`
- `docs/memory/index.md`
