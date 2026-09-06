# API

## lazyaddon/__main__.py

### build_parser `def build_parser()`
- Defined: `lazyaddon/__main__.py:20`
- Doc: Build the CLI argument parser.
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

### _make_engine `def _make_engine(args)`
- Defined: `lazyaddon/__main__.py:81`
- Doc: Build an engine honouring the CLI-level directory overrides.
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

### _parse_overrides `def _parse_overrides(raw)`
- Defined: `lazyaddon/__main__.py:92`
- Doc: Parse ``key=value`` CLI overrides into a parameter mapping.
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

### main `def main(argv)`
- Defined: `lazyaddon/__main__.py:103`
- Doc: Run the lazyaddon CLI.
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

### _dispatch `def _dispatch(args, parser)`
- Defined: `lazyaddon/__main__.py:118`
- Doc: Route a parsed command to its handler.
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

### _summary `def _summary(addon)`
- Defined: `lazyaddon/__main__.py:197`
- Doc: Build a compact serialisable summary of an addon.
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

### _json `def _json(payload)`
- Defined: `lazyaddon/__main__.py:223`
- Doc: Serialize ``payload`` to a compact JSON string.
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
- Imported by: `tests/test_cli.py`

## lazyaddon/engine.py

### _iter_yaml `def _iter_yaml(base, suffixes)`
- Defined: `lazyaddon/engine.py:388`
- Doc: Return sorted YAML files under ``base`` matching ``suffixes``.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### _safe_filename `def _safe_filename(name)`
- Defined: `lazyaddon/engine.py:396`
- Doc: Sanitise an addon name into a safe filename token.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### _project_config `def _project_config(base, data)`
- Defined: `lazyaddon/engine.py:402`
- Doc: Derive an updated config from optional project overrides.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### __init__ `def __init__(self, config, runner, hooks)`
- Defined: `lazyaddon/engine.py:41`
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### discover `def discover(self)`
- Defined: `lazyaddon/engine.py:60`
- Doc: Scan ``addons_dir`` and load every enabled addon into the registry.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### get `def get(self, name)`
- Defined: `lazyaddon/engine.py:77`
- Doc: Return the addon registered under ``name``, if any.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### all `def all(self)`
- Defined: `lazyaddon/engine.py:81`
- Doc: Return all currently registered addons.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### names `def names(self)`
- Defined: `lazyaddon/engine.py:85`
- Doc: Return the sorted names of all registered addons.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### build_params `def build_params(self, addon, overrides)`
- Defined: `lazyaddon/engine.py:90`
- Doc: Merge declared defaults with runtime overrides.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### install `def install(self, addon, overrides)`
- Defined: `lazyaddon/engine.py:127`
- Doc: Install (clone and build) an addon if not already present.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### run `def run(self, name, overrides, extra_args)`
- Defined: `lazyaddon/engine.py:145`
- Doc: Run a named addon through the full lifecycle.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### add `def add(self, raw, filename)`
- Defined: `lazyaddon/engine.py:185`
- Doc: Register a new addon by writing its YAML to ``addons_dir``.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### add_from_tool `def add_from_tool(self, name, repo_url, execute_command)`
- Defined: `lazyaddon/engine.py:218`
- Doc: Convenience builder for a tool-style addon.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### remove `def remove(self, name)`
- Defined: `lazyaddon/engine.py:262`
- Doc: Delete the addon file registered under ``name``.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### run_project `def run_project(self, project_path)`
- Defined: `lazyaddon/engine.py:281`
- Doc: Execute a declarative project file for non-programmers.
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### _load_file `def _load_file(self, path)`
- Defined: `lazyaddon/engine.py:340`
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### _addon_path `def _addon_path(self, name, filename)`
- Defined: `lazyaddon/engine.py:364`
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

### _find_addon_file `def _find_addon_file(self, name)`
- Defined: `lazyaddon/engine.py:373`
- Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`

## lazyaddon/installer.py

### __init__ `def __init__(self, config, runner, placeholders, security)`
- Defined: `lazyaddon/installer.py:33`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`

