# Strategic Evolution Framework v1.0

This document defines the deep-execution logic for the 4-phase self-evolution of the Antigravity framework.

## Phase 1: Contextual Audit (The Critique)
Agents must not just "check" files; they must "interrogate" them.
- **Goal**: Identify instructions that have become "baggage" (no longer applicable due to tech stack changes).
- **Metric**: If a rule was in scope for 10 tasks but never modified or referenced, evaluate its relevance.

## Phase 2: Architectural Refinement (The Bones)
Redesigning the workspace to minimize "Token Friction."
- **Goal**: Group related rules and workflows to reduce the search space for the agent (`list_dir` and `grep`).
- **Standard**: Always maintain the `docs/track/`, `.agents/`, and `.gemini/` hierarchy.

## Phase 3: Behavioral Optimization (The Mind)
Fine-tuning the "Triad Personality."
- **Antigravity**: Strategy and Handoff.
- **Gemini**: Surgical speed and Linting.
- **Jules**: Recursive coding and Test-fix loops.
- **Action**: Update `.gemini/agents/` profiles to reflect specialized "Expert Modes."

## Phase 4: Capability Expansion (The Skills)
Dynamic growth of the toolset.
- **Goal**: Add new `.agents/skills/` based on emerging project domains.
- **Trigger**: Three or more user requests for the same infrastructure task (e.g., "Set up S3 bucket").
