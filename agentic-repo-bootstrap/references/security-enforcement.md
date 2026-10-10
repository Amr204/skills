# Security Enforcement

Prompt rules are guidance, not the primary boundary. v2 uses layered enforcement.

## Layers

1. **Codex sandbox / approval policy**: reviewer, explorer, architect, and verifier roles default to `read-only`; implementation workers use `workspace-write` with approval policy appropriate to project risk.
2. **Validator v2**: rejects invalid TOML/YAML, unsafe `danger-full-access`, writable review roles, contradictory routing, unsafe paths/commands, missing required security hooks, writer network access without a harness waiver, and writable roots outside the repository without an explicit waiver.
3. **PreToolUse hook**: blocks a small set of high-confidence destructive shell commands and path-escape writes. Keep this deny list deliberately narrow to avoid pretending a hook parser is a full shell sandbox.
4. **Execution isolation**: parallel writers must have non-overlapping write claims or isolated Git worktrees.
5. **Independent verification**: critical changes cannot be approved only by the implementing role.

## Full-access policy

`danger-full-access` is not a normal project-agent mode. Validator v2 rejects it by default and always rejects it for review/security/architecture/exploration/verifier roles. If an exceptional project-level waiver is introduced, it must be explicit, narrow, reviewed, and never used as a shortcut around isolation or verification.

## Trust boundary

Hooks improve policy enforcement but are not a complete containment boundary. Untrusted repositories or commands still require an external sandbox/restricted environment when appropriate.

## Writer network / writable-root policy

The v2 harness defaults both `security.allow_network_access_for_writers` and `security.allow_external_writable_roots` to `false`. Enable either only as an explicit project-level security decision. The validator treats unapproved expansion as an error.
