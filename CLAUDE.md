# lazyaddon — Agent Context

**Project:** Declarative tool/extension manager (pip package).
**Repo:** `/home/grisun0/src_note/py/lazyaddon`
**Language:** Python 3.10+.

---

## What this project is

lazyaddon turns any GitHub/GitLab project into an installable, runnable addon
from a single YAML file. It is the standalone, pip-packaged realisation of the
LazyOwn `lazyaddons/*.yaml` schema and the Estorides source-marketplace spirit:
simplify extending a tool by adding new sources, origins or apps as versioned,
shareable YAML addons.

Three usage modes:

1. **Programmatic** — `LazyAddonEngine` imported in any Python project.
2. **CLI** — the `lazyaddon` console script (`list/show/install/run/add/remove/project`).
3. **Declarative project YAML** — non-programmers install/run addons by editing a project file.

## Architecture

Contracts are strictly **one file per responsibility** (DRY + SOLID):

| File | Contract |
|------|----------|
| `lazyaddon/config.py` | `AddonConfig` — every tunable knob, **no magic numbers / hardcoded paths**. |
| `lazyaddon/models.py` | `AddonSpec` / `AddonParam` / `ToolSpec` — schema parse + validate. Pure, no I/O. |
| `lazyaddon/placeholders.py` | `PlaceholderEngine` — safe `{var}` / `{{ var }}` substitution. |
| `lazyaddon/security.py` | `SecurityPolicy` — repo URL / command / path-traversal guards. |
| `lazyaddon/installer.py` | `AddonInstaller` — idempotent git clone + install_command. |
| `lazyaddon/runner.py` | `CommandRunner` (subprocess), `AddonRunner` (dispatch), `AddonHook`. |
| `lazyaddon/engine.py` | `LazyAddonEngine` — facade: discover/run/add/remove/project. |
| `lazyaddon/__main__.py` | CLI console entry (`python -m lazyaddon`). |

Data flow: `engine` → `security.validate` → `build_params` → `installer.install`
→ `runner.execute` → `hooks`.

## Security model (non-negotiable)

- `repo_url` must be `https` and (when configured) on the host allow-list.
- No `eval`; placeholders are pure string replacement.
- Runtime-injected param values are `shlex.quote`d before shell execution;
  YAML `default`s are trusted and unquoted.
- `install_path` is resolved inside `install_root` (no traversal).
- Commands are length-capped and null-byte rejected.
- `execute_command`/`install_command` run under a shell by design — treat every
  addon file as code. See `SECURITY.md`.

## Methodology (the contract)

Every change follows **SDD + TDD + BDD**:

1. **SDD** — define the contract and its single-responsibility file first.
2. **TDD** — write failing tests that pin the contract.
3. **BDD** — express behaviour through feature scenarios in `tests/`.

Then always: full suite + coverage + mutation testing. Boy-scout rule: any
technical debt or security flaw you encounter is in scope to fix, without
regressing behaviour.

### Mutation testing contract

```bash
mutmut run --paths-to-mutate "lazyaddon/models.py lazyaddon/placeholders.py lazyaddon/security.py"
```

Interpretation per the DOD:

- **At least one test fails → the mutant dies (good — tests caught the break).**
- **All tests pass → the mutant survives (danger — tests missed it). Fix it.**
- **Equivalent mutants**: string-literal and error-message mutations (e.g.
  changing a default empty string or an exception message) are semantically
  identical and intentionally left as the accepted equivalent baseline.

Current status: **100% of logic/value mutants killed**; remaining survivors are
equivalent string-literal / error-message mutants only. Do not regress this.

### Quality gates (all must pass before committing)

```bash
ruff check lazyaddon tests
mypy lazyaddon
bandit -r lazyaddon          # B602/B404 are documented as intentional
pytest --cov=lazyaddon       # target >= 90% coverage
```

## Coding standards (check before editing)

1. English only — identifiers, strings, logs, docstrings. No comments except
   `# nosec <ID>` markers; no emojis in code.
2. Docstring on every public function/class (Args/Returns/Raises).
3. No magic numbers / hardcoded paths — everything in `AddonConfig`.
4. One file per contract. Small, single-responsibility modules.
5. Rely on abstractions: inject `ProcessRunner` (fake in tests) — never call
   `subprocess` directly in tests.
6. Public API re-exported from `lazyaddon/__init__.py` (`__all__`).

## Releasing to PyPI

```bash
make lint test coverage
make build            # build sdist + wheel into dist/
make release          # twine upload dist/*
```

Update `__version__` in `lazyaddon/__init__.py` and `version` in
`pyproject.toml` in lockstep, then tag the release.

## Testing layout

- `tests/conftest.py` — `FakeRunner` (in-process subprocess substitute) + shared addon fixtures.
- `tests/test_models.py` — schema parsing/validation (BDD).
- `tests/test_placeholders.py` — substitution + quoting.
- `tests/test_placeholders_property.py` — hypothesis property tests.
- `tests/test_security.py` — URL/command/path policy.
- `tests/test_runner.py` — installer + runner dispatch/hooks.
- `tests/test_engine.py` — facade lifecycle, marketplace, project runner.
- `tests/test_cli.py` — console script end to end.

## Do NOT

- Do not add magic numbers or hardcoded paths; extend `AddonConfig` instead.
- Do not call `subprocess` directly in tests; use `FakeRunner`.
- Do not skip the mutation gate or add brittle exact-error-string assertions
  (error-message mutants are equivalent by design).