### install_path `def install_path(self, addon)`
- Defined: `lazyaddon/installer.py:45`
- Doc: Return the resolved on-disk install directory for an addon.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`

### is_installed `def is_installed(self, addon)`
- Defined: `lazyaddon/installer.py:60`
- Doc: Return True when the addon's install directory already exists.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`

### install `def install(self, addon, params)`
- Defined: `lazyaddon/installer.py:72`
- Doc: Clone and build an addon, skipping already-installed directories.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`

### _clone `def _clone(self, repo_url, target)`
- Defined: `lazyaddon/installer.py:108`
- Doc: Clone ``repo_url`` into ``target`` using a shallow checkout.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`

## lazyaddon/models.py

### _require_name `def _require_name(raw)`
- Defined: `lazyaddon/models.py:188`
- Doc: Extract and validate the required addon name field.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### _as_params `def _as_params(value)`
- Defined: `lazyaddon/models.py:196`
- Doc: Coerce the ``params`` field into a tuple of mappings.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### _build_param `def _build_param(raw, config)`
- Defined: `lazyaddon/models.py:209`
- Doc: Normalise a single parameter mapping into an ``AddonParam``.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### _build_tool `def _build_tool(name, raw, config)`
- Defined: `lazyaddon/models.py:225`
- Doc: Build and length-check the executable tool definition.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### _as_str_dict `def _as_str_dict(value)`
- Defined: `lazyaddon/models.py:242`
- Doc: Coerce an env mapping into ``{str: str}``.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### _as_str_tuple `def _as_str_tuple(value)`
- Defined: `lazyaddon/models.py:253`
- Doc: Coerce a trigger list into a tuple of strings.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### loads `def loads(cls, raw, config)`
- Defined: `lazyaddon/models.py:141`
- Doc: Build a validated ``AddonSpec`` from a parsed YAML mapping.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### param_by_name `def param_by_name(self, name)`
- Defined: `lazyaddon/models.py:176`
- Doc: Return the declared parameter matching ``name`` or None.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

### required_params `def required_params(self)`
- Defined: `lazyaddon/models.py:183`
- Doc: Return the names of all required parameters in declaration order.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`

## lazyaddon/placeholders.py

### __init__ `def __init__(self, config)`
- Defined: `lazyaddon/placeholders.py:34`
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `tests/test_placeholders.py`, `tests/test_placeholders_property.py`

### resolve `def resolve(self, command, params, untrusted_keys)`
- Defined: `lazyaddon/placeholders.py:37`
- Doc: Substitute placeholders in ``command`` using ``params``.
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `tests/test_placeholders.py`, `tests/test_placeholders_property.py`

### _replacement `def _replacement(self, match, params, untrusted)`
- Defined: `lazyaddon/placeholders.py:70`
- Depends on: `lazyaddon/config.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `tests/test_placeholders.py`, `tests/test_placeholders_property.py`

## lazyaddon/runner.py

### ok `def ok(self)`
- Defined: `lazyaddon/runner.py:46`
- Doc: True when the process exited with code zero.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### run `def run(self, command, cwd, env, timeout)`
- Defined: `lazyaddon/runner.py:54`
- Doc: Execute ``command`` and return its result.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### __init__ `def __init__(self, timeout_seconds, environment)`
- Defined: `lazyaddon/runner.py:72`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### run `def run(self, command, cwd, env, timeout)`
- Defined: `lazyaddon/runner.py:80`
- Doc: Execute ``command`` under a shell and capture its output.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### __call__ `def __call__(self, kind, payload, env)`
- Defined: `lazyaddon/runner.py:132`
- Doc: Handle one hook payload.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### execute `def execute(self, addon, params, extra_args, cwd, untrusted_keys)`
- Defined: `lazyaddon/runner.py:159`
- Doc: Resolve and run the addon's ``execute_command``.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### dispatch_hooks `def dispatch_hooks(self, addon, params, untrusted_keys)`
- Defined: `lazyaddon/runner.py:199`
- Doc: Dispatch framework-specific hooks declared on an addon.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### _dispatch_hooks `def _dispatch_hooks(self, addon, params, untrusted, env)`
- Defined: `lazyaddon/runner.py:218`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### _resolve_env `def _resolve_env(self, addon, params, untrusted)`
- Defined: `lazyaddon/runner.py:241`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### _default_untrusted `def _default_untrusted(self, addon)`
- Defined: `lazyaddon/runner.py:252`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

