"""Placeholder substitution contract.

Resolves ``{name}`` and ``{{ name }}`` tokens inside command strings using the
values from a parameter mapping, mirroring the original LazyOwn
``replace_command_placeholders`` semantics: whitespace inside the braces is
ignored and unknown tokens are left untouched.

Security boundary: parameter values that are injected at runtime (rather than
declared as trusted defaults inside the same YAML) may carry shell
metacharacters. To prevent command injection when a command is later executed
under a shell, those runtime values are shell-quoted via :func:`shlex.quote`
unless ``quote_runtime_values`` is disabled in the configuration.
"""

from __future__ import annotations

import re
import shlex
from collections.abc import Mapping
from typing import Any

from .config import AddonConfig

_TOKEN = re.compile(r"\{\{(.+?)\}\}|\{(.+?)\}")


class PlaceholderEngine:
    """Resolves placeholder tokens within command strings.

    Args:
        config: Engine configuration controlling delimiters and quoting.
    """

    def __init__(self, config: AddonConfig) -> None:
        self._config = config

    def resolve(
        self,
        command: str,
        params: Mapping[str, Any],
        untrusted_keys: set[str] | frozenset[str] | None = None,
    ) -> str:
        """Substitute placeholders in ``command`` using ``params``.

        Args:
            command: String possibly containing ``{name}`` or ``{{ name }}``
                tokens.
            params: Mapping of placeholder name to value.
            untrusted_keys: Param names whose values come from an untrusted
                runtime source and must be shell-quoted before substitution.
                When None, every key present in ``params`` is treated as
                untrusted (the conservative default).

        Returns:
            The command with every known placeholder replaced.

        Raises:
            TypeError: If ``command`` is not a string.
        """
        if not isinstance(command, str):
            raise TypeError("command must be a string")
        untrusted = untrusted_keys
        if untrusted is None:
            untrusted = set(params.keys())
        return _TOKEN.sub(
            lambda match: self._replacement(match, params, untrusted),
            command,
        )

    def _replacement(
        self,
        match: re.Match[str],
        params: Mapping[str, Any],
        untrusted: set[str] | frozenset[str],
    ) -> str:
        key = match.group(1) or match.group(2) or ""
        key = key.strip()
        if key not in params:
            return match.group(0)
        text = str(params[key])
        if self._config.quote_runtime_values and key in untrusted:
            return shlex.quote(text)
        return text
