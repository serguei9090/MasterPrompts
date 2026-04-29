---
version: v0.10.7
name: Morphic (LogLensAi Aesthetic)
description: Professional engine-precision dashboard with glassmorphic obsidian aesthetics and tactical green accents.
tokens:
  colors:
    primary: "#22C55E"
    primary-hover: "#16A34A"
    primary-muted: "#14532D"
    bg-base: "#0D0F0E"
    bg-surface: "#111613"
    bg-surface-bright: "#1A1F1C"
    bg-hover: "#1E2520"
    border: "#2A3430"
    border-muted: "#1D2420"
    border-glow: "#22C55E4D"
    error: "#EF4444"
    warning: "#F59E0B"
    info: "#38BDF8"
    debug: "#A78BFA"
    text-primary: "#E8F5EC"
    text-secondary: "#8FA898"
    text-muted: "#4D6057"
    text-inverse: "#0D0F0E"
    accent-violet: "#8B5CF6"
    accent-violet-bg: "#8B5CF610"
  typography:
    sans: "Inter Variable, system-ui, sans-serif"
    mono: "JetBrains Mono, monospace"
    h1:
      fontSize: "1.125rem"
      fontWeight: 700
      lineHeight: "1.5rem"
    h2:
      fontSize: "0.875rem"
      fontWeight: 600
      lineHeight: "1.25rem"
    body:
      fontSize: "0.875rem"
      fontWeight: 400
      lineHeight: "1.25rem"
    label-caps:
      fontSize: "0.625rem"
      fontWeight: 700
      letterSpacing: "0.1em"
      textTransform: "uppercase"
    log:
      fontSize: "0.75rem"
      fontWeight: 400
      lineHeight: "1rem"
  rounded:
    sm: "4px"
    md: "8px"
    lg: "12px"
    xl: "16px"
    modal: "1.5rem"
  spacing:
    xs: "0.25rem"
    sm: "0.5rem"
    md: "1rem"
    lg: "1.5rem"
    xl: "2rem"
---

# Morphic Framework: LogLensAi Design Specification

## **Overview**
LogLensAi is designed with an **"Engine Precision"** philosophy. The interface should feel like a professional diagnostic instrument — high-contrast, obsidian-based, and glassmorphic. It avoids generic UI tropes in favor of a tactical, dark-mode aesthetic that reduces eye strain during long-tail log analysis and AI orchestration sessions.

### **Core Principles**
- **Surgical Precision**: Every border, icon, and alignment must be intentional.
- **Glassmorphism**: Use layering and backdrop blurs (`backdrop-blur-xl`) to establish depth without losing the obsidian base.
- **Color Discipline**: Color is used strictly for semantic meaning (Log Levels) or tactical focus (Primary Actions).

## **Colors**
The color palette is built on an **Obsidian Base** (`#0D0F0E`) with **Tactical Green** (`#22C55E`) as the primary action and brand color.

- **Backgrounds**: Use `bg-base` for the main shell and `bg-surface` for nested panels.
- **Accents**: Use Violet (`accent-violet`) for AI-orchestration features to distinguish them from standard log management.
- **Semantics**: Log levels follow a strict mapping: 
    - `ERROR`: Red (`#EF4444`)
    - `WARN`: Amber (`#F59E0B`)
    - `INFO`: Primary Green (`#22C55E`)
    - `DEBUG`: Violet (`#A78BFA`)

## **Typography**
Typography is split between **Inter** (for UI controls) and **JetBrains Mono** (for data/logs).

- **UI Elements**: Use `text-sm` for labels and content.
- **Hierarchy**: Use `uppercase tracking-widest` for section labels to maintain a technical look.
- **Log Data**: Must always use `font-mono` at `text-xs` (`0.75rem`) to maximize horizontal space and readability of structured text.

## **Elevation & Depth**
Depth is communicated through **Glassmorphic Overlays** rather than traditional shadows.
- **Surface Elevation**: Elevated panels should use `backdrop-blur-xl` with a subtle white tint (`bg-white/[0.03]`).
- **Glows**: Primary buttons and active states use subtle color glows (`border-glow`) rather than black shadows to simulate a lit instrument panel.

## **Shapes & Spacing**
- **Strict Grid**: Adheres to the 4px/8px rhythm via the `spacing` tokens.
- **Buttons/Inputs**: `rounded-md` (8px).
- **Containers**: `rounded-lg` (12px).
- **Modals**: `rounded-modal` (1.5rem).

## **UX Mandates**
1. **Interactive Feedback**: Every button click MUST provide immediate visual feedback (e.g., scale-down or glow shift).
2. **Motion Law**: No element should appear or disappear without a transition (Fade/Slide/Scale).
3. **Token Adherence**: Hardcoded hex codes are strictly forbidden; always reference the CSS variables derived from the frontmatter tokens.

---
*This document is the absolute Source of Truth for the UI/UX Auditor. Any code deviating from these tokens will be rejected.*
