---
name: agentic-harness-refiner
description: Audit and safely refine an existing Adaptive Agentic Engineering harness using persistent runtime evidence. Use for harness drift, repeated failures, reviewer findings, agent performance, routing/budget tuning, stale commands, role changes, regression patterns, and conservative project-to-global promotion review.
metadata:
  version: "2.0.0"
  engine: "Adaptive Agentic Engineering Engine v2"
---

# Agentic Harness Refiner v2

Keep the harness aligned with the repository and improve future behavior from evidence without uncontrolled self-modification.

## Modes

- **audit** — inspect repository/config/runtime drift; read-only;
- **refine** — apply the smallest evidence-backed project-local change;
- **promotion-review** — decide whether a project lesson is a candidate for explicit human-approved global promotion.

If evidence is weak, default to audit.

## Persistent evidence model

Initialize or summarize:

```bash
python3 <skill-dir>/scripts/evidence_store.py init .
python3 <skill-dir>/scripts/evidence_store.py summary .
python3 <skill-dir>/scripts/evidence_store.py candidates .
```

Evidence includes:

- runs;
- failures and classifications;
- decisions/routing deviations;
- verification results;
- reviewer findings;
- agent results/performance signals;
- retries;
- learned patterns;
- refinement outcomes.

Lifecycle hooks provide baseline automatic evidence. The orchestrator should add task-specific evidence where richer semantics are needed.

Do not store secrets, full transcripts, or large raw logs in durable evidence.

## Audit

Run:

```bash
python3 <skill-dir>/scripts/harness_audit.py .
```

Audit combines:

- deterministic harness validation;
- repository security-zone drift;
- stale command sources;
- persistent runtime evidence;
- repeated cross-task patterns eligible for refinement review.

Audit is read-only.

## Refinement eligibility

A harness change needs evidence such as:

- same failure class across at least two independent tasks;
- repeated reviewer finding the harness could catch earlier;
- repeated manual routing to the same capability;
- measurable agent-role failure/retry imbalance;
- verified repository architecture/tooling change;
- stale verification command;
- repeated procedure that benefits from a project skill.

One unusual failure is not enough.

## Smallest-target rule

Choose the narrowest durable target:

| Evidence | Preferred target |
|---|---|
| repo-wide invariant | `AGENTS.md` |
| orchestration behavior | `.agentic/workflow.yaml` + `WORKFLOW.md` |
| verification gap | `.agentic/commands.yaml` / `VERIFICATION.md` |
| routing/model/reasoning issue | `.agentic/routing.yaml` or one role TOML |
| retry/concurrency issue | `.agentic/budgets.yaml` |
| repeated procedure | project `.agents/skills/<skill>/` |
| changed security zone | `harness.yaml` risk profile / security policy |

Never rewrite all role prompts because one role failed once.

## Controlled refinement workflow

1. capture evidence ids/task ids supporting the proposal;
2. inspect git status and preserve unrelated work;
3. define expected behavior change and rollback;
4. patch the smallest project-local component;
5. run Validator v2;
6. run relevant harness self-tests if engine files changed;
7. inspect diff;
8. append `refinement_applied` evidence;
9. mark the outcome `pending` until later tasks demonstrate improvement.

A syntactically valid refinement is not automatically an effective refinement.

## Agent performance

Do not rank agents by raw completion count alone. Use evidence such as:

- verification pass/fail outcomes;
- retry frequency;
- repeated reviewer rejection categories;
- blocked permission requests;
- task type/risk;
- whether the role was used outside its intended scope.

Only tune model/reasoning/concurrency after accounting for task difficulty and role scope.

## Promotion review

Global promotion is never automatic.

A candidate must:

- repeat across independent tasks and preferably multiple repositories;
- be generalized without repository-specific paths/names;
- improve reliability, security, or efficiency;
- preserve least privilege;
- have a rollback path;
- be explicitly approved before modifying user/global skills.

Return a proposal, not a mutation:

```yaml
candidate: true | false
evidence: []
generalized_rule: ...
repo_specific_details_removed: []
recommended_global_target: ...
risks: []
validation_needed: []
```

## Final output

```yaml
mode: audit | refine | promotion-review
status: complete | partial | blocked
evidence_used: []
changes: []
validation: []
expected_effect: []
outcome: pending | improved | ineffective | reverted
promotion_candidates: []
remaining_risks: []
```
