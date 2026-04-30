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
- **Commands**:
  - Impact: `codanna mcp analyze_impact --args '{"name": "SymbolName"}' --json`
  - Search: `codanna mcp search_documents --args '{"query": "pattern"}' --json`
  - Calls: `codanna mcp get_calls --args '{"name": "FunctionName"}' --json`
  - Index: `codanna index .` (after structural changes)
- **Trigger**: Before changing any shared function, module, or API boundary.

### L2 — Cognee (Semantic Memory)
- **Purpose**: Retrieve the "Why" — architectural rationale, historical decisions, lessons learned.
- **Commands**:
  - Recall: `uv run python scripts/cognee/recall.py "query here"`
  - Store: `uv run python scripts/cognee/trace.py` (post-task distillation)
  - Sync: `uv run python scripts/cognee/indexer.py` (after refactor)
  - Improve: `uv run python scripts/cognee/improve.py` (graph optimization)
- **Dataset Isolation**: All operations are automatically scoped to the current project dataset.
- **Trigger**: Before refactoring existing logic, after completing any `feat`/`fix` task.

### L3 — Context (Local Docs — Fast)
- **Purpose**: Verify library API syntax using locally installed documentation packages.
- **Commands**:
  - Search: `mcp_context_search_packages(name="<library>", registry="<npm/pip>")`
  - Install: `mcp_context_download_package(name="<library>", registry="<registry>", version="<ver>")`
  - Query: `mcp_context_get_docs(library="<name>@<version>", topic="<method/pattern>")`
- **Trigger**: Before using any external library API. Do not rely on training data syntax.

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
1. `bd ready` — Load current task state.
2. `uv run python scripts/cognee/recall.py "[task description]"` — Load semantic context.
3. `codanna mcp analyze_impact --args '{"name": "[affected symbol]"}' --json` — Map physical impact.
4. `/DocsReview` — If external libraries are involved.
5. Sequential Thinking — Synthesize findings into a plan.
6. `bd create "<task>"` — Register the plan before touching code.

### Post-Task Checklist (Run in order)
1. `uv run python scripts/cognee/trace.py` — Distill lessons.
2. `uv run python scripts/cognee/indexer.py` — Sync codebase to graph.
3. `bd update <id> --status completed` — Close the task.
4. `bd dolt push` + `git push` — Sync state.

---

## Guardrails
- **Never commit inferred code**: If a layer failed and you had to infer, label it `[INFERRED]` and create a verification task.
- **No skipping**: A layer can only be skipped if a tool is confirmed unavailable (MCP error).
- **Silent Mode**: Use the `scripts/cognee/` proxy scripts — never call cognee CLI directly.
- **Local Isolation**: Cognee data lives in `.cognee/` (Git ignored). Never commit the graph.
