---
trigger: always_on
description: "Governs the 5-layer Intelligence Stack: how and when to use Sequential Thinking, Codanna, Cognee, Context (local), and Context7 (external)."
---

# Intelligence Stack Protocol (v0.11.0)

This rule defines the mandatory 5-layer Intelligence Stack. Every agent in the Morphic Framework MUST use this stack in order before making any significant implementation decision. Skipping a layer without a confirmed reason is a protocol violation.

## The 5-Layer Stack (Ordered by Priority)

```
L0: Sequential Thinking  →  Plan and reason through ripple effects
L1: Codanna (Physical)   →  Verify real code structure and call sites  
L2: Cognee (Semantic)    →  Retrieve architectural rationale and lessons
L3: Context (Local)      →  Verify library API syntax (offline, fast)
L4: Context7 (External)  →  Fetch latest live documentation
L5: Beads (Operational)  →  Ground truth for task state and history
```

---

## Layer Definitions & Mandatory Commands

### L0 — Sequential Thinking (Planning Engine)
- **Purpose**: Break down complex tasks, identify ripple effects, and map dependencies.
- **Trigger**: MANDATORY before any multi-file refactor, new feature, or architectural change.
- **Fallback**: If unavailable, execute the `/SequentialThinkingBackup` workflow.
- **Law**: The output of Sequential Thinking MUST be anchored in a `bd` task before implementation.

### L1 — Codanna (Physical Truth)
- **Purpose**: Map real, physical code dependencies, call graphs, and symbol locations.
- **Commands** (always use proxy scripts — never raw `--args JSON` directly):
  - Impact: `uv run scripts/codanna/impact.py <SymbolName>`
  - Search: `uv run scripts/codanna/search.py "query" [--context] [--lang X]`
  - Calls: `uv run scripts/codanna/calls.py <SymbolName>`
  - Callers: `uv run scripts/codanna/callers.py <SymbolName>`
  - Doc RAG: `uv run scripts/codanna/docs_search.py "query"`
  - Index: `uv run scripts/codanna/index.py` (after structural changes)
- **Trigger**: Before changing any shared function, module, or API boundary.

### L2 — Cognee (Semantic Memory)
- **Purpose**: Retrieve the "Why" — architectural rationale, historical decisions, lessons learned, and task-specific "Post-it" notes.
- **Commands**:
  - **Thought Memory (Task Context)**: `uv run python scripts/cognee/memory.py recall <BEAD_ID>` (Retrieve micro-decisions for current task)
  - **Checkpoint (Task Note)**: `uv run python scripts/cognee/memory.py add <BEAD_ID> --content "..."` (Save discovery/decision mid-task)
  - **Semantic Recall (Rationale)**: `uv run python scripts/cognee/recall.py "query here"` (Retrieve permanent architectural rationale)
  - **Store (Distillation)**: `uv run python scripts/cognee/trace.py` (Save permanent lessons post-task)
  - **Sync (Ingestion)**: `uv run scripts/cognee/indexer.py` (Index codebase after structural changes)
  - **Prune (Reset)**: `uv run python scripts/cognee/prune.py` (MANUAL ONLY: Hard reset for corrupted ingestion queues. Destructive.)
- **Dataset Isolation**: All operations are automatically scoped to the current project dataset.
- **Trigger**: Before refactoring existing logic, during coding for micro-decisions, and after completing any `feat`/`fix` task.

### L3 — Context (Local Docs — Fast)
- **Purpose**: Verify library API syntax using locally installed documentation packages.
- **Commands**:
  - Search: `mcp_context_search_packages(name="<library>", registry="<npm/pip>")`
  - Install: `mcp_context_download_package(name="<library>", registry="<registry>", version="<ver>")`
  - Query: `mcp_context_get_docs(library="<name>@<version>", topic="<method/pattern>")`
- **Trigger**: Before using any external library API. Do not rely on training data syntax.
- **Note**: Ensure `cognee` is added to the `uv` environment via `uv add cognee` or `uv pip install cognee` to enable these tools.

### L4 — Context7 (External — Live)
- **Purpose**: Fetch real-time, up-to-date library documentation when L3 is insufficient.
- **Commands**:
  - Resolve: `mcp_context7_resolve-library-id(libraryName="<name>", query="<context>")`
  - Query: `mcp_context7_query-docs(libraryId="<id>", query="<specific question>")`
- **Trigger**: When L3 is missing, stale, or the library version is not locally installed.

### L5 — Beads (Operational State)
- **Purpose**: Ground truth for active tasks, roadmap, and session-to-session continuity.
- **Commands**:
  - Load: `bd ready` (start of session)
  - Create: `bd create "<title>" --label "<type>"` (new task)
  - Sub-task: `bd create "<title>" --parent <id>` (breakdown)
  - Update: `bd update <id> --status completed`
  - Remember: `bd remember "RULE [context]: [fact]"` (atomic knowledge)
  - Sync: `bd dolt push` (persist to remote)
- **Trigger**: Before and after every task. No task is started without a `bd` entry.

---

## Mandatory Usage Protocol

### Pre-Task Checklist (Run in order)
1. `bd ready` — Load current task state and identify the active `BEAD_ID`.
2. `uv run python scripts/cognee/memory.py recall <BEAD_ID>` — Retrieve any existing "Thought Memory" (short-term notes) for this task.
3. `uv run scripts/cognee/recall.py "[task description]"` — Load broader semantic context and permanent architectural rationale.
4. `codanna mcp analyze_impact --args '{"name": "[affected symbol]"}' --json` — Map physical impact.
5. `/DocsReview` — If external libraries are involved.
6. Sequential Thinking — Synthesize findings into a plan.
7. `bd create "<task>"` — Register the plan before touching code.

### Post-Task Checklist (Run in order)
1. `uv run scripts/cognee/trace.py` — Distill lessons.
2. `uv run scripts/cognee/indexer.py` — Sync codebase to graph.
3. `bd update <id> --status completed` — Close the task.
4. `bd dolt push` + `git push` — Sync state.

---

## Guardrails
- **Never commit inferred code**: If a layer failed and you had to infer, label it `[INFERRED]` and create a verification task.
- **No skipping**: A layer can only be skipped if a tool is confirmed unavailable (MCP error).
- **Silent Mode**: Use the `scripts/cognee/` proxy scripts — never call cognee CLI directly.
- **No Autonomous Reset**: The `prune.py` (Nuclear Reset) script MUST NEVER be executed by an AI agent autonomously. It is a manual recovery tool only.
- **Local Isolation**: Cognee data lives in `.cognee/` (Git ignored). Never commit the graph.
