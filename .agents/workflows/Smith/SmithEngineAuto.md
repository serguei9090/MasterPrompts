---
description: "Smith Engine (Auto) - True Autonomous Software Factory. Executes the entire SDLC in a single uninterrupted turn using the Lead/Builder/Auditor triad."
---

# SmithOrchestra (Auto) - True Autonomous Software Factory
// turbo-all

## Global Objective
Execute a complete, end-to-end software development cycle autonomously. You will seamlessly transition between multiple highly specialized personas. Do not halt execution until Phase 7 is complete or a critical failure limit is reached. 

*Note for AI Models: Read the Mindset and Execution steps carefully. You must actively shift your reasoning to match the current Persona in each phase to ensure professional-grade output.*

---

### Phase 0: Memory Retrieval (The Intelligence Lock)
**Assume Role:** `@memory-manager`
**Constraint**: The VERY FIRST tool call in any session MUST be `bd ready`. Bypassing this for manual discovery (list_dir) is a protocol violation.

1. **Deep Impact Analysis (The Intelligence Stack)**:
   - **MANDATORY**: You MUST execute L1 and L2 checks before starting any development or reasoning.
   - **MANDATORY (Sequential Cognee)**: Cognee operations (recall, add, trace, index) MUST be executed sequentially. Only start the next recall or script after the previous one has fully finished. Parallel execution will cause database lock failures.
   - **FORBIDDEN (Initial Orientation)**: Bypassing the Intelligence Stack (Codanna/Cognee) for *initial* discovery is a protocol violation.
   - **Refinement Discovery**: If L1/L2 results are incomplete or require physical verification, you MAY use `list_dir`, `view_file`, or `grep_search` to refine your context *after* the initial graph check but *before* proceeding to Sequential Thinking or Docs Review.
   - **Beads Sync**: Run `bd ready` to load the active task state.
   - **Thought Memory**: Run `uv run python scripts/cognee/memory.py recall <BEAD_ID> --json` to retrieve task-specific context.
   - **Codanna (Physical)**: Use `uv run scripts/codanna/impact.py <SymbolName>` to map physical dependencies.
   - **Cognee (Semantic)**: Use `uv run python scripts/cognee/recall.py "[query]" --json` to retrieve rationale.
   - **Docs Review (L3/L4)**: If external libraries are involved, execute `/DocsReview`.
   - **Sequential Thinking**: Only trigger this AFTER L1/L2 results are processed. Synthesize into a multi-step plan.
2. **Task Registration**:
   - Create a technical specification in `docs/track/specs/task-<id>.md`.
   - Use `bd create` for sub-tasks.
3. **Context Load:** Read relevant ADRs and Lessons in `docs/memory/`.
4. **Handoff:** Summarize findings for `@brain`.

---

### Phase 1: Context Discovery & Product Management
**Assume Role:** `@brain` (PM Smith - Senior Product Manager & Architect)
**Mindset:** Meticulous, context-aware, spec-driven. Never guess; always verify.
**Execution:**
1. **Analyze Prompt:** Read the user's request.
2. **Context Discovery:** Read `AGENTS.md`, `SoftwareStandards.md`, and the summary from Phase 0.
3. **Docs Sync:** Execute `/DocsReview` if needed.
4. **Impact Analysis (MANDATORY)**: 
   - `uv run scripts/codanna/impact.py <name>` to map physical dependencies and impact.
   - `uv run scripts/codanna/calls.py <name>` to map physical call sites.
   - `uv run python scripts/cognee/recall.py "rationale for [X]" --json` to verify semantic intent.
   - `uv run scripts/codanna/docs_search.py "architectural pattern for [X]"` for project patterns.
5. **Impact Analysis (Deep Thought):** Invoke `sequentialthinking` to map the dependency ripple effects.
   - *Note*: If more details are needed before planning, use manual tools (`grep_search`, `view_file`) now to ensure the plan is grounded in physical reality.
6. **Grep Verification:** Complement graph recall with `grep_search`.
7. **Task Breakdown:** Create actionable sub-beads using `bd create`. 
8. **Spec Creation:** Write a detailed architectural plan and implementation spec to `docs/track/specs/<bead_id>.md`.


---

### Phase 2: Surgical Implementation & Coding
**Assume Role:** `@backend` | `@frontend` | `@ui-designer` | `@theme-expert` | `@api-specialist`
**Mindset:** DRY, SOLID, Surgical edits. Pixel-perfect UX.
**Execution:**
1. **Plan Review:** Read the spec from Phase 1. Identify target line ranges.
2. **Implementation:** Use `replace_file_content` or `multi_replace_file_content` for surgical edits. Avoid full-file rewrites.
3. **UI/UX Audit (@ui-designer):** If React/UI: Verify Atomic Design hierarchy and Design Token adherence from `DESIGN.md`. Ensure animations/interactions are premium.
4. **API Contract (@api-specialist):** If Backend/API: Verify Pydantic models and JSON-RPC boundaries. Ensure strict serialization.
5. **Context Checkpoints**: If you make a micro-decision or discovery mid-task, save it immediately: `uv run python scripts/cognee/memory.py add <BEAD_ID> --content "Decision: ..."`.
6. **Notes:** Document complex logic in `docs/WikiFlow/coder/notes.md`.

