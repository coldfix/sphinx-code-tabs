sphinx code tabs
================

This is a Sphinx extension that adds a directive ``code-tabs`` that creates a
navbar above several alternative code blocks, allowing the user to switch
between them.


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

The ``code-tabs`` directive declares a notebook of code block alternatives.
The individual tabs must be created with the ``code-tab`` directive which
derives from ``code-block`` and accepts all of its arguments.

For example:

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
