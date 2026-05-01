---
description: Init Project Workflow
---

# Init Project Workflow

> **Assume Role:** `@brain` (Lead Architect)
> **Mandatory Skills:** `beads`, `clarify`, `codanna`, `cognee-indexer`, `stitch-design-taste`

This is the **absolute starting point** for any project. It runs the environment installer,
initialises the intelligence stack, then walks the user through every architecture selector
file until every checkbox is resolved. No implementation starts before this workflow completes.

---

## 🏁 Phase 1 — Environment Bootstrap

> The bootstrap scripts handle dependency detection automatically and are idempotent (safe to re-run).

### 1.1 Run the Unified Installer

**Cross-Platform (Python):**
```bash
# Run from the project root — installs all missing tools automatically
python install.py
```

The script installs (if not already present):
- **Dolt** (Beads database engine) via system checks
- **Node.js / npm** (for `bd` CLI) check
- **Beads (`bd`)** via `npm install -g @beads/bd`
- **uv** (Python package manager) via `pip`
- **Lefthook** via `npm install -g @arkweid/lefthook`
- **Codanna** & **Cognee** via `uv add / uv pip install`
- Creates and activates `.venv`, sets up Git Hooks

> [!IMPORTANT]
> The user typically runs `install.py` *before* invoking this workflow. Ensure it has been completed.
> If any tool shows ❌ MISSING, follow the manual fallback instructions printed by the script.

### 1.2 Sync HAL Environment Variables

```powershell
# Windows
./scripts/hal-sync.ps1

# Linux / macOS
source ./scripts/hal-sync.sh
```

Resolves `agents.yaml` variables (`ROOT`, `AGENTS`, `DOCS`, `TRACK`) into the current shell session.

### 1.3 Verify Cognee Initialization

Check if Cognee has been initialized by the user:

```bash
uv run python scripts/cognee/status.py
```

If the status shows that the graph is empty or not initialized, **DO NOT run the indexer yourself**. Instead, instruct the user:
> "Please run `uv run python scripts/cognee/indexer.py --full` in your terminal to build the initial knowledge graph. Let me know when it is complete."

Pause the workflow until the user confirms.

### 1.4 Install Git Hooks

```bash
lefthook install
```

---

## 🔍 Phase 2 — Codebase Scan & Stack Detection

*(This phase is now handled automatically by the `install.py` script. If it detects a framework (e.g. `package.json`, `pyproject.toml`), it will automatically seed the `bd` memory with the runtime details).*

**Action Required**:
Review the terminal output from the installer. If it printed `Stack detected and seeded to Beads memory`, you can skip directly to Phase 3. If it printed `No existing stack detected`, continue to Phase 3 normally.

---

## 📋 Phase 3 — Architecture Selector Questionnaire

> For each selector file below, if it has **no box checked**, ask the user the minimal questions
> to select an option. Once confirmed, check the box and populate the specification section.
> **Do not proceed to Phase 4 until all mandatory selectors are resolved.**

### 3.1 Project Identity *(Mandatory)*
**File**: `docs/architecture/project_summary.md`

Ask the user:
1. "What is the project name and one-sentence mission?"
2. "Who is the primary user and what is their technical level?"
3. "What are the top 3 goals for v1.0?"
4. "What is explicitly OUT of scope for v1.0?"
5. "Are there any hard constraints? (platform, offline requirement, privacy, licensing)"

→ Populate `project_summary.md` with answers.
→ Run: `bd remember "PROJECT: [name] — [mission statement]"`

---

### 3.2 Technology Stack *(Mandatory)*
**File**: `docs/architecture/stack.md`

Ask the user (if not auto-detected in Phase 2):
1. "What is the primary delivery target? (Desktop/Web/CLI/API/Mobile)"
2. "Do you need a Python backend / AI sidecar, or is this frontend-only?"
3. "Do you have a preferred UI library? (shadcn / Mantine / Flutter native / none)"
4. "Is offline-first a requirement? (affects DB choice)"
5. "Do you need AI/LLM integration? If so, local (Ollama) or cloud (Gemini/OpenAI)?"

If user is unsure about a layer, propose the **top 3 options** that fit the answers, e.g.:
> "Based on your choices, I recommend: (1) Tauri v2 + React 19 + shadcn/ui, (2) Next.js 15 + Vercel, or (3) Bun + Hono API + React SPA. Which fits best?"

→ Check the selected boxes in `stack.md`.
→ Run: `bd remember "RUNTIME: [pkg manager based on stack]"`

---

### 3.3 Communication Protocol *(Mandatory)*
**File**: `docs/architecture/communication.md`

Automatically recommend based on `stack.md`:
- Tauri + Python sidecar → **JSON-RPC 2.0 over Tauri IPC** (pre-check this)
- Next.js / web → **REST/HTTP (FastAPI)** or **tRPC** depending on TypeScript stack
- Microservices → **gRPC**

If ambiguous, present the top 2 options with a 1-line rationale and ask user to confirm.

