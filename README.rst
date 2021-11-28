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

By enabling the extension you get access to the ``tabs`` directive that
declares a notebook of code block alternatives.

The individual tabs are created with the ``tab`` or ``code-tab`` directives. A
``tab`` can contain arbitrary restructuredText, while a ``code-tab`` acts like
a ``code-block`` and accepts all corresponding arguments. Both types of tabs
can appear in the same notebook.

For example, this is the source of above example:

.. code-block:: rst

    .. tabs::

        .. code-tab:: bash

            echo "Hello, *World*!"

        .. code-tab:: c
            :caption: C/C++
            :emphasize-lines: 2

            #include <stdio.h>
            int main() { printf("Hello, *World*!\n"); }

        .. code-tab:: python

            print("Hello, *World*!")

        .. tab:: Output

            Hello, *World*!


Planned changes
---------------

This project has just started. Planned features for the next releases (this might
initially include backward-incompatible changes!):

- add mechanism to group several tab widgets together, so that the selection
  is kept in sync (which means users interested in a specific language won't
  have to change the language on each snippet individually in a longer article)
- reuse "code-block" rather than introducing our own "code-tab" (?)


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
   :alt:                Code tabs screenshot
