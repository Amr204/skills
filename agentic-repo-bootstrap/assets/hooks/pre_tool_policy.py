from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

BLOCK_PATTERNS = [
    (re.compile(r"(^|[;&|]\s*)sudo\b", re.I), "privileged sudo execution is blocked by repository policy"),
    (re.compile(r"\brm\s+-[^\n]*r[^\n]*f\s+/(?:\s|$)", re.I), "destructive root deletion is blocked"),
    (re.compile(r"\bgit\s+reset\s+--hard\b", re.I), "git reset --hard is blocked; preserve user work"),
    (re.compile(r"\bgit\s+clean\s+-[^\n]*f", re.I), "git clean -f is blocked; preserve untracked user work"),
    (re.compile(r"\bcurl\b[^\n|]*\|\s*(?:sh|bash)\b", re.I), "curl-pipe-shell execution is blocked"),
    (re.compile(r"\bwget\b[^\n|]*\|\s*(?:sh|bash)\b", re.I), "wget-pipe-shell execution is blocked"),
    (re.compile(r"\bchmod\s+-R\s+777\b", re.I), "recursive world-writable permissions are blocked"),
    (re.compile(r"(?:>|>>|tee\s+)(?:\s*)(/etc/|/usr/|/bin/|/sbin/|/boot/|/root/)", re.I), "writes to system paths are blocked"),
]
PATCH_ESCAPE = re.compile(r"^\*\*\*\s+(?:Update|Add|Delete)\s+File:\s+(?:/|\.\./)", re.M)


def deny(reason: str) -> dict[str, Any]:
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}


def main() -> int:
    try: payload = json.load(sys.stdin)
    except Exception as exc:
        print(json.dumps(deny(f"invalid hook input: {exc}"))); return 0
    if payload.get("hook_event_name") != "PreToolUse": return 0
    tool = payload.get("tool_name")
    inp = payload.get("tool_input") or {}
    command = inp.get("command") if isinstance(inp, dict) else None
    if not isinstance(command, str): return 0
    if payload.get("permission_mode") == "bypassPermissions":
        # Full-access/bypass mode is never silently trusted for destructive local operations.
        for pat, reason in BLOCK_PATTERNS:
            if pat.search(command): print(json.dumps(deny(reason))); return 0
    if tool == "Bash":
        for pat, reason in BLOCK_PATTERNS:
            if pat.search(command): print(json.dumps(deny(reason))); return 0
    if tool == "apply_patch" and PATCH_ESCAPE.search(command):
        print(json.dumps(deny("patch attempts to modify an absolute or parent path outside the repository"))); return 0
    return 0

if __name__ == "__main__": raise SystemExit(main())
