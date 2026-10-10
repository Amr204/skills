# Repository Discovery

## Goal

Build an evidence-based project map before creating any harness files.

## Fast inventory

Inspect, as applicable:

- git root and status;
- top-level directories;
- package manifests and lockfiles;
- language/project files (`pyproject.toml`, `package.json`, `.csproj`, `go.mod`, `Cargo.toml`, etc.);
- container and deployment files;
- CI workflows;
- test directories and test runner config;
- lint/type-check config;
- security or dependency scanning config;
- existing docs and agent instructions;
- API/schema/migration directories;
- generated/vendor directories.

## Evidence hierarchy

Prefer:

1. executable config and scripts;
2. CI definitions;
3. package manifests;
4. current source structure;
5. maintained documentation;
6. comments / stale docs last.

When sources disagree, record the discrepancy instead of guessing.

## Discovery outputs

Summarize:

```yaml
project_shape:
languages: []
frameworks: []
entry_points: []
boundaries: []
build_commands: []
test_commands: []
lint_commands: []
typecheck_commands: []
security_checks: []
ci: []
critical_zones: []
existing_agentic_files: []
do_not_edit: []
unknowns: []
```

## Stop condition

Discovery is sufficient when the bootstrap can make safe decisions about:

- which agents are useful;
- which files agents may touch;
- what checks prove completion;
- what areas require elevated review.
