# 🧬 Evolution Layer

This folder documents the **self-improvement and strategic growth** of the Morphic AI Engineering Framework. It captures versioned backlog, orchestration philosophies, and the 4-phase autonomous evolution protocol.

---

## 📂 File Index

| File | Purpose | Referenced By |
|------|---------|---------------|
| [`evolution-strategy.md`](./evolution-strategy.md) | 4-phase deep-execution logic for autonomous framework evolution | Rule: `SelfEvolution.md`, Workflow: `/self-evolve` |
| [`triad-v1.md`](./triad-v1.md) | Default Antigravity → Gemini → Jules orchestration workflow v1.0 | Rule: `AGENTS.md`, Workflow: `/triad-cycle` |
| [`v2_backlog.md`](./v2_backlog.md) | High-level goals for v2.0 upgrade (HAL, Telemetry, Context Optimization) | Beads tracker, `docs/track/` |

---

## 🔄 The 4-Phase Evolution Protocol

The **self-evolution loop** is triggered by the `SelfEvolution.md` and `AgentSelfEvolution.md` rules after any significant task. It follows four phases defined in `evolution-strategy.md`:

```
Phase 1: Contextual Audit  →  Interrogate rules for "baggage"
Phase 2: Architectural Refinement  →  Reduce token friction via grouping
Phase 3: Behavioral Optimization  →  Fine-tune Triad personalities
Phase 4: Capability Expansion  →  Add new skills for emerging domains
```

---

## 🤝 The Triad Orchestration Model

The **Triad** (Antigravity + Gemini CLI + Jules CLI) is the core execution model. Version 1.0 is documented in `triad-v1.md`:

- **Small tasks** (< 3 files / < 200 lines) → Handled locally by **Antigravity** or **Gemini CLI**
- **Large refactors** → Delegated to **Jules CLI** via `jules remote new ... --record`
- See `docs/architecture/triad.md` for the full AVAS-compliant Mermaid diagram

---

## 📋 V2 Backlog Status

`v2_backlog.md` tracks the five phased upgrade goals for the framework. Items map directly to **Beads tasks** (`bd search "IO_001"`, etc.):

| Phase | Label | Focus |
|-------|-------|-------|
| 1 | `IO_*` | Foundation & HAL (Hardware Abstraction Layer) |
| 2 | `MET_*` | Telemetry & Measurement |
| 3 | `OPT_*` | Context Optimization (Lean Machine) |
| 4 | `HO_*` / `AUTO_*` | State Handoff & Autonomy |
| 5 | `GEN_*` | Generative Architecture |

> **AI Prompt**: When reviewing this folder, cross-reference `v2_backlog.md` items with `bd list --status open` to surface backlog items that are already tracked. Do not duplicate.
