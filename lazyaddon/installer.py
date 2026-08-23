"""Installation contract: clone and build an addon from its upstream repo.

``AddonInstaller`` is responsible for materialising an addon's tool on disk.
It clones the ``repo_url`` into a validated location under the install root
(when ``install_path`` is declared and not already present) and then runs the
``install_command`` inside that directory. Installation is idempotent: an
existing install path is left untouched unless the caller forces a reinstall.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .config import AddonConfig
from .models import AddonSpec
from .placeholders import PlaceholderEngine
from .runner import ProcessRunner
from .security import SecurityPolicy


class AddonInstaller:
    """Clones and builds addons on disk.

    Args:
        config: Engine configuration.
        runner: Process runner used for ``git clone`` and install commands.
        placeholders: Placeholder engine for resolving install commands.
        security: Security policy validating URLs and install paths.
    """

    def __init__(
        self,
        config: AddonConfig,
        runner: ProcessRunner,
        placeholders: PlaceholderEngine,
        security: SecurityPolicy,
    ) -> None:
        self._config = config
        self._runner = runner
        self._placeholders = placeholders
        self._security = security

    def install_path(self, addon: AddonSpec) -> Path | None:
        """Return the resolved on-disk install directory for an addon.

        Args:
            addon: The addon to inspect.

        Returns:
            The validated absolute install directory, or None when the addon
            declares no ``install_path``.
        """
        tool = addon.tool
        if not tool.install_path:
            return None
        return self._security.resolve_install_path(tool.install_path)

    def is_installed(self, addon: AddonSpec) -> bool:
        """Return True when the addon's install directory already exists.

        Args:
            addon: The addon to inspect.

        Returns:
            True if the addon declares no install path or its directory exists.
        """
        target = self.install_path(addon)
        return target is None or target.exists()

    def install(
        self,
        addon: AddonSpec,
        params: Mapping[str, Any] | None = None,
        *,
        force: bool = False,
    ) -> None:
        """Clone and build an addon, skipping already-installed directories.

        Args:
            addon: The addon to install.
            params: Runtime parameter values used for install_command tokens.
            force: When True, reinstall even if the directory already exists.

        Raises:
            ValueError: If the addon declares no ``repo_url``.
            SchemaError: If the repo URL or install path is not permitted.
        """
        self._security.validate_addon(addon)
        tool = addon.tool
        target = self.install_path(addon)
        if target is None:
            return
        if target.exists() and not force:
            return
        if not tool.repo_url:
            raise ValueError(f"addon '{addon.name}' has no repo_url to install")
        self._clone(tool.repo_url, target)
        if tool.install_command:
            resolved = self._placeholders.resolve(tool.install_command, params or {})
            self._runner.run(
                resolved,
                cwd=str(target),
                timeout=self._config.command_timeout_seconds,
            )

    def _clone(self, repo_url: str, target: Path) -> None:
        """Clone ``repo_url`` into ``target`` using a shallow checkout."""
        target.parent.mkdir(parents=True, exist_ok=True)
        command = (
            f"git clone --depth {self._config.clone_depth} -- {repo_url} {target}"
        )
        self._runner.run(command, timeout=self._config.command_timeout_seconds)
