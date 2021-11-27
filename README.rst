sphinx code tabs
================

|Version| |License| |Documentation|

This is a Sphinx extension that adds a directive ``code-tabs`` that creates a
navbar above several alternative code blocks, allowing the user to switch
between them.

This can be used to e.g. show a snippet in multiple languages, display
instructions for alternative platforms, or (in the future) switch between
source and output.

|Screenshot|


Installation
------------

.. code-block:: bash

    pip install sphinx_code_tabs

To enable the extension in sphinx, simply add the package name in your
``conf.py`` to the list of ``extensions``:

.. code-block:: python

    extensions = [
        ...
        'sphinx_code_tabs',
    ]


Usage
-----

By enabling the extension you get access to the ``code-tabs`` directive that
declares a notebook of code block alternatives.

The individual tabs must be created with the ``code-tab`` directive which
derives from ``code-block`` and accepts all of its arguments:

.. code-block:: rst

    .. code-tabs::

        .. code-tab:: bash
            :caption: bash

            echo "Hello, World!"

        .. code-tab:: c
            :caption: C/C++
            :emphasize-lines: 2

            #include <stdio.h>
            int main() { printf("Hello, world!\n"); }

        .. code-tab:: python
            :caption: python

            print("Hello, world!")


Planned changes
---------------

This project has just started. Planned features for the next releases (this might
initially include backward-incompatible changes!):

- add mechanism to group several tab widgets together, so that the selection
  is kept in sync (which means users interested in a specific language won't
  have to change the language on each snippet individually in a longer article)
- reuse "code-block" rather than introducing our own "code-tab" (?)
- allow tabs other than code-blocks (maybe)


.. |Documentation| image::  https://readthedocs.org/projects/sphinx-code-tabs/badge/?version=latest
   :target:                 https://sphinx-code-tabs.readthedocs.io/en/latest/
   :alt:                    Documentation

.. |License| image::    https://img.shields.io/pypi/l/sphinx-code-tabs.svg
   :target:             https://github.com/coldfix/sphinx-code-tabs/blob/main/UNLICENSE
   :alt:                License: Unlicense

.. |Version| image::    https://img.shields.io/pypi/v/sphinx-code-tabs.svg
   :target:             https://pypi.org/project/sphinx-code-tabs
   :alt:                Latest Version

.. |Screenshot| image:: https://raw.githubusercontent.com/coldfix/sphinx-code-tabs/main/screenshot.webp
   :target:             https://sphinx-code-tabs.readthedocs.io/en/latest/#usage
   :alt:                Screenshot (usernames were changed)
