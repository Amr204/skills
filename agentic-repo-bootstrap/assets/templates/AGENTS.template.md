# Project Agentic Engineering Contract

This repository uses Adaptive Agentic Engineering Engine v2.

## Authority

The parent Codex agent owns task interpretation, decomposition, delegation, integration, conflict resolution, and final acceptance. Specialized subagents own only the bounded work delegated to them.

## Machine-readable policy

Treat these files as authoritative execution policy and keep human docs consistent with them:
- `.agentic/harness.yaml`
- `.agentic/routing.yaml`
- `.agentic/budgets.yaml`
- `.agentic/workflow.yaml`
- `.agentic/commands.yaml`

If policy is invalid, stop and repair/validate the harness before normal implementation work.

## Delegation

- Use the minimum useful team.
- Give subagents only context required for their task.
- Parallelize independent read-only work.
- Parallel write work requires disjoint write claims or isolated Git worktrees; otherwise serialize.
- Do not let an implementation agent be the only reviewer of a critical change.

## Verification

Every implementation must be checked against explicit acceptance criteria using the repository's real verification commands. A failed verification is classified before retry. Retry and repair loops are bounded by `.agentic/budgets.yaml`.

## Security

- Follow project sandbox and approval policies.
- Reviewer/explorer/architecture/security/verifier roles are least-privilege and read-only by default.
- `danger-full-access` is forbidden unless an exceptional explicit policy waiver passes Validator v2; it is never appropriate for review-oriented roles.
- Project hooks are defense-in-depth, not a substitute for OS/container isolation when handling untrusted code.

## Evidence and refinement

Record material runs, decisions, failures, retries, verification results, reviewer findings, agent outcomes, and learned patterns under `.agentic/evidence/`.

Refinement must be evidence-backed, minimal, project-local by default, validated after change, and never silently promote project behavior into a global Skill.
