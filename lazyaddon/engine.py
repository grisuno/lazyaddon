"""Facade contract orchestrating the lazyaddon lifecycle.

``LazyAddonEngine`` is the single entry point consumers import. It ties
together discovery, schema validation, security policy, installation and
execution, and additionally exposes a marketplace-style ``add``/``remove``
interface so new tools and sources can be registered as YAML addons — the
core "spirit" of lazyaddon: turn any GitHub/GitLab project into an
installable, runnable addon from a single declarative file.
"""

from __future__ import annotations

import logging
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import yaml

from .config import AddonConfig
from .installer import AddonInstaller
from .models import AddonError, AddonSpec, SchemaError
from .placeholders import PlaceholderEngine
from .runner import AddonHook, AddonRunner, CommandResult, CommandRunner, ProcessRunner
from .security import SecurityPolicy

log = logging.getLogger("lazyaddon")

_DEFAULT_DESCRIPTION = "Registered by lazyaddon marketplace."


class LazyAddonEngine:
    """High-level addon management and execution engine.

    Args:
        config: Engine configuration; defaults to a fresh :class:`AddonConfig`.
        runner: Process runner override (mainly for tests).
        hooks: Mapping of hook kind to host-implemented handler.
    """

    def __init__(
        self,
        config: AddonConfig | None = None,
        runner: ProcessRunner | None = None,
        hooks: Mapping[str, AddonHook] | None = None,
    ) -> None:
        self.config = config or AddonConfig()
        self.placeholders = PlaceholderEngine(self.config)
        self.security = SecurityPolicy(self.config)
        self.runner = runner or CommandRunner(
            timeout_seconds=self.config.command_timeout_seconds,
            environment=self.config.environment,
        )
        self.installer = AddonInstaller(self.config, self.runner, self.placeholders, self.security)
        self.hooks = hooks
        self.addons_runner = AddonRunner(self.config, self.runner, self.placeholders, hooks)
        self._registry: dict[str, AddonSpec] = {}

    # ---------------------------------------------------------------- discover --
    def discover(self) -> list[AddonSpec]:
        """Scan ``addons_dir`` and load every enabled addon into the registry.

        Returns:
            The list of discovered, validated addons.
        """
        addons_dir = Path(self.config.addons_dir)
        self._registry.clear()
        if not addons_dir.is_dir():
            return []
        for path in sorted(_iter_yaml(addons_dir, self.config.yaml_suffixes)):
            spec = self._load_file(path)
            if spec is None:
                continue
            self._registry[spec.name] = spec
        return list(self._registry.values())

    def get(self, name: str) -> AddonSpec | None:
        """Return the addon registered under ``name``, if any."""
        return self._registry.get(name)

    def all(self) -> list[AddonSpec]:
        """Return all currently registered addons."""
        return list(self._registry.values())

    def names(self) -> list[str]:
        """Return the sorted names of all registered addons."""
        return sorted(self._registry)

    # --------------------------------------------------------------- parameters --
    def build_params(
        self,
        addon: AddonSpec,
        overrides: Mapping[str, Any] | None = None,
    ) -> tuple[dict[str, Any], set[str]]:
        """Merge declared defaults with runtime overrides.

        Args:
            addon: The addon whose params are being resolved.
            overrides: Runtime-supplied parameter values.

        Returns:
            A ``(merged, untrusted)`` pair where ``merged`` is the resolved
            parameter mapping and ``untrusted`` is the set of keys whose values
            must be shell-quoted before substitution.

        Raises:
            AddonError: If a required parameter is missing a value.
        """
        overrides = dict(overrides or {})
        merged: dict[str, Any] = {}
        default_keys: set[str] = set()
        for param in addon.params:
            if param.default is not None:
                merged[param.name] = param.default
                default_keys.add(param.name)
        merged.update(overrides)
        untrusted = set(overrides.keys())
        untrusted.update(p.name for p in addon.params if p.default is None)
        missing = [name for name in addon.required_params() if name not in merged]
        if missing:
            raise AddonError(
                f"addon '{addon.name}' missing required params: {', '.join(missing)}"
            )
        return merged, untrusted

    # ------------------------------------------------------------------ install --
    def install(
        self,
        addon: AddonSpec,
        overrides: Mapping[str, Any] | None = None,
        *,
        force: bool = False,
    ) -> None:
        """Install (clone and build) an addon if not already present.

        Args:
            addon: The addon to install.
            overrides: Runtime params for install_command placeholders.
            force: Reinstall even if the directory already exists.
        """
        params, _ = self.build_params(addon, overrides)
        self.installer.install(addon, params, force=force)

    # --------------------------------------------------------------------- run --
    def run(
        self,
        name: str,
        overrides: Mapping[str, Any] | None = None,
        extra_args: tuple[str, ...] = (),
        *,
        install: bool = True,
    ) -> CommandResult:
        """Run a named addon through the full lifecycle.

        Args:
            name: Addon name as registered.
            overrides: Runtime parameter values.
            extra_args: Extra arguments appended to the execute command.
            install: When True, install the addon first if needed.

        Returns:
            The executed command result.

        Raises:
            KeyError: If the addon name is unknown.
            SchemaError: If the addon fails security validation.
        """
        addon = self.get(name)
        if addon is None:
            raise KeyError(f"no addon registered under name: {name}")
        if not addon.enabled:
            raise AddonError(f"addon '{name}' is disabled")
        self.security.validate_addon(addon)
        params, untrusted = self.build_params(addon, overrides)
        if install and not self.installer.is_installed(addon):
            self.installer.install(addon, params)
        tool = addon.tool
        if tool.install_path:
            cwd = str(self.installer.install_path(addon))
        else:
            cwd = None
        return self.addons_runner.execute(addon, params, extra_args, cwd=cwd, untrusted_keys=untrusted)

    # ---------------------------------------------------------------- marketplace --
    def add(
        self,
        raw: Mapping[str, Any],
        filename: str | None = None,
        *,
        category: str | None = None,
    ) -> Path:
        """Register a new addon by writing its YAML to ``addons_dir``.

        Args:
            raw: Addon schema mapping (or a simplified marketplace form).
            filename: Optional explicit filename; defaults to ``<name>.yaml``.
            category: Optional category override applied to the document.

        Returns:
            The path of the written addon file.

        Raises:
            SchemaError: If the resulting addon is invalid.
        """
        data = dict(raw)
        if category is not None:
            data["category"] = category
        spec = AddonSpec.loads(data, self.config)
        self.security.validate_addon(spec)
        target = self._addon_path(spec.name, filename)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(data, fh, default_flow_style=False, allow_unicode=True, sort_keys=False)
        self._registry[spec.name] = spec
        log.info("registered addon %s -> %s", spec.name, target)
        return target

    def add_from_tool(
        self,
        name: str,
        repo_url: str,
        execute_command: str,
        *,
        install_path: str = "",
        install_command: str = "",
        description: str = _DEFAULT_DESCRIPTION,
        category: str | None = None,
        enabled: bool = True,
        params: list[dict[str, Any]] | None = None,
    ) -> Path:
        """Convenience builder for a tool-style addon.

        Args:
            name: Addon name.
            repo_url: Upstream repository URL.
            execute_command: Command run on execution.
            install_path: Relative install destination directory.
            install_command: Command run after cloning.
            description: Addon description.
            category: Category label.
            enabled: Whether the addon is active.
            params: Declared parameter list.

        Returns:
            The path of the written addon file.
        """
        data: dict[str, Any] = {
            "name": name,
            "description": description,
            "enabled": enabled,
            "params": params or [],
            "tool": {
                "name": name,
                "repo_url": repo_url,
                "install_path": install_path,
                "install_command": install_command,
                "execute_command": execute_command,
            },
        }
        return self.add(data, category=category)

    def remove(self, name: str) -> Path | None:
        """Delete the addon file registered under ``name``.

        Args:
            name: Addon name to remove.

        Returns:
            The deleted path, or None if no file was found.
        """
        target = self._find_addon_file(name)
        if target is None:
            self._registry.pop(name, None)
            return None
        target.unlink(missing_ok=True)
        self._registry.pop(name, None)
        log.info("removed addon %s", name)
        return target

    # ------------------------------------------------------------------ project --
    def run_project(self, project_path: str | Path) -> list[CommandResult]:
        """Execute a declarative project file for non-programmers.

        Project schema:

        .. code-block:: yaml

            install_root: external
            addons_dir: addons
            addons:
              - name: beacon
                install: true
                run: true
                params:
                  lhost: 10.0.0.1

        Args:
            project_path: Path to the project YAML.

        Returns:
            The results of every executed addon.

        Raises:
            AddonError: If the project file is malformed.
        """
        path = Path(project_path)
        try:
            with path.open("r", encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
        except (yaml.YAMLError, OSError) as exc:
            raise AddonError(f"project file {path} is not valid YAML: {exc}") from exc
        if not isinstance(data, dict):
            raise AddonError(f"project file {path} must be a mapping")
        self.config = _project_config(self.config, data)
        self.discover()
        results: list[CommandResult] = []
        entries = data.get("addons")
        if not isinstance(entries, list):
            return results
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            entry_name = entry.get("name")
            if not entry_name:
                continue
            do_install = bool(entry.get("install", False))
            do_run = bool(entry.get("run", False))
            params = entry.get("params")
            params_dict = dict(params) if isinstance(params, dict) else {}
            addon = self.get(str(entry_name))
            if addon is None:
                raise AddonError(f"project references unknown addon: {entry_name}")
            if do_install:
                self.install(addon, params_dict)
            if do_run:
                results.append(self.run(str(entry_name), params_dict))
        return results

    # ---------------------------------------------------------------- internal --
    def _load_file(self, path: Path) -> AddonSpec | None:
        try:
            with path.open("r", encoding="utf-8") as fh:
                raw = yaml.safe_load(fh)
        except (yaml.YAMLError, OSError) as exc:
            log.warning("could not read addon %s: %s", path, exc)
            return None
        if not isinstance(raw, dict):
            log.warning("skipping non-mapping addon file: %s", path)
            return None
        try:
            spec = AddonSpec.loads(raw, self.config)
        except SchemaError as exc:
            log.warning("skipping invalid addon %s: %s", path, exc)
            return None
        if not spec.enabled:
            return None
        try:
            self.security.validate_addon(spec)
        except SchemaError as exc:
            log.warning("skipping insecure addon %s: %s", path, exc)
            return None
        return spec

    def _addon_path(self, name: str, filename: str | None) -> Path:
        base = Path(self.config.addons_dir)
        safe = _safe_filename(name)
        filename = filename or f"{safe}.yaml"
        path = (base / filename).resolve()
        if not path.is_relative_to(base.resolve()):
            raise SchemaError("addon filename escapes the addons directory")
        return path

    def _find_addon_file(self, name: str) -> Path | None:
        base = Path(self.config.addons_dir)
        if not base.is_dir():
            return None
        for path in _iter_yaml(base, self.config.yaml_suffixes):
            try:
                with path.open("r", encoding="utf-8") as fh:
                    raw = yaml.safe_load(fh)
            except (yaml.YAMLError, OSError):
                continue
            if isinstance(raw, dict) and raw.get("name") == name:
                return path
        return None


def _iter_yaml(base: Path, suffixes: tuple[str, ...]) -> list[Path]:
    """Return sorted YAML files under ``base`` matching ``suffixes``."""
    paths: list[Path] = []
    for suffix in suffixes:
        paths.extend(base.rglob(f"*{suffix}"))
    return sorted(paths)


def _safe_filename(name: str) -> str:
    """Sanitise an addon name into a safe filename token."""
    cleaned = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in name)
    return cleaned or "addon"


def _project_config(base: AddonConfig, data: Mapping[str, Any]) -> AddonConfig:
    """Derive an updated config from optional project overrides."""
    addons_dir = data.get("addons_dir", base.addons_dir)
    install_root = data.get("install_root", base.install_root)
    return AddonConfig(
        addons_dir=str(addons_dir),
        install_root=str(install_root),
        allowed_repo_hosts=base.allowed_repo_hosts,
        allowed_repo_schemes=base.allowed_repo_schemes,
        clone_depth=base.clone_depth,
        command_timeout_seconds=base.command_timeout_seconds,
        quote_runtime_values=base.quote_runtime_values,
        allowed_os_values=base.allowed_os_values,
        environment=dict(base.environment),
    )
