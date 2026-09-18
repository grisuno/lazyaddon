# Subsystem: tests

## tests/__init__.py
- Layer: testing
- Doc: Test package for lazyaddon.
- Language: py

## tests/conftest.py
- Layer: testing
- Doc: Shared fixtures for the lazyaddon test suite.  Provides a fake :class:`ProcessRunner` that records invocations instead o
- Language: py
- Symbols:
  - `FakeRunner` (class, line 19) `class FakeRunner`
  - `make_config` (method, line 79) `def make_config(tmp_path)`
  - `runner` (method, line 88) `def runner()`
  - `__init__` (method, line 22) `def __init__(self)`
  - `run` (method, line 27) `def run(self, command, cwd, env, timeout)`
  - `last` (method, line 44) `def last(self)`
  - `commands` (method, line 49) `def commands(self)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/runner.py`
- Imported by: `tests/test_cli.py`, `tests/test_engine.py`, `tests/test_runner.py`

## tests/test_cli.py
- Layer: testing
- Doc: BDD-style CLI tests exercising the console script end to end.
- Language: py
- Symbols:
  - `_run` (function, line 15) `def _run(argv)`
  - `test_list_empty_directory` (function, line 24) `def test_list_empty_directory(tmp_path, monkeypatch)`
  - `test_add_then_list_and_show` (function, line 29) `def test_add_then_list_and_show(tmp_path, monkeypatch)`
  - `test_show_unknown_addon_fails` (function, line 50) `def test_show_unknown_addon_fails(tmp_path, monkeypatch)`
  - `test_add_rejects_insecure_repo` (function, line 55) `def test_add_rejects_insecure_repo(tmp_path, monkeypatch)`
  - `test_remove_addon` (function, line 68) `def test_remove_addon(tmp_path, monkeypatch)`
  - `test_run_addon_missing_param_fails` (function, line 76) `def test_run_addon_missing_param_fails(tmp_path, monkeypatch)`
  - `test_version_flag` (function, line 86) `def test_version_flag(tmp_path, monkeypatch)`
  - `test_list_json_emits_machine_readable` (function, line 92) `def test_list_json_emits_machine_readable(tmp_path, monkeypatch)`
  - `test_run_success_executes_addon` (function, line 102) `def test_run_success_executes_addon(tmp_path, monkeypatch)`
  - `test_project_success` (function, line 120) `def test_project_success(tmp_path, monkeypatch)`
- Depends on: `lazyaddon/__main__.py`, `tests/conftest.py`

