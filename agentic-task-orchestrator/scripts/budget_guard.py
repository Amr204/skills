#!/usr/bin/env python3
from __future__ import annotations
import os
import sys
from pathlib import Path

def _runtime_root() -> Path:
    base = Path(os.environ.get("AGENTS_HOME", str(Path.home() / ".agents"))).expanduser()
    return base / "adaptive-agentic-engineering-engine-v2"

def _maybe_reexec_runtime_python() -> None:
    runtime = _runtime_root()
    if runtime is None:
        return
    py = runtime / ".venv" / "bin" / "python"
    if os.name == "nt":
        py = runtime / ".venv" / "Scripts" / "python.exe"
    try:
        same = Path(sys.executable).resolve() == py.resolve()
    except Exception:
        same = False
    if py.exists() and not same and os.environ.get("AE_ENGINE_REEXEC") != "1":
        env = dict(os.environ); env["AE_ENGINE_REEXEC"] = "1"
        os.execve(str(py), [str(py), str(Path(__file__).resolve()), *sys.argv[1:]], env)

def _engine_path() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "engine"
        if (candidate / "agentic_engine").is_dir():
            return candidate
    installed = _runtime_root() / "engine"
    if installed.is_dir():
        return installed
    raise SystemExit("Adaptive Agentic Engineering Engine v2 runtime not found. Re-run the v2 installer.")

_maybe_reexec_runtime_python()
sys.path.insert(0, str(_engine_path()))
from agentic_engine.budget import main

if __name__ == "__main__":
    raise SystemExit(main())
