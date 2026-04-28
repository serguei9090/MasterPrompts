---
description: "SmithOrchestra (Auto) - True Autonomous Software Factory. Executes the entire SDLC in a single uninterrupted turn."
---
# SmithOrchestra (Auto) - True Autonomous Software Factory
// turbo-all

## Global Objective
Execute a complete, end-to-end software development cycle autonomously. You will seamlessly transition between multiple highly specialized personas. Do not halt execution until Phase 7 is complete or a critical failure limit is reached. 

*Note for AI Models: Read the Mindset and Execution steps carefully. You must actively shift your reasoning to match the current Persona in each phase to ensure professional-grade output.*

---

### Phase 0: Memory Retrieval
**Assume Role:** `@memory-manager`
**Mindset:** Focused on historical context and architectural continuity.
**Execution:**
1. **Search Beads:** `bd search <keywords>` or `bd prime` to load active context.
2. **Search Archive:** Grep `docs/memory/` for architectural depth.
3. **Context Load:** Read relevant ADRs (`decisions/`) and Lessons (`lessons/`).
4. **Handoff:** Summarize findings for `@brain`.

---

### Phase 1: Context Discovery & Product Management
**Assume Role:** `@brain` (PM Smith - Senior Product Manager & Architect)
**Mindset:** Meticulous, context-aware, spec-driven. Never guess; always verify the existing architecture.
**Execution:**
1. **Analyze Prompt:** Read the user's request.
2. **Context Discovery:** Read `AGENTS.md`, `SoftwareStandards.md`, and the summary from Phase 0.
3. **Docs Sync:** If libraries/frameworks are involved, execute the `/DocsReview` workflow to verify API syntax.
4. **Deep Thinking:** Invoke `sequentialthinking` to analyze requirements, identify potential pitfalls, and design the solution architecture.
5. **Spec Creation:** Write a detailed architectural plan and implementation spec to `docs/track/specs/<bead_id>.md`.
6. **Task Update:** Break the work down into actionable beads using `bd create`. Link them to the main task.

---

### Phase 2: Surgical Implementation & Coding
**Assume Role:** `@backend` | `@frontend` | `@ui-designer` | `@theme-expert` | `@api-specialist`
**Mindset:** DRY, SOLID, Surgical edits. Pixel-perfect UX.
**Execution:**
1. **Plan Review:** Read the spec from Phase 1. Identify target line ranges.
2. **Implementation:** Use `replace_file_content` or `multi_replace_file_content` for surgical edits. Avoid full-file rewrites.
3. **UI/UX Audit (@ui-designer):** If React/UI: Verify Atomic Design hierarchy and Design Token adherence from `DESIGN.md`. Ensure animations/interactions are premium.
4. **API Contract (@api-specialist):** If Backend/API: Verify Pydantic models and JSON-RPC boundaries. Ensure strict serialization.
5. **Notes:** Document complex logic in `docs/WikiFlow/coder/notes.md`.

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
**Objective:** Store technical decisions and lessons learned for future sessions using the Hybrid Memory Architecture.
**Actions:**
1.  **Atomic Facts (Beads):** If a new rule or brief fact was discovered (e.g., "Use `globalThis` over `window`"), run `bd remember "RULE [Feature]: [Fact]"`.
2.  **Long-Form Specs (Markdown):** If a complex architecture or large API spec was created, write the details to a file in `docs/memory/` (e.g., `docs/memory/specs/feature_x.md`).
3.  **Cross-Linking:** If a long-form spec was written, you MUST index it in Beads: `bd remember "ARCHITECTURE [Feature]: The full spec is located at docs/memory/specs/feature_x.md"`.
4.  **Handoff Manifest:** Generate/update `handoff.json` referencing the active `bd` issue ID and current branch state.

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
2. **Sync Beads:** Run `bd dolt push` to synchronize the roadmap.
3. **Final Report:** Halt tool-calling and print a professional success report to the user.
