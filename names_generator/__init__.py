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
from typing import Tuple, List, Dict, Callable

# standard libs
import sys
import random
import logging

# internal libs
from names_generator.__meta__ import __version__, __description__, __authors__, __contact__
from names_generator import names

# external libs
from cmdkit.app import Application
from cmdkit.cli import Interface


# In the interest of keeping with the original implementation :)
restricted_names: List[Tuple[str, str]] = [
    ('boring', 'wozniak')  # Steve Wozniak is not boring.
]


def random_names() -> Tuple[str, str]:
    """Select a random choice of names from `names.LEFT` and `names.RIGHT`."""
    _names = random.choice(names.LEFT), random.choice(names.RIGHT)
    return _names if _names not in restricted_names else random_names()


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


def generate_name(style: str = 'underscore', seed: int = None) -> str:
    """Generate a random name."""
    if seed is not None:
        random.seed(seed)
    return format_names(random_names(), style=style)


# Command-line interface implementation
PROGRAM = 'generate_name'
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
