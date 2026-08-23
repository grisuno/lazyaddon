"""BDD/TDD tests for the installer and runner contracts."""

from __future__ import annotations

from pathlib import Path

import pytest

from lazyaddon.engine import LazyAddonEngine
from lazyaddon.models import AddonSpec
from lazyaddon.runner import AddonRunner

from .conftest import BEACON_ADDON, FakeRunner


def _engine(tmp_path: Path, runner: FakeRunner) -> LazyAddonEngine:
    config = AddonConfigFixture(tmp_path)
    return LazyAddonEngine(config=config, runner=runner)


def AddonConfigFixture(tmp_path: Path):
    from lazyaddon.config import AddonConfig

    return AddonConfig(addons_dir=str(tmp_path / "addons"), install_root=str(tmp_path / "external"))


def _addon() -> AddonSpec:
    return AddonSpec.loads(BEACON_ADDON, AddonConfigFixture(Path("/tmp/x")))


def test_installer_clones_and_builds(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    spec = AddonSpec.loads(BEACON_ADDON, engine.config)
    engine.installer.install(spec, {"lhost": "1.1.1.1"})
    commands = runner.commands
    assert commands[0].startswith("git clone --depth 1 -- ")
    assert "https://github.com/grisuno/beacon.git" in commands[0]
    assert commands[1] == "make windows"
    assert runner.last()["cwd"].endswith("c2/beacon")


def test_installer_skips_when_already_installed(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    spec = AddonSpec.loads(BEACON_ADDON, engine.config)
    install_dir = engine.installer.install_path(spec)
    assert install_dir is not None
    install_dir.mkdir(parents=True)
    engine.installer.install(spec, {"lhost": "1.1.1.1"})
    assert runner.commands == []


def test_installer_force_reinstalls(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    spec = AddonSpec.loads(BEACON_ADDON, engine.config)
    install_dir = engine.installer.install_path(spec)
    assert install_dir is not None
    install_dir.mkdir(parents=True)
    engine.installer.install(spec, {"lhost": "1.1.1.1"}, force=True)
    assert runner.commands and "git clone" in runner.commands[0]


def test_installer_requires_repo_url(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    spec = AddonSpec.loads(
        {"name": "t", "tool": {"install_path": "d", "execute_command": "x"}},
        engine.config,
    )
    with pytest.raises(ValueError):
        engine.installer.install(spec, {})


def test_installer_no_install_path_is_noop(tmp_path: Path, runner: FakeRunner) -> None:
    engine = _engine(tmp_path, runner)
    spec = AddonSpec.loads(
        {"name": "t", "tool": {"execute_command": "x"}},
        engine.config,
    )
    engine.installer.install(spec, {})
    assert runner.commands == []


def test_runner_executes_with_quoted_runtime_params(runner: FakeRunner) -> None:
    engine = _engine(Path("/tmp/x"), runner)
    addon = _addon()
    merged, untrusted = engine.build_params(addon, {"lhost": "1.1.1.1"})
    assert "lhost" in untrusted
    assert "lport" not in untrusted
    result = engine.addons_runner.execute(addon, merged, untrusted_keys=untrusted)
    assert result.ok
    assert "--lhost 1.1.1.1" in runner.last()["command"]
    assert "--lport 4444" in runner.last()["command"]


def test_runner_quotes_injected_injection_value(runner: FakeRunner) -> None:
    engine = _engine(Path("/tmp/x"), runner)
    addon = _addon()
    merged, untrusted = engine.build_params(addon, {"lhost": "1.1.1.1; rm -rf /"})
    engine.addons_runner.execute(addon, merged, untrusted_keys=untrusted)
    command = runner.last()["command"]
    assert "--lhost '" in command
    assert "' --lport" in command


def test_runner_raises_without_execute_command(runner: FakeRunner) -> None:
    engine = _engine(Path("/tmp/x"), runner)
    addon = AddonSpec.loads({"name": "t", "tool": {}}, engine.config)
    with pytest.raises(ValueError):
        engine.addons_runner.execute(addon, {})


def test_runner_dispatches_hooks(runner: FakeRunner) -> None:
    fired: list[tuple[str, str]] = []
    engine = _engine(Path("/tmp/x"), runner)
    engine.hooks = {"lazy": lambda kind, payload, env: fired.append((kind, payload))}
    engine.addons_runner = AddonRunner(
        engine.config, runner, engine.placeholders, engine.hooks
    )
    addon = _addon()
    merged, untrusted = engine.build_params(addon, {"lhost": "1.1.1.1"})
    engine.addons_runner.dispatch_hooks(addon, merged, untrusted_keys=untrusted)
    assert fired == [("lazy", "encode --in out.bin")]


def test_runner_resolves_env_placeholders(runner: FakeRunner) -> None:
    engine = _engine(Path("/tmp/x"), runner)
    addon = _addon()
    merged, untrusted = engine.build_params(addon, {"lhost": "1.1.1.1", "aes_key": "k123"})
    engine.addons_runner.execute(addon, merged, untrusted_keys=untrusted)
    env = runner.last()["env"]
    assert env is not None
    assert env["AES"] == "k123"


def test_runner_env_injection_value_is_quoted(runner: FakeRunner) -> None:
    engine = _engine(Path("/tmp/x"), runner)
    addon = _addon()
    merged, untrusted = engine.build_params(addon, {"lhost": "1.1.1.1", "aes_key": "a; rm -rf /"})
    engine.addons_runner.execute(addon, merged, untrusted_keys=untrusted)
    env = runner.last()["env"]
    assert env is not None
    assert env["AES"].startswith("'") and env["AES"].endswith("'")
