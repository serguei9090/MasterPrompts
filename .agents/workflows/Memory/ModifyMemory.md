---
name: ModifyMemory
description: Workflow for partial edits or refinements to existing memory artifacts.
---

# /ModifyMemory Workflow

Use this workflow for incremental improvements to existing memories (e.g., adding a new edge case to a 'lesson' or updating a tool's version in 'entities').

## 🔄 Sequence

### 1. Delta Identification
- Read the existing memory file.
- Identify specific sections that need refinement.

### 2. Surgical Edit
- Use `replace_file_content` or `multi_replace_file_content` to update the specific sections.
- Add an "Updated" timestamp if the change is significant.

### 3. Impact Assessment
- **Thinking Mode**: Use `sequentialthinking` to check if this modification ripples into other documented patterns or decisions.
