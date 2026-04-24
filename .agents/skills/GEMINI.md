Assume Role: Orchestra Hub (@scribe)

# 📂 .agents/skills Context

## 🎯 Purpose
This folder contains the **Capability Layer** of the framework. It houses modular, domain-specific Agent Skills that provide the AI with specialized knowledge, procedural guidance, and executable tools. These skills act as "force multipliers," enabling the AI to handle complex tasks like high-fidelity design, system debugging, or architectural visualization with expert-level precision.

## 🏗️ Architectural Role
**Capability & Extension Layer**. Skills are the "muscles" of the AI. While the `rules/` folder defines the "Laws of Physics" (the *what*), the `skills/` folder defines the "Technique" (the *how*). They are activated via the `activate_skill` tool to provide localized expertise and specialized workflows.

## 🔑 Key Files & Exports
- **`skill-creator/`**: The meta-skill for building, standardizing, and bootstrapping new capabilities.
- **`find-skills/`**: Integration with the `npx skills` CLI for discovering and installing ecosystem extensions.
- **`adk-expert/`**: Specialized guidance for Google Agent Development Kit (ADK) 2.0 orchestration and graph-based workflows.
- **Domain Skills**: 
    - **Design**: `frontend-design`, `ui-ux-pro-max`, `shadcn`, `tailwind-design-system`.
    - **Logic/Code**: `code-quality`, `systematic-debugging`, `test-driven-development`.
    - **Ops/Workflow**: `executing-plans`, `subagent-driven-development`, `session-handover`.
- **`SKILL.md`**: The mandatory entry point for every skill, containing the triggering description and procedural body.

## 🛠️ Operational Logic
- **Activation**: Skills are activated dynamically when the AI identifies a task that aligns with a skill's `description` in its frontmatter.
- **Priority**: Once activated, a skill's instructions (found in `<activated_skill><instructions>`) take precedence over general system defaults.
- **Standard Anatomy**:
    - `SKILL.md`: Core logic and instructions.
    - `scripts/`: Executable utilities (Python/Bash) used by the skill.
    - `references/`: Deep-dive documentation and patterns.

## 📜 Local Rules & Standards
- **Modular Isolation**: Each skill must be self-contained within its own directory.
- **Trigger Integrity**: The `description` in `SKILL.md` must be high-signal to ensure reliable activation without false positives.
- **Documentation**: All scripts and reference patterns must be idiomatically documented according to the `skill-creator` standard.

## 🔗 Dependencies
- **Internal**: Heavily dependent on `.agents/rules` for foundational standards and `AGENTS.md` for global integration.
- **External**: Utilizes `npx skills` (Skills CLI) for package management and `google-adk` for agent orchestration.
