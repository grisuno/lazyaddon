# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_dispatch` | function | `lazyaddon/__main__.py:118` | `def _dispatch(args, parser)` |
| `_json` | function | `lazyaddon/__main__.py:223` | `def _json(payload)` |
| `_make_engine` | function | `lazyaddon/__main__.py:81` | `def _make_engine(args)` |
| `_parse_overrides` | function | `lazyaddon/__main__.py:92` | `def _parse_overrides(raw)` |
| `_summary` | function | `lazyaddon/__main__.py:197` | `def _summary(addon)` |
| `build_parser` | function | `lazyaddon/__main__.py:20` | `def build_parser()` |
| `main` | function | `lazyaddon/__main__.py:103` | `def main(argv)` |
| `AddonConfig` | class | `lazyaddon/config.py:33` | `class AddonConfig` |
| `LazyAddonEngine` | class | `lazyaddon/engine.py:32` | `class LazyAddonEngine` |
| `__init__` | method | `lazyaddon/engine.py:41` | `def __init__(self, config, runner, hooks)` |
| `_addon_path` | method | `lazyaddon/engine.py:364` | `def _addon_path(self, name, filename)` |
| `_find_addon_file` | method | `lazyaddon/engine.py:373` | `def _find_addon_file(self, name)` |
| `_iter_yaml` | method | `lazyaddon/engine.py:388` | `def _iter_yaml(base, suffixes)` |
| `_load_file` | method | `lazyaddon/engine.py:340` | `def _load_file(self, path)` |
| `_project_config` | method | `lazyaddon/engine.py:402` | `def _project_config(base, data)` |
| `_safe_filename` | method | `lazyaddon/engine.py:396` | `def _safe_filename(name)` |
| `add` | method | `lazyaddon/engine.py:185` | `def add(self, raw, filename)` |
| `add_from_tool` | method | `lazyaddon/engine.py:218` | `def add_from_tool(self, name, repo_url, execute_command)` |
| `all` | method | `lazyaddon/engine.py:81` | `def all(self)` |
| `build_params` | method | `lazyaddon/engine.py:90` | `def build_params(self, addon, overrides)` |
| `discover` | method | `lazyaddon/engine.py:60` | `def discover(self)` |
| `get` | method | `lazyaddon/engine.py:77` | `def get(self, name)` |
| `install` | method | `lazyaddon/engine.py:127` | `def install(self, addon, overrides)` |
| `names` | method | `lazyaddon/engine.py:85` | `def names(self)` |
| `remove` | method | `lazyaddon/engine.py:262` | `def remove(self, name)` |
| `run` | method | `lazyaddon/engine.py:145` | `def run(self, name, overrides, extra_args)` |
| `run_project` | method | `lazyaddon/engine.py:281` | `def run_project(self, project_path)` |
| `AddonInstaller` | class | `lazyaddon/installer.py:23` | `class AddonInstaller` |
| `__init__` | method | `lazyaddon/installer.py:33` | `def __init__(self, config, runner, placeholders, security)` |
| `_clone` | method | `lazyaddon/installer.py:108` | `def _clone(self, repo_url, target)` |
| `install` | method | `lazyaddon/installer.py:72` | `def install(self, addon, params)` |
| `install_path` | method | `lazyaddon/installer.py:45` | `def install_path(self, addon)` |
| `is_installed` | method | `lazyaddon/installer.py:60` | `def is_installed(self, addon)` |
| `AddonError` | class | `lazyaddon/models.py:53` | `class AddonError(Exception)` |
| `AddonParam` | class | `lazyaddon/models.py:62` | `class AddonParam` |
| `AddonSpec` | class | `lazyaddon/models.py:113` | `class AddonSpec` |
| `SchemaError` | class | `lazyaddon/models.py:57` | `class SchemaError(AddonError)` |
| `ToolSpec` | class | `lazyaddon/models.py:81` | `class ToolSpec` |
| `_as_params` | method | `lazyaddon/models.py:196` | `def _as_params(value)` |
| `_as_str_dict` | method | `lazyaddon/models.py:242` | `def _as_str_dict(value)` |
| `_as_str_tuple` | method | `lazyaddon/models.py:253` | `def _as_str_tuple(value)` |
| `_build_param` | method | `lazyaddon/models.py:209` | `def _build_param(raw, config)` |
| `_build_tool` | method | `lazyaddon/models.py:225` | `def _build_tool(name, raw, config)` |
| `_require_name` | method | `lazyaddon/models.py:188` | `def _require_name(raw)` |
| `loads` | method | `lazyaddon/models.py:141` | `def loads(cls, raw, config)` |
| `param_by_name` | method | `lazyaddon/models.py:176` | `def param_by_name(self, name)` |
| `required_params` | method | `lazyaddon/models.py:183` | `def required_params(self)` |
| `PlaceholderEngine` | class | `lazyaddon/placeholders.py:27` | `class PlaceholderEngine` |
| `__init__` | method | `lazyaddon/placeholders.py:34` | `def __init__(self, config)` |
| `_replacement` | method | `lazyaddon/placeholders.py:70` | `def _replacement(self, match, params, untrusted)` |
| `resolve` | method | `lazyaddon/placeholders.py:37` | `def resolve(self, command, params, untrusted_keys)` |
| `AddonHook` | class | `lazyaddon/runner.py:124` | `class AddonHook(Protocol)` |
| `AddonRunner` | class | `lazyaddon/runner.py:143` | `class AddonRunner` |
| `CommandResult` | class | `lazyaddon/runner.py:30` | `class CommandResult` |
| `CommandRunner` | class | `lazyaddon/runner.py:64` | `class CommandRunner` |
| `ProcessRunner` | class | `lazyaddon/runner.py:51` | `class ProcessRunner(Protocol)` |
| `__call__` | method | `lazyaddon/runner.py:132` | `def __call__(self, kind, payload, env)` |
| `__init__` | method | `lazyaddon/runner.py:72` | `def __init__(self, timeout_seconds, environment)` |
| `_default_untrusted` | method | `lazyaddon/runner.py:252` | `def _default_untrusted(self, addon)` |
| `_dispatch_hooks` | method | `lazyaddon/runner.py:218` | `def _dispatch_hooks(self, addon, params, untrusted, env)` |
| `_resolve_env` | method | `lazyaddon/runner.py:241` | `def _resolve_env(self, addon, params, untrusted)` |
| `_tool_cwd` | method | `lazyaddon/runner.py:255` | `def _tool_cwd(self, addon)` |
| `dispatch_hooks` | method | `lazyaddon/runner.py:199` | `def dispatch_hooks(self, addon, params, untrusted_keys)` |
| `execute` | method | `lazyaddon/runner.py:159` | `def execute(self, addon, params, extra_args, cwd, untrusted_keys)` |
| `ok` | method | `lazyaddon/runner.py:46` | `def ok(self)` |
| `run` | method | `lazyaddon/runner.py:54` | `def run(self, command, cwd, env, timeout)` |
| `run` | method | `lazyaddon/runner.py:80` | `def run(self, command, cwd, env, timeout)` |
| `SecurityPolicy` | class | `lazyaddon/security.py:27` | `class SecurityPolicy` |
| `__init__` | method | `lazyaddon/security.py:35` | `def __init__(self, config)` |
| `resolve_install_path` | method | `lazyaddon/security.py:103` | `def resolve_install_path(self, install_path)` |
| `validate_addon` | method | `lazyaddon/security.py:38` | `def validate_addon(self, addon)` |
| `validate_command` | method | `lazyaddon/security.py:86` | `def validate_command(self, command, label)` |
| `validate_repo_url` | method | `lazyaddon/security.py:60` | `def validate_repo_url(self, url)` |
| `FakeRunner` | class | `tests/conftest.py:19` | `class FakeRunner` |
| `__init__` | method | `tests/conftest.py:22` | `def __init__(self)` |
| `commands` | method | `tests/conftest.py:49` | `def commands(self)` |
| `last` | method | `tests/conftest.py:44` | `def last(self)` |
| `make_config` | method | `tests/conftest.py:79` | `def make_config(tmp_path)` |
| `run` | method | `tests/conftest.py:27` | `def run(self, command, cwd, env, timeout)` |
| `runner` | method | `tests/conftest.py:88` | `def runner()` |
| `_run` | function | `tests/test_cli.py:15` | `def _run(argv)` |
| `test_add_rejects_insecure_repo` | function | `tests/test_cli.py:55` | `def test_add_rejects_insecure_repo(tmp_path, monkeypatch)` |
| `test_add_then_list_and_show` | function | `tests/test_cli.py:29` | `def test_add_then_list_and_show(tmp_path, monkeypatch)` |
| `test_list_empty_directory` | function | `tests/test_cli.py:24` | `def test_list_empty_directory(tmp_path, monkeypatch)` |
| `test_list_json_emits_machine_readable` | function | `tests/test_cli.py:92` | `def test_list_json_emits_machine_readable(tmp_path, monkeypatch)` |
| `test_project_success` | function | `tests/test_cli.py:120` | `def test_project_success(tmp_path, monkeypatch)` |
| `test_remove_addon` | function | `tests/test_cli.py:68` | `def test_remove_addon(tmp_path, monkeypatch)` |
| `test_run_addon_missing_param_fails` | function | `tests/test_cli.py:76` | `def test_run_addon_missing_param_fails(tmp_path, monkeypatch)` |
| `test_run_success_executes_addon` | function | `tests/test_cli.py:102` | `def test_run_success_executes_addon(tmp_path, monkeypatch)` |
| `test_show_unknown_addon_fails` | function | `tests/test_cli.py:50` | `def test_show_unknown_addon_fails(tmp_path, monkeypatch)` |
| `test_version_flag` | function | `tests/test_cli.py:86` | `def test_version_flag(tmp_path, monkeypatch)` |
| `_engine` | function | `tests/test_engine.py:26` | `def _engine(tmp_path, runner)` |
| `_write_addon` | function | `tests/test_engine.py:17` | `def _write_addon(tmp_path, data, name)` |
| `test_add_registers_new_addon` | function | `tests/test_engine.py:105` | `def test_add_registers_new_addon(tmp_path, runner)` |
| `test_add_rejects_insecure_repo` | function | `tests/test_engine.py:120` | `def test_add_rejects_insecure_repo(tmp_path, runner)` |
| `test_discover_finds_enabled_addons` | function | `tests/test_engine.py:31` | `def test_discover_finds_enabled_addons(tmp_path, runner)` |
| `test_discover_skips_disabled_addons` | function | `tests/test_engine.py:40` | `def test_discover_skips_disabled_addons(tmp_path, runner)` |
| `test_discover_skips_invalid_and_insecure` | function | `tests/test_engine.py:48` | `def test_discover_skips_invalid_and_insecure(tmp_path, runner)` |
| `test_remove_deletes_file` | function | `tests/test_engine.py:126` | `def test_remove_deletes_file(tmp_path, runner)` |
| `test_remove_unknown_returns_none` | function | `tests/test_engine.py:136` | `def test_remove_unknown_returns_none(tmp_path, runner)` |
| `test_run_disabled_raises` | function | `tests/test_engine.py:72` | `def test_run_disabled_raises(tmp_path, runner)` |
| `test_run_full_lifecycle` | function | `tests/test_engine.py:55` | `def test_run_full_lifecycle(tmp_path, runner)` |
| `test_run_missing_required_param_raises` | function | `tests/test_engine.py:81` | `def test_run_missing_required_param_raises(tmp_path, runner)` |
| `test_run_no_install_leaves_install_alone` | function | `tests/test_engine.py:89` | `def test_run_no_install_leaves_install_alone(tmp_path, runner)` |
| `test_run_project_file` | function | `tests/test_engine.py:141` | `def test_run_project_file(tmp_path, runner)` |
| `test_run_project_malformed_raises` | function | `tests/test_engine.py:181` | `def test_run_project_malformed_raises(tmp_path, runner)` |
| `test_run_project_unknown_addon_raises` | function | `tests/test_engine.py:170` | `def test_run_project_unknown_addon_raises(tmp_path, runner)` |
| `test_run_unknown_name_raises` | function | `tests/test_engine.py:65` | `def test_run_unknown_name_raises(tmp_path, runner)` |
| `test_run_with_extra_args` | function | `tests/test_engine.py:97` | `def test_run_with_extra_args(tmp_path, runner)` |
| `_load` | function | `tests/test_models.py:11` | `def _load(raw, config)` |
| `test_all_allowed_os_values_are_accepted` | function | `tests/test_models.py:77` | `def test_all_allowed_os_values_are_accepted(os_value)` |
| `test_default_param_trusted_lookup` | function | `tests/test_models.py:117` | `def test_default_param_trusted_lookup()` |
| `test_disabled_flag_is_preserved` | function | `tests/test_models.py:107` | `def test_disabled_flag_is_preserved()` |
| `test_empty_name_raises` | function | `tests/test_models.py:87` | `def test_empty_name_raises()` |
| `test_full_addon_parses_params_and_tool` | function | `tests/test_models.py:24` | `def test_full_addon_parses_params_and_tool()` |
| `test_minimal_addon_defaults` | function | `tests/test_models.py:15` | `def test_minimal_addon_defaults()` |
| `test_missing_name_raises` | function | `tests/test_models.py:82` | `def test_missing_name_raises()` |
| `test_missing_tool_mapping_raises` | function | `tests/test_models.py:92` | `def test_missing_tool_mapping_raises()` |
| `test_non_required_param_defaults_to_optional` | function | `tests/test_models.py:102` | `def test_non_required_param_defaults_to_optional()` |
| `test_param_custom_type_and_description_are_kept` | function | `tests/test_models.py:136` | `def test_param_custom_type_and_description_are_kept()` |
| `test_param_type_and_description_defaults` | function | `tests/test_models.py:129` | `def test_param_type_and_description_defaults()` |
| `test_param_without_name_raises` | function | `tests/test_models.py:97` | `def test_param_without_name_raises()` |
| `test_tool_name_custom_wins` | function | `tests/test_models.py:154` | `def test_tool_name_custom_wins()` |
| `test_tool_name_falls_back_to_addon_name` | function | `tests/test_models.py:149` | `def test_tool_name_falls_back_to_addon_name()` |
| `test_trigger_string_is_split` | function | `tests/test_models.py:112` | `def test_trigger_string_is_split()` |
| `test_unknown_os_falls_back_to_default` | function | `tests/test_models.py:71` | `def test_unknown_os_falls_back_to_default()` |
| `_engine` | function | `tests/test_placeholders.py:11` | `def _engine()` |
| `test_double_brace_substitution` | function | `tests/test_placeholders.py:21` | `def test_double_brace_substitution()` |
| `test_no_placeholders_is_passthrough` | function | `tests/test_placeholders.py:33` | `def test_no_placeholders_is_passthrough()` |
| `test_non_string_command_raises` | function | `tests/test_placeholders.py:68` | `def test_non_string_command_raises()` |
| `test_null_char_value_is_quoted_not_bare` | function | `tests/test_placeholders.py:57` | `def test_null_char_value_is_quoted_not_bare()` |
| `test_quote_disabled_by_config` | function | `tests/test_placeholders.py:63` | `def test_quote_disabled_by_config()` |
| `test_quoted_value_survives_dangerous_metachars` | function | `tests/test_placeholders.py:52` | `def test_quoted_value_survives_dangerous_metachars()` |
| `test_repeated_placeholder_all_replaced` | function | `tests/test_placeholders.py:37` | `def test_repeated_placeholder_all_replaced()` |
| `test_runtime_values_are_shell_quoted` | function | `tests/test_placeholders.py:42` | `def test_runtime_values_are_shell_quoted()` |
| `test_single_brace_substitution` | function | `tests/test_placeholders.py:15` | `def test_single_brace_substitution()` |
| `test_trusted_values_are_not_quoted` | function | `tests/test_placeholders.py:47` | `def test_trusted_values_are_not_quoted()` |
| `test_unknown_placeholder_left_untouched` | function | `tests/test_placeholders.py:29` | `def test_unknown_placeholder_left_untouched()` |
| `test_whitespace_inside_braces_is_ignored` | function | `tests/test_placeholders.py:25` | `def test_whitespace_inside_braces_is_ignored()` |
| `test_known_single_token_resolves` | function | `tests/test_placeholders_property.py:22` | `def test_known_single_token_resolves(key, value)` |
| `test_unknown_token_left_untouched` | function | `tests/test_placeholders_property.py:30` | `def test_unknown_token_left_untouched(key, value)` |
| `test_untrusted_value_is_never_bare_metachar` | function | `tests/test_placeholders_property.py:38` | `def test_untrusted_value_is_never_bare_metachar(value)` |
| `AddonConfigFixture` | function | `tests/test_runner.py:21` | `def AddonConfigFixture(tmp_path)` |
| `_addon` | function | `tests/test_runner.py:27` | `def _addon()` |
| `_engine` | function | `tests/test_runner.py:16` | `def _engine(tmp_path, runner)` |
| `test_installer_clones_and_builds` | function | `tests/test_runner.py:31` | `def test_installer_clones_and_builds(tmp_path, runner)` |
| `test_installer_force_reinstalls` | function | `tests/test_runner.py:52` | `def test_installer_force_reinstalls(tmp_path, runner)` |
| `test_installer_no_install_path_is_noop` | function | `tests/test_runner.py:72` | `def test_installer_no_install_path_is_noop(tmp_path, runner)` |
| `test_installer_requires_repo_url` | function | `tests/test_runner.py:62` | `def test_installer_requires_repo_url(tmp_path, runner)` |
| `test_installer_skips_when_already_installed` | function | `tests/test_runner.py:42` | `def test_installer_skips_when_already_installed(tmp_path, runner)` |
| `test_runner_dispatches_hooks` | function | `tests/test_runner.py:111` | `def test_runner_dispatches_hooks(runner)` |
| `test_runner_env_injection_value_is_quoted` | function | `tests/test_runner.py:134` | `def test_runner_env_injection_value_is_quoted(runner)` |
| `test_runner_executes_with_quoted_runtime_params` | function | `tests/test_runner.py:82` | `def test_runner_executes_with_quoted_runtime_params(runner)` |
| `test_runner_quotes_injected_injection_value` | function | `tests/test_runner.py:94` | `def test_runner_quotes_injected_injection_value(runner)` |
| `test_runner_raises_without_execute_command` | function | `tests/test_runner.py:104` | `def test_runner_raises_without_execute_command(runner)` |
| `test_runner_resolves_env_placeholders` | function | `tests/test_runner.py:124` | `def test_runner_resolves_env_placeholders(runner)` |
| `_addon` | function | `tests/test_security.py:20` | `def _addon(repo_url, install_path, install_cmd, exec_cmd)` |
| `_policy` | function | `tests/test_security.py:16` | `def _policy(config)` |
| `test_absolute_install_path_rejected` | function | `tests/test_security.py:119` | `def test_absolute_install_path_rejected(tmp_path)` |
| `test_disallowed_host_rejected` | function | `tests/test_security.py:41` | `def test_disallowed_host_rejected()` |
| `test_empty_host_allowed_when_allowlist_empty` | function | `tests/test_security.py:62` | `def test_empty_host_allowed_when_allowlist_empty()` |
| `test_empty_install_path_no_tool_dir` | function | `tests/test_security.py:126` | `def test_empty_install_path_no_tool_dir()` |
| `test_empty_repo_url_rejected` | function | `tests/test_security.py:57` | `def test_empty_repo_url_rejected()` |
| `test_install_path_stays_in_root` | function | `tests/test_security.py:104` | `def test_install_path_stays_in_root(tmp_path)` |
| `test_install_path_traversal_rejected` | function | `tests/test_security.py:112` | `def test_install_path_traversal_rejected(tmp_path)` |
| `test_missing_path_rejected` | function | `tests/test_security.py:46` | `def test_missing_path_rejected()` |
| `test_non_https_scheme_rejected` | function | `tests/test_security.py:36` | `def test_non_https_scheme_rejected()` |
| `test_null_byte_in_command_rejected` | function | `tests/test_security.py:67` | `def test_null_byte_in_command_rejected()` |
| `test_overlong_command_rejected` | function | `tests/test_security.py:72` | `def test_overlong_command_rejected()` |
| `test_overlong_repo_url_rejected` | function | `tests/test_security.py:51` | `def test_overlong_repo_url_rejected()` |
| `test_repo_url_with_port_and_path_ok` | function | `tests/test_security.py:100` | `def test_repo_url_with_port_and_path_ok()` |
| `test_valid_command_accepted` | function | `tests/test_security.py:77` | `def test_valid_command_accepted()` |
| `test_valid_repo_url_accepted` | function | `tests/test_security.py:31` | `def test_valid_repo_url_accepted()` |
| `test_validate_addon_accepts_wellformed` | function | `tests/test_security.py:96` | `def test_validate_addon_accepts_wellformed()` |
| `test_validate_addon_rejects_bad_execute_command` | function | `tests/test_security.py:91` | `def test_validate_addon_rejects_bad_execute_command()` |
| `test_validate_addon_rejects_bad_install_command` | function | `tests/test_security.py:86` | `def test_validate_addon_rejects_bad_install_command()` |
| `test_validate_addon_rejects_bad_url` | function | `tests/test_security.py:81` | `def test_validate_addon_rejects_bad_url()` |
