"""Process execution and addon dispatch contract.

``CommandRunner`` wraps :func:`subprocess.run` behind a small, injectable
interface so tests can substitute a fake runner without launching real
processes. ``AddonRunner`` turns a validated ``AddonSpec`` into an executed
command, resolving placeholders, applying environment overrides and delegating
framework-specific hooks (lazy/remote/upload/download commands) to the host
application through an extensible hook registry.

Values that flow in from the runtime ``params`` mapping are treated as
untrusted and shell-quoted before substitution, unless the value is declared
as a trusted default inside the same YAML document.
"""

from __future__ import annotations

import os
import subprocess  # nosec B404
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from .config import AddonConfig
from .models import AddonSpec
from .placeholders import PlaceholderEngine


@dataclass(frozen=True)
class CommandResult:
    """Outcome of a shell command execution.

    Attributes:
        command: The fully resolved command that was executed.
        returncode: Process exit code.
        stdout: Captured standard output text.
        stderr: Captured standard error text.
    """

    command: str
    returncode: int
    stdout: str = ""
    stderr: str = ""

    @property
    def ok(self) -> bool:
        """True when the process exited with code zero."""
        return self.returncode == 0


class ProcessRunner(Protocol):
    """Minimal protocol satisfied by :class:`CommandRunner` and test fakes."""

    def run(
        self,
        command: str,
        cwd: str | os.PathLike[str] | None = None,
        env: Mapping[str, str] | None = None,
        timeout: int | None = None,
    ) -> CommandResult:
        """Execute ``command`` and return its result."""


class CommandRunner:
    """Executes shell command strings via :func:`subprocess.run`.

    Args:
        timeout_seconds: Default timeout applied when none is passed.
        environment: Base environment merged with per-call overrides.
    """

    def __init__(
        self,
        timeout_seconds: int,
        environment: Mapping[str, str] | None = None,
    ) -> None:
        self._timeout = timeout_seconds
        self._base_env = dict(environment or {})

    def run(
        self,
        command: str,
        cwd: str | os.PathLike[str] | None = None,
        env: Mapping[str, str] | None = None,
        timeout: int | None = None,
    ) -> CommandResult:
        """Execute ``command`` under a shell and capture its output.

        Args:
            command: Shell command string.
            cwd: Working directory for the subprocess.
            env: Extra environment overrides merged over the base environment.
            timeout: Seconds to wait before raising; defaults to the runner's
                configured timeout.

        Returns:
            The captured command result.

        Raises:
            subprocess.TimeoutExpired: If the command exceeds the timeout.
        """
        merged_env = dict(os.environ)
        merged_env.update(self._base_env)
        if env:
            merged_env.update(env)
        completed = subprocess.run(
            command,
            shell=True,  # nosec B602
            cwd=cwd,
            env=merged_env,
            capture_output=True,
            text=True,
            timeout=timeout or self._timeout,
            check=False,
        )
        return CommandResult(
            command=command,
            returncode=completed.returncode,
            stdout=completed.stdout or "",
            stderr=completed.stderr or "",
        )


class AddonHook(Protocol):
    """Protocol for a single extensible lazyaddon hook.

    Implementations are provided by the host application to handle
    framework-specific command families (lazycommand, remote_command,
    upload_file, download_file). Returning normally indicates success.
    """

    def __call__(self, kind: str, payload: str, env: Mapping[str, str]) -> None:
        """Handle one hook payload.

        Args:
            kind: Hook kind, e.g. ``lazy``, ``remote``, ``upload``, ``download``.
            payload: Comma-separated payload string resolved against params.
            env: Resolved environment variables for the addon.
        """


