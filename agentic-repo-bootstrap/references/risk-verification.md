# Risk and Verification

## Risk levels

### Low

Localized, reversible, no important contract or security boundary.

Typical path: implement -> targeted check -> diff review -> accept.

### Medium

Multiple files or behavior paths, but no critical trust/data boundary.

Typical path: implement -> tests -> diff review -> accept.

### High

Cross-module behavior, public API, important data flow, difficult rollback, or architecture-sensitive change.

Typical path: explore/plan -> implement -> tests -> independent review -> parent accept.

### Critical

Authentication, authorization, cryptography, money movement, destructive migrations, network/security policy, privileged infrastructure, irreversible data changes, or similarly high-impact change.

Typical path: architecture/risk analysis -> implement -> targeted tests -> security review -> independent review -> parent accept.

## Verification gates

Use project-native checks. Examples may include:

- unit tests;
- integration tests;
- end-to-end tests;
- type-check;
- lint/static analysis;
- dependency/security scan;
- schema validation;
- browser reproduction;
- API contract tests;
- migration dry run;
- configuration validation.

Do not add a gate just because it exists in this list.

## Bounded repair

Default behavior for a failed gate:

1. classify failure owner;
2. return to the appropriate agent;
3. make a bounded fix;
4. rerun the smallest meaningful gate;
5. run full required gates before final acceptance.

Escalate to the parent if:

- the same failure repeats with no meaningful relevant change;
- two repair attempts fail for the same root cause unless the repo has another explicit policy;
- the failure reveals an architectural or requirement ambiguity;
- a fix would exceed task scope.

The parent may choose a different bounded limit based on the task.
