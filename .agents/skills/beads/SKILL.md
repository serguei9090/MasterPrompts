---
name: beads
description: Expert skill for managing tasks, issues, and memory using the Beads (bd) graph-based system powered by Dolt. Use this for all roadmap management, task claiming, and persistent project knowledge.
---

# Beads (bd) Skill

This skill provides instructions for using the **Beads (bd)** issue tracking and memory system.

## 🎯 Core Principles
- **Graph Consistency**: Maintain relationships between beads (blocks, relates, duplicate).
- **Persistent Memory**: Use `bd remember` for knowledge that must survive context resets.
- **Versioned Roadmap**: Always commit and push beads data using `bd dolt push`.

## 🛠️ Essential Commands

### Task Discovery & Management
- `bd ready`: List all available tasks that are not blocked.
- `bd list --status open`: View all open tasks.
- `bd show <id>`: Get full details, history, and dependencies for a specific bead.
- `bd create "<title>"`: Create a new task.
- `bd update <id> --claim`: Assign a task to yourself.
- `bd close <id>`: Mark a task as completed.

### Knowledge & Context
- `bd remember "<fact>"`: Store a persistent piece of information.
- `bd search "<query>"`: Search through beads and memory.
- `bd prime`: Load full context and workflow instructions for the current session.

### Synchronization
- `bd dolt push`: Push beads database to the remote repository.
- `bd dolt pull`: Sync beads from the remote.

## 🏛️ Stack Management
Always maintain a "Source of Truth" for the tech stack using specialized knowledge beads.
- `bd remember "STACK: [Primary Framework/Language]"`
- `bd remember "DATABASE: [Primary Storage]"`
- `bd remember "RUNTIME: [Package Manager/Runner]"`
- `bd remember "STANDARDS: [Linting/Formatting rules]"`

When the stack changes, update the relevant bead:
`bd update <id> --comment "Migrated from npm to bun"`

## 🔄 Workflow Integration

### 1. Session Start (// turbo)
At the beginning of a session, run:
```bash
bd dolt pull
bd prime
bd ready
```
This ensures you have the latest roadmap, knowledge, and workflow context.

### 2. Task Execution
When starting a task:
1. Claim it: `bd update <id> --claim`
2. Reference the ID in comments: `// bead: <id>`
3. Once verified, close it: `bd close <id>`

### 3. Session Wrap-up (// turbo)
Before ending the session:
1. File issues for remaining work: `bd create "..."`
2. PUSH:
```bash
bd dolt push
git push
```

## ⚠️ Important Rules
- **NEVER** use markdown `TODO.md` for active tracking.
- **NEVER** leave a session without `bd dolt push`.
- Use descriptive titles for beads to ensure high-signal retrieval.