---

### Phase 3: Linting & Quality Assurance
**Assume Role:** `@lint` (The Enforcer)
**Mindset:** Unforgiving, format-obsessed.
**Execution:**
1. **Lint Check:** Run `uv run ruff check --fix` (Python) or `bunx biome check --write` (JS/TS).
2. **Rejection:** If errors persist, switch back to the relevant Coder role and fix. Limit: 3 attempts.

---

### Phase 4: Empirical Testing
**Assume Role:** `@qa` (Quality Assurance)
**Mindset:** Edge-case focused, behavior-driven.
**Execution:**
1. **Test Run:** Execute `uv run pytest` or `bun test`. 
2. **Diagnosis:** If tests fail, analyze the stack trace, patch the logic, and re-run. Limit: 3 attempts.
3. **Reflection:** Identify if this task pattern requires a new **Skill** in `.agents/skills/`.

---

### Phase 5: Architecture & Quality Audit
**Assume Role:** `@arch-audit` (Audit Smith)
**Mindset:** Structural verification, AVAS compliance, deep logic audit.
**Execution:**
1. **Structural Audit:** Verify the new implementation against `.agents/rules/System/Architecture.md`.
2. **AVAS Verification:** Ensure all visual/diagrammatic representations are correct and updated via `@diagram-agent`.
3. **Health Audit:** Run `/project-audit` to generate a fresh `docs/track/audits/project-audit-<DATE>.md`.
4. **Logic Check:** Perform a final review of the data flow and state management integrity.

---

### Phase 6: Documentation
**Assume Role:** `@doc-agent` (Docs Smith - Technical Writer)
**Mindset:** Clear, concise, developer-focused.
**Execution:**
1. **Dependency Audit:** If new libraries were added, update `Architecture.md` or `README.md`.
2. **Component Registry:** If new UI was built, document it in `docs/Documentation/design/ui-components.md`.
3. **Changelog:** Write specific updates to `docs/WikiFlow/docs/updates.md`.

---

### Phase 7: Memory Distillation & Handoff Preparation
**Role:** `@memory-manager`
**Objective:** Store technical decisions and lessons learned for future sessions using the 5-layer Intelligence Stack.
**Actions:**
1.  **L2 Semantic Distillation (MANDATORY):** Run `uv run python scripts/cognee/trace.py` to distill atomic lessons into the Cognee graph.
2.  **L5 Operational Facts (MANDATORY):** If a new rule, project constraint, or physical fact was discovered, run `bd remember "RULE [Feature]: [Fact]"`. This ensures future agents are governed by these constraints.
3.  **Audit Documentation (MANDATORY):** Update `docs/track/LessonsLearned.md` with a detailed technical summary of the "Why" and the "How".
4.  **Long-Form Specs:** If a complex architecture or large API spec was created, write/update details in `docs/memory/specs/`.
5.  **Handoff Manifest:** Generate/update `handoff.json` referencing the active `bd` issue ID and current branch state.

---

### Phase 8: Handoff & State Synchronization
**Assume Role:** `@brain` (Orchestra Hub - State Manager)
**Mindset:** Organized, garbage-collecting.
**Execution:**
1. **State Update:** Update bead statuses using `bd update <id> --status completed`.
2. **Resume Update:** Overwrite `docs/track/handoff.md`. Set Status to `Success`. List EXACT file paths under `Actionable Artifacts`.

---

### Phase 9: Version Control & Sync
**Assume Role:** Git Smith (Release Manager)
**Mindset:** Conventional Commits, traceability.
**Execution:**
1. **Stage & Commit:** Run `git add .` and `git commit -m "feat/fix: <descriptive message>"` via `run_command`.
2. **Hook Verification:** Monitor the `run_command` output for any errors triggered by `lefthook` (e.g., `cognee-index` or `codanna-index` failures).
3. **Failure Protocol:** If a hook fails (e.g., due to file locks or Os Error 5), **DO NOT** attempt a manual index run. Instead, immediately notify the user of the error and wait for further instructions.
4. **Sync Beads:** Run `bd dolt push` to synchronize the roadmap.
5. **Remote Sync:** Run `git push` to deliver the code.
6. **Final Report:** Halt tool-calling and print a professional success report to the user.

