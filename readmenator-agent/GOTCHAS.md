# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `lazyaddon/config.py` (score: 30.10)
- `lazyaddon/models.py` (score: 23.40)
- `lazyaddon/engine.py` (score: 21.90)
- `lazyaddon/runner.py` (score: 17.60)
- `lazyaddon/installer.py` (score: 14.60)
- `lazyaddon/placeholders.py` (score: 14.40)
- `lazyaddon/__init__.py` (score: 14.00)
- `lazyaddon/security.py` (score: 12.60)
- `tests/test_runner.py` (score: 11.40)
- `tests/conftest.py` (score: 10.70)

## Hotspots (complexity + centrality)

- `lazyaddon/engine.py` -- complexity: 0.9, centrality: 1.0, combined: 1.0
- `lazyaddon/runner.py` -- complexity: 0.8, centrality: 0.8, combined: 0.8
- `lazyaddon/models.py` -- complexity: 0.7, centrality: 0.7, combined: 0.7
- `tests/test_engine.py` -- complexity: 0.9, centrality: 0.5, combined: 0.7
- `tests/test_security.py` -- complexity: 1.0, centrality: 0.4, combined: 0.6
- `tests/test_runner.py` -- complexity: 0.7, centrality: 0.6, combined: 0.6
- `lazyaddon/installer.py` -- complexity: 0.3, centrality: 0.7, combined: 0.6
- `lazyaddon/__main__.py` -- complexity: 0.3, centrality: 0.6, combined: 0.5
- `tests/test_models.py` -- complexity: 0.8, centrality: 0.3, combined: 0.5
- `lazyaddon/config.py` -- complexity: 0.0, centrality: 0.8, combined: 0.5
