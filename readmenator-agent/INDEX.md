# Index

| File | Purpose | Subsystem | Symbols |
|------|---------|-----------|---------|
| `lazyaddon/__init__.py` | lazyaddon: declarative tool and extension manager.  Turns any GitHub/GitLab proj | lazyaddon | 0 |
| `lazyaddon/__main__.py` | Console entry point for lazyaddon.  Exposes subcommands for discovery, installat | lazyaddon | 7 |
| `lazyaddon/config.py` | Centralized configuration contract for the lazyaddon engine.  Holds every tunabl | lazyaddon | 1 |
| `lazyaddon/engine.py` | Facade contract orchestrating the lazyaddon lifecycle.  ``LazyAddonEngine`` is t | lazyaddon | 19 |
| `lazyaddon/installer.py` | Installation contract: clone and build an addon from its upstream repo.  ``Addon | lazyaddon | 6 |
| `lazyaddon/models.py` | Domain models for the lazyaddon schema.  Defines the typed representation of an  | lazyaddon | 14 |
| `lazyaddon/placeholders.py` | Placeholder substitution contract.  Resolves ``{name}`` and ``{{ name }}`` token | lazyaddon | 4 |
| `lazyaddon/runner.py` | Process execution and addon dispatch contract.  ``CommandRunner`` wraps :func:`s | lazyaddon | 16 |
| `lazyaddon/security.py` | Security policy contract for the lazyaddon engine.  Defines the defensive bounda | lazyaddon | 6 |
| `tests/__init__.py` | Test package for lazyaddon. | tests | 0 |
| `tests/conftest.py` | Shared fixtures for the lazyaddon test suite.  Provides a fake :class:`ProcessRu | tests | 7 |
| `tests/test_cli.py` | BDD-style CLI tests exercising the console script end to end. | tests | 11 |
| `tests/test_engine.py` | BDD/TDD tests for the engine facade: discovery, run, marketplace, project. | tests | 18 |
| `tests/test_models.py` | BDD/TDD behavioural tests for addon schema parsing and validation. | tests | 17 |
| `tests/test_placeholders.py` | BDD/TDD tests for the placeholder substitution engine. | tests | 13 |
| `tests/test_placeholders_property.py` | Property-based tests for the placeholder engine using hypothesis.  These complem | tests | 3 |
| `tests/test_runner.py` | BDD/TDD tests for the installer and runner contracts. | tests | 14 |
| `tests/test_security.py` | BDD/TDD tests for the security policy contract. | tests | 21 |
