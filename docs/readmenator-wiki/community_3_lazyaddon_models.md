# lazyaddon: models

*Community 3 | 3 files | cohesion 0.18*

## Definition

This community groups 3 file(s) rooted at `lazyaddon` with dominant language py (cohesion 0.18). Central symbols: `AddonError`, `AddonParam`, `AddonSpec`, `SchemaError`, `SecurityPolicy`, `ToolSpec`, `__init__`, `_addon`. Core file: `tests/test_security.py` (21 symbols). Documented purpose: Domain models for the lazyaddon schema.  Defines the typed representation of an addon YAML document. The contract is a pure data layer: parsing, coercion and va.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `lazyaddon/models.py` | py | business_logic | 14 | yes |
| `lazyaddon/security.py` | py | utility | 6 | yes |
| `tests/test_security.py` | py | testing | 21 | yes |

## Key Symbols

- `AddonError` (class, `lazyaddon/models.py:53`) `class AddonError(Exception)` - Base error raised for any lazyaddon schema or runtime failure.
- `SchemaError` (class, `lazyaddon/models.py:57`) `class SchemaError(AddonError)` - Raised when an addon document violates the expected schema.
- `AddonParam` (class, `lazyaddon/models.py:62`) `class AddonParam` - A single declared input parameter for an addon.
- `ToolSpec` (class, `lazyaddon/models.py:81`) `class ToolSpec` - Executable description of the tool an addon wraps.
- `AddonSpec` (class, `lazyaddon/models.py:113`) `class AddonSpec` - A fully validated addon definition.
- `loads` (method, `lazyaddon/models.py:141`) `def loads(cls, raw, config)` - Build a validated ``AddonSpec`` from a parsed YAML mapping.
- `param_by_name` (method, `lazyaddon/models.py:176`) `def param_by_name(self, name)` - Return the declared parameter matching ``name`` or None.
- `required_params` (method, `lazyaddon/models.py:183`) `def required_params(self)` - Return the names of all required parameters in declaration order.
- `_require_name` (method, `lazyaddon/models.py:188`) `def _require_name(raw)` - Extract and validate the required addon name field.
- `_as_params` (method, `lazyaddon/models.py:196`) `def _as_params(value)` - Coerce the ``params`` field into a tuple of mappings.
- `_build_param` (method, `lazyaddon/models.py:209`) `def _build_param(raw, config)` - Normalise a single parameter mapping into an ``AddonParam``.
- `_build_tool` (method, `lazyaddon/models.py:225`) `def _build_tool(name, raw, config)` - Build and length-check the executable tool definition.
- `_as_str_dict` (method, `lazyaddon/models.py:242`) `def _as_str_dict(value)` - Coerce an env mapping into ``{str: str}``.
- `_as_str_tuple` (method, `lazyaddon/models.py:253`) `def _as_str_tuple(value)` - Coerce a trigger list into a tuple of strings.
- `SecurityPolicy` (class, `lazyaddon/security.py:27`) `class SecurityPolicy` - Validates external inputs before they reach the engine.
- `__init__` (method, `lazyaddon/security.py:35`) `def __init__(self, config)`
- `validate_addon` (method, `lazyaddon/security.py:38`) `def validate_addon(self, addon)` - Validate the network, filesystem and command fields of an addon.
- `validate_repo_url` (method, `lazyaddon/security.py:60`) `def validate_repo_url(self, url)` - Validate a repository URL and return it unchanged.
- `validate_command` (method, `lazyaddon/security.py:86`) `def validate_command(self, command, label)` - Validate a shell command string for length and null bytes.
- `resolve_install_path` (method, `lazyaddon/security.py:103`) `def resolve_install_path(self, install_path)` - Resolve an addon install path inside the configured install root.
- `_policy` (function, `tests/test_security.py:16`) `def _policy(config)`
- `_addon` (function, `tests/test_security.py:20`) `def _addon(repo_url, install_path, install_cmd, exec_cmd)`
- `test_valid_repo_url_accepted` (function, `tests/test_security.py:31`) `def test_valid_repo_url_accepted()`
- `test_non_https_scheme_rejected` (function, `tests/test_security.py:36`) `def test_non_https_scheme_rejected()`
- `test_disallowed_host_rejected` (function, `tests/test_security.py:41`) `def test_disallowed_host_rejected()`
- `test_missing_path_rejected` (function, `tests/test_security.py:46`) `def test_missing_path_rejected()`
- `test_overlong_repo_url_rejected` (function, `tests/test_security.py:51`) `def test_overlong_repo_url_rejected()`
- `test_empty_repo_url_rejected` (function, `tests/test_security.py:57`) `def test_empty_repo_url_rejected()`
- `test_empty_host_allowed_when_allowlist_empty` (function, `tests/test_security.py:62`) `def test_empty_host_allowed_when_allowlist_empty()`
- `test_null_byte_in_command_rejected` (function, `tests/test_security.py:67`) `def test_null_byte_in_command_rejected()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 3
- Cross-boundary resolved imports (EXTRACTED): 14

## Connections

- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__init__.py imports lazyaddon/models.py.
- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: lazyaddon/__main__.py imports lazyaddon/models.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: lazyaddon/models.py imports lazyaddon/config.py.
- [INFERRED] bridges community 3 <-> 1 (strength 0.7): Inferred cross-community bridge: lazyaddon/security.py reaches tests/test_cli.py in 3 hops.
- [INFERRED] shares_context community 3 <-> 4 (strength 0.5): Inferred shared context (language py) with no import path between community 3 (lazyaddon: models) and community 4 (orphans).

## Risks

- [taint high] `lazyaddon/runner.py` -> `lazyaddon/models.py` via `subprocess` (1 hops)

## Open Questions

- What would break if the most connected file in lazyaddon: models changed?
- Should lazyaddon: models be split, given cohesion 0.18?

## Sources

- `lazyaddon/models.py`
- `lazyaddon/security.py`
- `tests/test_security.py`