### _tool_cwd `def _tool_cwd(self, addon)`
- Defined: `lazyaddon/runner.py:255`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`

## lazyaddon/security.py

### __init__ `def __init__(self, config)`
- Defined: `lazyaddon/security.py:35`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/test_security.py`

### validate_addon `def validate_addon(self, addon)`
- Defined: `lazyaddon/security.py:38`
- Doc: Validate the network, filesystem and command fields of an addon.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/test_security.py`

### validate_repo_url `def validate_repo_url(self, url)`
- Defined: `lazyaddon/security.py:60`
- Doc: Validate a repository URL and return it unchanged.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/test_security.py`

### validate_command `def validate_command(self, command, label)`
- Defined: `lazyaddon/security.py:86`
- Doc: Validate a shell command string for length and null bytes.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/test_security.py`

### resolve_install_path `def resolve_install_path(self, install_path)`
- Defined: `lazyaddon/security.py:103`
- Doc: Resolve an addon install path inside the configured install root.
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`
- Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/test_security.py`

## tests/conftest.py

### make_config `def make_config(tmp_path)`
- Defined: `tests/conftest.py:79`
- Doc: Build an isolated config rooted at ``tmp_path``.
- Depends on: `lazyaddon/config.py`, `lazyaddon/runner.py`
- Imported by: `tests/test_cli.py`, `tests/test_engine.py`, `tests/test_runner.py`

### runner `def runner()`
- Defined: `tests/conftest.py:88`
- Doc: Yield a fresh fake process runner.
- Depends on: `lazyaddon/config.py`, `lazyaddon/runner.py`
- Imported by: `tests/test_cli.py`, `tests/test_engine.py`, `tests/test_runner.py`

### __init__ `def __init__(self)`
- Defined: `tests/conftest.py:22`
- Depends on: `lazyaddon/config.py`, `lazyaddon/runner.py`
- Imported by: `tests/test_cli.py`, `tests/test_engine.py`, `tests/test_runner.py`

### run `def run(self, command, cwd, env, timeout)`
- Defined: `tests/conftest.py:27`
- Depends on: `lazyaddon/config.py`, `lazyaddon/runner.py`
- Imported by: `tests/test_cli.py`, `tests/test_engine.py`, `tests/test_runner.py`

### last `def last(self)`
- Defined: `tests/conftest.py:44`
- Doc: Return the most recent invocation.
- Depends on: `lazyaddon/config.py`, `lazyaddon/runner.py`
- Imported by: `tests/test_cli.py`, `tests/test_engine.py`, `tests/test_runner.py`

### commands `def commands(self)`
- Defined: `tests/conftest.py:49`
- Doc: Return all recorded command strings.
- Depends on: `lazyaddon/config.py`, `lazyaddon/runner.py`
- Imported by: `tests/test_cli.py`, `tests/test_engine.py`, `tests/test_runner.py`

## tests/test_cli.py

### _run `def _run(argv)`
- Defined: `tests/test_cli.py:15`
- Doc: Invoke the CLI, capturing its exit code via SystemExit.
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_list_empty_directory `def test_list_empty_directory(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:24`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_add_then_list_and_show `def test_add_then_list_and_show(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:29`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_show_unknown_addon_fails `def test_show_unknown_addon_fails(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:50`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_add_rejects_insecure_repo `def test_add_rejects_insecure_repo(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:55`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_remove_addon `def test_remove_addon(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:68`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_run_addon_missing_param_fails `def test_run_addon_missing_param_fails(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:76`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_version_flag `def test_version_flag(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:86`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_list_json_emits_machine_readable `def test_list_json_emits_machine_readable(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:92`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_run_success_executes_addon `def test_run_success_executes_addon(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:102`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

### test_project_success `def test_project_success(tmp_path, monkeypatch)`
- Defined: `tests/test_cli.py:120`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

## tests/test_engine.py

### _write_addon `def _write_addon(tmp_path, data, name)`
- Defined: `tests/test_engine.py:17`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### _engine `def _engine(tmp_path, runner)`
- Defined: `tests/test_engine.py:26`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_discover_finds_enabled_addons `def test_discover_finds_enabled_addons(tmp_path, runner)`
- Defined: `tests/test_engine.py:31`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_discover_skips_disabled_addons `def test_discover_skips_disabled_addons(tmp_path, runner)`
- Defined: `tests/test_engine.py:40`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_discover_skips_invalid_and_insecure `def test_discover_skips_invalid_and_insecure(tmp_path, runner)`
- Defined: `tests/test_engine.py:48`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_full_lifecycle `def test_run_full_lifecycle(tmp_path, runner)`
- Defined: `tests/test_engine.py:55`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_unknown_name_raises `def test_run_unknown_name_raises(tmp_path, runner)`
- Defined: `tests/test_engine.py:65`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_disabled_raises `def test_run_disabled_raises(tmp_path, runner)`
- Defined: `tests/test_engine.py:72`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_missing_required_param_raises `def test_run_missing_required_param_raises(tmp_path, runner)`
- Defined: `tests/test_engine.py:81`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_no_install_leaves_install_alone `def test_run_no_install_leaves_install_alone(tmp_path, runner)`
- Defined: `tests/test_engine.py:89`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_with_extra_args `def test_run_with_extra_args(tmp_path, runner)`
- Defined: `tests/test_engine.py:97`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_add_registers_new_addon `def test_add_registers_new_addon(tmp_path, runner)`
- Defined: `tests/test_engine.py:105`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_add_rejects_insecure_repo `def test_add_rejects_insecure_repo(tmp_path, runner)`
- Defined: `tests/test_engine.py:120`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_remove_deletes_file `def test_remove_deletes_file(tmp_path, runner)`
- Defined: `tests/test_engine.py:126`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_remove_unknown_returns_none `def test_remove_unknown_returns_none(tmp_path, runner)`
- Defined: `tests/test_engine.py:136`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_project_file `def test_run_project_file(tmp_path, runner)`
- Defined: `tests/test_engine.py:141`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_project_unknown_addon_raises `def test_run_project_unknown_addon_raises(tmp_path, runner)`
- Defined: `tests/test_engine.py:170`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

### test_run_project_malformed_raises `def test_run_project_malformed_raises(tmp_path, runner)`
- Defined: `tests/test_engine.py:181`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

## tests/test_models.py

### _load `def _load(raw, config)`
- Defined: `tests/test_models.py:11`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_minimal_addon_defaults `def test_minimal_addon_defaults()`
- Defined: `tests/test_models.py:15`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_full_addon_parses_params_and_tool `def test_full_addon_parses_params_and_tool()`
- Defined: `tests/test_models.py:24`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_unknown_os_falls_back_to_default `def test_unknown_os_falls_back_to_default()`
- Defined: `tests/test_models.py:71`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_all_allowed_os_values_are_accepted `def test_all_allowed_os_values_are_accepted(os_value)`
- Defined: `tests/test_models.py:77`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_missing_name_raises `def test_missing_name_raises()`
- Defined: `tests/test_models.py:82`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_empty_name_raises `def test_empty_name_raises()`
- Defined: `tests/test_models.py:87`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_missing_tool_mapping_raises `def test_missing_tool_mapping_raises()`
- Defined: `tests/test_models.py:92`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_param_without_name_raises `def test_param_without_name_raises()`
- Defined: `tests/test_models.py:97`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_non_required_param_defaults_to_optional `def test_non_required_param_defaults_to_optional()`
- Defined: `tests/test_models.py:102`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_disabled_flag_is_preserved `def test_disabled_flag_is_preserved()`
- Defined: `tests/test_models.py:107`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_trigger_string_is_split `def test_trigger_string_is_split()`
- Defined: `tests/test_models.py:112`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_default_param_trusted_lookup `def test_default_param_trusted_lookup()`
- Defined: `tests/test_models.py:117`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_param_type_and_description_defaults `def test_param_type_and_description_defaults()`
- Defined: `tests/test_models.py:129`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_param_custom_type_and_description_are_kept `def test_param_custom_type_and_description_are_kept()`
- Defined: `tests/test_models.py:136`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_tool_name_falls_back_to_addon_name `def test_tool_name_falls_back_to_addon_name()`
- Defined: `tests/test_models.py:149`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

### test_tool_name_custom_wins `def test_tool_name_custom_wins()`
- Defined: `tests/test_models.py:154`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

## tests/test_placeholders.py

### _engine `def _engine()`
- Defined: `tests/test_placeholders.py:11`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_single_brace_substitution `def test_single_brace_substitution()`
- Defined: `tests/test_placeholders.py:15`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_double_brace_substitution `def test_double_brace_substitution()`
- Defined: `tests/test_placeholders.py:21`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_whitespace_inside_braces_is_ignored `def test_whitespace_inside_braces_is_ignored()`
- Defined: `tests/test_placeholders.py:25`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_unknown_placeholder_left_untouched `def test_unknown_placeholder_left_untouched()`
- Defined: `tests/test_placeholders.py:29`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_no_placeholders_is_passthrough `def test_no_placeholders_is_passthrough()`
- Defined: `tests/test_placeholders.py:33`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_repeated_placeholder_all_replaced `def test_repeated_placeholder_all_replaced()`
- Defined: `tests/test_placeholders.py:37`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_runtime_values_are_shell_quoted `def test_runtime_values_are_shell_quoted()`
- Defined: `tests/test_placeholders.py:42`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_trusted_values_are_not_quoted `def test_trusted_values_are_not_quoted()`
- Defined: `tests/test_placeholders.py:47`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_quoted_value_survives_dangerous_metachars `def test_quoted_value_survives_dangerous_metachars()`
- Defined: `tests/test_placeholders.py:52`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_null_char_value_is_quoted_not_bare `def test_null_char_value_is_quoted_not_bare()`
- Defined: `tests/test_placeholders.py:57`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_quote_disabled_by_config `def test_quote_disabled_by_config()`
- Defined: `tests/test_placeholders.py:63`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_non_string_command_raises `def test_non_string_command_raises()`
- Defined: `tests/test_placeholders.py:68`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

## tests/test_placeholders_property.py

### test_known_single_token_resolves `def test_known_single_token_resolves(key, value)`
- Defined: `tests/test_placeholders_property.py:22`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_unknown_token_left_untouched `def test_unknown_token_left_untouched(key, value)`
- Defined: `tests/test_placeholders_property.py:30`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

### test_untrusted_value_is_never_bare_metachar `def test_untrusted_value_is_never_bare_metachar(value)`
- Defined: `tests/test_placeholders_property.py:38`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

## tests/test_runner.py

### _engine `def _engine(tmp_path, runner)`
- Defined: `tests/test_runner.py:16`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### AddonConfigFixture `def AddonConfigFixture(tmp_path)`
- Defined: `tests/test_runner.py:21`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### _addon `def _addon()`
- Defined: `tests/test_runner.py:27`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_installer_clones_and_builds `def test_installer_clones_and_builds(tmp_path, runner)`
- Defined: `tests/test_runner.py:31`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_installer_skips_when_already_installed `def test_installer_skips_when_already_installed(tmp_path, runner)`
- Defined: `tests/test_runner.py:42`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_installer_force_reinstalls `def test_installer_force_reinstalls(tmp_path, runner)`
- Defined: `tests/test_runner.py:52`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_installer_requires_repo_url `def test_installer_requires_repo_url(tmp_path, runner)`
- Defined: `tests/test_runner.py:62`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_installer_no_install_path_is_noop `def test_installer_no_install_path_is_noop(tmp_path, runner)`
- Defined: `tests/test_runner.py:72`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_runner_executes_with_quoted_runtime_params `def test_runner_executes_with_quoted_runtime_params(runner)`
- Defined: `tests/test_runner.py:82`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_runner_quotes_injected_injection_value `def test_runner_quotes_injected_injection_value(runner)`
- Defined: `tests/test_runner.py:94`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_runner_raises_without_execute_command `def test_runner_raises_without_execute_command(runner)`
- Defined: `tests/test_runner.py:104`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_runner_dispatches_hooks `def test_runner_dispatches_hooks(runner)`
- Defined: `tests/test_runner.py:111`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_runner_resolves_env_placeholders `def test_runner_resolves_env_placeholders(runner)`
- Defined: `tests/test_runner.py:124`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

### test_runner_env_injection_value_is_quoted `def test_runner_env_injection_value_is_quoted(runner)`
- Defined: `tests/test_runner.py:134`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

## tests/test_security.py

### _policy `def _policy(config)`
- Defined: `tests/test_security.py:16`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### _addon `def _addon(repo_url, install_path, install_cmd, exec_cmd)`
- Defined: `tests/test_security.py:20`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_valid_repo_url_accepted `def test_valid_repo_url_accepted()`
- Defined: `tests/test_security.py:31`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_non_https_scheme_rejected `def test_non_https_scheme_rejected()`
- Defined: `tests/test_security.py:36`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_disallowed_host_rejected `def test_disallowed_host_rejected()`
- Defined: `tests/test_security.py:41`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_missing_path_rejected `def test_missing_path_rejected()`
- Defined: `tests/test_security.py:46`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_overlong_repo_url_rejected `def test_overlong_repo_url_rejected()`
- Defined: `tests/test_security.py:51`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_empty_repo_url_rejected `def test_empty_repo_url_rejected()`
- Defined: `tests/test_security.py:57`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_empty_host_allowed_when_allowlist_empty `def test_empty_host_allowed_when_allowlist_empty()`
- Defined: `tests/test_security.py:62`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_null_byte_in_command_rejected `def test_null_byte_in_command_rejected()`
- Defined: `tests/test_security.py:67`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_overlong_command_rejected `def test_overlong_command_rejected()`
- Defined: `tests/test_security.py:72`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_valid_command_accepted `def test_valid_command_accepted()`
- Defined: `tests/test_security.py:77`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_validate_addon_rejects_bad_url `def test_validate_addon_rejects_bad_url()`
- Defined: `tests/test_security.py:81`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_validate_addon_rejects_bad_install_command `def test_validate_addon_rejects_bad_install_command()`
- Defined: `tests/test_security.py:86`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_validate_addon_rejects_bad_execute_command `def test_validate_addon_rejects_bad_execute_command()`
- Defined: `tests/test_security.py:91`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_validate_addon_accepts_wellformed `def test_validate_addon_accepts_wellformed()`
- Defined: `tests/test_security.py:96`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_repo_url_with_port_and_path_ok `def test_repo_url_with_port_and_path_ok()`
- Defined: `tests/test_security.py:100`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_install_path_stays_in_root `def test_install_path_stays_in_root(tmp_path)`
- Defined: `tests/test_security.py:104`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_install_path_traversal_rejected `def test_install_path_traversal_rejected(tmp_path)`
- Defined: `tests/test_security.py:112`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_absolute_install_path_rejected `def test_absolute_install_path_rejected(tmp_path)`
- Defined: `tests/test_security.py:119`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`

### test_empty_install_path_no_tool_dir `def test_empty_install_path_no_tool_dir()`
- Defined: `tests/test_security.py:126`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`
