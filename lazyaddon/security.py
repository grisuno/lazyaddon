"""Security policy contract for the lazyaddon engine.

Defines the defensive boundaries applied before any network fetch, filesystem
write or subprocess launch. The policy is deliberately conservative: it is
better to reject a suspicious addon than to risk command injection, URL
confusion or path traversal.

Enforced rules:

* ``repo_url`` must use an allowed scheme and, when a host allow-list is
  configured, an allowed hostname; it must not exceed the configured length.
* Command strings must not contain null bytes and must not exceed the
  configured length.
* ``install_path`` is resolved relative to ``install_root`` and must stay
  inside that root (rejects ``..`` traversal and absolute escapes).
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

from .config import AddonConfig
from .models import AddonSpec, SchemaError


class SecurityPolicy:
    """Validates external inputs before they reach the engine.

    Args:
        config: Engine configuration governing allowed hosts, schemes, lengths
            and the install root.
    """

    def __init__(self, config: AddonConfig) -> None:
        self._config = config

    def validate_addon(self, addon: AddonSpec) -> None:
        """Validate the network, filesystem and command fields of an addon.

        Args:
            addon: The addon to validate.

        Raises:
            SchemaError: If any security boundary is violated.
        """
        tool = addon.tool
        if tool.repo_url:
            self.validate_repo_url(tool.repo_url)
        for label, command in (
            ("install_command", tool.install_command),
            ("execute_command", tool.execute_command),
            ("lazycommand", tool.lazycommand),
            ("remote_command", tool.remote_command),
        ):
            self.validate_command(command, label)
        if tool.install_path:
            self.resolve_install_path(tool.install_path)

    def validate_repo_url(self, url: str) -> str:
        """Validate a repository URL and return it unchanged.

        Args:
            url: Repository URL, typically a GitHub/GitLab clone source.

        Returns:
            The validated URL.

        Raises:
            SchemaError: If the scheme, host or length is not permitted.
        """
        if not isinstance(url, str) or not url.strip():
            raise SchemaError("repo_url must be a non-empty string")
        if len(url) > self._config.max_repo_url_length:
            raise SchemaError("repo_url exceeds maximum allowed length")
        parsed = urlparse(url.strip())
        if parsed.scheme not in self._config.allowed_repo_schemes:
            raise SchemaError(f"repo_url scheme '{parsed.scheme}' is not allowed")
        host = parsed.hostname or ""
        if self._config.allowed_repo_hosts and host not in self._config.allowed_repo_hosts:
            raise SchemaError(f"repo_url host '{host}' is not in the allowed list")
        if not host or not parsed.path:
            raise SchemaError("repo_url must include a host and a repository path")
        return url

    def validate_command(self, command: str, label: str = "command") -> None:
        """Validate a shell command string for length and null bytes.

        Args:
            command: The command string to validate.
            label: Human-readable label used in error messages.

        Raises:
            SchemaError: If the command is malformed.
        """
        if not isinstance(command, str):
            raise SchemaError(f"{label} must be a string")
        if "\x00" in command:
            raise SchemaError(f"{label} contains a null byte")
        if len(command) > self._config.max_command_length:
            raise SchemaError(f"{label} exceeds maximum allowed length")

    def resolve_install_path(self, install_path: str) -> Path:
        """Resolve an addon install path inside the configured install root.

        Args:
            install_path: Relative destination directory from the addon.

        Returns:
            The resolved, validated absolute path.

        Raises:
            SchemaError: If the path escapes the install root.
        """
        root = Path(self._config.install_root).expanduser().resolve()
        if not root.is_relative_to(Path.cwd().resolve()):
            root = Path.cwd().resolve() / self._config.install_root
        candidate = (root / install_path).resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise SchemaError("install_path escapes the configured install root") from exc
        return candidate
