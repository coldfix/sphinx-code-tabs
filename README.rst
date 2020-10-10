sphinx code tabs
================

|Version| |License| |Documentation|

This is a Sphinx extension that adds a directive ``code-tabs`` that creates a
navbar above several alternative code blocks, allowing the user to switch
between them.

This can be used to e.g. show a snippet in multiple languages, on multiple
platforms, or source and render.

For a visual example, see `Documentation#Usage`_..

.. _Documentation#Usage: https://sphinx-code-tabs.readthedocs.io/en/latest/#usage


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

For a visual example, see `Documentation#Usage`_..

The individual tabs must be created with the ``code-tab`` directive which
derives from ``code-block`` and accepts all of its arguments:

.. code-block:: rst

    .. code-tabs::

        .. code-tab:: bash
            :title: bash

            echo "Hello, World!"

        .. code-tab:: c
            :title: C/C++
            :emphasize-lines: 2

            #include <stdio.h>
            int main() { printf("Hello, world!\n"); }

        .. code-tab:: python
            :title: python

            print("Hello, world!")


Planned changes
---------------

This project has just started. Planned features for the next releases (this might
initially include backward-incompatible changes!):

- prerender navbar, and CSS "hidden" classes, so that the layout doesn't change
  during page reload
- add mechanism to group several tab widgets together, so that the selection
  is kept in sync (which means users interested in a specific language won't
  have to change the language on each snippet individually in a longer article)
- adopt "caption" attribute rather using our own "title"
- reuse "code-block" rather than introducing our own "code-tab" (?)
- allow tabs other than code-blocks (maybe)


.. |Documentation| image::  https://readthedocs.org/projects/sphinx-code-tabs/badge/?version=latest
   :target:                 https://sphinx-code-tabs.readthedocs.io/en/latest/
   :alt:                    Documentation

.. |License| image::    https://img.shields.io/pypi/l/sphinx-code-tabs.svg
   :target:             https://github.com/coldfix/sphinx-code-tabs/blob/master/UNLICENSE
   :alt:                License: Unlicense

.. |Version| image::    https://img.shields.io/pypi/v/sphinx-code-tabs.svg
   :target:             https://pypi.org/project/sphinx-code-tabs
   :alt:                Latest Version
