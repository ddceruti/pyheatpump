# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import shutil

sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../examples'))

# Copy README.md to docs/source
src = os.path.abspath('../../README.md')
dest = os.path.abspath('./README.md')
if os.path.exists(src) and not os.path.exists(dest):
    shutil.copyfile(src, dest)


# -- Project information -----------------------------------------------------
project = 'pyheatpump'
copyright = '2025, Amedeo Ceruti'
author = 'Amedeo Ceruti'
release = '0.1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinxcontrib.programoutput',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
