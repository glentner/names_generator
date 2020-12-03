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
from typing import List, Dict

# standard libs
import re
import random

# internal libs
from names_generator import random_names, generate_name, names


REPEAT: int = 100_000
PATTERNS: Dict[str, re.Pattern] = {
    'underscore': re.compile('^[a-z]+_[a-z]+$'),
    'capital': re.compile('^[A-Z][a-z]+ [A-Z][a-z]+$'),
    'hyphen': re.compile('^[a-z]+-[a-z]+$'),
    'plain': re.compile('^[a-z]+ [a-z]+$')
}


def test_generate_name() -> None:
    """Test name generator against different formatting styles."""
    for i in range(REPEAT):
        style = random.choice(list(PATTERNS))
        assert PATTERNS[style].match(generate_name(style=style)) is not None


def test_random_names() -> None:
    """Test underlying random choice selector."""
    for i in range(REPEAT):
        left, right = random_names()
        assert left in names.LEFT and right in names.RIGHT


def test_random_seed_consistency() -> None:
    """Test that setting a seed value reproduces the same name pair."""
    for i in range(REPEAT):
        assert generate_name(seed=i) == generate_name(seed=i)
