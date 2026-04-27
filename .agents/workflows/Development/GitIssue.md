---
description: "Properly generate a GitHub issue description from a problem or feature request, including why, what it solves, complexity, files, and proposed code."
---

# /git-issue: GitHub Issue Architect
> **Assume Role:** `@pm` (Product Manager) / `@brain` (Lead Architect)

## Overview
This workflow transforms raw ideas or bug reports into professional, high-signal GitHub issues. It ensures that every task has clear context, technical scope, and a proposed implementation path, aligning with the framework's **Spec-Driven Development** law.

## Workflow

### 1) Triage & Research
- **Identify Intent:** Determine if the request is a `Bug`, `Feature`, `Refactor`, or `Security` issue.
- **Context Discovery:** Scan the codebase to identify the specific logic, components, or rules that relate to the request.
- **Scope Analysis:** Identify the specific files that need updates and evaluate the potential for regressions.

### 2) Issue Drafting
Generate the issue body using the following mandatory sections:

#### **Title:** `[Type]: Short, descriptive title`

#### **1. Problem Statement (The Why)**
- **Context:** Describe the current state and the friction point or gap in functionality.
- **Rationale:** Explain *why* this change is necessary and what user/agent pain it resolves.

#### **2. Proposed Solution (The What)**
- **Objective:** Describe the high-level logic or architectural change that solves the problem.
- **Expected Outcome:** List the specific behaviors or states that will be achieved.

#### **3. Technical Scope**
- **Complexity Score:** `[Low | Medium | High]` (based on cross-file dependencies and architectural risk).
- **Files to Update:** Provide a bulleted list of absolute or relative paths.
- **Architectural Impact:** Note if this affects core rules (`.agents/rules/`) or framework mandates.

#### **4. Implementation Proposal (The How)**
- **Code Snippet:** Include a fenced code block showing the proposed implementation or a mock-up of the logic change.
- **Implementation Steps:** A 1-3 step checklist for the developer/agent.

### 3) Validation & Verification
- **Success Criteria:** Define exactly what "Done" looks like (e.g., "Linter passes", "New unit test passes").
- **Quality Check:** Ensure the proposal complies with **DRY, KISS, and SOLID** principles.

### 4) Final Handoff
- Present the generated issue to the user in a clean Markdown block.
- **Action:** Ask: *"The issue has been drafted. Would you like me to save this as a new Spec file in `docs/track/specs/` or register it in `TODO.md`?"*

## Success Criteria
- [ ] Issue draft includes clear "Why" and "What" sections.
- [ ] Technical scope accurately lists affected files and complexity.
- [ ] A valid, high-signal code snippet or technical plan is included.
- [ ] Success criteria are specific and measurable.
