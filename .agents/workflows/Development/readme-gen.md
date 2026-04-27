---
description: "Proper explanation of the project making proper readme.md file, with information about project how to use and other global standards."
---

# /readme-gen: Project Readme & Explanation Generator
> **Assume Role:** `@docs` (Technical Writer) / `@brain` (Lead Architect)

## Overview
This workflow automates the creation of a high-fidelity `README.md` that serves as the "Source of Truth" for human developers and AI agents alike. It aligns with the Morphic Engineering Framework's standards.

## Workflow

### 1) Deep Research (The Discovery Phase)
- **Scan Filesystem:** Identify the core tech stack (Python, React, Bun, UV, Node, etc.).
- **Read Core Specs:** Extract system mandates from `AGENTS.md`, `GEMINI.md`, and `.agents/rules/`.
- **Roadmap Sync:** Read `docs/track/TODO.md` to understand current progress and next steps.
- **Identify Entry Points:** Locate the main application logic (e.g., `src/`, `sidecar/`, `app/`, `api/`).

### 2) Content Generation
Draft the `README.md` using the following mandatory sections:
- **Project Header:** Premium name, high-signal tagline, and visual badges (if applicable).
- **Core Architecture:** Explain the "Sidecar" pattern, Hexagonal design, or any specific architectural laws in place.
- **The AI Framework:** Document the `@agent` ecosystem, the `.agents/rules/` governance, and the available slash command workflows.
- **Tech Stack Table:** List all major tools (e.g., Bun, UV, DuckDB, Biome, Ruff) with their versions and specific roles.
- **Getting Started (Onboarding):** Provide precise, copy-pasteable steps to clone, install, and run the app locally.
- **Operational Laws:** Mention the `TODO(ID)` protocol, the `Surgical Strike` (AutoCode) workflow, and linting/formatting standards.

### 3) Global Standards Check
- **Premium Aesthetics:** Use standard Markdown with professional formatting, clear hierarchies, and GitHub-style alerts (`> [!NOTE]`, etc.).
- **AVAS Alignment:** Include a Mermaid.js diagram (using the `diagram-creator` skill) if the architecture is complex enough to warrant it.
- **SEO & Searchability:** Ensure all headers are semantic, descriptive, and follow a logical flow (H1 -> H2 -> H3).

### 4) Final Polish & Save
- Run a "Distillation" pass to remove redundant text and ensure "Vibe Coding" clarity.
- Save the file as `README.md` in the project root.
- **Action:** Ask the user: *"The README has been generated and saved to the root. Would you like me to refine any specific section or add a visual architecture diagram via `@diagram-agent`?"*

## Success Criteria
- [ ] Root `README.md` created or updated.
- [ ] Architecture section accurately reflects the actual codebase structure.
- [ ] Onboarding steps are verified against `package.json`, `pyproject.toml`, or `agents.yaml`.
- [ ] AI Rules, Personas, and Workflows are properly categorized and explained.
