# lazyaddon: config

*Community 2 | 4 files | cohesion 0.17*

## Definition

This community groups 4 file(s) rooted at `tests` with dominant language py (cohesion 0.17). Central symbols: `AddonConfig`, `_engine`, `_load`, `test_all_allowed_os_values_are_accepted`, `test_default_param_trusted_lookup`, `test_disabled_flag_is_preserved`, `test_double_brace_substitution`, `test_empty_name_raises`. Core file: `tests/test_models.py` (17 symbols). Documented purpose: Centralized configuration contract for the lazyaddon engine.  Holds every tunable knob used across the package so no magic numbers or hardcoded strings leak int.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `lazyaddon/config.py` | py | infrastructure | 1 | yes |
| `tests/test_models.py` | py | testing | 17 | yes |
| `tests/test_placeholders.py` | py | testing | 13 | yes |
| `tests/test_placeholders_property.py` | py | testing | 3 | yes |

## Key Symbols

- `AddonConfig` (class, `lazyaddon/config.py:33`) `class AddonConfig` - Immutable engine configuration.
- `_load` (function, `tests/test_models.py:11`) `def _load(raw, config)`
- `test_minimal_addon_defaults` (function, `tests/test_models.py:15`) `def test_minimal_addon_defaults()`
- `test_full_addon_parses_params_and_tool` (function, `tests/test_models.py:24`) `def test_full_addon_parses_params_and_tool()`
- `test_unknown_os_falls_back_to_default` (function, `tests/test_models.py:71`) `def test_unknown_os_falls_back_to_default()`
- `test_all_allowed_os_values_are_accepted` (function, `tests/test_models.py:77`) `def test_all_allowed_os_values_are_accepted(os_value)`
- `test_missing_name_raises` (function, `tests/test_models.py:82`) `def test_missing_name_raises()`
- `test_empty_name_raises` (function, `tests/test_models.py:87`) `def test_empty_name_raises()`
- `test_missing_tool_mapping_raises` (function, `tests/test_models.py:92`) `def test_missing_tool_mapping_raises()`
- `test_param_without_name_raises` (function, `tests/test_models.py:97`) `def test_param_without_name_raises()`
- `test_non_required_param_defaults_to_optional` (function, `tests/test_models.py:102`) `def test_non_required_param_defaults_to_optional()`
- `test_disabled_flag_is_preserved` (function, `tests/test_models.py:107`) `def test_disabled_flag_is_preserved()`
- `test_trigger_string_is_split` (function, `tests/test_models.py:112`) `def test_trigger_string_is_split()`
- `test_default_param_trusted_lookup` (function, `tests/test_models.py:117`) `def test_default_param_trusted_lookup()`
- `test_param_type_and_description_defaults` (function, `tests/test_models.py:129`) `def test_param_type_and_description_defaults()`
- `test_param_custom_type_and_description_are_kept` (function, `tests/test_models.py:136`) `def test_param_custom_type_and_description_are_kept()`
- `test_tool_name_falls_back_to_addon_name` (function, `tests/test_models.py:149`) `def test_tool_name_falls_back_to_addon_name()`
- `test_tool_name_custom_wins` (function, `tests/test_models.py:154`) `def test_tool_name_custom_wins()`
- `_engine` (function, `tests/test_placeholders.py:11`) `def _engine()`
- `test_single_brace_substitution` (function, `tests/test_placeholders.py:15`) `def test_single_brace_substitution()`
- `test_double_brace_substitution` (function, `tests/test_placeholders.py:21`) `def test_double_brace_substitution()`
- `test_whitespace_inside_braces_is_ignored` (function, `tests/test_placeholders.py:25`) `def test_whitespace_inside_braces_is_ignored()`
- `test_unknown_placeholder_left_untouched` (function, `tests/test_placeholders.py:29`) `def test_unknown_placeholder_left_untouched()`
- `test_no_placeholders_is_passthrough` (function, `tests/test_placeholders.py:33`) `def test_no_placeholders_is_passthrough()`
- `test_repeated_placeholder_all_replaced` (function, `tests/test_placeholders.py:37`) `def test_repeated_placeholder_all_replaced()`
- `test_runtime_values_are_shell_quoted` (function, `tests/test_placeholders.py:42`) `def test_runtime_values_are_shell_quoted()`
- `test_trusted_values_are_not_quoted` (function, `tests/test_placeholders.py:47`) `def test_trusted_values_are_not_quoted()`
- `test_quoted_value_survives_dangerous_metachars` (function, `tests/test_placeholders.py:52`) `def test_quoted_value_survives_dangerous_metachars()`
- `test_null_char_value_is_quoted_not_bare` (function, `tests/test_placeholders.py:57`) `def test_null_char_value_is_quoted_not_bare()`
- `test_quote_disabled_by_config` (function, `tests/test_placeholders.py:63`) `def test_quote_disabled_by_config()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 3
- Cross-boundary resolved imports (EXTRACTED): 15

## Connections

- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__init__.py imports lazyaddon/config.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__main__.py imports lazyaddon/config.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: lazyaddon/models.py imports lazyaddon/config.py.
- [INFERRED] bridges community 1 <-> 2 (strength 0.7): Inferred cross-community bridge: tests/test_cli.py reaches tests/test_models.py in 3 hops.
- [INFERRED] shares_context community 2 <-> 4 (strength 0.5): Inferred shared context (language py and layer testing) with no import path between community 2 (lazyaddon: config) and community 4 (orphans).

## Risks

- [taint high] `lazyaddon/runner.py` -> `lazyaddon/config.py` via `subprocess` (1 hops)

## Open Questions

- What would break if the most connected file in lazyaddon: config changed?
- Should lazyaddon: config be split, given cohesion 0.17?

## Sources

- `lazyaddon/config.py`
- `tests/test_models.py`
- `tests/test_placeholders.py`
- `tests/test_placeholders_property.py`
