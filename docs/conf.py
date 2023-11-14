# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("."))


# -- Project information -----------------------------------------------------
project = "dt-sdk"
copyright = f"2023–{datetime.now().year}, Dynatrace LLC"
author = "Dynatrace"

# Short version
version = "1.0.0"
# The full version, including alpha/beta/rc tags
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx_wagtail_theme",
    "sphinxcontrib.programoutput",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# True to prefix each section label with the name of the document it is in,
# followed by a colon. For example, index:Introduction for a section called
# Introduction that appears in document index.rst. Useful for avoiding
# ambiguity when the same section heading appears in different documents.
autosectionlabel_prefix_document = True

# -- Autodoc -----------------------------------------------------------------

autodoc_default_options = {"member-order": "bysource", "undoc-members": True}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_wagtail_theme"
html_favicon = "_static/favicon.ico"
html_show_copyright = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_sidebars = {"**": ["search-field.html", "sidebar-nav-bs.html"]}

html_theme_options = {
    "project_name": "dt-sdk",
    "logo": "dt-sdk-logo.png",
    "logo_alt": "dt-sdk",
    "logo_url": "/",
    "github_url": "https://github.com/dynatrace-extensions/dt-extensions-python-sdk",
}
