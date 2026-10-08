# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `lazyaddon/config.py` (score: 30.10, imported by 15 files)
- `lazyaddon/models.py` (score: 23.40, imported by 10 files)
- `lazyaddon/engine.py` (score: 21.90, imported by 4 files)
- `lazyaddon/runner.py` (score: 17.60, imported by 5 files)
- `lazyaddon/installer.py` (score: 14.60, imported by 2 files)
- `lazyaddon/placeholders.py` (score: 14.40, imported by 6 files)
- `lazyaddon/__init__.py` (score: 14.00)
- `lazyaddon/security.py` (score: 12.60, imported by 4 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `lazyaddon/config.py` -- 15 direct, 16 total dependents
- `lazyaddon/models.py` -- 10 direct, 12 total dependents
- `lazyaddon/placeholders.py` -- 6 direct, 11 total dependents
- `lazyaddon/runner.py` -- 5 direct, 8 total dependents
- `lazyaddon/security.py` -- 4 direct, 8 total dependents
- `lazyaddon/installer.py` -- 2 direct, 6 total dependents
- `lazyaddon/engine.py` -- 4 direct, 5 total dependents
- `lazyaddon/__main__.py` -- 1 direct, 1 total dependents

## Hotspots (complexity + centrality)

- `lazyaddon/engine.py` -- complexity: 0.9, centrality: 1.0, combined: 1.0
- `lazyaddon/runner.py` -- complexity: 0.8, centrality: 0.8, combined: 0.8
- `lazyaddon/models.py` -- complexity: 0.7, centrality: 0.7, combined: 0.7
- `lazyaddon/installer.py` -- complexity: 0.3, centrality: 0.7, combined: 0.6
- `lazyaddon/__main__.py` -- complexity: 0.3, centrality: 0.6, combined: 0.5
- `lazyaddon/config.py` -- complexity: 0.0, centrality: 0.8, combined: 0.5
- `lazyaddon/placeholders.py` -- complexity: 0.2, centrality: 0.6, combined: 0.4
- `lazyaddon/security.py` -- complexity: 0.3, centrality: 0.5, combined: 0.4
- `lazyaddon/__init__.py` -- complexity: 0.0, centrality: 0.7, combined: 0.4
