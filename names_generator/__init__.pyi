# This program is free software: you can redistribute it and/or modify it under the
# terms of the Apache License (v2.0) as published by the Apache Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the Apache License for more details.
#
# You should have received a copy of the Apache License along with this program.
# If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

"""Stub file for __init__.py"""

#Type annotations in this file mirror the source file
from typing import Tuple, List, Dict, Callable, Optional

restricted_names: List[Tuple[str, str]]
_formatting_methods: Dict[str, Callable[[Tuple[str, str]], str]]

def random_names() -> Tuple[str, str]: ...
def _format_plain(pair: Tuple[str, str]) -> str:...
def _format_capital(pair: Tuple[str, str]) -> str:...
def _format_hyphen(pair: Tuple[str, str]) -> str:...
def _format_underscore(pair: Tuple[str, str]) -> str:...
def format_names(pair: Tuple[str, str], style: str = 'underscore') -> str:...
def generate_name(style: str = 'underscore', seed: Optional[int] = None) -> str:...