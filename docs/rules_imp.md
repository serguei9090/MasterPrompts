# Rules Audit and Just-In-Time Context Plan

This document outlines the audit of all existing rules in `.agents/rules/` and maps them to appropriate Just-In-Time (JIT) triggers (`always_on`, `glob`, `model_decision`, `manual`), according to the `rule-creator` SKILL guidelines. 

Currently, many rules are either missing frontmatter or are set to `always_on`, which pollutes the active context. This plan resolves that by surgically loading rules only when needed.

## 1. `always_on` (Core Directives)
These rules are the unshakeable "Laws of Physics" for the framework. They must be active on every prompt.
- `.agents/rules/System/NoGuesswork.md`
- `.agents/rules/System/SoftwareStandards.md`
- `.agents/rules/System/CodeQuality.md`
- `.agents/rules/Automation/BootSequence.md`
- `.agents/rules/System/HAL_Interoperability.md`
- `.agents/rules/System/IntelligenceStack.md`

## 2. `glob` (File-System Bound)
These rules only trigger when specific file patterns are within the active context or being modified.
- **`.agents/rules/Testing/TestingStandard.md`** -> `globs: ["tests/**", "*.test.*", "*.spec.*"]`
- **`.agents/rules/Testing/ProtocolRetrofittingStandard.md`** -> `globs: ["tests/**", "*.test.*"]`
- **`.agents/rules/Architecture/ApiStandards.md`** -> `globs: ["src/api/**", "routes/**", "controllers/**"]`
- **`.agents/rules/Architecture/DatabaseStandard.md`** -> `globs: ["schema.prisma", "drizzle/**", "db/**", "models/**", "*.sql"]`
- **`.agents/rules/Architecture/DiagramStandard.md`** -> `globs: ["*.md", "*.mermaid", "*.mmd"]`
- **`.agents/rules/CICD/CiCdStandard.md`** -> `globs: [".github/workflows/**", "lefthook.yml", ".gitlab-ci.yml"]`
- **`.agents/rules/CICD/CICDToolsStandard.md`** -> `globs: [".github/workflows/**", "lefthook.yml"]`
- **`.agents/rules/Internationalization/i18nStandard.md`** -> `globs: ["locales/**", "i18n/**", "*.json"]`
- **`.agents/rules/StateManagement/StateManagementStandard.md`** -> `globs: ["store/**", "state/**", "context/**", "*.store.*"]`

## 3. `model_decision` (Contextually Triggered)
These rules are triggered by the AI itself when it detects the task domain matches the rule's description.
- **`.agents/rules/System/Architecture.md`** -> When designing overall system or module architecture.
- **`.agents/rules/System/DocsFirst.md`** -> When integrating or writing code for 3rd-party libraries.
- **`.agents/rules/System/SkillMatrix.md`** -> When selecting which skill or sub-agent to invoke.
- **`.agents/rules/Automation/AgentSelfEvolution.md`** (also SelfCorrection/SelfEvolution) -> Upon task completion, errors, or post-mortem reflection.
- **`.agents/rules/Automation/ContextDecay.md`** (also ContextManagement) -> When session memory reaches 50+ turns or gets bloated.
- **`.agents/rules/CodeQuality/CodeQualityStandard.md`** -> When performing explicit refactoring or linting audits.
- **`.agents/rules/Data_Governance/PrivacyByDesignStandard.md`** -> When defining User models, handling PII, or auth logic.
- **`.agents/rules/ErrorHandling/ErrorStandard.md`** -> When setting up try/catch blocks, error boundaries, or logging.
- **`.agents/rules/Performance/PerformanceStandard.md`** -> When explicitly asked to optimize latency, query speed, or bundle size.
- **`.agents/rules/ProDoc/ProDocStandard.md`** (also RelationsStandard) -> When updating system documentation or traceability files.
- **`.agents/rules/Security/SecurityStandard.md`** -> When implementing authentication, authorization, or cryptography.
- **`.agents/rules/Specialized/JulesCLI.md`** -> When specifically using or troubleshooting the Jules CLI tool.
- **`.agents/rules/Specialized/VisualArchitecture.md`** -> When creating architecture visuals (AVAS).

## 4. `manual` (Explicitly Requested)
These rules are only loaded if the user explicitly references them or runs a specific command.
- **`.agents/rules/Automation/AutonomousExecution.md`** -> Only during `/startcycle` or Smith Engine auto-loops.
- **`.agents/rules/Specialized/AIExpertPractices.md`** -> Only when reviewing AI collaboration best practices.
- **`.agents/rules/Testing/MasterAgentOpsModeStandard.md`** -> Specific ops mode overrides.

## Next Steps for Implementation
1. **Scripted Updates:** Write a script or individually edit each `.md` file in `.agents/rules/` to ensure the correct YAML frontmatter is injected at the top of the file:
   ```yaml
   ---
   trigger: <trigger_type>
   globs: [<glob_array>] # if applicable
   description: <high_signal_summary>
   ---
   ```
2. **Prune Duplicates:** Resolve overlaps (e.g., `AgentSelfEvolution.md` vs `SelfEvolution.md`, `CodeQualityStandard.md` vs `System/CodeQuality.md`).
3. **Commit:** Push changes so the AI framework adopts the optimized Just-In-Time context loading.
