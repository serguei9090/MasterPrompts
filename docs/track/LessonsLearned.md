# Lessons Learned

## 2026-04-26 - Project Documentation & Issue Architect Workflows

### 1. Root Cause Analysis
The project lacked a central README, leading to ambiguity about its role as a Governance Hub vs. an Application. Initial README generation over-applied global standards (DuckDB) to a meta-repository where it wasn't actually used.

### 2. Resolution Strategy
- Created `/readme-gen` workflow to automate high-fidelity documentation.
- Refined the generated README to accurately reflect the repo as a "Governance Hub".
- Created `/git-issue` to standardize high-signal task definitions.

### 3. Preventative Measures
- **Rule update**: Updated the `readme-gen.md` workflow to include a mandatory "Verification/Truth Check" step against the filesystem.
- **Workflow modification**: Ensured `/git-issue` requires a "Technical Proposal" (code snippet/logic) to guide subsequent implementation cycles.

### 4. Reusable Patterns
- **Standardized Readme Structure**: Header -> Architecture (AVAS) -> AI Ecosystem -> Tech Stack -> Onboarding -> Laws.
- **High-Signal Issue Template**: Problem Statement (Why) -> Proposed Solution (What) -> Technical Scope -> Implementation Proposal (How).
