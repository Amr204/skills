# Idea → Project Mode

Use this mode when there is no meaningful repository yet.

## Required sequence

1. Capture the raw idea without inventing business facts.
2. Separate **requirements** from **assumptions**.
3. Define measurable non-functional requirements (security, availability, latency, scale, operability, cost constraints).
4. Propose architecture and explicit tradeoffs.
5. Produce a lightweight threat model before choosing security-sensitive components.
6. Select a stack from requirements and constraints, not preference alone.
7. Create an `idea-spec.yaml` that validates against `engine/schemas/idea-spec.schema.json`.
8. Run `scripts/idea_project.py <idea-spec.yaml> --write-planning-docs`.
9. Scaffold the project using the selected stack's native tooling.
10. Add test/lint/typecheck/build commands and CI/CD.
11. Run Repository Discovery v2 against the generated repository; never trust the original plan as current evidence.
12. Bootstrap the normal v2 agent harness and validate it.
13. Produce an implementation plan with dependencies, acceptance criteria, security checkpoints, and rollback considerations.

## Assumption rule

Unknown facts must stay visible as assumptions. Do not silently convert an assumption into a requirement or an established project fact.

## Output contract

The mode must leave behind:
- `docs/requirements.md`
- `docs/architecture.md`
- `docs/threat-model.md`
- `docs/implementation-plan.md`
- a real scaffold with build/test tooling
- the same validated v2 harness used for existing repositories
