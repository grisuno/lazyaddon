"""BDD-style CLI tests exercising the console script end to end."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from lazyaddon.__main__ import main

from .conftest import BEACON_ADDON


def _run(argv: list[str]) -> int:
    """Invoke the CLI, capturing its exit code via SystemExit."""
    try:
        main(argv)
        return 0
    except SystemExit as exc:
        return int(exc.code or 0)


def test_list_empty_directory(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    assert _run(["--dir", str(tmp_path), "list"]) == 0


def test_add_then_list_and_show(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    addons_dir = tmp_path / "addons"
    rc = _run(
        [
            "--dir", str(addons_dir),
            "add", "scanner",
            "--repo", "https://github.com/a/scanner.git",
            "--cmd", "./scan.sh --target {rhost}",
        ]
    )
    assert rc == 0
    assert (addons_dir / "scanner.yaml").exists()

    rc = _run(["--dir", str(addons_dir), "list"])
    assert rc == 0

    rc = _run(["--dir", str(addons_dir), "show", "scanner", "--json"])
    assert rc == 0


def test_show_unknown_addon_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    assert _run(["--dir", str(tmp_path), "show", "nope"]) == 1


def test_add_rejects_insecure_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    rc = _run(
        [
            "--dir", str(tmp_path / "addons"),
            "add", "bad",
            "--repo", "http://x/y.git",
            "--cmd", "echo hi",
        ]
    )
    assert rc == 1


def test_remove_addon(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    addons_dir = tmp_path / "addons"
    _run(["--dir", str(addons_dir), "add", "scanner", "--repo", "https://github.com/a/scanner.git", "--cmd", "echo hi"])
    assert _run(["--dir", str(addons_dir), "remove", "scanner"]) == 0
    assert not (addons_dir / "scanner.yaml").exists()


def test_run_addon_missing_param_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    addons_dir = tmp_path / "addons"
    addons_dir.mkdir()
    with (addons_dir / "beacon.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(BEACON_ADDON, fh, sort_keys=False)
    rc = _run(["--dir", str(addons_dir), "run", "beacon"])
    assert rc == 1


def test_version_flag(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    rc = _run(["--version"])
    assert rc == 0


def test_list_json_emits_machine_readable(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    addons_dir = tmp_path / "addons"
    addons_dir.mkdir()
    with (addons_dir / "demo.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump({"name": "demo", "tool": {"execute_command": "echo hi"}}, fh, sort_keys=False)
    rc = _run(["--dir", str(addons_dir), "--json", "list"])
    assert rc == 0


def test_run_success_executes_addon(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    addons_dir = tmp_path / "addons"
    addons_dir.mkdir()
    with (addons_dir / "demo.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(
            {
                "name": "demo",
                "params": [{"name": "who", "required": True}],
                "tool": {"execute_command": "echo hello {who}"},
            },
            fh,
            sort_keys=False,
        )
    rc = _run(["--dir", str(addons_dir), "run", "demo", "-p", "who=world"])
    assert rc == 0


def test_project_success(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    addons_dir = tmp_path / "addons"
    addons_dir.mkdir()
    with (addons_dir / "demo.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump({"name": "demo", "tool": {"execute_command": "echo hi"}}, fh, sort_keys=False)
    project = tmp_path / "p.yaml"
    project.write_text(
        yaml.safe_dump(
            {"addons_dir": str(addons_dir), "addons": [{"name": "demo", "run": True}]},
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    assert _run(["project", str(project)]) == 0
