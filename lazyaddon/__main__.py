"""Console entry point for lazyaddon.

Exposes subcommands for discovery, installation, execution, marketplace
registration and declarative project runs. Invoked via the ``lazyaddon``
console script or ``python -m lazyaddon``.
"""

from __future__ import annotations

import argparse
import logging
import sys
from collections.abc import Sequence

from . import __version__
from .engine import LazyAddonEngine
from .models import AddonError, AddonSpec, SchemaError


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="lazyaddon",
        description="Declarative tool and extension manager.",
        epilog=(
            "Subcommands:\n"
            "  list [dir]            List registered addons\n"
            "  show <name>           Show one addon definition\n"
            "  install <name>        Clone + build an addon\n"
            "  run <name> [args...]  Install (if needed) and run an addon\n"
            "  add <name> --repo <url> --cmd <cmd>   Register a new addon\n"
            "  remove <name>         Delete an addon file\n"
            "  project <file.yaml>   Run a declarative project file\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "-d",
        "--dir",
        default=None,
        help="Overrides the addons directory (default: from config).",
    )
    parser.add_argument("--install-root", default=None, help="Overrides the install root directory.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="List registered addons.")
    p_show = sub.add_parser("show", help="Show one addon definition.")
    p_show.add_argument("name")
    p_show.add_argument("--json", action="store_true")

    p_install = sub.add_parser("install", help="Clone and build an addon.")
    p_install.add_argument("name")
    p_install.add_argument("--force", action="store_true")

    p_run = sub.add_parser("run", help="Install and run an addon.")
    p_run.add_argument("name")
    p_run.add_argument("args", nargs="*", help="Extra arguments appended to the command.")
    p_run.add_argument("--no-install", action="store_true")
    p_run.add_argument("-p", "--param", action="append", default=[], help="Override param as key=value.")

    p_add = sub.add_parser("add", help="Register a new addon.")
    p_add.add_argument("name")
    p_add.add_argument("--repo", required=True, help="Upstream repository URL.")
    p_add.add_argument("--cmd", required=True, help="execute_command to run.")
    p_add.add_argument("--install-path", default="", help="Relative install destination directory.")
    p_add.add_argument("--install-cmd", default="", help="Command to run after cloning.")
    p_add.add_argument("--category", default=None, help="Category label.")
    p_add.add_argument("--description", default="Registered by lazyaddon CLI.", help="Addon description.")

    p_remove = sub.add_parser("remove", help="Delete an addon file.")
    p_remove.add_argument("name")

    p_project = sub.add_parser("project", help="Run a declarative project file.")
    p_project.add_argument("file")

    return parser


def _make_engine(args: argparse.Namespace) -> LazyAddonEngine:
    """Build an engine honouring the CLI-level directory overrides."""
    from .config import AddonConfig

    addons_dir = args.dir or AddonConfig().addons_dir
    install_root = args.install_root or AddonConfig().install_root
    return LazyAddonEngine(
        config=AddonConfig(addons_dir=addons_dir, install_root=install_root)
    )


def _parse_overrides(raw: Sequence[str]) -> dict[str, str]:
    """Parse ``key=value`` CLI overrides into a parameter mapping."""
    overrides: dict[str, str] = {}
    for token in raw:
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        overrides[key] = value
    return overrides


def main(argv: Sequence[str] | None = None) -> None:
    """Run the lazyaddon CLI."""
    logging.basicConfig(level=logging.WARNING, format="%(message)s")
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return
    try:
        _dispatch(args, parser)
    except (AddonError, SchemaError, KeyError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)


def _dispatch(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    """Route a parsed command to its handler."""
    engine = _make_engine(args)
    command = args.command
    if command == "list":
        addons = engine.discover()
        if args.json:
            print(_json([_summary(a) for a in addons]))
            return
        for addon in addons:
            state = "enabled" if addon.enabled else "disabled"
            print(f"{addon.name}\t[{state}]\t{addon.category}\t{addon.tool.repo_url}")
    elif command == "show":
        engine.discover()
        show_addon = engine.get(args.name)
        if show_addon is None:
            raise KeyError(f"no addon registered under name: {args.name}")
        if args.json:
            print(_json(_summary(show_addon)))
            return
        print(f"name: {show_addon.name}")
        print(f"description: {show_addon.description}")
        print(f"os: {show_addon.os}")
        print(f"category: {show_addon.category}")
        print(f"enabled: {show_addon.enabled}")
        print(f"repo_url: {show_addon.tool.repo_url}")
        print(f"install_path: {show_addon.tool.install_path}")
        print(f"execute_command: {show_addon.tool.execute_command}")
        for param in show_addon.params:
            required = "required" if param.required else "optional"
            print(f"param {param.name} ({required}): {param.description}")
    elif command == "install":
        engine.discover()
        install_addon = engine.get(args.name)
        if install_addon is None:
            raise KeyError(f"no addon registered under name: {args.name}")
        engine.install(install_addon, force=args.force)
        print(f"installed: {install_addon.name}")
    elif command == "run":
        engine.discover()
        overrides = _parse_overrides(args.param)
        result = engine.run(args.name, overrides, tuple(args.args), install=not args.no_install)
        if result.stdout:
            print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
        if result.stderr:
            print(result.stderr, file=sys.stderr, end="" if result.stderr.endswith("\n") else "\n")
        if args.json:
            print(_json(
                {
                    "command": result.command,
                    "returncode": result.returncode,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                }
            ))
        sys.exit(0 if result.ok else 1)
    elif command == "add":
        path = engine.add_from_tool(
            args.name,
            args.repo,
            args.cmd,
            install_path=args.install_path,
            install_command=args.install_cmd,
            description=args.description,
            category=args.category,
        )
        print(f"registered addon: {path}")
    elif command == "remove":
        removed_path = engine.remove(args.name)
        if removed_path is None:
            raise KeyError(f"no addon file found for name: {args.name}")
        print(f"removed: {removed_path}")
    elif command == "project":
        results = engine.run_project(args.file)
        print(f"ran {len(results)} addon(s) from project file")
    else:
        parser.print_help()


def _summary(addon: AddonSpec) -> dict[str, object]:
    """Build a compact serialisable summary of an addon."""
    return {
        "name": addon.name,
        "description": addon.description,
        "os": addon.os,
        "category": addon.category,
        "enabled": addon.enabled,
        "version": addon.version,
        "author": addon.author,
        "params": [
            {
                "name": p.name,
                "type": p.type,
                "required": p.required,
                "default": p.default,
            }
            for p in addon.params
        ],
        "repo_url": addon.tool.repo_url,
        "install_path": addon.tool.install_path,
        "install_command": addon.tool.install_command,
        "execute_command": addon.tool.execute_command,
    }


def _json(payload: object) -> str:
    """Serialize ``payload`` to a compact JSON string."""
    import json

    return json.dumps(payload, ensure_ascii=False)


if __name__ == "__main__":
    main()
