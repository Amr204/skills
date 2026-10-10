# Harness Drift Audit

Audit compares durable project policy against current repository evidence.

Check:
- repository languages/frameworks/manifests/package managers versus `harness.yaml`,
- security-sensitive areas versus risk profile,
- current test/lint/typecheck/build commands versus `commands.yaml`,
- project agents versus routing model/reasoning/sandbox/approval settings,
- routing concurrency versus budgets,
- security hook presence/configuration,
- stale or unsafe command paths,
- evidence trends: repeated failures, retries, reviewer findings, underperforming roles.

Drift is a finding, not automatic permission to modify global policy.
