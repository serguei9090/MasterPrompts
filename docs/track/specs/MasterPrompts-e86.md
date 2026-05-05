# Implementation Spec - MasterPrompts-e86
## Circular Dashboard UI

### Objective
Create a new HTML dashboard `test/dashboard2.html` that features a circular layout and circular UI elements, distinguishing it from the grid-based `test/dashboard.html`.

### Requirements
- **File Path**: `test/dashboard2.html`
- **Layout**: Elements (cards) arranged in a circle around a central header.
- **Visuals**: 
    - Circular cards (border-radius: 50%).
    - Maintain the "Morphic" aesthetic (dark theme, glassmorphism, glowing borders).
    - Different accent colors (e.g., more purple/blue focus vs. green focus).
- **Functionality**: Re-implement the same 5 logic functions from `dashboard.html`:
    1. Randomizer
    2. Greetings
    3. Sum Engine
    4. Product Lab
    5. Square Rootless

### Implementation Plan
1. **HTML Structure**:
    - Central `div` for the header.
    - Container with `position: relative` for the cards.
    - 5 card elements.
2. **CSS Styling**:
    - Use absolute positioning with `transform` to place cards at 72-degree intervals (360/5).
    - `border-radius: 50%` for all cards.
    - CSS variables for theme consistency.
3. **JS Logic**:
    - Same logic as `dashboard.html`.
    - Update handlers to match the new IDs.

### Verification
- Open in browser (if possible, or verify source code).
- Ensure all 5 functions work as expected.
- Confirm circular layout and styling.
