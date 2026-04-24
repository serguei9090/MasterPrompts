Assume Role: Orchestra Hub (@scribe)

# 📂 .gemini/agents Context

## 🎯 Purpose
This folder contains the **Agentic Persona Layer** of the Morphic framework. It defines the specialized sub-agents that make up the multi-agent ecosystem. Each file represents a domain expert with a focused mission, a specific toolset, and a tailored system prompt. This modular approach allows the orchestrator to delegate complex tasks to specialized agents, maintaining a lean main session and high signal quality.

## 🏗️ Architectural Role
**Sub-Agent Registry & Persona Layer**. This directory provides the configuration and "mental models" for the framework's specialized agents. It defines the boundaries of expertise and the communication protocols for multi-agent collaboration.

## 🔑 Key Sub-Agents & Roles
- **`brain.md`**: The Lead Architect and Product Manager (@brain). Manages the roadmap, system design, and strategic evolution.
- **`qa.md`**: The Quality Assurance specialist (@qa). Responsible for testing, bug reproduction, and quality audits.
- **`api-specialist.md`**: Backend Architect. Focuses on JSON-RPC contracts, data modeling, and server-side logic.
- **`ui-designer.md`**: Frontend UI/UX Architect. Handles atomic design, accessibility, and high-fidelity component logic.
- **`arch-audit.md`**: Structural Auditor. Verifies architectural integrity and ensures compliance with the AVAS standard.
- **`diagram-agent.md`**: Visual Architect. Specialized in generating C4-compliant Mermaid.js diagrams.
- **`reviewer-agent.md`**: Senior Code Reviewer. Performs audits against the plan and coding standards.

## 🛠️ Operational Logic
- **Delegation**: The orchestrator (Gemini CLI) invokes these agents using the `invoke_agent` tool based on the `description` provided in each agent's frontmatter.
- **Tool Isolation**: Agents are granted only the tools necessary for their domain (e.g., `qa` has test runners; `ui-designer` has styling tools).
- **Communication**: Agents communicate through shared state in `docs/track/` and `conductor/`, and via the parent orchestrator's history.

## 📜 Local Rules & Standards
- **Persona Integrity**: Every sub-agent must strictly adhere to its defined focus areas and guidelines.
- **Zero Cross-Talk**: Sub-agents do not call other sub-agents (no recursion) unless explicitly orchestrated by the parent.
- **Evidence-Based**: All sub-agents must provide technical rationale and proof of validation (test results, linter output) for their work.

## 🔗 Dependencies
- **Internal**: Governed by `.agents/rules` and utilizes `.agents/skills`. Orchestrated by `.agents/workflows`.
- **External**: Individual agents may interface with external APIs or CLI tools relevant to their domain (e.g., `npx skills`, `git`, `biome`).
