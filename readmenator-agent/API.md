# API

## lazyaddon/__main__.py
Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`
Imported by: `tests/test_cli.py`
- `build_parser` (function) `lazyaddon/__main__.py:20` `def build_parser()` -- Build the CLI argument parser.
- `main` (function) `lazyaddon/__main__.py:103` `def main(argv)` -- Run the lazyaddon CLI.

## lazyaddon/engine.py
Depends on: `lazyaddon/config.py`, `lazyaddon/installer.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `tests/test_engine.py`, `tests/test_runner.py`
- `LazyAddonEngine.__init__` (method) `lazyaddon/engine.py:41` `def __init__(self, config, runner, hooks)`
- `LazyAddonEngine.discover` (method) `lazyaddon/engine.py:60` `def discover(self)` -- Scan ``addons_dir`` and load every enabled addon into the registry.
- `LazyAddonEngine.get` (method) `lazyaddon/engine.py:77` `def get(self, name)` -- Return the addon registered under ``name``, if any.
- `LazyAddonEngine.all` (method) `lazyaddon/engine.py:81` `def all(self)` -- Return all currently registered addons.
- `LazyAddonEngine.names` (method) `lazyaddon/engine.py:85` `def names(self)` -- Return the sorted names of all registered addons.
- `LazyAddonEngine.build_params` (method) `lazyaddon/engine.py:90` `def build_params(self, addon, overrides)` -- Merge declared defaults with runtime overrides.
- `LazyAddonEngine.install` (method) `lazyaddon/engine.py:127` `def install(self, addon, overrides)` -- Install (clone and build) an addon if not already present.
- `LazyAddonEngine.run` (method) `lazyaddon/engine.py:145` `def run(self, name, overrides, extra_args)` -- Run a named addon through the full lifecycle.
- `LazyAddonEngine.add` (method) `lazyaddon/engine.py:185` `def add(self, raw, filename)` -- Register a new addon by writing its YAML to ``addons_dir``.
- `LazyAddonEngine.add_from_tool` (method) `lazyaddon/engine.py:218` `def add_from_tool(self, name, repo_url, execute_command)` -- Convenience builder for a tool-style addon.
- `LazyAddonEngine.remove` (method) `lazyaddon/engine.py:262` `def remove(self, name)` -- Delete the addon file registered under ``name``.
- `LazyAddonEngine.run_project` (method) `lazyaddon/engine.py:281` `def run_project(self, project_path)` -- Execute a declarative project file for non-programmers.

## lazyaddon/installer.py
Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`
Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`
- `AddonInstaller.__init__` (method) `lazyaddon/installer.py:33` `def __init__(self, config, runner, placeholders, security)`
- `AddonInstaller.install_path` (method) `lazyaddon/installer.py:45` `def install_path(self, addon)` -- Return the resolved on-disk install directory for an addon.
- `AddonInstaller.is_installed` (method) `lazyaddon/installer.py:60` `def is_installed(self, addon)` -- Return True when the addon's install directory already exists.
- `AddonInstaller.install` (method) `lazyaddon/installer.py:72` `def install(self, addon, params)` -- Clone and build an addon, skipping already-installed directories.

## lazyaddon/models.py
Depends on: `lazyaddon/config.py`
Imported by: `lazyaddon/__init__.py`, `lazyaddon/__main__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `lazyaddon/security.py`, `tests/test_engine.py`, `tests/test_models.py`, `tests/test_runner.py`, `tests/test_security.py`
- `AddonSpec.loads` (method) `lazyaddon/models.py:141` `def loads(cls, raw, config)` -- Build a validated ``AddonSpec`` from a parsed YAML mapping.
- `AddonSpec.param_by_name` (method) `lazyaddon/models.py:176` `def param_by_name(self, name)` -- Return the declared parameter matching ``name`` or None.
- `AddonSpec.required_params` (method) `lazyaddon/models.py:183` `def required_params(self)` -- Return the names of all required parameters in declaration order.

## lazyaddon/placeholders.py
Depends on: `lazyaddon/config.py`
Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `lazyaddon/runner.py`, `tests/test_placeholders.py`, `tests/test_placeholders_property.py`
- `PlaceholderEngine.__init__` (method) `lazyaddon/placeholders.py:34` `def __init__(self, config)`
- `PlaceholderEngine.resolve` (method) `lazyaddon/placeholders.py:37` `def resolve(self, command, params, untrusted_keys)` -- Substitute placeholders in ``command`` using ``params``.

## lazyaddon/runner.py
Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/placeholders.py`
Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/conftest.py`, `tests/test_runner.py`
- `CommandResult.ok` (method) `lazyaddon/runner.py:46` `def ok(self)` -- True when the process exited with code zero.
- `ProcessRunner.run` (method) `lazyaddon/runner.py:54` `def run(self, command, cwd, env, timeout)` -- Execute ``command`` and return its result.
- `CommandRunner.__init__` (method) `lazyaddon/runner.py:72` `def __init__(self, timeout_seconds, environment)`
- `CommandRunner.run` (method) `lazyaddon/runner.py:80` `def run(self, command, cwd, env, timeout)` -- Execute ``command`` under a shell and capture its output.
- `AddonHook.__call__` (method) `lazyaddon/runner.py:132` `def __call__(self, kind, payload, env)` -- Handle one hook payload.
- `AddonRunner.execute` (method) `lazyaddon/runner.py:159` `def execute(self, addon, params, extra_args, cwd, untrusted_keys)` -- Resolve and run the addon's ``execute_command``.
- `AddonRunner.dispatch_hooks` (method) `lazyaddon/runner.py:199` `def dispatch_hooks(self, addon, params, untrusted_keys)` -- Dispatch framework-specific hooks declared on an addon.

## lazyaddon/security.py
Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`
Imported by: `lazyaddon/__init__.py`, `lazyaddon/engine.py`, `lazyaddon/installer.py`, `tests/test_security.py`
- `SecurityPolicy.__init__` (method) `lazyaddon/security.py:35` `def __init__(self, config)`
- `SecurityPolicy.validate_addon` (method) `lazyaddon/security.py:38` `def validate_addon(self, addon)` -- Validate the network, filesystem and command fields of an addon.
- `SecurityPolicy.validate_repo_url` (method) `lazyaddon/security.py:60` `def validate_repo_url(self, url)` -- Validate a repository URL and return it unchanged.
- `SecurityPolicy.validate_command` (method) `lazyaddon/security.py:86` `def validate_command(self, command, label)` -- Validate a shell command string for length and null bytes.
- `SecurityPolicy.resolve_install_path` (method) `lazyaddon/security.py:103` `def resolve_install_path(self, install_path)` -- Resolve an addon install path inside the configured install root.
