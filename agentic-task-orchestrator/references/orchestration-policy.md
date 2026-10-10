# Orchestration Policy v2

The parent owns objective interpretation, decomposition, delegation, integration, and final acceptance.

## Decision sequence

1. Read the machine-readable harness policies.
2. Classify risk and security-sensitive scope.
3. Prefer direct execution for trivial bounded work.
4. For complex work, define task contracts and only the dependencies that matter.
5. Select the minimum useful set of roles.
6. Route role model/reasoning/sandbox/concurrency from `.agentic/routing.yaml`.
7. Run independent read-only tasks in parallel.
8. Require claims or worktrees for parallel writers.
9. Persist decisions and outcomes to the evidence store.
10. Run required verification and classify failures before retry.
11. Stop repeated failing strategies when the budget guard denies another attempt.
12. Require security/independent review according to risk.
13. Inspect final diff/evidence and decide acceptance.

Avoid rigid state-machine choreography when a bounded objective plus tools/context is sufficient. The workflow policy defines invariants and gates, not every reasoning step.
