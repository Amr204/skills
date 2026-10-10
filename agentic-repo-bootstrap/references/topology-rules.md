# Agent Topology Rules

## Core principle

Use the smallest useful team. More agents increase token use and coordination cost.

## Six role archetypes

### repository-explorer

Use for large or unfamiliar codebases where read-heavy mapping materially reduces implementation risk.

Do not use when the relevant files and execution path are already obvious.

### architecture-advisor

Use for cross-boundary design, major refactors, public contracts, distributed state, migrations, or changes with meaningful architectural tradeoffs.

Do not give it final authority; the parent decides.

### implementation-worker

Use for focused code changes where a dedicated write-capable worker helps isolate implementation context.

Prefer built-in `worker` if no project-specific specialization is needed.

### test-verifier

Use where independent execution of tests, reproduction, regression design, or evidence gathering materially improves confidence.

Default it to read-only verification. If authoring new tests requires writes, create a separate bounded write-capable task rather than silently escalating the verifier.

### security-reviewer

Use for auth, authorization, cryptography, secrets, payments, network/security controls, IAM, unsafe deserialization, injection surfaces, or other high-impact trust boundaries.

Default read-only.

### independent-reviewer

Use for high-risk or critical changes and for final diff review where the implementer must not be the sole reviewer.

Default read-only.

## Role selection matrix

| Situation | Suggested topology |
|---|---|
| tiny / obvious / low risk | parent or built-in worker only |
| medium feature | implementation-worker + test-verifier |
| unfamiliar cross-module feature | repository-explorer + implementation-worker + test-verifier |
| architectural change | architecture-advisor + implementation-worker + test-verifier + independent-reviewer |
| security-sensitive change | implementation-worker + test-verifier + security-reviewer + independent-reviewer |
| critical cross-system change | architecture-advisor + explorer + implementation-worker + test-verifier + security-reviewer + independent-reviewer |

This is guidance, not a rigid state machine.

## Sandbox policy

- exploration/review roles: read-only by default;
- implementation: workspace-write;
- test verifier: read-only; test-authoring writes are a separate bounded implementation task;
- security reviewer: read-only unless remediation is a separate explicit task.

## Model policy

The bundled blueprints include v2 routing defaults, but bootstrap must confirm model availability in the active Codex environment and may adapt model slugs while preserving intent.

Use faster/lower-cost models for read-heavy bounded scans and stronger reasoning for architecture/security/critical review. Never trade down sandbox or review independence to compensate for model availability.
