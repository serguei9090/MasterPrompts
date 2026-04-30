---
trigger: always_on
description: Canonical binding of every available skill to its responsible persona and SDLC phase. Read this before activating any skill.
---

# Skill Matrix (v0.11.0)
> **Law**: Every persona MUST activate its bound skills at the start of its phase. Activating a skill outside its canonical persona is a protocol violation unless explicitly justified.

---

## 🏛️ @lead / @brain / @pm — Strategy & Planning

| Skill | When to Activate |
| :--- | :--- |
| `beads` | **Always** at session start. `bd ready` → `bd create` → `bd close` lifecycle. |
| `clarify` | When the user request is ambiguous or under-specified. Run before any spec is written. |
| `diagram-creator` | When producing architecture diagrams, data-flow maps, or AVAS-compliant C4 visuals. |
| `codetographer` | When generating an interactive code map (`.cgraph`) of the project's physical structure. |
| `codanna` | When performing physical impact analysis (`analyze_impact`, `get_calls`, `search_documents`). |
| `rule-creator` | When the task is to create or update `.agents/rules/` governance files. |
| `skill-creator` | When the task is to create or update a new `.agents/skills/` capability. |
| `shape` | Before any new UI feature: run a structured UX discovery interview to produce a design brief. |

---

## 🧠 @memory-manager / @scribe — Memory & Intelligence

| Skill | When to Activate |
| :--- | :--- |
| `cognee-indexer` | After any structural refactor, to sync the codebase into the Knowledge Graph. |
| `memory` | When recording architectural decisions, patterns, and lessons to `docs/memory/`. |
| `distill` | When compressing a long session or conversation into an atomic lesson set. |
| `session-handover` | **Always** at session end. Generates `handoff.md` for the next session. |
| `find-skills` | When the agent needs to discover which skill is best for an unknown sub-task. |

---

## 💻 @backend / @api-specialist — Server & Logic

| Skill | When to Activate |
| :--- | :--- |
| `code-quality` | On every Python/backend implementation phase. Enforces correctness, no over-engineering. |
| `adk-expert` | When building with Google ADK 2.0, Pydantic AI, or LangGraph agent pipelines. |
| `fullstack-developer` | When the task spans both frontend and backend in a single implementation pass. |
| `optimize` | When diagnosing and fixing backend performance, bundle size, or DB query latency. |

---

## 🎨 @frontend / @ui-designer — React & UI Implementation

| Skill | When to Activate |
| :--- | :--- |
| `react` | When writing or editing React/TSX components. Enforces Lobehub/ui patterns and routing. |
| `vercel-react-best-practices` | When refactoring for performance (code splitting, data fetching, bundle optimization). |
| `design-taste-frontend` | **Always first** when starting any new UI component. Establishes premium design baseline. |
| `frontend-design` | When building the full frontend architecture (folder structure, design system setup). |
| `shadcn` | When using `shadcn/ui` component registry, `components.json`, or presets. |
| `tailwind-design-system` | When building scalable design systems with Tailwind CSS v4 tokens. |
| `turborepo` | When managing a monorepo with multiple packages sharing a design system. |
| `image-to-code` | When converting a visual mockup or screenshot into working HTML/CSS/React code. |
| `full-output-enforcement` | When the model is truncating code. Forces complete, uncut file output. |

---

## 🎭 @theme-expert — Visual Identity & Design Tokens

| Skill | When to Activate |
| :--- | :--- |
| `ui-ux-pro-max` | When selecting a design style, palette, or font pairing from scratch. Covers 50 styles. |
| `stitch-design-taste` | When generating or updating the `DESIGN.md` token file for a project. |
| `high-end-visual-design` | When maximum premium quality is required — editorial-grade, award-winning aesthetic. |
| `gpt-taste` | When you want a design that feels like state-of-the-art GPT/OpenAI product aesthetics. |
| `impeccable` | When building production-grade UI that avoids generic AI aesthetics. Use `craft` mode. |
| `minimalist-ui` | When the design must be clean, monochrome, editorial, bento-grid style. |
| `industrial-brutalist-ui` | When the design must feel like a military terminal or declassified blueprint dashboard. |
| `huashu-design` | When the design should use Chinese ink / Huashu-inspired aesthetics. |
| `bolder` | When the current design is too safe or timid. Pushes contrast, scale, and intensity up. |
| `quieter` | When the current design is too loud, aggressive, or garish. Tones it down elegantly. |
| `colorize` | When adding or refining the color palette on an existing interface. |
| `typeset` | When fixing typography: font choice, weight, hierarchy, sizing, or readability. |

