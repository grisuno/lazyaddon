"""Shared fixtures for the lazyaddon test suite.

Provides a fake :class:`ProcessRunner` that records invocations instead of
launching real subprocesses, and reusable addon YAML documents.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest

from lazyaddon.config import AddonConfig
from lazyaddon.runner import CommandResult


class FakeRunner:
    """In-process substitute for :class:`CommandRunner`."""

    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []
        self.returncode = 0
        self.stdout = "fake-out"

    def run(
        self,
        command: str,
        cwd: str | Path | None = None,
        env: Mapping[str, str] | None = None,
        timeout: int | None = None,
    ) -> CommandResult:
        self.calls.append(
            {
                "command": command,
                "cwd": str(cwd) if cwd else None,
                "env": dict(env) if env else None,
                "timeout": timeout,
            }
        )
        return CommandResult(command, self.returncode, self.stdout, "")

    def last(self) -> dict[str, Any]:
        """Return the most recent invocation."""
        return self.calls[-1]

    @property
    def commands(self) -> list[str]:
        """Return all recorded command strings."""
        return [c["command"] for c in self.calls]


BEACON_ADDON = {
    "name": "beacon",
    "description": "Builds a beacon.",
    "author": "Red Team",
    "version": "1.0",
    "enabled": True,
    "os": "any",
    "category": "10. Command & Control",
    "params": [
        {"name": "lhost", "type": "string", "required": True, "description": "Listener."},
        {"name": "lport", "type": "string", "default": "4444"},
    ],
    "trigger": [],
    "tool": {
        "name": "beacon",
        "repo_url": "https://github.com/grisuno/beacon.git",
        "install_path": "c2/beacon",
        "install_command": "make windows",
        "execute_command": "./gen.sh --lhost {lhost} --lport {lport}",
        "lazycommand": "encode --in out.bin",
        "env": {"AES": "{aes_key}"},
    },
}


def make_config(tmp_path: Path) -> AddonConfig:
    """Build an isolated config rooted at ``tmp_path``."""
    return AddonConfig(
        addons_dir=str(tmp_path / "addons"),
        install_root=str(tmp_path / "external"),
    )


@pytest.fixture
def runner() -> FakeRunner:
    """Yield a fresh fake process runner."""
    return FakeRunner()
