# lazyaddon

Declarative tool and extension manager. Turn any GitHub/GitLab project into an
installable, runnable addon from a single YAML file — then use it
programmatically, from the `lazyaddon` CLI, or through a declarative project
file. Born from the spirit of LazyOwn's `lazyaddons` and Estorides' source
marketplace: simplify extending a tool by adding new sources, origins or apps
as versioned, shareable YAML addons.

## Features

- YAML-declared addons with params, install and execute commands.
- Safe placeholder substitution (`{name}` / `{{ name }}`) with shell-quoting of
  runtime-injected values to prevent command injection.
- Security policy: allows only `https` repo URLs, optional host allow-list,
  length limits, and install paths that cannot escape the install root.
- Install is idempotent: clone + build only when not already present.
- Marketplace: `add` / `remove` register new addons as YAML files.
- Declarative project runner for non-programmers.
- Fully typed, single-file-per-contract, DRY and SOLID.

## Installation

```bash
pip install lazyaddon
```

## Quick start

### Programmatic

```python
from lazyaddon import LazyAddonEngine

engine = LazyAddonEngine()          # configurable via AddonConfig
engine.discover()                   # scan ./addons/*.yaml
result = engine.run("beacon", {"lhost": "10.0.0.1"})
print(result.stdout)
```

### CLI

```bash
lazyaddon list
lazyaddon run beacon --param lhost=10.0.0.1
lazyaddon add mytool --repo https://github.com/user/repo.git --cmd "./build.sh"
```

### Declarative project YAML (non-programmers)

`project.yaml`:

```yaml
install_root: external
addons_dir: addons
addons:
  - name: beacon
    install: true
    run: true
    params:
      lhost: 10.0.0.1
```

```bash
lazyaddon project project.yaml
```

## Addon schema

```yaml
name: beacon
description: Builds and deploys a C2 beacon.
author: Red Team
version: "1.0"
enabled: true
os: any
category: 10. Command & Control
params:
  - name: lhost
    type: string
    required: true
    description: Listener host.
tool:
  name: beacon
  repo_url: https://github.com/grisuno/beacon.git
  install_path: c2/beacon
  install_command: make windows
  execute_command: ./gen_beacon.sh --lhost {lhost}
  lazycommand: encode --in payload.bin
  remote_command: run --payload payload.bin
  upload_file: payload.bin
  download_file: C:\\results\\out.txt
  env:
    KEY: "{aes_key}"
```

Runtime parameter values are shell-quoted on substitution; YAML-declared
`default`s are trusted and left unquoted.

## Configuration

Every tunable knob lives in `AddonConfig` (no magic numbers):

| Field | Default | Purpose |
|-------|---------|---------|
| `addons_dir` | `addons` | Directory scanned for addon YAMLs |
| `install_root` | `external` | Root for cloned repos |
| `allowed_repo_hosts` | `()` | Allowed repo hostnames (empty = any https) |
| `allowed_repo_schemes` | `("https",)` | Permitted repo URL schemes |
| `clone_depth` | `1` | `git clone --depth` |
| `command_timeout_seconds` | `600` | Subprocess timeout |
| `quote_runtime_values` | `True` | Shell-quote runtime param values |

## Security

See [SECURITY.md](SECURITY.md). Key guarantees:

- `https`-only repository URLs, optional host allow-list.
- No arbitrary code evaluation in placeholders.
- Install paths confined to the install root (no traversal).
- Null-byte and length checks on commands.
- Shell-quoting of untrusted parameter values.

## Development

```bash
pip install -e ".[dev]"
pytest                          # TDD/BDD suite
pytest --cov=lazyaddon          # coverage
ruff check lazyaddon tests      # lint
mypy lazyaddon                  # types
bandit -r lazyaddon             # security scan
mutmut run --paths-to-mutate lazyaddon  # mutation testing
python -m build                 # build sdist + wheel for PyPI
```

## License

GPL-3.0-or-later. See [LICENSE](LICENSE).