→ Check the selected box in `communication.md`.
→ Populate the bridge hook scaffold.

---

### 3.4 Database *(If backend/sidecar exists)*
**File**: `docs/architecture/database.md`

Auto-recommend based on `stack.md`:
- Tauri + Sidecar → **DuckDB** (embedded, thread-safe, no server)
- Next.js web app → **PostgreSQL + Drizzle** or **Supabase**
- Flutter + local → **SQLite + Drift**

→ Check the selected box.
→ Begin populating the Schema Definitions table (even if empty at init — add placeholders).

---

### 3.5 State Management *(If frontend exists)*
**File**: `docs/architecture/state_management.md`

Auto-recommend based on `stack.md`:
- React → **Zustand** (default recommendation)
- Flutter → **Bloc** (default recommendation)

→ Check the selected box.

---

### 3.6 Diagram Types *(Mandatory — at least Sequence + ERD)*
**File**: `docs/architecture/diagrams.md`

Sequence and ERD are pre-checked by default. Ask user:
- "Does this project have a complex UI state machine? (e.g., multi-step workflow, AI agent loop)"
  → If yes, also check **State Machine Diagram**
- "Is this a system that talks to external services?"
  → If yes, also check **System Context (C4 L1)**
- "Is this an AI agent orchestration system?"
  → If yes, also check **AI Agent Orchestration Diagram**

→ Generate initial draft for each checked diagram using the `diagram-creator` skill.

---

### 3.7 Deployment Target *(Mandatory)*
**File**: `docs/architecture/deployment.md`

Ask the user:
1. "Where does this app run? (User's desktop / Web browser / Cloud server / Mobile / All)"
2. "Do you need a CI/CD pipeline now, or is manual deploy fine for v1.0?"

→ Check selected boxes.
→ If GitHub Actions selected: scaffold `.github/workflows/build.yml` (empty, to be filled).

---

### 3.8 Testing Strategy *(Mandatory)*
**File**: `docs/architecture/testing_strategy.md`

Always check:
- **Unit testing** (pytest for Python / Bun test for JS) — always mandatory
- **Integration testing** if backend exists

Ask:
- "Do you need E2E tests at launch? (adds Playwright or Patrol)"

→ Check selected boxes.

---

### 3.9 DESIGN.md — Visual Identity *(Mandatory for UI projects)*
**File**: `DESIGN.md` (copied from `DESIGN.template.md` in the bundle)

If this is a UI project and `DESIGN.md` has not been customized yet (still contains LogLensAi values):
1. Activate the `stitch-design-taste` skill.
2. Ask user: "What feeling should the UI convey? (e.g., professional dashboard, playful app, minimalist tool)"
3. Generate a new token set and update `DESIGN.md` with project-specific colors, typography, and name.

→ Run: `bd remember "DESIGN: [Project] uses [primary color] / [font] / [aesthetic description]. Source of truth: DESIGN.md"`

---

## 🧠 Phase 4 — Beads Memory Population

After all selectors are resolved, seed the full context into Beads:

```bash
bd remember "STACK: [summary from stack.md]"
bd remember "DATABASE: [selected engine] — schema source: docs/architecture/database.md"
bd remember "COMMUNICATION: [protocol] — methods registry: docs/architecture/communication.md"
bd remember "TESTING: [strategy] — config: docs/architecture/testing_strategy.md"
bd remember "DEPLOYMENT: [target] — config: docs/architecture/deployment.md"
bd remember "DESIGN: [aesthetic] — tokens: DESIGN.md"
bd remember "ARCHITECTURE: Init selectors complete. All docs/architecture/*.md files populated."
```

---

## 📄 Phase 5 — Documentation Scaffolding

1. **Layers Init** — If backend: add first row to `docs/architecture/layers/backend.md` (module table).
   If frontend: add Atom rows to `docs/architecture/layers/frontend.md` (component table).

2. **Distill Init Findings to Cognee**:
   ```bash
   uv run python scripts/cognee/trace.py
   ```

---

## ✅ Phase 6 — Completion Verification

Run this checklist before declaring the project ready:

- [ ] All `docs/architecture/*.md` selector files have at least one box checked
- [ ] `DESIGN.md` has project-specific tokens (not LogLensAi defaults)
- [ ] `bd ready` returns at least the project-identity seed entries
- [ ] `codanna index .` completed without errors
- [ ] `uv run python scripts/cognee/status.py` shows indexed documents
- [ ] `lefthook install` completed (hooks active)
- [ ] `.env` has been created from `.env.example` with real values

### Announce Completion

```
✅ Morphic Framework initialized for [PROJECT NAME].
   Intelligence Stack: Beads ✓ | Codanna ✓ | Cognee ✓ | Lefthook ✓
   Architecture: [STACK_SUMMARY]
   Ready for: /feature, /bugfix, or /startcycle workflows.
```

---

## 🚀 Execution

Run this workflow whenever:
- A repository is cloned fresh
- A completely new project is started
- The framework is installed into an existing project via `install.ps1` / `install.sh`