---
trigger: always_on
description: Mandatory standards for implementation hygiene, documentation, and session continuity.
---

# Code Quality & Operational Hygiene (v0.11.0)

## 1. MANDATORY: The Skill Trigger Matrix
Use these elite skills at specific SDLC phases without exception:
| Phase | Mandatory Skill | Trigger |
| :--- | :--- | :--- |
| **Discovery** | `codanna`, `cognee` | Use `codanna` for impact analysis; `cognee` for rationale retrieval. |
| **Planning** | `beads`, `diagram-creator` | Use `bd` for tasking; `diagram-creator` for AVAS maps. |
| **Styling** | `design-taste-frontend` | Initialize EVERY new UI component with this foundation. |
| **Motion** | `animate`, `overdrive` | Use for interactive states, transitions, and scroll reveals. |
| **Final Pass** | `polish`, `audit` | MANDATORY before any `bd close`. Fix alignment/a11y/perf. |

## 2. Session Boot Sequence (Imperative)
1. **Sync Roadmap**: Run `bd ready` immediately. No exceptions.
2. **Review Handoff**: Read `docs/track/handoff.md` to identify the last active state.
3. **Calibrate**: Synthesize all research into a `sequentialthinking` plan before typing code.

## 3. Zero-Guesswork Documentation
- **Rationale Law**: Comments MUST explain the "Why," not the "What."
- **Document-on-Change**: Any structural modification REQUIRES an update to `docs/Documentation/architecture/` in the same turn.
- **Contract Mandate**: Mandatory JSDoc (TS/JS) and Google-style Docstrings (Python) for all public members.

## 4. Beads Protocol (Task Memory)
- **Authority**: `bd` is the exclusive source of truth for task status.
- **Syntax**: `// TODO(bead_id): [WHAT] ... [WHY] ... [EXPECTATION]`
- **Lifecycle**: Create via `bd create`. Start implementation ONLY with a spec in `docs/track/specs/`. Close via `bd close`.

## 5. UI/UX & Atomic Governance
- **Source of Truth**: `DESIGN.md` tokens are absolute. Hardcoded hex/px values trigger a REJECT.
- **Atomic Hierarchy**: 
  - **Atoms**: Pure, stateless UI (Buttons, Inputs).
  - **Molecules**: Combined atoms (SearchField).
  - **Organisms**: Data-bound blocks (Sidebar, Header).
- **Technical Constraints**:
  - **Hooks**: Pure UI logic only in shared hooks. Business logic MUST stay in the app layer.
  - **Motion**: Standard durations: `fast` (100ms), `normal` (200ms), `slow` (300ms).
  - **Accessibility**: Mandatory focus rings and `aria-label` for all interactive elements.
- **Visual Parity Audit**: `@auditor` MUST scan for token compliance and motion semantic alignment. Only 100% parity allows a PASS.

## 6. Distillation & Intelligence Sync
- **Intelligence Stack**: Utilize the 5-layer stack (Thinking, Codanna, Cognee, Context, Beads).
- **Distillation Mandate**: Run the `/cognee:trace` workflow upon task completion to record lessons.
- **Physical Sync**: Run `codanna index .` and the `/cognee:index` workflow after any structural refactor.
