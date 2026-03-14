---
trigger: always_on
description: Global engineering standards for scalable and orthogonal architecture.
---

# Architecture Standards

To maintain a clean codebase and avoid tight coupling, all code must adhere to the following global principles. These principles ensure that business logic remains completely separate from infrastructure or side-effects (like UI, databases, or networking).

## 1. Separation of Concerns (SoC)
Ensure that modules are highly cohesive and loosely coupled. Business logic should not be aware of infrastructure details (e.g., database clients, HTTP frameworks). The entry point should act merely as a traffic controller, orchestrating dependencies and routing data between the domain layer and infrastructure layer.

## 2. Interface-First Design
Define abstractions (Interfaces, Traits, or Protocols) before writing concrete logic. Code against these abstractions, not specific implementations. This ensures that you can swap out infrastructure without modifying domain logic.

## 3. Dependency Injection (DI)
Inject components (like loggers, database repositories, and metrics recorders) into functions and classes. Avoid hardcoding infrastructure connections or instantiations deep within domain logic files.

## 4. Spec-Driven Development Workflow
Follow this "Definition Path" before writing code:
1. **Define the Contract**: Specify the communication contract (e.g., OpenAPI spec, Protobuf definition, or explicit data types).
2. **Define the Interface**: Write the abstract interface representing the input/output boundaries.
3. **The "Mock" Test**: Write tests against mock implementations of the interface to validate the contract.
4. **The Implementation**: Write the actual concrete logic connecting to the real systems.

## 5. Ports and Adapters (Hexagonal Architecture)
- **Port**: Defines what needs to be done. These are interfaces inside the Domain layer.
- **Adapter**: Defines how it is implemented. These are concrete classes or functions inside the Infrastructure layer.
- **Usage**: The domain calls a Port, and the dependency injection framework provides the Adapter.
