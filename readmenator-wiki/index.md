# Second Brain

*Last synthesized: 2026-10-07 | 18 files | 5 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `config.py`, `models.py`, `engine.py`. Architecturally it is 4 layers, dominant testing (9 files) across 5 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between lazyaddon: engine, lazyaddon: __main__, lazyaddon: config: 6 extracted cross-community imports and 9 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (100% file coverage), 0 security findings, 4 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 18 |
| Symbols | 177 |
| Resolved imports | 50 |
| Languages | py |
| Communities | 5 |
| Doc coverage | 100% (18/18 files) |
| Security findings | 0 |
| Estimated read cost | ~6708 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_lazyaddon_wcfzfttp
```

## Concept Wiki

- [lazyaddon: engine (5 files, cohesion 0.34)](./community_0_lazyaddon_engine.md)
- [lazyaddon: __main__ (5 files, cohesion 0.25)](./community_1_lazyaddon_main.md)
- [lazyaddon: config (4 files, cohesion 0.17)](./community_2_lazyaddon_config.md)
- [lazyaddon: models (3 files, cohesion 0.18)](./community_3_lazyaddon_models.md)
- [orphans (1 files, cohesion 0.00)](./community_4_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `lazyaddon/config.py` | 30.1 |
| `lazyaddon/models.py` | 23.4 |
| `lazyaddon/engine.py` | 21.9 |
| `lazyaddon/runner.py` | 17.6 |
| `lazyaddon/installer.py` | 14.6 |

## Strongest Connections

- 0 -> 2: depends_on (strength 0.9, EXTRACTED)
- 0 -> 3: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: depends_on (strength 0.9, EXTRACTED)
- 1 -> 3: depends_on (strength 0.9, EXTRACTED)
- 1 -> 2: depends_on (strength 0.9, EXTRACTED)
- 3 -> 2: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: bridges (strength 0.7, INFERRED)
- 0 -> 1: bridges (strength 0.7, INFERRED)
- 0 -> 1: bridges (strength 0.7, INFERRED)
- 3 -> 1: bridges (strength 0.7, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
