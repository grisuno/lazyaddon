# lazyaddon

## Reporting a vulnerability

Please report security vulnerabilities privately. Open an issue at
<https://github.com/grisuno/lazyaddon/issues/new> with a clear description of
the issue and, when possible, a minimal reproducer. Do not publish a full
exploit before a maintainer has had a chance to respond.

## Security model

lazyaddon executes shell commands declared in YAML addon files. Treat every
addon file as code: only enable addons from trusted sources.

### Guarantees

- **Repository URLs** are restricted to `https` and, when configured, to a
  host allow-list. Non-https URLs are rejected.
- **No code evaluation** in placeholders. Substitution is pure string
  replacement — no `eval`, no shell is spawned by the substitution itself.
- **Command injection hardening**: values injected from the runtime `params`
  mapping are shell-quoted via `shlex.quote` before substitution, unless the
  value is a trusted YAML `default` declared in the same file as the command.
- **Path traversal** is blocked: `install_path` is resolved against
  `install_root` and rejected if it escapes.
- **Limits**: command strings are length-capped and null-byte rejected;
  repository URLs are length-capped.
- **Idempotent installs** clone only when the target is absent (or `force`).

### Operator responsibilities

The `execute_command` and `install_command` fields are executed under a shell.
Only author or import addons you trust. Do not add addon files from untrusted
parties without reviewing their commands.

## Supported versions

The current release. Older releases are not security-patched.

## Reporting process

1. File a private issue with reproduction details.
2. A maintainer will triage and respond within a reasonable window.
3. Fixes land on `main` and are back-ported on request.
