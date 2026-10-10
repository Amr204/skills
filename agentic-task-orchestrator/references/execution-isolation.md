# Execution Isolation

Parallel read work is cheap; parallel writes require ownership.

## Default policy

- Read-only subtasks may run concurrently up to the configured agent budget.
- Two write tasks may run concurrently only when their write sets are demonstrably disjoint **or** each runs in its own Git worktree.
- If ownership cannot be proven, run serially.

## Write claims

Before a parallel writer starts:

```bash
python scripts/isolation.py --root . claim TASK-ID path/one path/two --mode write
```

A conflicting claim fails with exit code 2. Release the claim when integrated:

```bash
python scripts/isolation.py --root . release TASK-ID
```

## Worktrees

For broader independent implementation:

```bash
python scripts/isolation.py --root . worktree-create TASK-ID --base HEAD
```

Detached is the safer default. If a dedicated branch is useful, request one explicitly with `--branch <validated-name>`; the isolation engine rejects invalid or already-existing branch names. The parent owns integration. Removal refuses a dirty worktree unless explicitly forced.

The write-claim registry also enforces the configured `max_parallel_writers` limit and can prune sufficiently old claims whose owning process no longer exists.

## Integration rule

Child work is not accepted merely because it exists in a worktree. The parent must inspect the diff, run the relevant verification in the integration state, and resolve cross-task assumptions before final acceptance.
