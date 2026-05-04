## 2026-05-04 - Advanced Calculator Functions
- **Trigonometric Functions**: Successfully integrated math.cos and math.sin into the sidecar. Used 
um1 as the single operand for these unary operations to fit the existing CalculatorRequest schema.
- **UI Consistency**: Maintained existing design patterns using lucide-react icons and glassmorphism.
- **Testing**: Extended existing pytest suite to cover new operations, ensuring regression safety.

# Lessons Learned

## 2026-04-30 - Cognee Indexer: "Nuclear Silence" & Terminal Stability

### 1. The "Nuclear Silence" Protocol
- **Problem**: Third-party libraries (Cognee, Instructor, LiteLLM) leaked initialization, networking, and warning logs to the console even with `LOG_LEVEL=ERROR`, cluttering the user interface and burying progress bars.
- **Solution**: Implemented a **Global Bootstrap** that hijacks `sys.stdout` and `sys.stderr` to a dedicated log file *before* any library imports occur.
- **Key Technique**: Preserve the original terminal streams as `TERM_OUT` and `TERM_ERR` to allow explicit, clean user feedback (progress bars, headers) while suppressing all background noise.

### 2. Windows Terminal Encoding (CP1252 vs. UTF-8)
- **Problem**: Using Unicode box-drawing characters (`â”Œ`, `â”€`, `Â·`, `â†’`) caused `UnicodeEncodeError: 'charmap' codec can't encode...` on default Windows terminal configurations (CP1252).
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

## 2026-04-26 - Project Documentation & Issue Architect Workflows
... (rest of previous content)