@dataclass
class AddonRunner:
    """Resolves and dispatches an addon's executable command.

    Args:
        config: Engine configuration.
        runner: Process runner used for the primary execute command.
        placeholders: Placeholder engine used for token substitution.
        hooks: Mapping of hook kind to host-implemented handler. Any kind
            without a handler is skipped.
    """

    config: AddonConfig
    runner: ProcessRunner
    placeholders: PlaceholderEngine
    hooks: Mapping[str, AddonHook] | None = None

    def execute(
        self,
        addon: AddonSpec,
        params: Mapping[str, Any],
        extra_args: tuple[str, ...] = (),
        cwd: str | None = None,
        untrusted_keys: set[str] | frozenset[str] | None = None,
    ) -> CommandResult:
        """Resolve and run the addon's ``execute_command``.

        Args:
            addon: The addon to execute.
            params: Runtime parameter values.
            extra_args: Extra positional arguments appended to the command.
            cwd: Working directory; when None, runs from the addon's
                ``install_path`` if present, else the current directory.
            untrusted_keys: Param names whose values must be shell-quoted.
                When None, every key without a trusted YAML default is treated
                as untrusted.

        Returns:
            The result of the executed command.

        Raises:
            ValueError: If the addon has no ``execute_command``.
        """
        tool = addon.tool
        if not tool.execute_command:
            raise ValueError(f"addon '{addon.name}' has no execute_command")
        if untrusted_keys is None:
            untrusted_keys = self._default_untrusted(addon)
        resolved = self.placeholders.resolve(tool.execute_command, params, untrusted_keys=untrusted_keys)
        if extra_args:
            resolved = f"{resolved} {' '.join(extra_args)}"
        resolved_env = self._resolve_env(addon, params, untrusted_keys)
        run_cwd = cwd or self._tool_cwd(addon)
        result = self.runner.run(resolved, cwd=run_cwd, env=resolved_env or None)
        self._dispatch_hooks(addon, params, untrusted_keys, resolved_env)
        return result

    def dispatch_hooks(
        self,
        addon: AddonSpec,
        params: Mapping[str, Any],
        untrusted_keys: set[str] | frozenset[str] | None = None,
    ) -> None:
        """Dispatch framework-specific hooks declared on an addon.

        Args:
            addon: The addon whose hooks should fire.
            params: Runtime parameter values.
            untrusted_keys: Param names to treat as untrusted (quoted). When
                None, every key without a trusted YAML default is untrusted.
        """
        if untrusted_keys is None:
            untrusted_keys = self._default_untrusted(addon)
        resolved_env = self._resolve_env(addon, params, untrusted_keys)
        self._dispatch_hooks(addon, params, untrusted_keys, resolved_env)

    def _dispatch_hooks(
        self,
        addon: AddonSpec,
        params: Mapping[str, Any],
        untrusted: set[str] | frozenset[str],
        env: Mapping[str, str],
    ) -> None:
        tool = addon.tool
        families: list[tuple[str, str]] = [
            ("lazy", tool.lazycommand),
            ("remote", tool.remote_command),
            ("upload", tool.upload_file),
            ("download", tool.download_file),
        ]
        for kind, payload in families:
            if not payload:
                continue
            resolved_payload = self.placeholders.resolve(payload, params, untrusted_keys=untrusted)
            handler = self.hooks.get(kind) if self.hooks else None
            if handler is None:
                continue
            handler(kind, resolved_payload, env)

    def _resolve_env(
        self,
        addon: AddonSpec,
        params: Mapping[str, Any],
        untrusted: set[str] | frozenset[str],
    ) -> dict[str, str]:
        resolved: dict[str, str] = {}
        for key, value in addon.tool.env.items():
            resolved[str(key)] = self.placeholders.resolve(value, params, untrusted_keys=untrusted)
        return resolved

    def _default_untrusted(self, addon: AddonSpec) -> set[str]:
        return {param.name for param in addon.params if param.default is None}

    def _tool_cwd(self, addon: AddonSpec) -> str | None:
        tool = addon.tool
        if not tool.install_path:
            return None
        root = Path(self.config.install_root).expanduser().resolve()
        return str(root / tool.install_path)