---

## ✨ @ui-designer — Motion & Interaction

| Skill | When to Activate |
| :--- | :--- |
| `animate` | When implementing transitions, hover effects, or scroll-based animations. |
| `overdrive` | When the task demands technically ambitious effects: shaders, spring physics, 60fps reveals. |
| `delight` | When adding micro-interaction polish that makes the UI feel alive and joyful. |

---

## 🔧 @ui-designer — Layout & Composition

| Skill | When to Activate |
| :--- | :--- |
| `layout` | When spacing, visual rhythm, or grid composition is broken or monotonous. |
| `adapt` | When an existing design must be adapted to a new context, platform, or constraint. |
| `redesign-existing-projects` | When upgrading an existing app from generic/MVP quality to premium production quality. |

---

## 🧪 @auditor / @qa / @lint — Quality & Review

| Skill | When to Activate |
| :--- | :--- |
| `audit` | **Always** as the final pass before `bd close`. Fixes alignment, a11y, and performance. |
| `polish` | Pre-launch quality pass: fixes micro-detail issues, spacing inconsistencies, final cleanup. |
| `critique` | When performing a structured, adversarial design or code review. Generates a scored report. |
| `code-gap-reviewer` | When auditing for architectural drift, missing implementations, or contract gaps. |

---

## 🏗️ @diagram-agent — Architecture Visualization

| Skill | When to Activate |
| :--- | :--- |
| `diagram-creator` | **Always** when generating architecture diagrams. Enforces C4/AVAS compliance. |
| `codetographer` | When building an interactive `.cgraph` visual map of the physical codebase structure. |

---

## 🌐 @platform-engineer / @devops — Infrastructure & Browser

| Skill | When to Activate |
| :--- | :--- |
| `browser-use` | When automating browser interactions, scraping, or UI end-to-end testing via a browser. |
| `chrome-devtools` | When debugging performance, memory, or network issues in Chrome DevTools. |

---

## 📝 @docs / @scribe — Documentation

| Skill | When to Activate |
| :--- | :--- |
| `obsidian-markdown` | When creating or editing `.md` files with Obsidian-specific syntax (wikilinks, callouts). |
| `caveman` | When simplifying complex technical documentation into plain, readable language. |

---

## 🔮 @flow-creator — Meta / Framework Evolution

| Skill | When to Activate |
| :--- | :--- |
| `rule-creator` | When creating new `.agents/rules/` governance files for the framework. |
| `skill-creator` | When creating new `.agents/skills/` capabilities. |
| `find-skills` | When discovering the right skill for an unknown domain. |

---

## 📐 Quick Reference — SDLC Phase → Skills

| SDLC Phase | Required Skills |
| :--- | :--- |
| **Boot** | `beads` (`bd ready`), `codanna` (impact scan) |
| **Discovery** | `clarify`, `shape`, `codanna`, `cognee-indexer` |
| **Planning** | `beads` (`bd create`), `diagram-creator`, `rule-creator` |
| **Design** | `stitch-design-taste`, `ui-ux-pro-max`, `design-taste-frontend` |
| **Implementation (Backend)** | `code-quality`, `adk-expert`, `full-output-enforcement` |
| **Implementation (Frontend)** | `react`, `design-taste-frontend`, `animate`, `shadcn` |
| **Motion & Polish** | `overdrive`, `delight`, `layout`, `typeset` |
| **Quality Gate** | `audit`, `polish`, `critique`, `code-gap-reviewer` |
| **Memory Distill** | `distill`, `memory`, `cognee-indexer` |
| **Session End** | `session-handover`, `beads` (`bd close`, `bd dolt push`) |
