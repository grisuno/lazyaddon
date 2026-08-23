"""BDD/TDD tests for the engine facade: discovery, run, marketplace, project."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from lazyaddon.config import AddonConfig
from lazyaddon.engine import LazyAddonEngine
from lazyaddon.models import AddonError, SchemaError

from .conftest import BEACON_ADDON, FakeRunner


def _write_addon(tmp_path: Path, data: dict, name: str = "beacon.yaml") -> Path:
    addons_dir = tmp_path / "addons"
    addons_dir.mkdir(parents=True, exist_ok=True)
    path = addons_dir / name
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, sort_keys=False)
    return path


def _engine(tmp_path: Path, runner: FakeRunner) -> LazyAddonEngine:
    config = AddonConfig(addons_dir=str(tmp_path / "addons"), install_root=str(tmp_path / "external"))
    return LazyAddonEngine(config=config, runner=runner)


def test_discover_finds_enabled_addons(tmp_path: Path, runner: FakeRunner) -> None:
    _write_addon(tmp_path, BEACON_ADDON)
    engine = _engine(tmp_path, runner)
    addons = engine.discover()
    assert [a.name for a in addons] == ["beacon"]
    assert engine.get("beacon") is not None
    assert engine.names() == ["beacon"]


def test_discover_skips_disabled_addons(tmp_path: Path, runner: FakeRunner) -> None:
    data = dict(BEACON_ADDON)
    data["enabled"] = False
    _write_addon(tmp_path, data)
    engine = _engine(tmp_path, runner)
    assert engine.discover() == []


def test_discover_skips_invalid_and_insecure(tmp_path: Path, runner: FakeRunner) -> None:
    _write_addon(tmp_path, {"name": "bad"}, "bad.yaml")
    _write_addon(tmp_path, {**BEACON_ADDON, "tool": {"execute_command": "x", "repo_url": "http://x/y.git"}}, "insecure.yaml")
    engine = _engine(tmp_path, runner)
    assert engine.discover() == []


def test_run_full_lifecycle(tmp_path: Path, runner: FakeRunner) -> None:
    _write_addon(tmp_path, BEACON_ADDON)
    engine = _engine(tmp_path, runner)
    engine.discover()
    result = engine.run("beacon", {"lhost": "1.1.1.1"})
    assert result.ok
    assert runner.commands[0].startswith("git clone")
    assert "--lhost 1.1.1.1" in runner.commands[-1]


def test_run_unknown_name_raises(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    engine.discover()
    with pytest.raises(KeyError):
        engine.run("nope", {})


def test_run_disabled_raises(tmp_path: Path, runner: FakeRunner) -> None:
    data = dict(BEACON_ADDON)
    data["enabled"] = False
    engine = _engine(tmp_path, runner)
    engine.add(data)
    with pytest.raises(AddonError):
        engine.run("beacon", {})


def test_run_missing_required_param_raises(tmp_path: Path, runner: FakeRunner) -> None:
    _write_addon(tmp_path, BEACON_ADDON)
    engine = _engine(tmp_path, runner)
    engine.discover()
    with pytest.raises(AddonError):
        engine.run("beacon", {})


def test_run_no_install_leaves_install_alone(tmp_path: Path, runner: FakeRunner) -> None:
    _write_addon(tmp_path, BEACON_ADDON)
    engine = _engine(tmp_path, runner)
    engine.discover()
    engine.run("beacon", {"lhost": "1.1.1.1"}, install=False)
    assert not any("git clone" in c for c in runner.commands)


def test_run_with_extra_args(tmp_path: Path, runner: FakeRunner) -> None:
    _write_addon(tmp_path, BEACON_ADDON)
    engine = _engine(tmp_path, runner)
    engine.discover()
    engine.run("beacon", {"lhost": "1.1.1.1"}, extra_args=("--extra", "1"), install=False)
    assert runner.last()["command"].endswith("--extra 1")


def test_add_registers_new_addon(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    path = engine.add_from_tool(
        "scanner",
        "https://github.com/a/scanner.git",
        "./scan.sh --target {rhost}",
        install_path="tools/scanner",
        category="10. Recon",
    )
    assert path.exists()
    assert engine.get("scanner") is not None
    engine.discover()
    assert engine.get("scanner") is not None


def test_add_rejects_insecure_repo(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    with pytest.raises(SchemaError):
        engine.add_from_tool("bad", "http://x/y.git", "echo hi")


def test_remove_deletes_file(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    path = engine.add_from_tool("scanner", "https://github.com/a/scanner.git", "echo hi")
    engine.discover()
    removed = engine.remove("scanner")
    assert removed is not None
    assert not path.exists()
    assert engine.get("scanner") is None


def test_remove_unknown_returns_none(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    assert engine.remove("missing") is None


def test_run_project_file(tmp_path: Path, runner: FakeRunner) -> None:
    _write_addon(tmp_path, BEACON_ADDON)
    engine = _engine(tmp_path, runner)
    project = tmp_path / "project.yaml"
    project.write_text(
        yaml.safe_dump(
            {
                "addons_dir": str(tmp_path / "addons"),
                "install_root": str(tmp_path / "external"),
                "addons": [
                    {
                        "name": "beacon",
                        "install": True,
                        "run": True,
                        "params": {"lhost": "10.0.0.1"},
                    }
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    results = engine.run_project(project)
    assert len(results) == 1
    assert results[0].ok
    assert "git clone" in runner.commands[0]
    assert "--lhost 10.0.0.1" in runner.commands[-1]


def test_run_project_unknown_addon_raises(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    project = tmp_path / "project.yaml"
    project.write_text(
        yaml.safe_dump({"addons": [{"name": "missing", "run": True}]}, sort_keys=False),
        encoding="utf-8",
    )
    with pytest.raises(AddonError):
        engine.run_project(project)


def test_run_project_malformed_raises(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    project = tmp_path / "project.yaml"
    project.write_text("not: [a mapping\n", encoding="utf-8")
    with pytest.raises(AddonError):
        engine.run_project(project)
