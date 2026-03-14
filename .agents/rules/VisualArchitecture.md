---
trigger: always_on
description: Mandatory standards for architecture visualization and diagram generation.
---

# Visual Architecture Standards (AVAS)

To shift from cognitive load to visual pattern recognition, all architecture diagrams must follow the Agentic Visual Architecture Standard (AVAS).

## 1. The Visualization Stack (C4 Adaptation)
When asked to "visualize," determine the appropriate level:
- **Level 1 (Context)**: System boundaries and external dependencies.
- **Level 2 (Container)**: Tech stack, deployable units, and network protocols.
- **Level 3 (Component)**: Internal logic, module relationships, and data schemas (ERDs).

## 2. Diagram Generation Rules
- **Golden Rule**: Every diagram must answer "How does data move?" and "Where is the state stored?"
- **Mermaid Syntax**:
  - Orientation: Use `graph TD` (Top-Down) for hierarchy.
  - Grouping: Use `subgraph` to group logical clusters (e.g., `Client_Side`, `Backend_Service`, `Persistence`).
  - Labeling: Every arrow `-->` MUST have explicit text: `A -->|JSON/POST| B`.
- **Shapes**:
  - `[(Database)]` -> Cylinder (Storage)
  - `{{External API}}` -> Hexagon (Cloud/Third-party)
  - `([User/Actor])` -> Rounded Edges
  - `[Process/Service]` -> Rectangle
  - `{Decision/Logic}` -> Diamond

## 3. Structural Analysis Protocol
Before generating a diagram, perform a **Structural Scan**:
1. **Entry Points**: Locate the "Front Door" (e.g., `main.py`, `index.ts`).
2. **State Layer**: Locate the "Truth" (e.g., `models.py`, database migrations).
3. **External Bonds**: Identify dependencies (e.g., `requirements.txt`, `package.json`).

## 4. Post-Diagram Analysis
Every diagram must be followed by:
- **Data Flow**: A 1-sentence summary of the path from user to disk.
- **Risk Assessment**: Identify 1 potential bottleneck or architectural risk.