## tests/test_engine.py
- Layer: testing
- Doc: BDD/TDD tests for the engine facade: discovery, run, marketplace, project.
- Language: py
- Symbols:
  - `_write_addon` (function, line 17) `def _write_addon(tmp_path, data, name)`
  - `_engine` (function, line 26) `def _engine(tmp_path, runner)`
  - `test_discover_finds_enabled_addons` (function, line 31) `def test_discover_finds_enabled_addons(tmp_path, runner)`
  - `test_discover_skips_disabled_addons` (function, line 40) `def test_discover_skips_disabled_addons(tmp_path, runner)`
  - `test_discover_skips_invalid_and_insecure` (function, line 48) `def test_discover_skips_invalid_and_insecure(tmp_path, runner)`
  - `test_run_full_lifecycle` (function, line 55) `def test_run_full_lifecycle(tmp_path, runner)`
  - `test_run_unknown_name_raises` (function, line 65) `def test_run_unknown_name_raises(tmp_path, runner)`
  - `test_run_disabled_raises` (function, line 72) `def test_run_disabled_raises(tmp_path, runner)`
  - `test_run_missing_required_param_raises` (function, line 81) `def test_run_missing_required_param_raises(tmp_path, runner)`
  - `test_run_no_install_leaves_install_alone` (function, line 89) `def test_run_no_install_leaves_install_alone(tmp_path, runner)`
  - `test_run_with_extra_args` (function, line 97) `def test_run_with_extra_args(tmp_path, runner)`
  - `test_add_registers_new_addon` (function, line 105) `def test_add_registers_new_addon(tmp_path, runner)`
  - `test_add_rejects_insecure_repo` (function, line 120) `def test_add_rejects_insecure_repo(tmp_path, runner)`
  - `test_remove_deletes_file` (function, line 126) `def test_remove_deletes_file(tmp_path, runner)`
  - `test_remove_unknown_returns_none` (function, line 136) `def test_remove_unknown_returns_none(tmp_path, runner)`
  - `test_run_project_file` (function, line 141) `def test_run_project_file(tmp_path, runner)`
  - `test_run_project_unknown_addon_raises` (function, line 170) `def test_run_project_unknown_addon_raises(tmp_path, runner)`
  - `test_run_project_malformed_raises` (function, line 181) `def test_run_project_malformed_raises(tmp_path, runner)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `tests/conftest.py`

## tests/test_models.py
- Layer: testing
- Doc: BDD/TDD behavioural tests for addon schema parsing and validation.
- Language: py
- Symbols:
  - `_load` (function, line 11) `def _load(raw, config)`
  - `test_minimal_addon_defaults` (function, line 15) `def test_minimal_addon_defaults()`
  - `test_full_addon_parses_params_and_tool` (function, line 24) `def test_full_addon_parses_params_and_tool()`
  - `test_unknown_os_falls_back_to_default` (function, line 71) `def test_unknown_os_falls_back_to_default()`
  - `test_all_allowed_os_values_are_accepted` (function, line 77) `def test_all_allowed_os_values_are_accepted(os_value)`
  - `test_missing_name_raises` (function, line 82) `def test_missing_name_raises()`
  - `test_empty_name_raises` (function, line 87) `def test_empty_name_raises()`
  - `test_missing_tool_mapping_raises` (function, line 92) `def test_missing_tool_mapping_raises()`
  - `test_param_without_name_raises` (function, line 97) `def test_param_without_name_raises()`
  - `test_non_required_param_defaults_to_optional` (function, line 102) `def test_non_required_param_defaults_to_optional()`
  - `test_disabled_flag_is_preserved` (function, line 107) `def test_disabled_flag_is_preserved()`
  - `test_trigger_string_is_split` (function, line 112) `def test_trigger_string_is_split()`
  - `test_default_param_trusted_lookup` (function, line 117) `def test_default_param_trusted_lookup()`
  - `test_param_type_and_description_defaults` (function, line 129) `def test_param_type_and_description_defaults()`
  - `test_param_custom_type_and_description_are_kept` (function, line 136) `def test_param_custom_type_and_description_are_kept()`
  - `test_tool_name_falls_back_to_addon_name` (function, line 149) `def test_tool_name_falls_back_to_addon_name()`
  - `test_tool_name_custom_wins` (function, line 154) `def test_tool_name_custom_wins()`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`

## tests/test_placeholders.py
- Layer: testing
- Doc: BDD/TDD tests for the placeholder substitution engine.
- Language: py
- Symbols:
  - `_engine` (function, line 11) `def _engine()`
  - `test_single_brace_substitution` (function, line 15) `def test_single_brace_substitution()`
  - `test_double_brace_substitution` (function, line 21) `def test_double_brace_substitution()`
  - `test_whitespace_inside_braces_is_ignored` (function, line 25) `def test_whitespace_inside_braces_is_ignored()`
  - `test_unknown_placeholder_left_untouched` (function, line 29) `def test_unknown_placeholder_left_untouched()`
  - `test_no_placeholders_is_passthrough` (function, line 33) `def test_no_placeholders_is_passthrough()`
  - `test_repeated_placeholder_all_replaced` (function, line 37) `def test_repeated_placeholder_all_replaced()`
  - `test_runtime_values_are_shell_quoted` (function, line 42) `def test_runtime_values_are_shell_quoted()`
  - `test_trusted_values_are_not_quoted` (function, line 47) `def test_trusted_values_are_not_quoted()`
  - `test_quoted_value_survives_dangerous_metachars` (function, line 52) `def test_quoted_value_survives_dangerous_metachars()`
  - `test_null_char_value_is_quoted_not_bare` (function, line 57) `def test_null_char_value_is_quoted_not_bare()`
  - `test_quote_disabled_by_config` (function, line 63) `def test_quote_disabled_by_config()`
  - `test_non_string_command_raises` (function, line 68) `def test_non_string_command_raises()`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

## tests/test_placeholders_property.py
- Layer: testing
- Doc: Property-based tests for the placeholder engine using hypothesis.  These complement the unit tests by checking the core 
- Language: py
- Symbols:
  - `test_known_single_token_resolves` (function, line 22) `def test_known_single_token_resolves(key, value)`
  - `test_unknown_token_left_untouched` (function, line 30) `def test_unknown_token_left_untouched(key, value)`
  - `test_untrusted_value_is_never_bare_metachar` (function, line 38) `def test_untrusted_value_is_never_bare_metachar(value)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/placeholders.py`

