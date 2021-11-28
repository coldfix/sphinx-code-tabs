sphinx code tabs
================

|Version| |License| |Documentation|

This is a Sphinx extension that adds a ``tabs`` directive for creating a
tabbed widget, allowing the user to switch between them. The individual tabs
can be code blocks or general content.

This can be used to e.g. show a snippet in multiple languages, display
instructions for alternative platforms, or switch between code and output.

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

The ``:selected:`` option allows to switch to a specified tab at start. By
default, the first tab is used.

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
            :selected:

            Hello, *World*!


Grouped tabs
~~~~~~~~~~~~

The ``tabs`` directive takes an optional argument that identifies its *tab
group*. Within a given tab group, all notebooks will automatically be switched
to the same tab number if the tab is switched in one member of the group.
It is your responsibility to make sure that each member of the group has the
same number and ordering of tabs. Example:

|Tabgroup|

Source:

.. code-block:: rst

    .. tabs:: lang

        .. code-tab:: bash

            echo "Hello, group!"

        .. code-tab:: python

            print("Hello, group!")


    .. tabs:: lang

        .. code-tab:: bash

            echo "Goodbye, group!"

        .. code-tab:: python

            print("Goodbye, group!")



.. |Documentation| image::  https://readthedocs.org/projects/sphinx-code-tabs/badge/?version=latest
   :target:                 https://sphinx-code-tabs.readthedocs.io/en/latest/
   :alt:                    Documentation

.. |License| image::    https://img.shields.io/pypi/l/sphinx-code-tabs.svg
   :target:             https://github.com/coldfix/sphinx-code-tabs/blob/main/UNLICENSE
   :alt:                License: Unlicense

.. |Version| image::    https://img.shields.io/pypi/v/sphinx-code-tabs.svg
   :target:             https://pypi.org/project/sphinx-code-tabs
   :alt:                Latest Version

.. |Screenshot| image:: https://raw.githubusercontent.com/coldfix/sphinx-code-tabs/main/screenshot1.webp
   :target:             https://sphinx-code-tabs.readthedocs.io/en/latest/#usage
   :alt:                Code tabs screenshot

.. |Tabgroup| image::   https://raw.githubusercontent.com/coldfix/sphinx-code-tabs/main/screenshot2.webp
   :target:             https://sphinx-code-tabs.readthedocs.io/en/latest/#grouped-tabs
   :alt:                Grouped tabs screenshot
