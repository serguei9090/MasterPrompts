# Lessons Learned

## 2026-05-04 - Project Health Audit & Structural Integrity
- **Test Infrastructure Fragility**: Discovered that a single `ImportError` in a test file can block the entire `pytest` collection process, effectively blinding the CI/CD pipeline. Recommendation: Use `ruff check` as a pre-test gate to catch import errors before running the full suite.
- **Async Test Support**: Standard `pytest` does not natively support `async def` tests. Even with `anyio` installed, explicit plugin configuration or decorators (`@pytest.mark.asyncio`) are required. Recommendation: Standardize the test environment with `pytest-asyncio` in `auto` mode.
- **Documentation Drift**: In high-velocity development, architecture docs (`AGENTS.md`) and specs (`Technical_Specification.md`) can quickly diverge from the actual file structure (e.g., `sidecar/src` vs `scripts/`). Recommendation: Periodic automated gap reviews are mandatory to keep the "Source of Truth" synchronized with the "Source of Code."
- **DRY Applied to Docs**: When a project shifts from markdown TODOs to a database-backed tracker like Beads, old markdown references must be aggressively pruned to prevent "Dual Source of Truth" confusion.

## 2026-04-30 - Cognee Indexer: "Nuclear Silence" & Terminal Stability

### 1. The "Nuclear Silence" Protocol
- **Problem**: Third-party libraries (Cognee, Instructor, LiteLLM) leaked initialization, networking, and warning logs to the console even with `LOG_LEVEL=ERROR`, cluttering the user interface and burying progress bars.
- **Solution**: Implemented a **Global Bootstrap** that hijacks `sys.stdout` and `sys.stderr` to a dedicated log file *before* any library imports occur.
- **Key Technique**: Preserve the original terminal streams as `TERM_OUT` and `TERM_ERR` to allow explicit, clean user feedback (progress bars, headers) while suppressing all background noise.

### 2. Windows Terminal Encoding (CP1252 vs. UTF-8)
- **Problem**: Using Unicode box-drawing characters caused `UnicodeEncodeError: 'charmap' codec can't encode...` on default Windows terminal configurations (CP1252).
- **Solution**: Strictly enforce **ASCII-Only Terminal Output** for all decorations (`-`, `|`, `*`, `->`). This ensures the tool is robust across all environments without requiring users to change system locales.

### 3. Graceful Asynchronous Teardown
- **Problem**: Interrupting the indexer (Ctrl+C) left un-awaited coroutines and database locks, causing messy tracebacks.
- **Solution**: Wrapped the main entry point in a standard `try/except KeyboardInterrupt` and used `warnings.filterwarnings` to suppress inevitable library-level teardown warnings that occur during an abrupt exit.

---

## 2026-04-27 - Beads-First & Hybrid Memory Transition

### 1. Architectural Shift
- **Tasks**: 100% migrated to **Beads (bd)**. All roadmaps and issues are now managed via the Dolt database. `TODO.md` is deprecated.
- **Memory**: Implemented a **Hybrid Model**. 
    - Atomic facts (coding rules, file logic) are stored in Beads via `bd remember`.
    - Long-form specifications (ADRs, Diagrams) are stored in `docs/memory/` but **indexed** in Beads with pointers.

### 2. Workflow Consolidation
- **Legacy Removal**: Deleted `AdaptProject.md`, `OnboardingSetup.md`, and `BeadsOnboarding.md`.
- **The `/init` Command**: Created a unified `InitProject.md` that handles infrastructure setup, stack analysis, agent adaptation, and memory population in a single turn.

### 3. Best Practices
- **Never Passive**: Do not use passive markdown mirrors for tasks. If it's not in Beads, it doesn't exist.
- **Index Everything**: Any file created in `docs/memory/` must have a corresponding entry in Beads so future agents can find it via keyword search.

---

## 2026-04-26 - Memory Management & Framework Self-Audit

### 1. Root Cause Analysis
The framework lacked a dedicated mechanism for long-term knowledge retention and architectural continuity across disparate sessions. Autonomous cycles (Smith) could potentially "forget" early design decisions or repeat mistakes documented only in chat history.

### 2. Resolution Strategy
- **Infrastructure**: Implemented a structured `docs/memory/` hierarchy optimized for AI ingestion.
- **Ecosystem**: Created the `@memory-manager` persona and a specialized `memory` skill.
- **Integration**: Deeply integrated memory sync/distillation into the `SmithOrchestra` (Auto/Manual) workflows as mandatory phases (Phase 0 and Phase 7).
- **Thinking Logic**: Integrated `sequentialthinking` MCP as a core reasoning requirement for memory and design tasks.
- **Resilience**: Created a `/SequentialThinkingBackup` workflow and a "Graceful Degradation" rule to handle cases where MCP tools are unavailable.

### 3. Preventative Measures
- **MemoryManagement.md Rule**: Mandates distillation upon completion of any `feat` or `fix` task to ensure the memory bank remains current.
- **Framework Audit**: Conducted an `/ai-framework-audit` to verify implementation quality and identified the need for explicit tool fallback laws.

### 4. Reusable Patterns
- **Memory Hierarchy**: `decisions/`, `entities/`, `patterns/`, `lessons/`, `sessions/`.
- **Graceful Degradation Protocol**: Automatic pivot to backup workflows when specialized tools fail.
- **Phase 0 Retrieval**: Starting every cycle with a memory search to load context before PM analysis.

---

## 2026-05-05 - Windows CLI: Quoting & Argument Splitting

### 1. The `uv run` Quoting Trap
- **Problem**: Passing complex JSON strings containing spaces and internal double-quotes via `uv run` in PowerShell results in `argparse` errors (Unrecognized arguments). The shell/wrapper fails to preserve the quoting boundary, causing the JSON to be shattered into multiple positional arguments.
- **Solution**: Promote **Individual Flag Usage** for critical scripts like `intel_lock.py`. By using `--bead`, `--query`, and `--symbols` directly, the need for complex nested quoting is eliminated, ensuring robust execution across Windows, macOS, and Linux.
- **Best Practice**: Update all "Auto" workflows (e.g., Smith V2) to prefer individual flags over the monolithic `--json` flag for Phase 0 discovery.