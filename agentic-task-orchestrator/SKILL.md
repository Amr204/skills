---
name: agentic-task-orchestrator
description: Execute non-trivial engineering work through the repository's Adaptive Agentic Engineering harness. Use for decomposition, adaptive subagent routing, dependency DAGs, context isolation, parallel/serial scheduling, safe worktree isolation, budgets, retries, verification gates, independent review, security review, and proof-of-work.
metadata:
  version: "2.0.0"
  engine: "Adaptive Agentic Engineering Engine v2"
---

# Agentic Task Orchestrator v2

Operate the harness created by `agentic-repo-bootstrap`. The parent thread remains the orchestrator and final authority.

## Start with repository policy

Read, when present:

- `AGENTS.md` chain;
- `.agentic/harness.yaml`;
- `.agentic/routing.yaml`;
- `.agentic/budgets.yaml`;
- `.agentic/workflow.yaml`;
- `.agentic/commands.yaml`;
- `.agentic/WORKFLOW.md`;
- `.agentic/VERIFICATION.md`;
- `.codex/agents/*.toml`.

If v2 machine-readable policy exists and fails validation, do not start a complex multi-agent run until the invalid harness is repaired or the user explicitly chooses a safe single-agent fallback.

## 1. Classify the task

Determine:

- objective and acceptance criteria;
- risk: `low | medium | high | critical`;
- affected ownership boundaries;
- known dependencies/blockers;
- read-heavy vs write-heavy work;
- whether a custom specialist materially improves the result.

Increasing risk should primarily increase independent evidence, not agent count.

## 2. Build a compact task DAG only when needed

Use dependencies to identify what can start now. Avoid turning a single coherent task into dozens of tiny nodes.

Task contracts follow [Task contracts](references/task-contracts.md): objective, minimal context, allowed/forbidden scope, dependencies, acceptance criteria, verification, expected return, stop condition.

## 3. Route adaptively

Use `.agentic/routing.yaml` as policy, not a guarantee that every model is available. Respect per-role:

- model;
- reasoning effort;
- sandbox;
- approval posture;
- logical permissions;
- concurrency;
- retry limit.

Typical intent:

- discovery/read-heavy mapping -> faster efficient model;
- architecture/security/critical review -> stronger reasoning;
- implementation -> capable write worker;
- final reviewer -> independent strong reasoning, read-only.

If a configured model is unavailable, choose the closest available model while preserving reasoning and permission intent; record the routing deviation as evidence.

## 4. Enforce budgets before retries/spawns

Before retrying a failed strategy:

```bash
python3 <skill-dir>/scripts/budget_guard.py . <task-id> --strategy "<short strategy>" --agent-role <role>
```

A blocked budget is an escalation signal, not permission to reset counters. Respect:

- maximum retries;
- repair loops;
- parallel agents;
- parallel writers;
- repeated-strategy failure cap;
- token/context budgets when the active Codex runtime exposes those measurements.

Never invent token accounting when the runtime does not expose it; record it as unavailable.

## 5. Isolation before parallel writes

Read [Execution isolation](references/execution-isolation.md).

Read-only independent agents may share a checkout.

For write-capable work:

1. claim expected paths before scheduling concurrent writers;
2. if claims overlap, serialize or redesign the task split;
3. for independent write tasks, create detached Git worktrees;
4. never force-remove a dirty worktree unless the user explicitly authorizes destructive cleanup.

Examples:

```bash
python3 <skill-dir>/scripts/isolation.py --root . claim TASK-A src/service-a tests/service-a
python3 <skill-dir>/scripts/isolation.py --root . worktree-create TASK-A --base HEAD
```

Release claims/worktrees after integration.

## 6. Record runtime evidence

The feedback loop is not a chat-memory metaphor. Persist useful execution evidence through `agentic-harness-refiner`'s evidence store or project lifecycle hooks.

Record at minimum when applicable:

- run start/completion;
- routing decisions;
- agent results;
- failures and failure class;
- retries;
- verification results;
- reviewer findings;
- useful learned patterns.

For manual evidence entry:

```bash
python3 ../agentic-harness-refiner/scripts/evidence_store.py add . failure TASK-42 \
  --agent-role implementation-worker \
  --strategy "update cache invalidation" \
  --data-json '{"failure_class":"logic","repair_loop":true}'
```

Prefer structured evidence over verbose transcripts.

## 7. Verification and failure routing

Every implementation must cross relevant verification gates from `.agentic/commands.yaml` and `.agentic/VERIFICATION.md`.

On failure:

1. classify `implementation | test | fixture | environment | infrastructure | security | requirement | architecture`;
2. identify the owning role;
3. check budget/repeated-strategy guard;
4. retry only after a meaningful strategy or workspace change;
5. escalate to parent if the same strategy keeps failing.

Do not route every failure back to the implementer.

## 8. Independent review

- Medium risk: independent testing may be enough.
- High risk: require independent review by default.
- Critical: require independent review plus security review when a trust boundary is involved.
- The implementer is never the sole reviewer of critical work.

Reviewers receive the objective, acceptance criteria, diff/evidence, and only the context needed to judge the change.

## 9. Final acceptance

The parent accepts only when evidence demonstrates the requested behavior and required gates passed. Distinguish:

- implementation complete;
- verification complete;
- review approved;
- final acceptance.

These are not synonyms.

## Final output

```yaml
task: ...
risk: low | medium | high | critical
agents_used: []
isolation: none | ownership | worktree | serial
decisions: []
verification: []
review: []
retries: 0
budget_status: within-limits | escalated
final_status: accepted | rejected | blocked | partial
remaining_risks: []
follow_up_candidates: []
```
