# Spec: HTML/JS Interactive Dashboard (b7p)

## Context
Create a web-based dashboard that replicates the logic of `test/simple_script.py` in JavaScript and provides a premium UI for user interaction.

## Requirements
- Single HTML file (Dashboard) with embedded CSS and JS.
- Replicate 5 functions:
    - `getRandomNumber()`
    - `printHello(name)`
    - `add(a, b)`
    - `multiply(a, b)`
    - `square(n)`
- UI: Premium design, dark mode, glassmorphism, responsive.
- Interaction: Input fields for arguments, buttons to trigger functions, and clear result displays.

## Implementation Plan
1. **File**: Create `test/dashboard.html`.
2. **Design**:
    - Dark theme with vibrant accent colors (violet/blue).
    - Bento-grid style layout for function cards.
    - Glassmorphism effects (backdrop-filter: blur).
3. **Logic**:
    - Use standard JS Math and DOM manipulation.
    - Ensure clean code and descriptive IDs.
4. **Verification**:
    - Lint with Biome.
    - Visual check (manual).

## Success Criteria
- [ ] Dashboard is visually stunning and responsive.
- [ ] All 5 functions work correctly.
- [ ] User can input arguments and see results.
