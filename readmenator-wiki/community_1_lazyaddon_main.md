# lazyaddon: __main__

*Community 1 | 5 files | cohesion 0.25*

## Definition

This community groups 5 file(s) rooted at `tests` with dominant language py (cohesion 0.25). Central symbols: `AddonConfigFixture`, `FakeRunner`, `__init__`, `_addon`, `_dispatch`, `_engine`, `_json`, `_make_engine`. Core file: `tests/test_engine.py` (18 symbols). Documented purpose: Console entry point for lazyaddon.  Exposes subcommands for discovery, installation, execution, marketplace registration and declarative project runs. Invoked v.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `lazyaddon/__main__.py` | py | utility | 7 | yes |
| `tests/conftest.py` | py | testing | 7 | yes |
| `tests/test_cli.py` | py | testing | 11 | yes |
| `tests/test_engine.py` | py | testing | 18 | yes |
| `tests/test_runner.py` | py | testing | 14 | yes |

## Key Symbols

- `build_parser` (function, `lazyaddon/__main__.py:20`) `def build_parser()` - Build the CLI argument parser.
- `_make_engine` (function, `lazyaddon/__main__.py:81`) `def _make_engine(args)` - Build an engine honouring the CLI-level directory overrides.
- `_parse_overrides` (function, `lazyaddon/__main__.py:92`) `def _parse_overrides(raw)` - Parse ``key=value`` CLI overrides into a parameter mapping.
- `main` (function, `lazyaddon/__main__.py:103`) `def main(argv)` - Run the lazyaddon CLI.
- `_dispatch` (function, `lazyaddon/__main__.py:118`) `def _dispatch(args, parser)` - Route a parsed command to its handler.
- `_summary` (function, `lazyaddon/__main__.py:197`) `def _summary(addon)` - Build a compact serialisable summary of an addon.
- `_json` (function, `lazyaddon/__main__.py:223`) `def _json(payload)` - Serialize ``payload`` to a compact JSON string.
- `FakeRunner` (class, `tests/conftest.py:19`) `class FakeRunner` - In-process substitute for :class:`CommandRunner`.
- `__init__` (method, `tests/conftest.py:22`) `def __init__(self)`
- `run` (method, `tests/conftest.py:27`) `def run(self, command, cwd, env, timeout)`
- `last` (method, `tests/conftest.py:44`) `def last(self)` - Return the most recent invocation.
- `commands` (method, `tests/conftest.py:49`) `def commands(self)` - Return all recorded command strings.
- `make_config` (method, `tests/conftest.py:79`) `def make_config(tmp_path)` - Build an isolated config rooted at ``tmp_path``.
- `runner` (method, `tests/conftest.py:88`) `def runner()` - Yield a fresh fake process runner.
- `_run` (function, `tests/test_cli.py:15`) `def _run(argv)` - Invoke the CLI, capturing its exit code via SystemExit.
- `test_list_empty_directory` (function, `tests/test_cli.py:24`) `def test_list_empty_directory(tmp_path, monkeypatch)`
- `test_add_then_list_and_show` (function, `tests/test_cli.py:29`) `def test_add_then_list_and_show(tmp_path, monkeypatch)`
- `test_show_unknown_addon_fails` (function, `tests/test_cli.py:50`) `def test_show_unknown_addon_fails(tmp_path, monkeypatch)`
- `test_add_rejects_insecure_repo` (function, `tests/test_cli.py:55`) `def test_add_rejects_insecure_repo(tmp_path, monkeypatch)`
- `test_remove_addon` (function, `tests/test_cli.py:68`) `def test_remove_addon(tmp_path, monkeypatch)`
- `test_run_addon_missing_param_fails` (function, `tests/test_cli.py:76`) `def test_run_addon_missing_param_fails(tmp_path, monkeypatch)`
- `test_version_flag` (function, `tests/test_cli.py:86`) `def test_version_flag(tmp_path, monkeypatch)`
- `test_list_json_emits_machine_readable` (function, `tests/test_cli.py:92`) `def test_list_json_emits_machine_readable(tmp_path, monkeypatch)`
- `test_run_success_executes_addon` (function, `tests/test_cli.py:102`) `def test_run_success_executes_addon(tmp_path, monkeypatch)`
- `test_project_success` (function, `tests/test_cli.py:120`) `def test_project_success(tmp_path, monkeypatch)`
- `_write_addon` (function, `tests/test_engine.py:17`) `def _write_addon(tmp_path, data, name)`
- `_engine` (function, `tests/test_engine.py:26`) `def _engine(tmp_path, runner)`
- `test_discover_finds_enabled_addons` (function, `tests/test_engine.py:31`) `def test_discover_finds_enabled_addons(tmp_path, runner)`
- `test_discover_skips_disabled_addons` (function, `tests/test_engine.py:40`) `def test_discover_skips_disabled_addons(tmp_path, runner)`
- `test_discover_skips_invalid_and_insecure` (function, `tests/test_engine.py:48`) `def test_discover_skips_invalid_and_insecure(tmp_path, runner)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 4
- Cross-boundary resolved imports (EXTRACTED): 12

## Connections

- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__main__.py imports lazyaddon/engine.py.
- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__main__.py imports lazyaddon/models.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__main__.py imports lazyaddon/config.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/__init__.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/installer.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/placeholders.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] bridges community 3 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/security.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] bridges community 1 <-> 2 (strength 0.7): Inferred cross-community bridge: tests/test_cli.py reaches tests/test_models.py in 3 hops.
- [INFERRED] shares_context community 1 <-> 4 (strength 0.5): Inferred shared context (language py and layer testing) with no import path between community 1 (lazyaddon: __main__) and community 4 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in lazyaddon: __main__ changed?
- Should lazyaddon: __main__ be split, given cohesion 0.25?

## Sources

- `lazyaddon/__main__.py`
- `tests/conftest.py`
- `tests/test_cli.py`
- `tests/test_engine.py`
- `tests/test_runner.py`
