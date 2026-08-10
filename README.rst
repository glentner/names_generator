names_generator
===============

.. image:: https://img.shields.io/badge/license-Apache-red.svg?style=flat
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: License

.. image:: https://img.shields.io/pypi/v/names_generator.svg?style=flat
    :target: https://pypi.org/project/names_generator
    :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/names_generator.svg?logo=python&logoColor=white&style=flat
    :target: https://pypi.org/project/names_generator
    :alt: Python Versions

.. image:: https://static.pepy.tech/badge/names_generator/month
    :target: https://www.pepy.tech/projects/names_generator
    :alt: Downloads per month

.. image:: https://github.com/glentner/names_generator/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/glentner/names_generator/actions/workflows/tests.yml
    :alt: Tests

|

Clone of the Moby/Docker random name generator as a Python package.


Installation
------------

.. code-block:: bash

    $ pip install names_generator

Or, with `uv <https://docs.astral.sh/uv>`_:

.. code-block:: bash

    $ uv add names_generator

|

Usage
-----

|

Python API
^^^^^^^^^^

|

The API only really consists of a single function.

.. code-block:: python

    >>> from names_generator import generate_name
    >>> generate_name()
    'vigorous_goldstine'

|

Customize the formatting of the name by specifying a `style`,
one of `plain`, `capital`, `hyphen`, or `underscore` (default).

.. code-block:: python

    >>> generate_name(style='capital')
    'Hardcore Thompson'

|

Pin a seed value for the underlying PRNG to reproduce a given name.
A seed is applied to a dedicated PRNG instance, so it never disturbs the
global `random` state on your behalf.

.. code-block:: python

    >>> generate_name(seed=42) == generate_name(seed=42)
    True

Note that a seed only guarantees reproducibility *within* a given release.
Whenever the underlying name listings change to stay in sync with upstream,
some seeds will map to a different name.

|

Command-line
^^^^^^^^^^^^

|

The package also exposes a basic command-line interface for scripting outside of Python

.. code-block:: bash

    $ generate_name
    clever_matsumoto

    $ generate_name --style=capital
    Heuristic Einstein

    $ generate_name --help
    Usage:
      generate_name [-h] [-v] [--style NAME]
      Generate random name pairing.

    Options:
      -s, --style    NAME    Formatting (default: underscore).
      -h, --help             Show this message and exit.
      -v, --version          Show the version and exit.

    Documentation and issue tracking at:
    https://github.com/glentner/names_generator

|

Development
-----------

|

This project uses `uv <https://docs.astral.sh/uv>`_.

.. code-block:: bash

    $ uv sync
    $ uv run pytest -v --cov

|

Upstream
--------

|

The name listings in ``names_generator/names.py`` are a direct port of
`internal/namesgenerator <https://github.com/moby/moby/blob/master/internal/namesgenerator/names-generator.go>`_
from the Moby project, kept in the same order so the two can be diffed mechanically.

Upstream declared the listing `frozen <https://github.com/moby/moby/pull/43210>`_, so no
new names are accepted here either. Changes to ``names.py`` are only made to bring this
port back in sync with upstream.
