# Optional QA / Long-Running Discovery Profile

Enable only for QA-heavy, exploratory, or repeated-system-testing repositories.

## Knowledge

Stable discovered facts:

- modules/pages/routes;
- important actions;
- APIs;
- role/permission relationships;
- data entities;
- known environment constraints.

Do not store transient test results as stable knowledge.

## Coverage

Track what was exercised and at what depth:

```yaml
surface: general-ledger
status: partial
covered:
  - create
  - edit
not_covered:
  - export
  - permission-boundaries
last_run: YYYY-MM-DD
```

## Checkpoints

Store a small durable continuation point for long runs:

```yaml
objective: ...
last_completed_area: ...
next_area: ...
open_findings: []
blocking_conditions: []
```

## Rule

Knowledge, Coverage, and Checkpoints serve different purposes. Never merge them into one giant memory file.
