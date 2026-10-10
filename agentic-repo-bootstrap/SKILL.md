---
name: agentic-repo-bootstrap
description: Bootstrap or upgrade a repository into a production-grade native Codex multi-agent engineering harness, or turn a raw project idea into a validated project foundation first. Use for repository setup, multi-agent harness creation, agent topology, idea-to-project architecture/scaffolding, Codex roles, routing, budgets, hooks, verification, and safe execution policies.
metadata:
  version: "2.0.0"
  engine: "Adaptive Agentic Engineering Engine v2"
---

# Agentic Repository Bootstrap v2

Create the smallest production-grade Codex harness justified by evidence. Preserve existing repository architecture and tooling. Do not install a fixed list of agents merely because templates exist.

## Modes

Choose one mode from the user's intent.

### Repository mode

Use when a repository already contains implementation or meaningful project structure.

### Idea mode

Use when the user starts with only a raw idea or an effectively empty repository. Follow the staged flow in [Idea to Project](references/idea-to-project.md):

`idea -> requirements -> assumptions -> NFRs -> architecture -> threat model -> stack -> scaffold -> tooling -> CI/CD -> agent harness -> implementation plan`

Do not scaffold code until assumptions, NFRs, major trust boundaries, and stack choice are explicit enough to avoid rework.

## Non-negotiable architecture

- The parent Codex thread owns user intent, decomposition, routing, dependency decisions, integration, and final acceptance.
- Agent role definitions describe capabilities; task contracts describe one assignment; workflow policy describes boundaries and evidence. Do not merge these concepts.
- Prefer objectives plus tools/context over rigid state-machine micro-steps.
- Use the minimum useful agent team.
- Read/review roles default to least privilege.
- Parallel write work requires isolation or explicit non-overlapping ownership.
- A self-reported success is never verification evidence.
- Harness refinement is evidence-driven and cannot silently modify user/global skills.

## Repository mode procedure

### 1. Preflight

Before modifying anything:

1. inspect `git status` and preserve unrelated work;
2. read existing `AGENTS.md` hierarchy and project instructions;
3. inspect existing `.codex/`, `.agents/skills/`, `.agentic/`, CI, manifests, build/test config;
4. run Repository Discovery v2:

```bash
python3 <skill-dir>/scripts/inspect_repo.py .
```

Discovery is evidence-oriented. Confirm its candidate commands and important classifications against native manifests before generating durable policy.

### 2. Classify the project

Determine from evidence:

- project shape and monorepo boundaries;
- languages/frameworks/package managers;
- package/service ownership boundaries;
- native build/test/lint/typecheck commands;
- CI system and required gates;
- security-sensitive zones;
- likely risk profile;
- whether QA-style Knowledge/Coverage/Checkpoints are useful.

Do not infer sensitive code from arbitrary substring matches. For example, `contest.ts` is not a test merely because it contains `test`, and `session-notes.md` is not auth code merely because it contains `session`.

### 3. Choose adaptive role topology

Use [Topology rules](references/topology-rules.md). Start with built-in parent/worker capabilities. Materialize custom roles only when specialization repeatedly improves context isolation, security, verification, or architecture quality.

Available blueprints:

- `repository-explorer`
- `architecture-advisor`
- `implementation-worker`
- `test-verifier`
- `security-reviewer`
- `independent-reviewer`

The role files contain model, reasoning effort, sandbox, approval, and behavioral defaults. Adapt model slugs only when the current Codex environment requires it; keep the least-privilege intent.

### 4. Generate the machine-readable contract

Create `.agentic/` using the templates under `assets/templates/`:

- `harness.yaml` — top-level contract;
- `routing.yaml` — per-role model/reasoning/sandbox/permissions/concurrency/retry policy;
- `budgets.yaml` — bounded retries, repair loops, parallelism, optional token/context budgets;
- `workflow.yaml` — deterministic orchestration invariants without over-constraining agent reasoning;
- `commands.yaml` — only commands verified from repository evidence;
- `WORKFLOW.md` — readable explanation and task-contract conventions;
- `VERIFICATION.md` — proof requirements and failure classification;
- `evidence/` — initialize persistent runtime evidence.

Keep v1 Markdown files compatible, but v2 machine-readable policy is the source for deterministic validation.

### 5. Configure Codex enforcement

Create or merge `.codex/config.toml` conservatively.

Default local posture:

- `sandbox_mode = "workspace-write"` for the parent;
- `approval_policy = "on-request"`;
- hooks enabled;
- bounded multi-agent concurrency;
- review/exploration custom roles override to `read-only`.

Never introduce `danger-full-access` merely to avoid permission friction.

Copy the project hooks from `assets/hooks/` into `.codex/hooks/` and configure `.codex/hooks.json` from the template. Hooks are a guardrail, not the only security boundary: sandbox and approval settings remain authoritative.

### 6. Preserve human-readable guidance

Create/update root `AGENTS.md` using `assets/templates/AGENTS.template.md`. Keep it concise. Put detailed routing, budgets, verification, and evidence procedures in `.agentic/` or project skills instead of inflating `AGENTS.md`.

### 7. Initialize evidence

```bash
python3 ../agentic-harness-refiner/scripts/evidence_store.py init .
```

If the sibling skill path is unavailable, create `.agentic/evidence/events.jsonl` and let the refiner initialize it on first use.

### 8. Validate before declaring success

Run:

```bash
python3 <skill-dir>/scripts/validate_harness.py .
```

Validation errors are blocking. Fix them before final acceptance. Do not downgrade structural or security errors to prose warnings.

Review the final git diff and confirm no unrelated project files changed.

## Idea mode procedure

Read [Idea to Project](references/idea-to-project.md).

1. Convert the raw idea into a structured `idea-spec.yaml` matching the bundled schema.
2. Validate it with:

```bash
python3 <skill-dir>/scripts/idea_project.py idea-spec.yaml --root .
```

3. Resolve material assumptions before stack/scaffold decisions.
4. Produce requirements/NFR/architecture/threat-model/stack/CI-CD decisions.
5. Scaffold using the selected stack's native tooling; do not invent package commands.
6. Verify the scaffold builds/tests before layering in the agent harness.
7. Run the normal repository-mode bootstrap against the newly created repository.
8. Finish with an implementation plan whose dependencies can be executed as a DAG when useful.

The optional `--write-planning-docs` flag creates planning documents only and refuses to overwrite existing files.

## Security rules

Read [Security enforcement](references/security-enforcement.md).

- Reviewers, security reviewers, architecture advisors, explorers, and default verifiers are read-only.
- The validator rejects inappropriate `danger-full-access` and conflicting sandbox/permission configuration.
- Project hooks block a small high-confidence set of destructive shell/edit patterns.
- Hooks do not replace OS/container isolation for untrusted code.
- Do not auto-enable network access for write-capable agents.
- Do not auto-configure external MCP servers or secrets.

## Compatibility

Preserve the useful v1 architecture and skill names. The validator accepts a v1 harness manifest with a deprecation warning, but new bootstraps MUST emit schema version `2.0`.

## Completion output

Return a concise report:

```yaml
mode: repository | idea
status: complete | partial | blocked
project_shape: {}
roles_created: []
roles_skipped: []
security_posture: {}
routing_policy: {}
budgets: {}
commands_verified: []
hooks_installed: []
validation:
  status: pass | fail
  errors: 0
  warnings: 0
remaining_risks: []
```
