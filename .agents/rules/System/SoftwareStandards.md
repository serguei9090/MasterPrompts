---
trigger: always_on
description: Senior-level software engineering philosophy and language-specific standards.
---

# Global Engineering Philosophy (v0.11.0)

## 1. Core Mandates
- **DRY**: Logic duplication is forbidden. Abstract repeated logic into shared modules.
- **KISS**: Prioritize readability over complex optimizations.
- **YAGNI**: Implement only what is required by the active `bd` task.
- **S.O.L.I.D. Enforcement**:
  - **Single Responsibility**: Modules must have exactly one reason to change.
  - **Open/Closed**: Logic must be extendable without modification.
  - **Dependency Inversion**: Depend strictly on abstractions (Ports), never concretions (Adapters).

## 2. Implementation Mandates
- **Composition**: Favor object composition over inheritance hierarchies.
- **Fail Fast**: Validate state/inputs at entry. Throw descriptive errors immediately.
- **Statelessness**: Prioritize pure functions to ensure testability.
- **Immutability**: Favor immutable structures to eliminate race conditions.

## 3. Language Specializations

### 3.1 Python (uv / ruff)
- **Immutable Globals**: Use `tuple` or `frozenset` for constants.
- **Logging**: Use lazy evaluation (%) for logging templates.
- **Type Safety**: Mandatory type hints for all signatures using `collections.abc`.
- **Default Sentinel**: Use `None` as the sentinel; mutable defaults are forbidden.

### 3.2 JavaScript / TypeScript (bun / biome)
- **Global Scope**: Use `globalThis` instead of `window`.
- **Typing**: Strict types only. `any` is prohibited.
- **React**: Strictly use functional components and hooks.

## 4. Ruthless Pruning
- **Delete, Don't Comment**: Rely on Git for history. Do not leave commented-out code.
- **Immediate Cleanup**: Delete original files immediately after a move or rename.
- **Import Hygiene**: Strip unused imports in every turn. Empty files must be deleted.
