"""BDD/TDD behavioural tests for addon schema parsing and validation."""

from __future__ import annotations

import pytest

from lazyaddon.config import ALLOWED_OS_VALUES, AddonConfig
from lazyaddon.models import AddonSpec, SchemaError


def _load(raw: dict, config: AddonConfig | None = None) -> AddonSpec:
    return AddonSpec.loads(raw, config or AddonConfig())


def test_minimal_addon_defaults() -> None:
    spec = _load({"name": "demo", "tool": {"execute_command": "echo hi"}})
    assert spec.name == "demo"
    assert spec.enabled is True
    assert spec.os == "any"
    assert spec.category == "00. Miscellaneous"
    assert spec.params == ()


def test_full_addon_parses_params_and_tool() -> None:
    raw = {
        "name": "beacon",
        "description": "Builds a beacon.",
        "author": "RT",
        "version": "1.0",
        "enabled": True,
        "os": "linux",
        "category": "10. C2",
        "params": [
            {"name": "lhost", "type": "string", "required": True},
            {"name": "lport", "default": "4444"},
        ],
        "trigger": ["http"],
        "tool": {
            "name": "beacon",
            "repo_url": "https://github.com/x/y.git",
            "install_path": "c2/b",
            "install_command": "make",
            "execute_command": "./run {lhost}",
            "lazycommand": "encode",
            "remote_command": "run",
            "upload_file": "a.bin",
            "download_file": "out.txt",
            "env": {"K": "{aes_key}"},
        },
    }
    spec = _load(raw)
    assert spec.os == "linux"
    assert spec.trigger == ("http",)
    assert spec.required_params() == ("lhost",)
    assert spec.param_by_name("lport").default == "4444"
    assert spec.tool.repo_url == "https://github.com/x/y.git"
    assert spec.tool.install_path == "c2/b"
    assert spec.tool.install_command == "make"
    assert spec.tool.execute_command == "./run {lhost}"
    assert spec.tool.lazycommand == "encode"
    assert spec.tool.remote_command == "run"
    assert spec.tool.upload_file == "a.bin"
    assert spec.tool.download_file == "out.txt"
    assert spec.tool.env == {"K": "{aes_key}"}
    assert spec.tool.name == "beacon"
    assert spec.param_by_name("lhost").type == "string"
    assert spec.param_by_name("lport").type == "string"
    assert spec.param_by_name("lport").required is False


def test_unknown_os_falls_back_to_default() -> None:
    spec = _load({"name": "a", "os": "not-a-real-os", "tool": {"execute_command": "x"}})
    assert spec.os == "any"


@pytest.mark.parametrize("os_value", list(ALLOWED_OS_VALUES))
def test_all_allowed_os_values_are_accepted(os_value: str) -> None:
    spec = _load({"name": "a", "os": os_value, "tool": {"execute_command": "x"}})
    assert spec.os == os_value


def test_missing_name_raises() -> None:
    with pytest.raises(SchemaError):
        _load({"tool": {"execute_command": "x"}})


def test_empty_name_raises() -> None:
    with pytest.raises(SchemaError):
        _load({"name": "  ", "tool": {"execute_command": "x"}})


def test_missing_tool_mapping_raises() -> None:
    with pytest.raises(SchemaError):
        _load({"name": "a"})


def test_param_without_name_raises() -> None:
    with pytest.raises(SchemaError):
        _load({"name": "a", "params": [{"default": "1"}], "tool": {"execute_command": "x"}})


def test_non_required_param_defaults_to_optional() -> None:
    spec = _load({"name": "a", "params": [{"name": "p"}], "tool": {"execute_command": "x"}})
    assert spec.params[0].required is False


def test_disabled_flag_is_preserved() -> None:
    spec = _load({"name": "a", "enabled": False, "tool": {"execute_command": "x"}})
    assert spec.enabled is False


def test_trigger_string_is_split() -> None:
    spec = _load({"name": "a", "trigger": "smb,http", "tool": {"execute_command": "x"}})
    assert spec.trigger == ("smb", "http")


def test_default_param_trusted_lookup() -> None:
    spec = _load(
        {
            "name": "a",
            "params": [{"name": "p", "default": "x"}],
            "tool": {"execute_command": "c"},
        }
    )
    assert spec.param_by_name("p") is not None
    assert spec.param_by_name("missing") is None


def test_param_type_and_description_defaults() -> None:
    spec = _load({"name": "a", "params": [{"name": "p"}], "tool": {"execute_command": "x"}})
    assert spec.params[0].type == "string"
    assert spec.params[0].description == ""
    assert spec.params[0].required is False


def test_param_custom_type_and_description_are_kept() -> None:
    spec = _load(
        {
            "name": "a",
            "params": [{"name": "p", "type": "int", "description": "a number", "required": True}],
            "tool": {"execute_command": "x"},
        }
    )
    assert spec.params[0].type == "int"
    assert spec.params[0].description == "a number"
    assert spec.params[0].required is True


def test_tool_name_falls_back_to_addon_name() -> None:
    spec = _load({"name": "addon-name", "tool": {"execute_command": "x"}})
    assert spec.tool.name == "addon-name"


def test_tool_name_custom_wins() -> None:
    spec = _load({"name": "addon-name", "tool": {"name": "custom", "execute_command": "x"}})
    assert spec.tool.name == "custom"
