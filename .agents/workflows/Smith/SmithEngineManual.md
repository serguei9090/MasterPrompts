---
description: "Smith Engine (Manual) - Semi-autonomous protocol with user approval gates at every critical decision point."
---

# Smith Engine (Manual)
// turbo-all

## Global Objective
Execute the software development cycle with explicit user gating at critical architectural and design decision points. The AI proposes; the user approves. Do not proceed past a GATE without explicit user confirmation.

*This mode is for tasks where architectural impact is unclear, design decisions are subjective, or the user wants full visibility before any code is written.*

---

### Phase 0: The Intelligence Lock (Mandatory Entry)
**Assume Role:** `@memory-manager`
**Protocol**: Even in manual mode, this phase is an atomic "Lock". Bypassing L1/L2 for manual discovery is a protocol violation.

> **[DIRECTIVE 0.1]: OPERATIONAL SYNC**
> 1. `bd ready` (Mandatory: Load task state)
> 2. `uv run python scripts/cognee/memory.py recall <BEAD_ID> --json` (Mandatory: Load thought history)

> **[DIRECTIVE 0.2]: INTELLIGENCE DISCOVERY**
> *If the target symbol is unknown, use search.py first. Once identified:*
> 1. `uv run scripts/codanna/impact.py <SymbolName>` (Mandatory: Map physical dependencies. *If 0 symbols are returned, you MUST try at least one alternative related symbol before proceeding.*)
> 2. `uv run python scripts/cognee/recall.py "[query]" --json` (Mandatory: Load architectural rationale)

**[TRUTH AUDIT 0]**: Did I run all L1/L2/L5 commands? If NO, run them now. If YES, summarize findings for `@brain`.

---

### Phase 1: Context Discovery & Refinement
**Assume Role:** `@brain` (PM Smith)
**Mindset:** Grounded in L1/L2 data. Refine with manual tools.

> **[DIRECTIVE 1.1]: PHYSICAL VERIFICATION**
> 1. `uv run scripts/codanna/calls.py <name>` (Mandatory: Map call sites)
> 2. `uv run scripts/codanna/docs_search.py "pattern for [X]"` (Mandatory: Verify local patterns)

> **[DIRECTIVE 1.2]: MANUAL REFINEMENT**
> Now you SHOULD use `view_file` or `grep_search` to verify line ranges or specific logic.

> **[DIRECTIVE 1.3]: ARCHITECTURAL ANCHOR**
> 1. `sequentialthinking` (Synthesize plan based on L1/L2/Physical data. *You MUST physically invoke the tool; synthesizing only in your internal thought block is a violation.*)
> 2. `bd create` (Anchor sub-tasks in the roadmap)
> 3. Write implementation spec to `docs/track/specs/<bead_id>.md`. (*You MUST physically create this file using write_to_file.*)

**[TRUTH AUDIT 1]**: Is the plan grounded in L1/L2 physical reality? Does it follow `Architecture.md`? If YES, proceed to Phase 2.

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
5. **Context Checkpoints**: If you make a micro-decision or discovery mid-task, save it immediately: `uv run python scripts/cognee/memory.py add <BEAD_ID> --content "Decision: ..."`.
6. **Notes**: Log complex decisions in `docs/WikiFlow/coder/notes.md`.

---

### Phase 4: Quality Gate
**Assume Role:** `@auditor` (`@lint` → `@test` → `@ui-auditor`)
**Mindset:** Unforgiving. A single failing check blocks the release.
**Execution:**
1. **Lint**: Run `uv run ruff check --fix` (Python) and `bunx biome check --write` (JS/TS). Max 3 fix attempts. *(Exception: If the binary is missing, document and proceed).*
2. **Tests**: Run `uv run pytest` or `bun test`. Max 3 fix attempts. A failing test is a hard stop.
3. **Visual Parity** (UI tasks): Compare implementation against `DESIGN.md`. Verify all states, focus rings, and motion timing.
4. **Audit Report**: Generate a brief pass/fail summary.

> **🚦 GATE 3**: Present the audit report. Ask: *"Quality gate passed. Shall I proceed with memory distillation and commit?"* Do NOT push until approved.

---

### Phase 5: Memory Distillation & Knowledge Sync
**Assume Role:** `@scribe` + `@memory-manager`
**Mindset:** Every task is a lesson. Distill it across the full Intelligence Stack.
**Execution:**
1.  **L2 Semantic Distillation (MANDATORY):** Run `uv run python scripts/cognee/trace.py` to distill architectural lessons into the graph.
2.  **L5 Operational Facts (MANDATORY):** Run `bd remember "RULE [feature]: [fact]"` for any high-signal discoveries or new constraints.
3.  **Audit Documentation (MANDATORY):** Update `docs/track/LessonsLearned.md` with a brief entry describing the changes and logic.
4.  **Physical Documentation:** If new libraries were added or architecture changed, update `Architecture.md` or `README.md`.
5.  **Long-Form Specs:** If a complex architecture or large API spec was created, write/update details in `docs/memory/specs/`.

---

### Phase 6: Handoff & Version Control
**Assume Role:** `@git` (Release Manager)
**Mindset:** Conventional Commits, traceability, atomic deployments.
**Execution:**
1. **Close Beads**: Run `bd update <id> --status completed` for all sub-tasks and the main bead.
2. **Commit**: Run `git add .` and `git commit -m "feat/fix(<scope>): <description>"`.
3. **Hook Verification**: Monitor output for errors from `lefthook` (e.g., `cognee-index` or `codanna-index` failures).
4. **Failure Protocol**: If a hook fails (e.g., due to file locks or Os Error 5), **DO NOT** attempt a manual index run. Instead, immediately notify the user of the error and wait for further instructions.
5. **Sync Beads**: Run `bd dolt push`.
6. **Push**: Run `git push`.
7. **Handoff**: Update `docs/track/handoff.md` with current state and active bead ID.
8. **Final Report**: Print a professional success summary to the user.

