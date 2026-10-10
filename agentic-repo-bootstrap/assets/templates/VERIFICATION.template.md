# Verification Policy

Verification is blocking when `.agentic/harness.yaml` sets `verification.required: true`.

## Evidence

For every material implementation, preserve:
- command executed,
- working directory,
- exit/result status,
- relevant bounded output or failure summary,
- diff inspected,
- reviewer/security findings when required.

Use only commands discovered from repository evidence or explicitly approved and recorded in `.agentic/commands.yaml`.

## Failure handling

A failure must be classified before retry (implementation, test expectation, environment/infrastructure, dependency, security, or unknown). Repeating an unchanged failing strategy is blocked after the configured budget.

## Critical changes

Security-sensitive or otherwise critical changes require the configured security review and an independent acceptance perspective. Passing tests alone is not sufficient evidence of security correctness.
