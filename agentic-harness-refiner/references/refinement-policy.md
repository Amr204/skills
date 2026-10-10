# Evidence-Backed Refinement Policy

Refinement is controlled maintenance, not unrestricted self-modification.

## Eligible evidence

Use persisted events under `.agentic/evidence/`: failures, retries, verification results, reviewer findings, decisions, agent results, and learned patterns.

A refinement candidate should normally be supported by repeated evidence across at least two independent task IDs, unless it closes a severe deterministic safety/configuration defect.

## Smallest-target rule

Change the smallest durable component that fixes the observed problem:
1. command or verification definition,
2. task-contract rule,
3. role definition or routing policy,
4. project Skill/reference,
5. `AGENTS.md` / workflow policy.

Do not rewrite the entire harness because one run failed.

## Controlled apply

1. summarize evidence,
2. state the proposed change and expected behavior,
3. validate the proposed files,
4. apply project-local change,
5. run regression/self-tests relevant to the change,
6. record `refinement_applied`,
7. observe subsequent runs and record `refinement_outcome`.

Global/personal Skill changes are proposals only unless explicitly reviewed and approved.
