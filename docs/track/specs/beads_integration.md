# Spec: Beads (bd) Integration

## Overview
Beads (bd) is a graph-based issue tracker powered by Dolt. Integrating it into the Morphic AI Engineering Framework moves us from markdown-based task tracking to a version-controlled, queryable database.

## Implementation Details
- **Binary**: `bd` (npm global)
- **Database**: Dolt (managed by bd)
- **Workflow Integration**: 
    - `bd create` for new tasks.
    - `bd claim` for agents to take tasks.
    - `bd resolve` for task completion.

## Benefits
- Durable memory across AI sessions.
- SQL-queryable project state.
- Version-controlled task history.
