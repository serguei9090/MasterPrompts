# Audit: Phase 0 Intelligence Lock (Morphic Framework v0.11.0)

## 📋 Executive Summary
The current "Phase 0" implementation in `SmithEngineAuto.md` requires 4-5 manual script executions. This "manual locking" phase is prone to protocol skips, context fragmentation, and high token overhead. The proposed `intel_lock.py` script successfully consolidates these into a single atomic operation.

## 🔍 Current Workflow Analysis (SmithAuto Step Reference)
| Directive | Script | Status | Complexity |
| :--- | :--- | :--- | :--- |
| **0.1 (L5)** | `bd ready` | Manual | Low |
| **0.1 (L2-S)** | `memory.py recall <ID>` | Manual | Medium |
| **0.2 (L1)** | `impact.py <Symbol>` | Manual | High (AI often guesses symbols) |
| **0.2 (L2-L)** | `recall.py "<query>"` | Manual | Medium |

### Identified Friction Points
1. **Symbol Guessing**: The AI often guesses which symbol to run `impact.py` on, leading to 0 hits and protocol violations.
2. **Context Pollution**: Each script outputs separate blocks of data, requiring the model to synthesize them in its next turn, which is token-expensive.
3. **Short-Term Memory Gaps**: If the model skips `memory.py`, it loses micro-decisions from previous sub-agents/turns.

## 🧪 Proposed "Master Script" (intel_lock.py) Validation
The new script addresses these by:
1. **Operational Intelligence**: Auto-detects the active `bd` task.
2. **Atomic Research**: Pulls both short-term (memory) and long-term (recall) semantic context in one pass.
3. **Intelligent Fallback**: If a symbol impact fails, it automatically triggers a semantic code search.

## 💡 Response to User Questions
- **"Nothing to ask?"**: The script will default to a general roadmap and graph health audit (`cognee status` + `bd list`).
- **"Codanna's different approach?"**: The script abstracts the choice between `impact`, `calls`, and `search`.
- **"Verification vs Context Pollution?"**: By structuring the output as a single JSON/Markdown report, we keep the context dense and high-signal, avoiding redundant metadata.

## 🚀 Recommendation
Proceed with the full implementation of `scripts/intel_lock.py` and update the `SmithEngine` workflows to mandate its use. This will reduce Phase 0 overhead by ~75%.
