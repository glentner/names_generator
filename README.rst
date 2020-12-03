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

.. code-block:: python

    >>> from names_generator import generate_name
    >>> generate_name()
    'vigorous_goldstine'


.. code-block:: python

    >>> generate_name(style='capital')
    'Hardcore Thompson'


.. code-block:: python

    >>> generate_name(seed=42) == generate_name(seed=42)
    True
