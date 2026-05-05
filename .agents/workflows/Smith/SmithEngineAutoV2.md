---
description: "Smith Engine (Auto) V2 - Optimized Intelligence Lock. Executes the entire SDLC using a unified Intelligence Lock (intel_lock.py) for Phase 0."
---

# SmithOrchestra (Auto) V2 - Optimized Autonomous Software Factory
// turbo-all

## Global Objective
Execute a complete, end-to-end software development cycle autonomously. This version uses the unified `intel_lock.py` script to consolidate operational, semantic, and physical discovery into a single atomic pass, including call-site mapping and internal documentation patterns.

---

### Phase 0: The Intelligence Lock (Unified Entry)
**Assume Role:** `@memory-manager`
**Protocol**: This phase is an atomic "Lock". You CANNOT move to Phase 1 until the unified research report is generated. Bypassing L1/L2 for manual `list_dir` is a terminal protocol violation.

> **[DIRECTIVE 0.1]: CONSOLIDATED RESEARCH**
> 1. Execute the unified research script:
>    `uv run python scripts/intel_lock.py --json '{"bead_id": "<ID>", "query": "<TASK_DESCRIPTION>", "symbols": ["<KNOWN_SYMBOLS>"]}'`
> 2. **Process Output**: Read the `INTELLIGENCE LOCK REPORT`. 
>    - Extract `operational_sync_l5` for task status.
>    - Extract `semantic_memory_l2` for rationale and previous micro-decisions.
>    - Extract `physical_truth_l1` for dependency mapping, **call sites**, and **internal patterns**.

**[TRUTH AUDIT 0]**: Did I receive a successful `INTELLIGENCE LOCK REPORT`? If the report flags a failure (e.g., missing index), resolve the underlying issue before proceeding. Summarize key research findings for `@brain`.

---

### Phase 1: Context Discovery & Architecture Plan
**Assume Role:** `@brain` (PM Smith)
**Mindset:** Grounded in consolidated L1/L2 data. Never plan from assumptions.

> **[DIRECTIVE 1.1]: PHYSICAL VERIFICATION (LEAN)**
> *The Phase 0 report already includes impact and call sites. Use this phase only for final visual/line-range verification.*
> 1. **Refinement**: You MAY use `view_file` or `grep_search` to verify line ranges or specific logic found in the report.

> **[DIRECTIVE 1.2]: ARCHITECTURAL ANCHOR**
> 1. `sequentialthinking` (Synthesize plan based on the Intelligence Lock findings.)
> 2. `bd create` (Anchor sub-tasks in the roadmap)
> 3. Write implementation spec to `docs/track/specs/<bead_id>.md`. (*Mandatory: Physically create this file.*)

**[TRUTH AUDIT 1]**: Is the plan grounded in L1/L2 physical reality? Does it follow `Architecture.md`? If YES, proceed to Phase 2.

---

### Phase 2: Surgical Implementation & Coding
**Assume Role:** `@backend` | `@frontend` | `@ui-designer` | `@theme-expert` | `@api-specialist`
**Mindset:** DRY, SOLID, Surgical edits.
**Execution:**
1. **Plan Review:** Read the spec from Phase 1.
2. **Implementation:** Use `replace_file_content` or `multi_replace_file_content`.
3. **Context Checkpoints**: Save micro-decisions: `uv run python scripts/cognee/memory.py add <BEAD_ID> --content "Decision: ..."`.
4. **Notes**: Document complex logic in `docs/WikiFlow/coder/notes.md`. (*Restore: Keep logic documented for human review.*)

---

### Phase 3: Linting & Quality Assurance
**Assume Role:** `@lint`
**Execution:**
1. **Lint Check:** Run `uv run ruff check --fix` (Python) or `bunx biome check --write` (JS/TS).

---

### Phase 4: Empirical Testing
**Assume Role:** `@qa`
**Execution:**
1. **Test Run:** Execute `uv run pytest` or `bun test`. 

---

### Phase 5: Architecture & Quality Audit
**Assume Role:** `@arch-audit`
**Mindset:** Structural verification, AVAS compliance.
**Execution:**
1. **Structural Audit:** Verify implementation against `Architecture.md`.
2. **Health Audit:** Run `/project-audit` to generate `docs/track/audits/project-audit-<DATE>.md`.

---

### Phase 6: Documentation
**Assume Role:** `@doc-agent`
**Execution:**
1. **Dependency Audit**: If new libraries were added, update `Architecture.md` or `README.md`.
2. **Component Registry**: If new UI was built, document it in `docs/Documentation/design/ui-components.md`.
3. **Changelog**: Update `docs/WikiFlow/docs/updates.md`.

---

### Phase 7: Memory Distillation & Handoff Preparation
**Role:** `@memory-manager`
**Actions:**
1. **L2 Semantic Distillation:** Run `uv run python scripts/cognee/trace.py`.
2. **L5 Operational Facts:** Run `bd remember "RULE [Feature]: [Fact]"`.
3. **Audit Documentation:** Update `docs/track/LessonsLearned.md`.
4. **Long-Form Specs**: Update details in `docs/memory/specs/`. (*Restore: Ensure specs are updated for long-term memory.*)

---

### Phase 8: Handoff & State Synchronization
**Assume Role:** `@brain`
**Execution:**
1. **State Update:** `bd update <id> --status completed`.
2. **Resume Update:** Overwrite `docs/track/handoff.md`. Set Status to `Success`. List EXACT file paths under `Actionable Artifacts`. (*Restore: Mandatory for session continuity.*)

---

### Phase 9: Version Control & Sync
**Assume Role:** Git Smith
**Execution:**
1. **Stage & Commit:** `git add .` and `git commit -m "feat/fix: <message>"`.
2. **Sync Beads:** `bd dolt push`.
3. **Remote Sync:** `git push`.
