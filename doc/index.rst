Welcome to sphinx_code_tabs's documentation!
============================================

This is a Sphinx extension that adds a directive ``code-tabs`` that creates a
navbar above several alternative code blocks, allowing the user to switch
between them.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Installation
============

.. code-block:: bash

    pip install sphinx_code_tabs

Usage
=====

To enable the extension in sphinx, simply add the package name in your
``conf.py`` to the list of ``extensions``:

.. code-block:: python

    extensions = [
        ...
        'sphinx_code_tabs',
    ]


By enabling the extension you get access to the ``code-tabs`` directive that
declares a notebook of code block alternatives. The individual tabs must be
created with the ``code-tab`` directive which derives from ``code-block`` and
accepts all of its arguments.

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

This should result in the following output:

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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
