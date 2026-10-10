# Task Contracts v2

Every delegated task should be self-contained enough that a child does not need the entire parent context.

Recommended fields:
- `task_id`
- `objective`
- `risk`
- `owner_role`
- `required_context`
- `dependencies`
- `allowed_reads`
- `allowed_writes`
- `forbidden_scope`
- `acceptance_criteria`
- `verification_commands`
- `expected_output`
- `retry_limit`
- `stop_condition`

For writers, `allowed_writes` doubles as an ownership claim. For reviewers, `allowed_writes` should normally be empty.

Return structured evidence: status, files changed/inspected, commands run, results, findings, unresolved risks, and assumptions.
