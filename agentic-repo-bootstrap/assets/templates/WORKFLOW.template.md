# Adaptive Engineering Workflow

1. Classify task risk and affected boundaries.
2. Decide whether direct parent execution is sufficient.
3. For complex work, create bounded task contracts and dependency relationships.
4. Route the minimum useful roles using `.agentic/routing.yaml`.
5. Enforce concurrency/budget limits from `.agentic/budgets.yaml`.
6. Parallelize independent reads. Use write claims/worktrees before parallel writes.
7. Record material decisions and agent outcomes in `.agentic/evidence/`.
8. Run repository-native verification commands from `.agentic/commands.yaml`.
9. On failure, classify the failure, record the strategy, and consult the budget guard before retry.
10. Require security/independent review according to `.agentic/workflow.yaml` and risk profile.
11. Parent inspects integrated diff + evidence and performs final acceptance.

The workflow defines invariants and gates rather than forcing every task through a rigid fixed state machine.
