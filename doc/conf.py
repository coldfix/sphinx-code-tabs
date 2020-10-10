# Configuration file for the Sphinx documentation builder.
#
# For a full # list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import sphinx_rtd_theme
import sphinx_code_tabs


# -- Project information -----------------------------------------------------
project = 'sphinx_code_tabs'
copyright = '2020, Thomas Gläßle'
author = 'Thomas Gläßle'
release = sphinx_code_tabs.__version__


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_code_tabs',
]

master_doc = 'index'
source_suffix = '.rst'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
