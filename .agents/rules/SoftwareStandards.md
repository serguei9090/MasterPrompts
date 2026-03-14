---
trigger: always_on
description: Senior-level software engineering standards and best practices.
---

# Global Software Engineering Standards (The Golden Rules)

To ensure high-quality, maintainable, and scalable software, all code must strictly adhere to these industry-standard best practices.

## 1. Core Principles
- **DRY (Don't Repeat Yourself)**: Avoid logic duplication. If you find the same logic in two places, abstract it into a reusable function, component, or module.
- **KISS (Keep It Simple, Stupid)**: Prefer simple, readable solutions over "clever" or overly complex ones. Code is read more often than it is written.
- **YAGNI (You Ain't Gonna Need It)**: Do not implement functionality until it is actually needed. Avoid speculative "just-in-case" engineering.
- **S.O.L.I.D. Principles**:
  - **Single Responsibility**: A class or module should have one, and only one, reason to change.
  - **Open/Closed**: Software entities should be open for extension but closed for modification.
  - **Liskov Substitution**: Subtypes must be substitutable for their base types.
  - **Interface Segregation**: Prefer many client-specific interfaces over one general-purpose interface.
  - **Dependency Inversion**: Depend on abstractions, not concretions.

## 2. Implementation Standards
- **Composition over Inheritance**: Prefer building complex functionality by combining simple objects rather than using deep inheritance hierarchies.
- **Fail Fast**: Validate inputs and state early. Throw descriptive errors as soon as an invalid state is detected.
- **Pure Functions**: Where possible, write functions that have no side effects and return the same output for the same input. This makes testing and reasoning significantly easier.
- **Immutability**: Favor immutable data structures. Avoid shared mutable state to prevent race conditions and unpredictable side effects.

## 3. Clean Code Practices
- **Meaningful Names**: Variables, functions, and classes must have descriptive names that reveal intent. Avoid abbreviations (e.g., use `userRepository` instead of `uRepo`).
- **Small Functions**: Functions should do one thing and do it well. If a function is longer than 20-30 lines, consider breaking it down.
- **No Magic Numbers**: Use named constants or enums instead of hardcoded literal values.
- **Explicit over Implicit**: Avoid "magic" behavior. It should be clear from the code how data flows and how dependencies are resolved.

## 4. Documentation & Comments
- **Code should be self-documenting**: Comments should explain *why* something is done, not *what* is being done (the code should tell you *what*).
- **Stale Comments are Dangerous**: Always update comments when the code they describe changes. If a comment is no longer accurate, delete it or fix it.
