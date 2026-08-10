# This program is free software: you can redistribute it and/or modify it under the
# terms of the Apache License (v2.0) as published by the Apache Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the Apache License for more details.
#
# You should have received a copy of the Apache License along with this program.
# If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

"""Unit tests for random name generator."""


# type annotations
from __future__ import annotations
from typing import Final, Dict

# standard libs
import re
import random

# external libs
import pytest

# internal libs
from names_generator import random_names, generate_name, restricted_names, names


REPEAT: Final[int] = 1_000
PATTERNS: Final[Dict[str, re.Pattern]] = {
    'underscore': re.compile('^[a-z]+_[a-z]+$'),
    'capital': re.compile('^[A-Z][a-z]+ [A-Z][a-z]+$'),
    'hyphen': re.compile('^[a-z]+-[a-z]+$'),
    'plain': re.compile('^[a-z]+ [a-z]+$')
}


@pytest.mark.parametrize('n', range(REPEAT))
def test_generate_name(n: int) -> None:
    """Test name generator against different formatting styles."""
    style = random.choice(list(PATTERNS))
    assert PATTERNS[style].match(generate_name(style=style)) is not None


@pytest.mark.parametrize('n', range(REPEAT))
def test_random_names(n: int) -> None:
    """Test underlying random choice selector."""
    left, right = random_names()
    assert left in names.LEFT and right in names.RIGHT


@pytest.mark.parametrize('n', range(REPEAT))
def test_random_seed_consistency(n: int) -> None:
    """Test that setting a seed value reproduces the same name pair."""
    assert generate_name(seed=n) == generate_name(seed=n)


def test_random_seed_leaves_global_state_alone() -> None:
    """Test that passing a seed does not re-seed the global PRNG."""
    random.seed(20250810)
    expected = [random.random() for _ in range(4)]
    random.seed(20250810)
    generate_name(seed=1)
    assert [random.random() for _ in range(4)] == expected


def test_random_names_accepts_a_prng() -> None:
    """Test that an explicit `random.Random` drives the selection."""
    assert random_names(random.Random(42)) == random_names(random.Random(42))


def test_unknown_style_is_not_implemented() -> None:
    """Test that an unrecognized formatting style is rejected."""
    with pytest.raises(NotImplementedError):
        generate_name(style='hexadecimal')


def test_restricted_names_are_never_selected(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that restricted pairings are re-drawn (Steve Wozniak is not boring)."""
    monkeypatch.setattr(names, 'LEFT', ['boring', 'happy'])
    monkeypatch.setattr(names, 'RIGHT', ['wozniak', 'turing'])
    drawn = {random_names() for _ in range(REPEAT)}
    assert ('boring', 'wozniak') not in drawn
    assert drawn == {('boring', 'turing'), ('happy', 'wozniak'), ('happy', 'turing')}


@pytest.mark.parametrize('listing', ['LEFT', 'RIGHT'])
def test_listings_match_upstream_conventions(listing: str) -> None:
    """Test that name listings stay sorted and free of duplicates, as upstream keeps them."""
    values = getattr(names, listing)
    assert values == sorted(values)
    assert len(values) == len(set(values))


def test_restricted_names_are_live() -> None:
    """Test that every restricted pairing is actually drawable (i.e., not dead code)."""
    for left, right in restricted_names:
        assert left in names.LEFT and right in names.RIGHT
