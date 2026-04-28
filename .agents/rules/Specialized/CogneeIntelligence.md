# Cognee Intelligence: Memory Operations Standard (v1.0)

This rule governs the use of **Cognee** as the framework's persistent, graph-based intelligence layer. It replaces manual context tracking with autonomous relationship mapping.

## 🧠 Core Operations (The Intelligence Primitives)

| Operation | Command | Purpose |
| :--- | :--- | :--- |
| **Store** | `uv run python scripts/cognee_memory.py remember "Fact"` | Commit atomic fact to the graph. |
| **Retrieve** | `uv run python scripts/cognee_memory.py recall "Query"` | Search for context using NL. |
| **Refine** | `uv run python scripts/cognee_memory.py improve` | Run graph optimization pass. |
| **Prune** | `uv run python scripts/cognee_memory.py forget "Fact"` | Remove stale data from the graph. |
| **Index (Full)** | `uv run python scripts/cognee_indexer.py --full` | Safe, ignore-aware full-project index. |

## 🛠️ Mandatory Intelligence Hooks

### 1. Dataset Isolation (The Project Boundary)
All Cognee operations MUST be isolated by dataset.
- **Dataset Name**: Always use the project root folder name (e.g., `MasterPrompts`).
- **Automation**: The `scripts/cognee_indexer.py` handles this automatically for ingestion.

### 2. The Planning Phase (Proactive Recall)
Before starting any implementation (especially refactors), the Agent MUST:
-   **Recall Impact**: `uv run python scripts/cognee_memory.py recall "What are the dependencies of function/module [X]?"`
-   **Recall Rationale**: `uv run python scripts/cognee_memory.py recall "What is the architectural rationale for [X]?"`
-   **Result**: Incorporate the graph insights into the implementation plan.

### 3. The Development Phase (Active Memory)
-   If a complex design decision is made, "mark" it for the post-task reflection.
-   Use `remember` via the proxy script for short, atomic facts discovered during debugging.

### 4. The Completion Phase (Final Enrichment)
Immediately after a successful `git push`:
-   **Remember Lessons**: `uv run python scripts/cognee_memory.py remember "Learned that [X] requires [Y] because of [Z]"`
-   **Codify Code**: Run `uv run python scripts/cognee_indexer.py <staged_files>` (Lefthook handles this automatically on commit).
-   **Improve**: Trigger a `uv run python scripts/cognee_memory.py improve` pass to refine retrieval structures.

## 🛡️ Guardrails
-   **Intelligence Proxy**: Always prefer using `scripts/cognee_memory.py` over raw `cognee-cli` to ensure project-dataset isolation and clean, log-free output.
-   **Dataset Isolation**: All operations MUST target the current project dataset (automatically handled by the proxy script).
-   **Silent Mode**: Use the proxy script to avoid terminal clutter from internal Cognee logs.
-   **No Duplication**: Cognee handles deduplication; do not worry about overlapping `remember` calls.
-   **Source of Truth**: The codebase (`src/`) and formal specs (`docs/`) are the "Ground Truth." Cognee is the "Semantic Map."
-   **Local Isolation**: All Cognee data stays in `.cognee/` (Git ignored). Never commit the graph.
