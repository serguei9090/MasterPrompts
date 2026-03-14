# Master AI Context: Morphic AI Engineering Framework

Welcome to the Morphic AI Engineering Framework. This workspace is governed by strict architectural and operational standards designed for high-performance software development, AI-agent automation, and 100% progress transparency.

## Core Mandates

1. **Spec-Driven Development**: Always define contracts and interfaces before writing implementations. Follow the Ports & Adapters (Hexagonal) architecture to ensure Separation of Concerns.
2. **Dual-Roadmap Parity**: Ensure that your internal task execution perfectly aligns with the project's human-facing `docs/track/TODO.md`. Keep statuses continuously synced.
3. **Software Excellence**: Strictly adhere to **DRY, KISS, YAGNI, and SOLID** principles. Favor composition over inheritance and pure functions where possible.
4. **TODO(ID) Protocol**: Track every piece of technical debt or missing implementation with a uniquely identified TODO and a dedicated detail file in `docs/TODOC/`.
5. **UI Atomic Design**: Structure frontend components strictly by Atoms, Molecules, Organisms, Templates, and Pages.
6. **Visual Architecture (AVAS)**: Every architecture request must generate a Mermaid.js diagram with subgraphs, labeled arrows, and a post-diagram risk assessment.

## AI Assistant Ecosystem
You are supported by a suite of specialized sub-agents:
- **`@doc-agent`**: Automates documentation updates based on code changes.
- **`@diagram-agent`**: Visualizes architecture and logic paths using Mermaid.js (AVAS compliant).
- **`@lint-agent`**: Enforces code style and documentation consistency.
- **`@reviewer-agent`**: Performs deep architectural audits and code reviews.

## Core Meta-Skills
You are equipped to evolve your own capabilities:
- **`rule-creator`**: Use this skill to create and maintain high-signal architectural and operational rules in `.agents/rules/`.
- **`skill-creator`**: Use this skill to build modular capabilities, workflows, and automated scripts in `.agents/skills/`.

## Initialization & Operational Logic
- **Context Injection**: Before starting a task, read `docs/track/TODO.md` to ensure your internal state matches the workspace.
- **Rules Persistence**: Every request you handle must be evaluated against the files in `.agents/rules/`.
- **Codetographer Mode**: When asked to "map" or "visualize," you must provide a multi-level (C4-style) architectural map.

## Golden Standards
- **Contract -> Interface -> Mock -> Impl**: Never write logic without defining the boundary first.
- **Abstractions over Concretes**: Never hardcode infrastructure inside domain files.
- **100% Transparency**: Never leave silent placeholders. If it's missing, it gets a `TODO(ID)`.
