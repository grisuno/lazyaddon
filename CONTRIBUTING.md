# Contributing to lazyaddon

Thanks for contributing. This project follows a strict quality bar so the
package stays safe, typed and production-ready.

## Standards

- English only: identifiers, docstrings, logs. No comments, no emojis in code.
- Docstring on every public function/class (Args/Returns/Raises).
- No magic numbers or hardcoded paths — everything lives in `AddonConfig`.
- Single file per contract. Keep modules small and single-responsibility.
- Boy-scout rule: fix any technical debt or security issue you encounter,
  without regressing behaviour.

## Methodology

Changes follow SDD + TDD + BDD:

1. **SDD** — define the contract and its single-responsibility file first.
2. **TDD** — write failing tests that pin the contract.
3. **BDD** — express behaviour through feature scenarios in tests.

Every change must pass the full suite and, where behaviour is critical, a
mutation-testing pass (mutants must die).

## Commands

```bash
pip install -e ".[dev]"
pytest                          # run the suite
pytest --cov=lazyaddon          # coverage
ruff check lazyaddon tests      # lint
ruff format --check lazyaddon tests
mypy lazyaddon                  # type check
bandit -r lazyaddon             # security scan
mutmut run --paths-to-mutate lazyaddon  # mutation testing
python -m build                 # build sdist + wheel
```

## Pull request checklist

- [ ] Code follows the standards above.
- [ ] New behaviour covered by tests (with mutation survivors removed).
- [ ] `ruff`, `mypy`, `bandit` are clean.
- [ ] README/CLAUDE updated if behaviour or contracts changed.
- [ ] No security regressions.

## Releasing to PyPI

```bash
python -m build
python -m twine upload dist/*
```

Tag the release and update `__version__` and `pyproject.toml` in lockstep.
