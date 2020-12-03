names_generator
===============

.. image:: https://img.shields.io/badge/license-Apache-blue.svg?style=flat
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: License

.. image:: https://img.shields.io/pypi/v/names_generator.svg?style=flat&color=blue
    :target: https://pypi.org/project/names_generator
    :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/names_generator.svg?logo=python&logoColor=white&style=flat
    :target: https://pypi.org/project/names_generator
    :alt: Python Versions

|

Clone of the Moby/Docker random name generator as a Python package.


Installation
------------

.. code-block:: bash

    $ pip install names_generator

|

Examples
--------

|

The API only really consists of a single function.

.. code-block:: python

    >>> from names_generator import generate_name
    >>> generate_name()
    'vigorous_goldstine'

|

Customize the formatting of the name by specifying a `style`,
One of `plain`, `capital`, `hyphen`, or `underscore` (default).

.. code-block:: python

    >>> generate_name(style='capital')
    'Hardcore Thompson'

|

Pin a seed value for the underlying PRNG to reproduce a given name.

.. code-block:: python

    >>> generate_name(seed=42) == generate_name(seed=42)
    True

|

The package also exposes a basic command-line interface for scripting outside of Python

.. code-block:: bash

    $ generate_name
    clever_matsumoto

    $ generate_name --style=capital
    Heuristic Einstein

    $ generate_name --help
    usage: generate_name [-h] [-v] [--style NAME]
    Generate random name pairing.

    options:
    -s, --style    NAME    Formatting (default: underscore).
    -h, --help             Show this message and exit.
    -v, --version          Show the version and exit.

    Documentation and issue tracking at:
    https://github.com/glentner/names_generator