## tests/test_runner.py
- Layer: testing
- Doc: BDD/TDD tests for the installer and runner contracts.
- Language: py
- Symbols:
  - `_engine` (function, line 16) `def _engine(tmp_path, runner)`
  - `AddonConfigFixture` (function, line 21) `def AddonConfigFixture(tmp_path)`
  - `_addon` (function, line 27) `def _addon()`
  - `test_installer_clones_and_builds` (function, line 31) `def test_installer_clones_and_builds(tmp_path, runner)`
  - `test_installer_skips_when_already_installed` (function, line 42) `def test_installer_skips_when_already_installed(tmp_path, runner)`
  - `test_installer_force_reinstalls` (function, line 52) `def test_installer_force_reinstalls(tmp_path, runner)`
  - `test_installer_requires_repo_url` (function, line 62) `def test_installer_requires_repo_url(tmp_path, runner)`
  - `test_installer_no_install_path_is_noop` (function, line 72) `def test_installer_no_install_path_is_noop(tmp_path, runner)`
  - `test_runner_executes_with_quoted_runtime_params` (function, line 82) `def test_runner_executes_with_quoted_runtime_params(runner)`
  - `test_runner_quotes_injected_injection_value` (function, line 94) `def test_runner_quotes_injected_injection_value(runner)`
  - `test_runner_raises_without_execute_command` (function, line 104) `def test_runner_raises_without_execute_command(runner)`
  - `test_runner_dispatches_hooks` (function, line 111) `def test_runner_dispatches_hooks(runner)`
  - `test_runner_resolves_env_placeholders` (function, line 124) `def test_runner_resolves_env_placeholders(runner)`
  - `test_runner_env_injection_value_is_quoted` (function, line 134) `def test_runner_env_injection_value_is_quoted(runner)`
- Depends on: `lazyaddon/config.py`, `lazyaddon/engine.py`, `lazyaddon/models.py`, `lazyaddon/runner.py`, `tests/conftest.py`

## tests/test_security.py
- Layer: testing
- Doc: BDD/TDD tests for the security policy contract.
- Language: py
- Symbols:
  - `_policy` (function, line 16) `def _policy(config)`
  - `_addon` (function, line 20) `def _addon(repo_url, install_path, install_cmd, exec_cmd)`
  - `test_valid_repo_url_accepted` (function, line 31) `def test_valid_repo_url_accepted()`
  - `test_non_https_scheme_rejected` (function, line 36) `def test_non_https_scheme_rejected()`
  - `test_disallowed_host_rejected` (function, line 41) `def test_disallowed_host_rejected()`
  - `test_missing_path_rejected` (function, line 46) `def test_missing_path_rejected()`
  - `test_overlong_repo_url_rejected` (function, line 51) `def test_overlong_repo_url_rejected()`
  - `test_empty_repo_url_rejected` (function, line 57) `def test_empty_repo_url_rejected()`
  - `test_empty_host_allowed_when_allowlist_empty` (function, line 62) `def test_empty_host_allowed_when_allowlist_empty()`
  - `test_null_byte_in_command_rejected` (function, line 67) `def test_null_byte_in_command_rejected()`
  - `test_overlong_command_rejected` (function, line 72) `def test_overlong_command_rejected()`
  - `test_valid_command_accepted` (function, line 77) `def test_valid_command_accepted()`
  - `test_validate_addon_rejects_bad_url` (function, line 81) `def test_validate_addon_rejects_bad_url()`
  - `test_validate_addon_rejects_bad_install_command` (function, line 86) `def test_validate_addon_rejects_bad_install_command()`
  - `test_validate_addon_rejects_bad_execute_command` (function, line 91) `def test_validate_addon_rejects_bad_execute_command()`
  - `test_validate_addon_accepts_wellformed` (function, line 96) `def test_validate_addon_accepts_wellformed()`
  - `test_repo_url_with_port_and_path_ok` (function, line 100) `def test_repo_url_with_port_and_path_ok()`
  - `test_install_path_stays_in_root` (function, line 104) `def test_install_path_stays_in_root(tmp_path)`
  - `test_install_path_traversal_rejected` (function, line 112) `def test_install_path_traversal_rejected(tmp_path)`
  - `test_absolute_install_path_rejected` (function, line 119) `def test_absolute_install_path_rejected(tmp_path)`
  - `test_empty_install_path_no_tool_dir` (function, line 126) `def test_empty_install_path_no_tool_dir()`
- Depends on: `lazyaddon/config.py`, `lazyaddon/models.py`, `lazyaddon/security.py`
