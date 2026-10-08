# Index

| File | Purpose | Subsystem | Symbols | Used by |
|------|---------|-----------|---------|---------|
| `lazyaddon/__init__.py` | lazyaddon: declarative tool and extension manager. | lazyaddon | 0 | 0 |
| `lazyaddon/__main__.py` | Console entry point for lazyaddon. | lazyaddon | 7 | 1 |
| `lazyaddon/config.py` | Centralized configuration contract for the lazyaddon engine. | lazyaddon | 1 | 15 |
| `lazyaddon/engine.py` | Facade contract orchestrating the lazyaddon lifecycle. | lazyaddon | 19 | 4 |
| `lazyaddon/installer.py` | Installation contract: clone and build an addon from its upstream repo. | lazyaddon | 6 | 2 |
| `lazyaddon/models.py` | Domain models for the lazyaddon schema. | lazyaddon | 14 | 10 |
| `lazyaddon/placeholders.py` | Placeholder substitution contract. | lazyaddon | 4 | 6 |
| `lazyaddon/runner.py` | Process execution and addon dispatch contract. | lazyaddon | 16 | 5 |
| `lazyaddon/security.py` | Security policy contract for the lazyaddon engine. | lazyaddon | 6 | 4 |
| `tests/__init__.py` | Test package for lazyaddon. | tests | 0 | 0 |
| `tests/conftest.py` | Shared fixtures for the lazyaddon test suite. | tests | 7 | 3 |
| `tests/test_cli.py` | BDD-style CLI tests exercising the console script end to end. | tests | 11 | 0 |
| `tests/test_engine.py` | BDD/TDD tests for the engine facade: discovery, run, marketplace, project. | tests | 18 | 0 |
| `tests/test_models.py` | BDD/TDD behavioural tests for addon schema parsing and validation. | tests | 17 | 0 |
| `tests/test_placeholders.py` | BDD/TDD tests for the placeholder substitution engine. | tests | 13 | 0 |
| `tests/test_placeholders_property.py` | Property-based tests for the placeholder engine using hypothesis. | tests | 3 | 0 |
| `tests/test_runner.py` | BDD/TDD tests for the installer and runner contracts. | tests | 14 | 0 |
| `tests/test_security.py` | BDD/TDD tests for the security policy contract. | tests | 21 | 0 |
