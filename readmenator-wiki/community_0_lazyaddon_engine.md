# lazyaddon: engine

*Community 0 | 5 files | cohesion 0.34*

## Definition

This community groups 5 file(s) rooted at `lazyaddon` with dominant language py (cohesion 0.34). Central symbols: `AddonHook`, `AddonInstaller`, `AddonRunner`, `CommandResult`, `CommandRunner`, `LazyAddonEngine`, `PlaceholderEngine`, `ProcessRunner`. Core file: `lazyaddon/engine.py` (19 symbols). Documented purpose: lazyaddon: declarative tool and extension manager.  Turns any GitHub/GitLab project into an installable, runnable addon from a single YAML file. Usable programm.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `lazyaddon/__init__.py` | py | utility | 0 | yes |
| `lazyaddon/engine.py` | py | utility | 19 | yes |
| `lazyaddon/installer.py` | py | utility | 6 | yes |
| `lazyaddon/placeholders.py` | py | utility | 4 | yes |
| `lazyaddon/runner.py` | py | utility | 16 | yes |

## Key Symbols

- `LazyAddonEngine` (class, `lazyaddon/engine.py:32`) `class LazyAddonEngine` - High-level addon management and execution engine.
- `__init__` (method, `lazyaddon/engine.py:41`) `def __init__(self, config, runner, hooks)`
- `discover` (method, `lazyaddon/engine.py:60`) `def discover(self)` - Scan ``addons_dir`` and load every enabled addon into the registry.
- `get` (method, `lazyaddon/engine.py:77`) `def get(self, name)` - Return the addon registered under ``name``, if any.
- `all` (method, `lazyaddon/engine.py:81`) `def all(self)` - Return all currently registered addons.
- `names` (method, `lazyaddon/engine.py:85`) `def names(self)` - Return the sorted names of all registered addons.
- `build_params` (method, `lazyaddon/engine.py:90`) `def build_params(self, addon, overrides)` - Merge declared defaults with runtime overrides.
- `install` (method, `lazyaddon/engine.py:127`) `def install(self, addon, overrides)` - Install (clone and build) an addon if not already present.
- `run` (method, `lazyaddon/engine.py:145`) `def run(self, name, overrides, extra_args)` - Run a named addon through the full lifecycle.
- `add` (method, `lazyaddon/engine.py:185`) `def add(self, raw, filename)` - Register a new addon by writing its YAML to ``addons_dir``.
- `add_from_tool` (method, `lazyaddon/engine.py:218`) `def add_from_tool(self, name, repo_url, execute_command)` - Convenience builder for a tool-style addon.
- `remove` (method, `lazyaddon/engine.py:262`) `def remove(self, name)` - Delete the addon file registered under ``name``.
- `run_project` (method, `lazyaddon/engine.py:281`) `def run_project(self, project_path)` - Execute a declarative project file for non-programmers.
- `_load_file` (method, `lazyaddon/engine.py:340`) `def _load_file(self, path)`
- `_addon_path` (method, `lazyaddon/engine.py:364`) `def _addon_path(self, name, filename)`
- `_find_addon_file` (method, `lazyaddon/engine.py:373`) `def _find_addon_file(self, name)`
- `_iter_yaml` (method, `lazyaddon/engine.py:388`) `def _iter_yaml(base, suffixes)` - Return sorted YAML files under ``base`` matching ``suffixes``.
- `_safe_filename` (method, `lazyaddon/engine.py:396`) `def _safe_filename(name)` - Sanitise an addon name into a safe filename token.
- `_project_config` (method, `lazyaddon/engine.py:402`) `def _project_config(base, data)` - Derive an updated config from optional project overrides.
- `AddonInstaller` (class, `lazyaddon/installer.py:23`) `class AddonInstaller` - Clones and builds addons on disk.
- `__init__` (method, `lazyaddon/installer.py:33`) `def __init__(self, config, runner, placeholders, security)`
- `install_path` (method, `lazyaddon/installer.py:45`) `def install_path(self, addon)` - Return the resolved on-disk install directory for an addon.
- `is_installed` (method, `lazyaddon/installer.py:60`) `def is_installed(self, addon)` - Return True when the addon's install directory already exists.
- `install` (method, `lazyaddon/installer.py:72`) `def install(self, addon, params)` - Clone and build an addon, skipping already-installed directories.
- `_clone` (method, `lazyaddon/installer.py:108`) `def _clone(self, repo_url, target)` - Clone ``repo_url`` into ``target`` using a shallow checkout.
- `PlaceholderEngine` (class, `lazyaddon/placeholders.py:27`) `class PlaceholderEngine` - Resolves placeholder tokens within command strings.
- `__init__` (method, `lazyaddon/placeholders.py:34`) `def __init__(self, config)`
- `resolve` (method, `lazyaddon/placeholders.py:37`) `def resolve(self, command, params, untrusted_keys)` - Substitute placeholders in ``command`` using ``params``.
- `_replacement` (method, `lazyaddon/placeholders.py:70`) `def _replacement(self, match, params, untrusted)`
- `CommandResult` (class, `lazyaddon/runner.py:30`) `class CommandResult` - Outcome of a shell command execution.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 10
- Cross-boundary resolved imports (EXTRACTED): 19

## Connections

- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__init__.py imports lazyaddon/config.py.
- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__init__.py imports lazyaddon/models.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__main__.py imports lazyaddon/engine.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/__init__.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/installer.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/placeholders.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] shares_context community 0 <-> 4 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (lazyaddon: engine) and community 4 (orphans).

## Risks

- [taint high] `lazyaddon/runner.py` -> `lazyaddon/runner.py` via `subprocess` (0 hops)
- [taint high] `lazyaddon/runner.py` -> `lazyaddon/placeholders.py` via `subprocess` (1 hops)
- [taint high] `lazyaddon/runner.py` -> `lazyaddon/models.py` via `subprocess` (1 hops)
- [taint high] `lazyaddon/runner.py` -> `lazyaddon/config.py` via `subprocess` (1 hops)

## Open Questions

- Is the dangerous import `subprocess` in `lazyaddon/runner.py` still required, or can it be isolated?
- What would break if the most connected file in lazyaddon: engine changed?
- Should lazyaddon: engine be split, given cohesion 0.34?

## Sources

- `lazyaddon/__init__.py`
- `lazyaddon/engine.py`
- `lazyaddon/installer.py`
- `lazyaddon/placeholders.py`
- `lazyaddon/runner.py`
