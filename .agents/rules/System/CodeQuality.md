---
trigger: always_on
description: Mandatory standards for code quality, documentation, commenting, and TODO management.
---

# Code Quality & Documentation Standards

To ensure maximum clarity, maintainability, and consistent UI, all code must adhere to the following standards.

## 1. Zero-Guesswork Documentation Standard
To maintain context for subagents across sessions, all files and structures must be thoroughly self-documenting.

### 1.1 Philosophy
Well-written code should be largely self-documenting. Comments should explain complex algorithms, non-obvious business logic, or the rationale behind a particular implementation choice—the things the code cannot express on its own. **Explain the Why, Not the What.** Avoid comments that merely restate what the code does.

### 1.2 General Commenting Rules
- **Functions/Classes (The Contract)**:
  - **JS/TS**: Every exported function, interface, or class MUST have a full `JSDoc` block (`/** ... */`).
  - **Python**: Every public function or class MUST have a full `Google-style Docstring` (`""" ... """`).
  - Every docstring must explicitly define:
    - **Purpose**: What it does and why it exists.
    - **Context**: Reference any relevant spec files (e.g., `docs/track/specs/api_001.md`) or documentation that provides the rationale for the implementation.
    - **Args/Returns**: Inputs and outputs with explicit types.
    - **Raises/Throws**: Expected errors.
- **Variables/Fields**: Every variable declaration (especially state and configuration) MUST have an inline comment explaining its intent and how it is used.
- **Complex Logic**: If a block of logic is highly algorithmic or non-trivial, write a multi-line comment above it mapping out the steps in plain English before the code begins.

## 2. TODO(ID) Protocol (The "Task Memory")
Any incomplete interface, bypassed error, or missing feature MUST NOT be left as a silent placeholder. It MUST use the `TODO` keyword accompanied by a unique identifier.

### 2.1 The Formal TODO Syntax
`// TODO(sync_001): [WHAT] Need to add debounce to this input. [WHY] API rate limits are being hit during fast typing. [EXPECTATION] Implement a 300ms debounce using lodash or a custom hook to batch requests. [CONTEXT] See specs/rate_limit_001.md.`

### 2.2 Creation Protocol (The "Detail File")
When a `TODO` is introduced:
1. **Assign a Unique ID**: (e.g., `api_gateway_001`).
2. **Create the Brain**: Create a markdown file in `docs/track/specs/<unique_id>.md`. This is the **Active Task Memory**—include architectural choices, chosen libraries, logic snippets, and why we made those decisions.
3. **Index the Task**: Add the high-level task to `docs/track/TODO.md`, linking to the detail file.

### 2.3 Completing TODOs
When the logic for a `TODO` is implemented:
1. **Replace Comment**: Remove the `TODO(...)` comment and replace it with a proper standard doc-comment.
2. **Mark as Done**: Update the status in `docs/track/TODO.md`.
3. **Archive/Update Detail**: The detail file in `docs/track/specs/` should be updated to reflect the implementation details or archived if no longer relevant.

## 3. Pure TDD & Architectural BDD (Hybrid)
We distinguish between **Architectural Guidance** and **Implementation Speed**:
- **BDD (Gherkin)**: Use `.feature` files ONLY for high-level architectural contracts and user flows. This provides the "Living Spec" that mirrors your requirements.
- **Pure TDD**: During the intense implementation phase, we skip the Gherkin layer for specific unit logic. AI is faster with pure code definitions than English abstraction parsing.
- **The Flow**: Define Interface -> (Optional) Write Gherkin Feature for high-level flow -> Write isolated failing TDD spec -> Invoke `@jules-agent` -> Pass.

## 4. Atomic Design / Modular Structure
For any structured content or frontend components, the modular hierarchy must be strictly enforced:
- **Atoms**: Smallest functional units (e.g., base MD snippets, singular icons).
- **Molecules**: Groups of atoms functioning together (e.g., specific rules, combined snippets).
- **Organisms**: Complex sections (e.g., full workflow descriptions, headers).
- **Templates**: Page-level layouts focusing on content structure.
- **Pages**: Specific instances of templates populated with real data and state.
