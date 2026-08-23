"""Centralized configuration contract for the lazyaddon engine.

Holds every tunable knob used across the package so no magic numbers or
hardcoded strings leak into the business logic. Values mirror the semantics
of the original LazyOwn lazyaddons schema while keeping the engine portable
and secure by default.

The ``AddonConfig`` dataclass is immutable-friendly: callers construct it with
overrides and pass it to the engine. Field names are deliberately flat so a
YAML project file can override them by simple key mapping.
"""

from __future__ import annotations

from dataclasses import dataclass, field

DEFAULT_OS = "any"
DEFAULT_CATEGORY = "00. Miscellaneous"
DEFAULT_PARAM_TYPE = "string"
DEFAULT_PARAM_REQUIRED = False
DEFAULT_COMMAND_TIMEOUT_SECONDS = 600
DEFAULT_CLONE_DEPTH = 1
DEFAULT_REPO_SCHEME = "https"
DEFAULT_MAX_REPO_LEN = 2048
DEFAULT_MAX_COMMAND_LEN = 8192
DEFAULT_YAML_SUFFIXES = (".yaml", ".yml")
DEFAULT_PLACEHOLDER_OPEN = "{"
DEFAULT_PLACEHOLDER_CLOSE = "}"
ALLOWED_OS_VALUES = ("any", "linux", "windows", "macos", "network", "containers", "saas", "iaas")


@dataclass(frozen=True)
class AddonConfig:
    """Immutable engine configuration.

    Attributes:
        addons_dir: Base directory where addon YAML files are discovered.
        install_root: Directory under which cloned repos are placed. Resolving
            against this root prevents path traversal from ``install_path``.
        allowed_repo_hosts: Hostnames permitted in ``repo_url``. Empty means
            any https host is accepted (handy for GitLab mirrors).
        allowed_repo_schemes: URL schemes permitted for ``repo_url``.
        clone_depth: Depth passed to ``git clone --depth``.
        command_timeout_seconds: Maximum seconds a subprocess may run.
        default_os: OS label applied when an addon omits ``os``.
        default_category: Category applied when an addon omits ``category``.
        default_param_type: Type label applied when a param omits ``type``.
        max_repo_url_length: Rejection ceiling for oversized ``repo_url``.
        max_command_length: Rejection ceiling for command strings.
        yaml_suffixes: File extensions scanned when discovering addons.
        placeholder_open: Left placeholder delimiter.
        placeholder_close: Right placeholder delimiter.
        quote_runtime_values: Shell-quote runtime-injected param values before
            substitution into commands that run under a shell.
        allowed_os_values: Recognised OS labels; anything else falls back to
            ``default_os``.
        environment: Environment variables injected into every subprocess.
    """

    addons_dir: str = "addons"
    install_root: str = "external"
    allowed_repo_hosts: tuple[str, ...] = ()
    allowed_repo_schemes: tuple[str, ...] = (DEFAULT_REPO_SCHEME,)
    clone_depth: int = DEFAULT_CLONE_DEPTH
    command_timeout_seconds: int = DEFAULT_COMMAND_TIMEOUT_SECONDS
    default_os: str = DEFAULT_OS
    default_category: str = DEFAULT_CATEGORY
    default_param_type: str = DEFAULT_PARAM_TYPE
    max_repo_url_length: int = DEFAULT_MAX_REPO_LEN
    max_command_length: int = DEFAULT_MAX_COMMAND_LEN
    yaml_suffixes: tuple[str, ...] = DEFAULT_YAML_SUFFIXES
    placeholder_open: str = DEFAULT_PLACEHOLDER_OPEN
    placeholder_close: str = DEFAULT_PLACEHOLDER_CLOSE
    quote_runtime_values: bool = True
    allowed_os_values: tuple[str, ...] = ALLOWED_OS_VALUES
    environment: dict[str, str] = field(default_factory=dict)
