# Subsystem: lazyaddon

## lazyaddon/__init__.py
- Layer: utility
- Doc: lazyaddon: declarative tool and extension manager.  Turns any GitHub/GitLab project into an installable, runnable addon 
- Language: py
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`

## lazyaddon/__main__.py
- Layer: utility
- Doc: Console entry point for lazyaddon.  Exposes subcommands for discovery, installation, execution, marketplace registration
- Language: py
- Symbols:
  - `build_parser` (function, line 20) `def build_parser()`
  - `_make_engine` (function, line 81) `def _make_engine(args)`
  - `_parse_overrides` (function, line 92) `def _parse_overrides(raw)`
  - `main` (function, line 103) `def main(argv)`
  - `_dispatch` (function, line 118) `def _dispatch(args, parser)`
  - `_summary` (function, line 197) `def _summary(addon)`
  - `_json` (function, line 223) `def _json(payload)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

## lazyaddon/config.py
- Layer: infrastructure
- Doc: Centralized configuration contract for the lazyaddon engine.  Holds every tunable knob used across the package so no mag
- Language: py
- Symbols:
  - `AddonConfig` (class, line 33) `class AddonConfig`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/conftest.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_placeholders.py`, `tests/test_placeholders_property.py`, `tests/test_runner.py`, `tests/test_security.py`

## lazyaddon/engine.py
- Layer: utility
- Doc: Facade contract orchestrating the lazyaddon lifecycle.  ``LazyAddonEngine`` is the single entry point consumers import. 
- Language: py
- Symbols:
  - `LazyAddonEngine` (class, line 32) `class LazyAddonEngine`
  - `_iter_yaml` (method, line 388) `def _iter_yaml(base, suffixes)`
  - `_safe_filename` (method, line 396) `def _safe_filename(name)`
  - `_project_config` (method, line 402) `def _project_config(base, data)`
  - `__init__` (method, line 41) `def __init__(self, config, runner, hooks)`
  - `discover` (method, line 60) `def discover(self)`
  - `get` (method, line 77) `def get(self, name)`
  - `all` (method, line 81) `def all(self)`
  - `names` (method, line 85) `def names(self)`
  - `build_params` (method, line 90) `def build_params(self, addon, overrides)`
  - `install` (method, line 127) `def install(self, addon, overrides)`
  - `run` (method, line 145) `def run(self, name, overrides, extra_args)`
  - `add` (method, line 185) `def add(self, raw, filename)`
  - `add_from_tool` (method, line 218) `def add_from_tool(self, name, repo_url, execute_command)`
  - `remove` (method, line 262) `def remove(self, name)`
  - `run_project` (method, line 281) `def run_project(self, project_path)`
  - `_load_file` (method, line 340) `def _load_file(self, path)`
  - `_addon_path` (method, line 364) `def _addon_path(self, name, filename)`
  - `_find_addon_file` (method, line 373) `def _find_addon_file(self, name)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

## lazyaddon/installer.py
- Layer: utility
- Doc: Installation contract: clone and build an addon from its upstream repo.  ``AddonInstaller`` is responsible for materiali
- Language: py
- Symbols:
  - `AddonInstaller` (class, line 23) `class AddonInstaller`
  - `__init__` (method, line 33) `def __init__(self, config, runner, placeholders, security)`
  - `install_path` (method, line 45) `def install_path(self, addon)`
  - `is_installed` (method, line 60) `def is_installed(self, addon)`
  - `install` (method, line 72) `def install(self, addon, params)`
  - `_clone` (method, line 108) `def _clone(self, repo_url, target)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`

## lazyaddon/models.py
- Layer: business_logic
- Doc: Domain models for the lazyaddon schema.  Defines the typed representation of an addon YAML document. The contract is a p
- Language: py
- Symbols:
  - `AddonError` (class, line 53) `class AddonError(Exception)`
  - `SchemaError` (class, line 57) `class SchemaError(AddonError)`
  - `AddonParam` (class, line 62) `class AddonParam`
  - `ToolSpec` (class, line 81) `class ToolSpec`
  - `AddonSpec` (class, line 113) `class AddonSpec`
  - `_require_name` (method, line 188) `def _require_name(raw)`
  - `_as_params` (method, line 196) `def _as_params(value)`
  - `_build_param` (method, line 209) `def _build_param(raw, config)`
  - `_build_tool` (method, line 225) `def _build_tool(name, raw, config)`
  - `_as_str_dict` (method, line 242) `def _as_str_dict(value)`
  - `_as_str_tuple` (method, line 253) `def _as_str_tuple(value)`
  - `loads` (method, line 141) `def loads(cls, raw, config)`
  - `param_by_name` (method, line 176) `def param_by_name(self, name)`
  - `required_params` (method, line 183) `def required_params(self)`
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

## lazyaddon/placeholders.py
- Layer: utility
- Doc: Placeholder substitution contract.  Resolves ``{name}`` and ``{{ name }}`` tokens inside command strings using the value
- Language: py
- Symbols:
  - `PlaceholderEngine` (class, line 27) `class PlaceholderEngine`
  - `__init__` (method, line 34) `def __init__(self, config)`
  - `resolve` (method, line 37) `def resolve(self, command, params, untrusted_keys)`
  - `_replacement` (method, line 70) `def _replacement(self, match, params, untrusted)`
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `tests/test_placeholders.py`, `tests/test_placeholders_property.py`

## lazyaddon/runner.py
- Layer: utility
- Doc: Process execution and addon dispatch contract.  ``CommandRunner`` wraps :func:`subprocess.run` behind a small, injectabl
- Language: py
- Symbols:
  - `CommandResult` (class, line 30) `class CommandResult`
  - `ProcessRunner` (class, line 51) `class ProcessRunner(Protocol)`
  - `CommandRunner` (class, line 64) `class CommandRunner`
  - `AddonHook` (class, line 124) `class AddonHook(Protocol)`
  - `AddonRunner` (class, line 143) `class AddonRunner`
  - `ok` (method, line 46) `def ok(self)`
  - `run` (method, line 54) `def run(self, command, cwd, env, timeout)`
  - `__init__` (method, line 72) `def __init__(self, timeout_seconds, environment)`
  - `run` (method, line 80) `def run(self, command, cwd, env, timeout)`
  - `__call__` (method, line 132) `def __call__(self, kind, payload, env)`
  - `execute` (method, line 159) `def execute(self, addon, params, extra_args, cwd, untrusted_keys)`
  - `dispatch_hooks` (method, line 199) `def dispatch_hooks(self, addon, params, untrusted_keys)`
  - `_dispatch_hooks` (method, line 218) `def _dispatch_hooks(self, addon, params, untrusted, env)`
  - `_resolve_env` (method, line 241) `def _resolve_env(self, addon, params, untrusted)`
  - `_default_untrusted` (method, line 252) `def _default_untrusted(self, addon)`
  - `_tool_cwd` (method, line 255) `def _tool_cwd(self, addon)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

## lazyaddon/security.py
- Layer: utility
- Doc: Security policy contract for the lazyaddon engine.  Defines the defensive boundaries applied before any network fetch, f
- Language: py
- Symbols:
  - `SecurityPolicy` (class, line 27) `class SecurityPolicy`
  - `__init__` (method, line 35) `def __init__(self, config)`
  - `validate_addon` (method, line 38) `def validate_addon(self, addon)`
  - `validate_repo_url` (method, line 60) `def validate_repo_url(self, url)`
  - `validate_command` (method, line 86) `def validate_command(self, command, label)`
  - `resolve_install_path` (method, line 103) `def resolve_install_path(self, install_path)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/test_security.py`
