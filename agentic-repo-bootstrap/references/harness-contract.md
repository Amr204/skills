# Harness Contract

## Parent authority

The parent thread owns:

- user intent;
- decomposition;
- delegation;
- dependency decisions;
- conflict resolution;
- integration;
- final acceptance.

Subagents own bounded analysis or execution inside their task contracts.

## Task contract

When delegating non-trivial work, pass a compact contract:

```yaml
objective: <one outcome>
context:
  relevant_files: []
  known_facts: []
scope:
  allowed: []
  forbidden: []
dependencies: []
acceptance_criteria: []
verification: []
expected_return:
  status: pass | fail | blocked
  summary: ...
  evidence: []
  changed_files: []
  risks: []
  follow_up_candidates: []
stop_condition: ...
```

Avoid copying the whole parent context into the task.

## Structured subagent return

Prefer concise structured summaries over raw logs.

Evidence should identify exact files, tests, commands, or observed behavior.

## Workflow contract

The workflow should define:

- how risk is classified;
- when agents are useful;
- dependency handling;
- write isolation;
- verification gates;
- repair limits;
- independent review requirements;
- escalation conditions;
- final acceptance.

## Out-of-scope work

When a specialist discovers useful work outside the current objective:

1. do not silently expand scope;
2. record a follow-up candidate with evidence;
3. create an issue only if issue tooling exists and the workflow explicitly permits it.
