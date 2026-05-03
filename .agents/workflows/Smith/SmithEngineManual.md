---
description: "Smith Engine (Manual) - Semi-autonomous protocol with user approval gates at every critical decision point."
---

# Smith Engine (Manual)
// turbo-all

## Global Objective
Execute the software development cycle with explicit user gating at critical architectural and design decision points. The AI proposes; the user approves. Do not proceed past a GATE without explicit user confirmation.

*This mode is for tasks where architectural impact is unclear, design decisions are subjective, or the user wants full visibility before any code is written.*

---

### Phase 0: Intelligence Load & Research
**Assume Role:** `@memory-manager`
**Mindset:** Zero-guesswork. Use real data only.
**Execution:**
1. **Beads Sync**: Run `bd ready` to load active task state.
2. **Semantic Recall**: Run `uv run python scripts/cognee/recall.py "[task description]"` to retrieve prior architectural context and lessons.
3. **Physical Impact**: Run `uv run scripts/codanna/impact.py [affected symbol]` to map dependencies.
4. **Docs Review**: If external libraries are involved, execute `/DocsReview` (L3 context → L4 context7 fallback).
5. **Sequential Thinking**: Synthesize the above into a structured, multi-step plan with identified risks and ripple effects.
6. **Handoff Summary**: Produce a concise brief for `@brain`.

---

### Phase 1: Propose & Gate — Plan
**Assume Role:** `@brain` (Lead Architect)
**Mindset:** Meticulous, spec-driven. Present facts, not guesses.
**Execution:**
1. **Present the Plan**: State the proposed approach, referencing the `sequentialthinking` output from Phase 0.
2. **Impact Map**: List ALL files that will be changed and WHY.
3. **Risk Register**: Enumerate any breaking changes, DB migrations, or API contract shifts.
4. **Task Registration**: Run `bd create "<main task>"` and `bd create "<subtask>" --parent <id>` for each identified sub-task.
5. **Spec File**: Write the full plan to `docs/track/specs/<bead_id>.md`.

> **🚦 GATE 1**: Present the plan and spec file to the user. Ask: *"Does this plan look correct? Any constraints I should know before I touch code?"* Do NOT proceed until the user confirms.

---

### Phase 2: Design Spec (UI/Visual Tasks Only)
**Assume Role:** `@ui-designer` + `@theme-expert`
**Mindset:** DESIGN.md is the Source of Truth. No hardcoded values.
**Execution:**
1. **Read DESIGN.md**: Identify relevant tokens (colors, spacing, typography, motion).
2. **Token Proposal**: Propose any NEW design tokens needed. Write them to `DESIGN.md` before touching component files.
3. **Atomic Hierarchy**: Confirm which Atomic level the component belongs to (Atom / Molecule / Organism).
4. **Spec Update**: Add the visual spec to `docs/track/specs/<bead_id>.md`.

> **🚦 GATE 2** (UI only): Present the design spec and token changes. Ask: *"Does this visual design align with your intent?"* Do NOT write component code until approved.

---

### Phase 3: Surgical Implementation
**Assume Role:** `@builder` (`@backend` | `@frontend` | `@api-specialist`)
**Mindset:** DRY, SOLID, Surgical edits. No full-file rewrites unless justified.
**Execution:**
1. **Read First**: `view_file` every target file before editing. Never edit from memory.
2. **Surgical Edits**: Use `replace_file_content` or `multi_replace_file_content` for targeted changes.
3. **API Contract** (`@api-specialist`): If crossing the React/Sidecar boundary, verify Pydantic models and `callSidecar` bridge compliance.
4. **UI Hygiene** (`@frontend`): Strictly use tokens from `DESIGN.md`. No hardcoded hex/px.
5. **Notes**: Log complex decisions in `docs/WikiFlow/coder/notes.md`.

---

### Phase 4: Quality Gate
**Assume Role:** `@auditor` (`@lint` → `@test` → `@ui-auditor`)
**Mindset:** Unforgiving. A single failing check blocks the release.
**Execution:**
1. **Lint**: Run `uv run ruff check --fix` (Python) and `bunx biome check --write` (JS/TS). Max 3 fix attempts.
2. **Tests**: Run `uv run pytest` or `bun test`. Max 3 fix attempts. A failing test is a hard stop.
3. **Visual Parity** (UI tasks): Compare implementation against `DESIGN.md`. Verify all states, focus rings, and motion timing.
4. **Audit Report**: Generate a brief pass/fail summary.

> **🚦 GATE 3**: Present the audit report. Ask: *"Quality gate passed. Shall I proceed with memory distillation and commit?"* Do NOT push until approved.

---

### Phase 5: Memory Distillation & Knowledge Sync
**Assume Role:** `@scribe` + `@memory-manager`
**Mindset:** Every task is a lesson. Distill it.
**Execution:**
1. **Cognify**: Run `uv run python scripts/cognee/trace.py` to distill architectural lessons into the graph.
2. **Sync Code**: Run `uv run python scripts/cognee/indexer.py` to update the codebase Knowledge Graph.
3. **Atomic Facts**: Run `bd remember "RULE [feature]: [fact]"` for any high-signal discoveries.
4. **LessonsLearned**: Update `docs/track/LessonsLearned.md` with a brief entry.
5. **Docs**: If new libraries were added or architecture changed, update `Architecture.md` or `README.md`.

---

### Phase 6: Handoff & Version Control
**Assume Role:** `@git` (Release Manager)
**Mindset:** Conventional Commits, traceability, atomic deployments.
**Execution:**
1. **Close Beads**: Run `bd update <id> --status completed` for all sub-tasks and the main bead.
2. **Commit**: Run `git add .` and `git commit -m "feat/fix(<scope>): <description>"`.
3. **Sync Beads**: Run `bd dolt push`.
4. **Push**: Run `git push`.
5. **Handoff**: Update `docs/track/handoff.md` with the current state, active bead ID, and next recommended task.
6. **Final Report**: Print a professional success summary to the user.
