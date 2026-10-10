#!/usr/bin/env python3
"""Best-effort, dependency-free Codex hook that records bounded runtime evidence.

It never blocks execution. Security blocking belongs in pre_tool_policy.py.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERIFY_RE = re.compile(r"(?:^|\s)(pytest|npm\s+(?:run\s+)?test|pnpm\s+test|yarn\s+test|bun\s+test|cargo\s+test|go\s+test|dotnet\s+test|mvn\s+test|gradle\s+test|ruff\s+check|mypy\b|tsc\b|eslint\b)", re.I)


def root_from_cwd(cwd: str) -> Path | None:
    p = Path(cwd).resolve()
    for candidate in (p, *p.parents):
        if (candidate / ".agentic" / "harness.yaml").exists(): return candidate
        if (candidate / ".git").exists(): return candidate
    return None


def excerpt(value: Any, limit: int = 1200) -> str:
    try: text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    except Exception: text = str(value)
    return text[:limit]


def append_event(root: Path, payload: dict[str, Any], event_type: str, data: dict[str, Any], *, role: str | None = None) -> None:
    d = root / ".agentic" / "evidence"; d.mkdir(parents=True, exist_ok=True)
    path = d / "events.jsonl"
    lock = d / ".hook.lock"
    task_id = str(payload.get("turn_id") or payload.get("session_id") or "unknown")
    event = {
        "schema_version": "1.0", "event_id": uuid.uuid4().hex,
        "timestamp": datetime.now(timezone.utc).isoformat(), "event_type": event_type,
        "task_id": task_id, "agent_role": role, "strategy": None, "data": data,
    }
    deadline = time.monotonic() + 1.5
    fd = None
    while fd is None:
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            if time.monotonic() >= deadline:
                return
            time.sleep(0.02)
    try:
        os.close(fd)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    finally:
        try: lock.unlink()
        except FileNotFoundError: pass


def main() -> int:
    try: payload = json.load(sys.stdin)
    except Exception: return 0
    root = root_from_cwd(str(payload.get("cwd") or "."))
    if root is None: return 0
    event = payload.get("hook_event_name")
    if event == "UserPromptSubmit":
        append_event(root, payload, "run_started", {"model": payload.get("model"), "permission_mode": payload.get("permission_mode")})
    elif event == "SubagentStart":
        append_event(root, payload, "decision", {"action": "subagent_start", "agent_id": payload.get("agent_id"), "model": payload.get("model"), "permission_mode": payload.get("permission_mode")}, role=payload.get("agent_type"))
    elif event == "SubagentStop":
        append_event(root, payload, "agent_result", {"agent_id": payload.get("agent_id"), "result_excerpt": excerpt(payload.get("last_assistant_message")), "transcript_path": payload.get("agent_transcript_path")}, role=payload.get("agent_type"))
    elif event == "PostToolUse" and payload.get("tool_name") == "Bash":
        tool_input = payload.get("tool_input") or {}; command = tool_input.get("command") if isinstance(tool_input, dict) else None
        if isinstance(command, str) and VERIFY_RE.search(command):
            response = payload.get("tool_response")
            status = "observed"
            if isinstance(response, dict):
                code = response.get("exit_code", response.get("returncode", response.get("code")))
                if isinstance(code, int): status = "PASS" if code == 0 else "FAIL"
            append_event(root, payload, "verification", {"command": command[:1000], "status": status, "response_excerpt": excerpt(response)})
    elif event == "Stop":
        append_event(root, payload, "run_completed", {"last_message_excerpt": excerpt(payload.get("last_assistant_message")), "permission_mode": payload.get("permission_mode")})
    return 0

if __name__ == "__main__": raise SystemExit(main())
