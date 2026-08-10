# This program is free software: you can redistribute it and/or modify it under the
# terms of the Apache License (v2.0) as published by the Apache Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the Apache License for more details.
#
# You should have received a copy of the Apache License along with this program.
# If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

"""API and entry-point for names_generator."""


# type annotations
from __future__ import annotations
from typing import Tuple, Dict, FrozenSet, Callable, Optional

# standard libs
import sys
import random
import logging

# internal libs
from names_generator.__meta__ import __version__
from names_generator import names

# external libs
from cmdkit.app import Application
from cmdkit.cli import Interface


__all__ = ['random_names', 'format_names', 'generate_name', 'main', 'names', ]


# In the interest of keeping with the original implementation :)
restricted_names: FrozenSet[Tuple[str, str]] = frozenset({
    ('boring', 'wozniak'),  # Steve Wozniak is not boring.
})


def random_names(rng: Optional[random.Random] = None) -> Tuple[str, str]:
    """Select a random choice of names from `names.LEFT` and `names.RIGHT`."""
    choice = random.choice if rng is None else rng.choice
    while True:
        pair = choice(names.LEFT), choice(names.RIGHT)
        if pair not in restricted_names:
            return pair


def _format_plain(pair: Tuple[str, str]) -> str:
    return f'{pair[0]} {pair[1]}'


def _format_capital(pair: Tuple[str, str]) -> str:
    return f'{pair[0].capitalize()} {pair[1].capitalize()}'


def _format_hyphen(pair: Tuple[str, str]) -> str:
    return f'{pair[0]}-{pair[1]}'


def _format_underscore(pair: Tuple[str, str]) -> str:
    return f'{pair[0]}_{pair[1]}'


_formatting_methods: Dict[str, Callable[[Tuple[str, str]], str]] = {
    'plain': _format_plain,
    'capital': _format_capital,
    'hyphen': _format_hyphen,
    'underscore': _format_underscore,
}


def format_names(pair: Tuple[str, str], style: str = 'underscore') -> str:
    """Format a pair of names in one of several styles."""
    try:
        return _formatting_methods[style](pair)
    except KeyError as error:
        raise NotImplementedError(f'No style \'{style}\'') from error


def generate_name(style: str = 'underscore', seed: Optional[int] = None) -> str:
    """Generate a random name."""
    # NOTE: an explicit seed gets its own PRNG instance so that we never reach in
    #       and disturb the global random state on behalf of the caller.
    rng = None if seed is None else random.Random(seed)
    return format_names(random_names(rng), style=style)


# Command-line interface implementation
# NOTE: `generate_name` remains installed as an alias, but the program names itself
#       after the distribution so that `uvx names-generator` and friends work.
PROGRAM = 'names-generator'
USAGE = f"""\
Usage:
  {PROGRAM} [-h] [-v] [--style NAME]
  Generate random name pairing.\
"""

EPILOG = f"""\
Documentation and issue tracking at:
https://github.com/glentner/names_generator\
"""

HELP = f"""\
{USAGE}

Options:
  -s, --style    NAME    Formatting (default: underscore).
  -h, --help             Show this message and exit.
  -v, --version          Show the version and exit.

{EPILOG}\
"""


class NamesGeneratorApp(Application):
    """Top-level application class for `generate_name` console application."""

    interface = Interface(PROGRAM, USAGE, HELP)
    interface.add_argument('-v', '--version', action='version', version=__version__)

    style: str = 'underscore'
    interface.add_argument('-s', '--style', default=style, choices=list(_formatting_methods))

    # run even without arguments (do not print usage)
    ALLOW_NOARGS = True

    def run(self) -> None:
        """Generate a random name and print it."""
        print(generate_name(style=self.style))


def main() -> int:
    """Entry-point for `generate_name` console application."""
    logging.basicConfig(format='%(msg)s')
    return NamesGeneratorApp.main(sys.argv[1:])
