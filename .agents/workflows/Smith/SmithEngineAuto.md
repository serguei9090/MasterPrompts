---
description: "Smith Engine (Auto) - True Autonomous Software Factory. Executes the entire SDLC in a single uninterrupted turn using the Lead/Builder/Auditor triad."
---

# Smith Engine (Auto)
// turbo-all

## Global Objective
Execute a complete, end-to-end software development cycle autonomously. Do not halt execution until Phase 5 is complete.

### Phase 0: Memory Retrieval & Research
**Assume Role:** `@lead`
1. **Intelligence Sync**: Run `bd ready` and `bd prime` to load active roadmap context.
2. **Impact Analysis (Physical)**: Run `codanna mcp analyze_impact` to map symbols and call sites.
3. **Semantic Recall (Semantic)**: Run `uv run python scripts/cognee_memory.py recall` to retrieve rationale.
4. **Planning**: Use `sequentialthinking` to synthesize research into a multi-step execution plan, identifying "ripple effects" and risks.
5. **Register**: Use `bd create` to register the roadmap and sub-tasks.

### Phase 1: Design-First Governance
**Assume Role:** `@lead` | `@ui-designer`
1. **UI Detection**: identify visual components or layout shifts.
2. **DESIGN.md Update**: Update `DESIGN.md` tokens and Atomic hierarchy BEFORE any code is written. **Hardcoded hex values are strictly forbidden.**

### Phase 2: Surgical Implementation & Coding
**Assume Role:** `@builder`
1. **Implementation**: Use `replace_file_content` for surgical edits. strictly adhere to the tokens and components defined in `DESIGN.md`.
2. **Atomic Integrity**: Verify that all components follow the Atoms -> Molecules -> Organisms hierarchy.
3. **Bridge Compliance**: Ensure all cross-layer communication uses the `callSidecar` protocol.

### Phase 3: Quality Gate & Visual Audit
**Assume Role:** `@auditor`
1. **Linting**: Run `uv run ruff check --fix` and `bunx biome check --write`.
2. **Empirical Proof**: Execute `uv run pytest` or `bun test`. Fix failures recursively (max 3 attempts).
3. **Visual Parity Audit**: Compare implementation against `DESIGN.md`. Verify states, transitions, and focus markers.

### Phase 4: Knowledge Distillation
**Assume Role:** `@lead` | `@scribe`
1. **Cognify**: Run `uv run python scripts/cognee_memory.py remember` to distill atomic lessons.
2. **Atomic Facts**: Run `bd remember` for high-signal rules or environment gotchas.
3. **Architecture Update**: Update `Architecture.md` boundaries if boundaries changed.

### Phase 5: Handoff & Version Control
**Assume Role:** `@lead`
1. **Sync**: Update bead statuses using `bd update <id> --status completed`.
2. **Release**: Stage, commit (Conventional Commits), and `git push`.
