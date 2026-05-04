# Spec: MasterPrompts-9pt — CLI Calculator Implementation

## Objective
Create a standalone Python-based CLI calculator inside a new subfolder in `IndexTest/Folder`.

## Proposed Architecture
- **Location**: `IndexTest/Folder/cli_calculator/calculator.py`
- **Logic**: All functions (addition, subtraction, multiplication, division) contained in a single file.
- **Interface**: Command-line interface using Python's `argparse` module.

## Implementation Details
1. **Directory Creation**: `IndexTest/Folder/cli_calculator/`.
2. **Logic Functions**:
   - `add(a, b)`
   - `subtract(a, b)`
   - `multiply(a, b)`
   - `divide(a, b)` (with zero-division protection).
3. **CLI Wrapper**:
   - Argument: `operation` (choices: add, sub, mul, div).
   - Argument: `num1` (float).
   - Argument: `num2` (float).

## Verification Plan
- **Manual Test**: Run `python calculator.py add 10 5` and verify output.
- **Lint**: Run `ruff check`.
