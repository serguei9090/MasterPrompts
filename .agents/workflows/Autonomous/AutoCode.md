---
description: Surgical Implementation Engine - High-performance edit-lint-test loop for code changes.
---

# 🛠️ Surgical Implementation Engine
> **Assume Role:** `@commander` (The Orchestrator)

This engine is the **canonical implementation factory** for the Morphic framework. It provides a standardized, high-performance loop for applying code changes, validating them, and ensuring documentation parity.

**Usage**: Every workflow that requires source code modification (e.g., `Feature`, `BugFix`, `AutoCycle`) MUST delegate its implementation phase to this engine.

## Workflow: [AutoCode Engine]
Execute the following loop for every task until verified perfect.

### Role Mapping for this Workflow:
- **Planner**: `@pm` (Planning & Requirement Check)
- **Reviewer**: `@critique` (Plan & Final Task Critique)
- **Builder**: `@backend` | `@frontend` | `@ui-designer` | `@theme-expert` | `@api-specialist` (Implementation & UX Audit)
- **Auditor**: `@qa` (Linting & Testing Validation)
- **Architect**: `@architect` (System Evolution & Standards)
- **Releaser**: `@devops` (Git & Atomic Commits)
- **Historian**: `@scribe` (Lessons Learned & Skill Discovery)

---

### 1. [PLAN] - Range Discovery (@pm)
1. **Scan Context**: Scan `bd search` and `.agents/rules/` for context.
2. **Docs Sync**: If libraries/frameworks are involved, execute the `/DocsReview` workflow to verify API syntax.
3. **Graph Impact Analysis**: `uv run python scripts/cognee_memory.py recall "What are the dependencies and call sites for [X]?"` to identify cross-module impacts.
4. **Impact Analysis (Deep Thought)**: Invoke `sequentialthinking` to analyze the recall results, identify all impacted files/functions, and map the dependency ripple effects.
5. **Grep Verification**: Complement graph recall with `grep_search` to verify physical call sites and identify affected line ranges.
6. **Task Breakdown**: Break the work down into actionable **sub-beads** using `bd create "<subtask>" --parent <bead_id>`.
7. **Spec Creation**: Produce a detailed implementation spec in `docs/track/specs/AUTOC-[TASK_ID].md` including the dependency map and subtask list.

### 2. [PLAN-REVIEW] - Critique & Skill Check (@critique)
- **Role**: `@critique`
- **Plan Critique**: Detailed critique of the `[PLAN]` for logic-domain correctness and edge-case handling.
- **Skill Usage Validation**: Evaluate if the proposed skills (or missing ones) fit the task. Mandate usage of relevant skills (e.g., `shadcn`, `mcp-builder`).
- **Approval**: Required to proceed to `[CODE]`.

### 3. [CODE] - Surgical Move (@backend | @frontend | @ui-designer | @theme-expert | @api-specialist)
- **Role**: `@backend` | `@frontend` | `@ui-designer` | `@theme-expert` | `@api-specialist`
- Apply minimalist edits using `replace_file_content` or `multi_replace_file_content`.
- **DRY Constraint**: If logic requires repetitive patterns, flag for `[EVOLVE]`.

### 4. [LINT] - Auto-Fix Standards (@qa)
- **Role**: `@qa`
- **Frontend**: Run `bun x biome check --write <file>`.
- **Backend**: Run `uv run ruff check --fix <file>`.
- Failure = Return to `[PLAN]` to adjust logic for compliance.

### 5. [TEST] - Empirical Validation (@qa)
- **Role**: `@qa`
- **Frontend**: Run `bun test`.
- **Backend**: Run `uv run pytest`.
- Failure = Capture logs, self-debug, and restart loop.

### 6. [UX/UI] - Visual Audit (@frontend)
- **Role**: `@frontend`
- Audit frontend against `docs/Documentation/design/theme.md` and `docs/Documentation/design/ui-components.md`.
- Ensure strict adherence to Atomic Design hierarchy and design tokens.

### 7. [EVOLVE] - Capability Hardening (@architect)
- **Role**: `@architect`
- If a task pattern is repetitive: Identify target for a new **Skill** in `.agents/skills/`.
- Verify architectural alignment with `Architecture.md`.

### 8. [REFLECT] - Knowledge Distillation (@scribe)
- **Role**: `@scribe`
- **Lessons Learned**: Update `docs/track/LessonsLearned.md` and `bd remember` with technical insights gained.
- **Memory Update**: `uv run python scripts/cognee_memory.py remember "Fixed [BUG] by changing [X] in [Y]."` to record the fix rationale.
- **Hybrid Distillation**: Store atomic facts in `bd` and long-form specs in `docs/memory/`.
- **Index Specs**: Run `uv run python scripts/cognee_indexer.py docs/track/specs/AUTOC-[TASK_ID].md` to selectively index the new architectural decisions.
- **Self-Improvement**: `uv run python scripts/cognee_memory.py improve()` to refine graph structures.

### 9. [GIT] - Atomic Commit (@devops)
- **Role**: `@devops`
- Run `git add .`.
- Commit using: `feat(autocode): [task] surgical update & validation`.
- **Re-Cognify Code**: The pre-commit lefthook will automatically trigger `cognee-index` for staged files. If bypassed, run `uv run python scripts/cognee_indexer.py <files>` manually.
- **Beads Update**: Run `bd update <id> --status` and `bd dolt push`.

### 10. [CRITIQUE-FINAL] - Task Double-Check (@critique)
- **Role**: `@critique`
- **Step Critique**: Detailed critique of each loop step (1-9) to identify friction or logic gaps.
- **Role Verification**: Verify if each persona properly executed their responsibilities.

### 11. [VERIFY] - Requirement Check (@pm)
- **Role**: `@pm`
- **3-Iteration Minimum**: The loop MUST execute at least 3 engineering iterations before finalization.
- **Auto-evaluate**: "Does this implementation meet 100% of the Documented LUX/Code requirements?"
- If No (or Iteration < 3): Loop starts back at [PLAN].
- If Yes AND Iteration >= 3: Final Report: "AutoCode Loop Finalized. Task <task> Verified."

### 12. [SELF-IMPROVE] - Workflow Evolution (@architect)
- **Role**: `@architect`
- **Workflow Audit**: Decide if `autocode.md` needs role refinement, new steps, or if a specialized version is required for this specific task domain.
