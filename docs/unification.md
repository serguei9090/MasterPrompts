# Spec: Intelligence Lock Unification (Phase 0 Master Script)

## 🎯 Objective
Simplify the mandatory "Phase 0" research process by consolidating multiple tool calls into a single, high-signal master script: `scripts/intel_lock.py`.

## 🛠️ Architecture
The script will act as an orchestrator for the following intelligence layers:
1. **L5 (Operational)**: `beads` status and task discovery.
2. **L2 (Semantic)**: `cognee` memory recall (short-term & long-term).
3. **L1 (Physical)**: `codanna` impact analysis and search.

### Input Schema (JSON)
```json
{
  "bead_id": "string (optional)",
  "query": "string (optional)",
  "symbols": ["list", "of", "symbols", "(optional)"],
  "depth": "int (optional, default: 3)",
  "force_search": "bool (optional, default: false)"
}
```

## 📋 Implementation Plan

### 1. Operation: `scripts/intel_lock.py`
- **L5 Integration**: If `bead_id` is missing, run `bd ready` to identify the most likely task.
- **L2 Integration**: 
    - Always attempt `cognee memory recall` for the `bead_id`.
    - Run `cognee recall` using the `query` or the `bead_id` title.
- **L1 Integration**:
    - For each symbol in `symbols`, run `codanna impact`.
    - If `symbols` is empty or `impact` returns 0 hits, run `codanna search` using the `query`.
- **Output Formatting**:
    - Provide a structured Markdown report designed for AI consumption.
    - Include "Actionable Files" section for Phase 1 verification.

### 2. Handling Edge Cases
- **"Nothing to ask"**: If query/symbols are missing, default to a "System Health & Roadmap" audit (Status of indices, active beads, high-level project structure).
- **Codanna Approach**: The script will automatically branch between `impact` (precise) and `search` (discovery) based on confidence/hit-rate.
- **Verification Support**: Optionally include `calls` and `docs_search` results if a `--verify` flag is passed.

### 3. Workflow Update
- Update `SmithEngineAuto.md` and `SmithEngineManual.md` to replace the 4-step manual lock with:
  > `uv run python scripts/intel_lock.py --json '{"bead_id": "...", "query": "..."}'`

## 📅 Timeline
1. **Draft Script**: Create `scripts/intel_lock.py`.
2. **Validation**: Test with active beads.
3. **Docs Sync**: Update `DESIGN.md` and `Architecture.md` to reflect the new L1-L5 entry point.
4. **Final Release**: Commit and push.
