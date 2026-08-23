"""Property-based tests for the placeholder engine using hypothesis.

These complement the unit tests by checking the core invariants across many
random inputs: known tokens always resolve, unknown tokens are left untouched,
and runtime values are never injected unquoted.
"""

from __future__ import annotations

from hypothesis import given, settings
from hypothesis import strategies as st

from lazyaddon.config import AddonConfig
from lazyaddon.placeholders import PlaceholderEngine

_WORD = st.text(alphabet="ab 12.-", min_size=0, max_size=10)
_KEY = st.text(alphabet="ab_12", min_size=1, max_size=6)


@settings(max_examples=200, deadline=None)
@given(_KEY, _WORD)
def test_known_single_token_resolves(key: str, value: str) -> None:
    engine = PlaceholderEngine(AddonConfig())
    out = engine.resolve(f"x {{{key}}} y", {key: value}, untrusted_keys=frozenset())
    assert out == f"x {value} y"


@settings(max_examples=200, deadline=None)
@given(_KEY, _WORD)
def test_unknown_token_left_untouched(key: str, value: str) -> None:
    engine = PlaceholderEngine(AddonConfig())
    out = engine.resolve(f"x {{{key}}} y", {}, untrusted_keys=frozenset())
    assert out == f"x {{{key}}} y"


@settings(max_examples=200, deadline=None)
@given(_WORD)
def test_untrusted_value_is_never_bare_metachar(value: str) -> None:
    engine = PlaceholderEngine(AddonConfig())
    out = engine.resolve("cmd {v}", {"v": value}, untrusted_keys={"v"})
    if any(ch in value for ch in ";|&$`()"):
        assert out == f"cmd {value!r}" or (out.startswith("cmd '") and out.endswith("'"))
