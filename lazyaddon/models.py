"""Domain models for the lazyaddon schema.

Defines the typed representation of an addon YAML document. The contract is a
pure data layer: parsing, coercion and validation only, with no I/O and no
side effects, so it can be unit-tested in isolation and reused by the engine
and the CLI alike.

Schema (mirrors the LazyOwn lazyaddons layout):

.. code-block:: yaml

    name: beacon
    description: Builds and deploys a C2 beacon.
    author: LazyOwn RedTeam
    version: "1.0"
    enabled: true
    os: any
    category: 10. Command & Control
    params:
      - name: lhost
        type: string
        required: true
        description: Listener host.
    trigger: []
    tool:
      name: beacon
      repo_url: https://github.com/grisuno/beacon.git
      install_path: c2/beacon
      install_command: make windows
      execute_command: ./gen_beacon.sh --lhost {lhost}
      lazycommand: encode --in payload.bin
      remote_command: run --payload payload.bin
      upload_file: payload.bin
      download_file: C:\\results\\out.txt
      env:
        KEY: "{aes_key}"
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .config import (
    DEFAULT_CATEGORY,
    DEFAULT_OS,
    DEFAULT_PARAM_REQUIRED,
    DEFAULT_PARAM_TYPE,
    AddonConfig,
)


class AddonError(Exception):
    """Base error raised for any lazyaddon schema or runtime failure."""


class SchemaError(AddonError):
    """Raised when an addon document violates the expected schema."""


@dataclass(frozen=True)
class AddonParam:
    """A single declared input parameter for an addon.

    Attributes:
        name: Unique parameter identifier referenced inside placeholders.
        type: Optional type label; preserved for tooling and documentation.
        required: Whether the value must be supplied at runtime.
        description: Human-readable explanation of the parameter.
        default: Trusted fallback value used when no runtime value is given.
    """

    name: str
    type: str = DEFAULT_PARAM_TYPE
    required: bool = DEFAULT_PARAM_REQUIRED
    description: str = ""
    default: str | None = None


@dataclass(frozen=True)
class ToolSpec:
    """Executable description of the tool an addon wraps.

    Attributes:
        name: Canonical tool name.
        repo_url: https URL of the upstream project (clone source).
        install_path: Relative destination directory under the install root.
        install_command: Command run inside ``install_path`` after cloning.
        execute_command: Command run when the addon is executed.
        lazycommand: Optional framework command chain, dispatched via the
            host's lazy-command hook.
        remote_command: Optional remote/agent command, dispatched via the
            remote-command hook.
        upload_file: Comma-separated files sent to a connected agent.
        download_file: Comma-separated files fetched from an agent.
        env: Environment variables injected for the command, with placeholders
            resolved at runtime.
    """

    name: str = ""
    repo_url: str = ""
    install_path: str = ""
    install_command: str = ""
    execute_command: str = ""
    lazycommand: str = ""
    remote_command: str = ""
    upload_file: str = ""
    download_file: str = ""
    env: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class AddonSpec:
    """A fully validated addon definition.

    Attributes:
        name: Unique addon identifier.
        description: Long-form description.
        author: Original author of the addon.
        version: Human-readable version string.
        enabled: Whether the addon may be executed.
        os: Target OS label; one of :data:`AddonConfig.allowed_os_values`.
        category: Palette/category label used for grouping and marketplaces.
        params: Declared input parameters.
        trigger: Service names that suggest this addon during recon.
        tool: Executable tool definition.
    """

    name: str
    description: str = ""
    author: str = ""
    version: str = ""
    enabled: bool = True
    os: str = DEFAULT_OS
    category: str = DEFAULT_CATEGORY
    params: tuple[AddonParam, ...] = field(default_factory=tuple)
    trigger: tuple[str, ...] = field(default_factory=tuple)
    tool: ToolSpec = field(default_factory=ToolSpec)

    @classmethod
    def loads(cls, raw: dict[str, Any], config: AddonConfig) -> AddonSpec:
        """Build a validated ``AddonSpec`` from a parsed YAML mapping.

        Args:
            raw: Parsed YAML document for a single addon.
            config: Engine configuration governing defaults and limits.

        Returns:
            A normalised, validated addon specification.

        Raises:
            SchemaError: If the document is malformed or exceeds safety limits.
        """
        name = _require_name(raw)
        tool_raw = raw.get("tool")
        if not isinstance(tool_raw, dict):
            raise SchemaError(f"addon '{name}': 'tool' must be a mapping")
        tool = _build_tool(name, tool_raw, config)
        params = tuple(_build_param(p, config) for p in _as_params(raw.get("params")))
        os_label = str(raw.get("os") or config.default_os).strip().lower()
        if os_label not in config.allowed_os_values:
            os_label = config.default_os
        return cls(
            name=name,
            description=str(raw.get("description") or "").strip(),
            author=str(raw.get("author") or "").strip(),
            version=str(raw.get("version") or "").strip(),
            enabled=bool(raw.get("enabled", True)),
            os=os_label,
            category=str(raw.get("category") or config.default_category).strip(),
            params=params,
            trigger=_as_str_tuple(raw.get("trigger")),
            tool=tool,
        )

    def param_by_name(self, name: str) -> AddonParam | None:
        """Return the declared parameter matching ``name`` or None."""
        for param in self.params:
            if param.name == name:
                return param
        return None

    def required_params(self) -> tuple[str, ...]:
        """Return the names of all required parameters in declaration order."""
        return tuple(p.name for p in self.params if p.required)


def _require_name(raw: dict[str, Any]) -> str:
    """Extract and validate the required addon name field."""
    name = raw.get("name")
    if not isinstance(name, str) or not name.strip():
        raise SchemaError("addon must have a non-empty string 'name'")
    return name.strip()


def _as_params(value: Any) -> tuple[dict[str, Any], ...]:
    """Coerce the ``params`` field into a tuple of mappings."""
    if value is None:
        return ()
    if not isinstance(value, list):
        return ()
    out: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            out.append(item)
    return tuple(out)


def _build_param(raw: dict[str, Any], config: AddonConfig) -> AddonParam:
    """Normalise a single parameter mapping into an ``AddonParam``."""
    name = raw.get("name")
    if not isinstance(name, str) or not name.strip():
        raise SchemaError("each param must have a non-empty string 'name'")
    default_raw = raw.get("default")
    default = str(default_raw) if default_raw is not None else None
    return AddonParam(
        name=name.strip(),
        type=str(raw.get("type") or config.default_param_type).strip(),
        required=bool(raw.get("required", DEFAULT_PARAM_REQUIRED)),
        description=str(raw.get("description") or "").strip(),
        default=default,
    )


def _build_tool(name: str, raw: dict[str, Any], config: AddonConfig) -> ToolSpec:
    """Build and length-check the executable tool definition."""
    tool_name = str(raw.get("name") or name).strip()
    return ToolSpec(
        name=tool_name,
        repo_url=str(raw.get("repo_url") or "").strip(),
        install_path=str(raw.get("install_path") or "").strip(),
        install_command=str(raw.get("install_command") or "").strip(),
        execute_command=str(raw.get("execute_command") or "").strip(),
        lazycommand=str(raw.get("lazycommand") or "").strip(),
        remote_command=str(raw.get("remote_command") or "").strip(),
        upload_file=str(raw.get("upload_file") or "").strip(),
        download_file=str(raw.get("download_file") or "").strip(),
        env=_as_str_dict(raw.get("env")),
    )


def _as_str_dict(value: Any) -> dict[str, str]:
    """Coerce an env mapping into ``{str: str}``."""
    if not isinstance(value, dict):
        return {}
    out: dict[str, str] = {}
    for key, item in value.items():
        if item is not None:
            out[str(key)] = str(item)
    return out


def _as_str_tuple(value: Any) -> tuple[str, ...]:
    """Coerce a trigger list into a tuple of strings."""
    if value is None:
        return ()
    if isinstance(value, str):
        parts = [s.strip() for s in value.split(",") if s.strip()]
        return tuple(parts)
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    return ()
