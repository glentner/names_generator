# This program is free software: you can redistribute it and/or modify it under the
# terms of the Apache License (v2.0) as published by the Apache Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the Apache License for more details.
#
# You should have received a copy of the Apache License along with this program.
# If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

"""Unit tests for the `generate_name` console application."""


# type annotations
from __future__ import annotations

# standard libs
import re
import sys
from importlib.metadata import distribution

# external libs
import pytest

# internal libs
from names_generator import NamesGeneratorApp, PROGRAM, HELP, main
from names_generator.__meta__ import __version__


def test_noargs_prints_a_name(capsys: pytest.CaptureFixture) -> None:
    """Test that the application runs without arguments."""
    assert NamesGeneratorApp.main([]) == 0
    assert re.match('^[a-z]+_[a-z]+$', capsys.readouterr().out.strip()) is not None


def test_style_option(capsys: pytest.CaptureFixture) -> None:
    """Test that `--style` selects an alternate formatting."""
    assert NamesGeneratorApp.main(['--style', 'capital']) == 0
    assert re.match('^[A-Z][a-z]+ [A-Z][a-z]+$', capsys.readouterr().out.strip()) is not None


def test_unknown_style_exits_with_usage_error() -> None:
    """Test that an unrecognized `--style` is rejected by the interface."""
    assert NamesGeneratorApp.main(['--style', 'hexadecimal']) == 2


def test_help_option(capsys: pytest.CaptureFixture) -> None:
    """Test that `--help` prints usage and exits cleanly."""
    assert NamesGeneratorApp.main(['--help']) == 0
    assert capsys.readouterr().out.strip() == HELP.strip()


def test_version_option(capsys: pytest.CaptureFixture) -> None:
    """Test that `--version` prints the package version and exits cleanly."""
    assert NamesGeneratorApp.main(['--version']) == 0
    assert capsys.readouterr().out.strip() == __version__


def test_entrypoint(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
    """Test the console-script entry-point against `sys.argv`."""
    monkeypatch.setattr(sys, 'argv', [PROGRAM, '--style', 'hyphen'])
    assert main() == 0
    assert re.match('^[a-z]+-[a-z]+$', capsys.readouterr().out.strip()) is not None


@pytest.mark.parametrize('command', ['names-generator', 'generate_name'])
def test_console_scripts_are_installed(command: str) -> None:
    """Test that both the canonical command and its legacy alias are installed.

    `names-generator` matches the distribution name, which is what lets `uvx
    names-generator` work; `generate_name` is kept for backwards compatibility.
    """
    # NOTE: entry_points(group=...) is 3.10+; Distribution.entry_points works everywhere
    #       we support, and scopes the check to this distribution rather than the env.
    scripts = {entry.name: entry.value
               for entry in distribution('names_generator').entry_points
               if entry.group == 'console_scripts'}
    assert scripts.get(command) == 'names_generator:main'


def test_program_names_itself_after_the_distribution() -> None:
    """Test that usage text advertises the canonical command."""
    assert PROGRAM == 'names-generator'
    assert HELP.splitlines()[1].strip().startswith(PROGRAM)
