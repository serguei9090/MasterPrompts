Assume Role: Orchestra Hub (@scribe)

# 📂 .agents Context

## 🎯 Purpose
The `.agents/` directory is the **Nerve Center** of the framework. It houses the collective intelligence, specialized capabilities, and operational protocols of the AI assistant ecosystem. It is divided into three core layers that work in concert to ensure autonomous and semi-autonomous engineering excellence.

## 🏗️ Architectural Role
**Intelligence & Automation Core**. This folder is the "Backend" of the AI assistant. It provides the logic that allows the AI to understand the project's laws, activate specialized tools, and execute complex workflows.

## 🔑 Sub-Layers & Responsibilities
- **`rules/` (Governance Layer)**: The "Brain." Contains the foundational "Laws of Physics" (Architecture, Quality, Security) that the AI must follow.
- **`skills/` (Capability Layer)**: The "Muscles." Modular extensions that provide the AI with expert-level techniques and domain-specific tools.
- **`workflows/` (Operational Layer)**: The "SOPs." Multi-step blueprints and procedures for executing project lifecycle and development tasks.

## 🛠️ Operational Logic
- **Interaction**: Rules govern Skills, and Workflows orchestrate both to achieve a task.
- **Activation**: The AI constantly references this directory to synchronize its behavior with the project's standards and available tools.
- **Evolution**: This directory is designed for "Self-Evolution," where the AI can create new rules, skills, or workflows to adapt to new requirements.

## 📜 Local Rules & Standards
- **Inter-Layer Dependency**: Every new Skill or Workflow must be verified against the existing Rules.
- **Standard Anatomy**: All content within this folder must follow the standardized templates (e.g., `SKILL.md` format, `Assume Role` headers).

## 🔗 Dependencies
- **Internal**: The absolute source of truth for the AI, dependent on `AGENTS.md` and `GEMINI.md` in the root.
- **External**: Integrates with ecosystem tools like `npx skills`, `google-adk`, and the project's language-specific toolchains (`bun`, `uv`).
