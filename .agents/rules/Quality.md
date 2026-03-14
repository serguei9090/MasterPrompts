---
trigger: always_on
description: Mandatory standards for code quality, commenting, TODO management, and UI design.
---

# Code Quality & Documentation Standards

To ensure maximum clarity, maintainability, and consistent UI, all code must adhere to the following standards.

## 1. General Commenting Rules
- **Functions/Methods**: Every public function or method must have a structured documentation comment detailing:
  - **Purpose**: What the function does.
  - **Callers**: Who is responsible for calling this function.
  - **Arguments/Returns**: Brief explanation of inputs and outputs.
- **Variables/Fields**: Every non-trivial variable or class field must have a comment explaining its role in the system.

## 2. TODO(ID) Protocol
Any incomplete or placeholder code MUST use the `TODO` keyword accompanied by a unique identifier and a corresponding tracking file.
- **Format**: `// TODO(unique_id_001): Description of exactly what is missing or needs implementation.`
- **Creation Protocol**:
  1. **Assign a Unique ID**: Use a descriptive prefix and a sequential number (e.g., `auth_flow_001`).
  2. **Create Detail File**: Create a detailed markdown file in `docs/TODOC/<unique_id>.md` explaining the requirements, constraints, and context.
  3. **Update Roadmap**: Add the task to `docs/track/TODO.md`, linking to the detail file and specifying the source file and line number.
- **Completion Protocol**: When implemented, remove the `TODO`, add proper standard comments, mark as done in `docs/track/TODO.md`, and update or archive the `docs/TODOC/` detail file.

## 3. Atomic Design (Frontend/UI)
For any frontend components, the modular hierarchy must be strictly enforced:
- **Atoms**: Smallest functional units (e.g., buttons, inputs, icons).
- **Molecules**: Groups of atoms functioning together (e.g., search bar, form field).
- **Organisms**: Complex UI sections (e.g., header, navigation, sidebar).
- **Templates**: Page-level layouts focusing on content structure without real data.
- **Pages**: Specific instances of templates populated with real data and state.
