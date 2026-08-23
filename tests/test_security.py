"""BDD/TDD tests for the security policy contract."""

from __future__ import annotations

from pathlib import Path

import pytest

from lazyaddon.config import AddonConfig
from lazyaddon.models import AddonSpec, SchemaError
from lazyaddon.security import SecurityPolicy

HOSTS = ("github.com", "gitlab.com")


def _policy(config: AddonConfig | None = None) -> SecurityPolicy:
    return SecurityPolicy(config or AddonConfig(allowed_repo_hosts=HOSTS))


def _addon(repo_url: str, install_path: str = "", install_cmd: str = "", exec_cmd: str = "echo x") -> AddonSpec:
    tool = {
        "name": "t",
        "repo_url": repo_url,
        "install_path": install_path,
        "install_command": install_cmd,
        "execute_command": exec_cmd,
    }
    return AddonSpec.loads({"name": "t", "tool": tool}, AddonConfig(allowed_repo_hosts=HOSTS))


def test_valid_repo_url_accepted() -> None:
    url = "https://github.com/grisuno/beacon.git"
    assert _policy().validate_repo_url(url) == url


def test_non_https_scheme_rejected() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_repo_url("http://github.com/a/b.git")


def test_disallowed_host_rejected() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_repo_url("https://evil.example.com/a/b.git")


def test_missing_path_rejected() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_repo_url("https://github.com")


def test_overlong_repo_url_rejected() -> None:
    long_url = "https://github.com/a/" + ("b" * 5000) + ".git"
    with pytest.raises(SchemaError):
        _policy().validate_repo_url(long_url)


def test_empty_repo_url_rejected() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_repo_url("   ")


def test_empty_host_allowed_when_allowlist_empty() -> None:
    policy = SecurityPolicy(AddonConfig(allowed_repo_hosts=()))
    assert policy.validate_repo_url("https://gitlab.example.com/a/b.git")


def test_null_byte_in_command_rejected() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_command("echo \x00")


def test_overlong_command_rejected() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_command("x" * 20000)


def test_valid_command_accepted() -> None:
    assert _policy().validate_command("make windows") is None


def test_validate_addon_rejects_bad_url() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_addon(_addon("http://github.com/a/b.git"))


def test_validate_addon_rejects_bad_install_command() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_addon(_addon("https://github.com/a/b.git", install_cmd="echo \x00"))


def test_validate_addon_rejects_bad_execute_command() -> None:
    with pytest.raises(SchemaError):
        _policy().validate_addon(_addon("https://github.com/a/b.git", exec_cmd="\x00rm"))


def test_validate_addon_accepts_wellformed() -> None:
    assert _policy().validate_addon(_addon("https://github.com/a/b.git", install_path="d/x", install_cmd="make")) is None


def test_repo_url_with_port_and_path_ok() -> None:
    assert _policy().validate_repo_url("https://github.com:443/a/b.git")


def test_install_path_stays_in_root(tmp_path: Path) -> None:
    config = AddonConfig(install_root=str(tmp_path / "external"))
    policy = SecurityPolicy(config)
    resolved = policy.resolve_install_path("c2/beacon")
    assert resolved.is_relative_to((tmp_path / "external").resolve())
    assert str(resolved).endswith("c2/beacon")


def test_install_path_traversal_rejected(tmp_path: Path) -> None:
    config = AddonConfig(install_root=str(tmp_path / "external"))
    policy = SecurityPolicy(config)
    with pytest.raises(SchemaError):
        policy.resolve_install_path("../../etc")


def test_absolute_install_path_rejected(tmp_path: Path) -> None:
    config = AddonConfig(install_root=str(tmp_path / "external"))
    policy = SecurityPolicy(config)
    with pytest.raises(SchemaError):
        policy.resolve_install_path(str(tmp_path / "outside"))


def test_empty_install_path_no_tool_dir() -> None:
    addon = _addon("https://github.com/a/b.git")
    assert addon.tool.install_path == ""
