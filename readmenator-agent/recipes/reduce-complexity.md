# Recipe: Reduce File Complexity

Target hotspot: `lazyaddon/engine.py`
(complexity 0.9, centrality 1.0)

1. Read dependents: `grep -n 'lazyaddon/engine.py' readmenator-agent/ARCHITECTURE.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
