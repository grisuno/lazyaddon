"""BDD/TDD tests for the placeholder substitution engine."""

from __future__ import annotations

import pytest

from lazyaddon.config import AddonConfig
from lazyaddon.placeholders import PlaceholderEngine


def _engine() -> PlaceholderEngine:
    return PlaceholderEngine(AddonConfig())


def test_single_brace_substitution() -> None:
    assert _engine().resolve("run {lhost} --port {lport}", {"lhost": "1.1.1.1", "lport": "80"}) == (
        "run 1.1.1.1 --port 80"
    )


def test_double_brace_substitution() -> None:
    assert _engine().resolve("run {{ lhost }}", {"lhost": "1.1.1.1"}) == "run 1.1.1.1"


def test_whitespace_inside_braces_is_ignored() -> None:
    assert _engine().resolve("a { var } b", {"var": "X"}) == "a X b"


def test_unknown_placeholder_left_untouched() -> None:
    assert _engine().resolve("a {missing} b", {"other": "X"}) == "a {missing} b"


def test_no_placeholders_is_passthrough() -> None:
    assert _engine().resolve("plain command", {}) == "plain command"


def test_repeated_placeholder_all_replaced() -> None:
    out = _engine().resolve("{x} and {x}", {"x": "V"})
    assert out == "V and V"


def test_runtime_values_are_shell_quoted() -> None:
    out = _engine().resolve("echo {value}", {"value": "a; rm -rf /"})
    assert out == "echo 'a; rm -rf /'"


def test_trusted_values_are_not_quoted() -> None:
    out = _engine().resolve("echo {value}", {"value": "safe"}, untrusted_keys=frozenset())
    assert out == "echo safe"


def test_quoted_value_survives_dangerous_metachars() -> None:
    out = _engine().resolve("cmd {v}", {"v": "$(rm -rf /)"})
    assert out == "cmd '$(rm -rf /)'"


def test_null_char_value_is_quoted_not_bare() -> None:
    out = _engine().resolve("cmd {v}", {"v": "\x00"})
    assert out.startswith("cmd '")
    assert out.endswith("'")


def test_quote_disabled_by_config() -> None:
    engine = PlaceholderEngine(AddonConfig(quote_runtime_values=False))
    assert engine.resolve("echo {v}", {"v": "a; b"}) == "echo a; b"


def test_non_string_command_raises() -> None:
    with pytest.raises(TypeError):
        _engine().resolve(123, {})  # type: ignore[arg-type]
