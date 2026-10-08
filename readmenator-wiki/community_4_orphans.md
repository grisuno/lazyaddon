# orphans

*Community 4 | 1 files | cohesion 0.00*

## Definition

This community groups 1 file(s) rooted at `tests` with dominant language py (cohesion 0.00). Central symbols: no extracted symbols. Documented purpose: Test package for lazyaddon..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/__init__.py` | py | testing | 0 | yes |

## Key Symbols

- No symbols extracted in this community.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 4 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (lazyaddon: engine) and community 4 (orphans).
- [INFERRED] shares_context community 1 <-> 4 (strength 0.5): Inferred shared context (language py and layer testing) with no import path between community 1 (lazyaddon: __main__) and community 4 (orphans).
- [INFERRED] shares_context community 2 <-> 4 (strength 0.5): Inferred shared context (language py and layer testing) with no import path between community 2 (lazyaddon: config) and community 4 (orphans).
- [INFERRED] shares_context community 3 <-> 4 (strength 0.5): Inferred shared context (language py) with no import path between community 3 (lazyaddon: models) and community 4 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `tests/__init__.py`
