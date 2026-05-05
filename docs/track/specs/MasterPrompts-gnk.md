# Spec: Create test folder and sample python script (gnk)

## Context
The user requested a `test/` folder and a Python script with 5 specific functions:
1. Random number generator.
2. Greet user function.
3. Three simple math/argument functions.

## Implementation Plan
1. **Directory**: Ensure `test/` exists.
2. **File**: Create/Verify `test/simple_script.py`.
3. **Functions**:
    - `get_random_number()`
    - `print_hello(name)`
    - `add(a, b)`
    - `multiply(a, b)`
    - `square(n)`
4. **Verification**:
    - Lint with `ruff`.
    - Test with `pytest`.

## Success Criteria
- [ ] `test/simple_script.py` exists and contains 5 functions.
- [ ] `ruff` check passes.
- [ ] `pytest` pass.
