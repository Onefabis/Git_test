# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os  # Importing OS module for path manipulations
import sys  # Importing sys to manipulate the Python path
import re 
from datetime import date
import json

sys.path.insert(0, os.path.abspath('../docs'))  # Adds the project root to sys.path

project = 'pfx'
copyright = f'{date.today().year}, PFX Studio'
author = 'PFX'
release = '0.0.1'

root_doc = 'index'
master_doc = 'index' 

# List of Sphinx extensions to use
extensions = [
    'sphinx.ext.autodoc',  # Automatically document Python code
    'sphinx.ext.intersphinx',  # Link to other projects’ documentation
    "sphinx.ext.extlinks",  # Define external links shortcuts
    'sphinx.ext.viewcode',  # Add links to highlighted source code
    'sphinx.ext.todo',  # Support for todo directives
    "sphinx_inline_tabs",  # Support for inline tabs in content
    'myst_parser',  # Support for Markdown files via MyST
    'sphinx_design',  # Additional layout and design features
    'sphinxcontrib.mermaid',  # Mermaid diagrams https://mermaid.live/edit
]

# ------------ Common settings --------------#
source_suffix = {  # Mapping of file suffixes to file types
    '.rst': 'restructuredtext',  # Treat .rst files as reStructuredText
    '.md': 'markdown',  # Treat .md files as Markdown
}
templates_path = ['_templates']  # Path to HTML templates
exclude_patterns = []  # Patterns to exclude from documentation build

# ------------ Intersphinx Ext. --------------#
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}  # Intersphinx mapping to Python docs

# ------------ Autodoc Ext. --------------#
autodoc_default_options = {  # Default options for autodoc
    'members': True,  # Document class/module members
    'undoc-members': True,  # Include undocumented members
    'show-inheritance': True,  # Show class inheritance info
}
autodoc_typehints = 'description'  # Show type hints as part of the description

# ------------ MyST Ext. --------------#
myst_enable_extensions = [  # Additional MyST extensions
    "colon_fence",  # Enable ::: fenced blocks https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#code-fences-using-colons
    "deflist",  # Enable definition lists  https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#definition-lists
    "attrs_inline",  # Enable inline attributes in MyST https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#inline-attributes
    "attrs_block",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#block-attributes
    "tasklist",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#task-lists
    "substitution",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2
    "replacements",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#typography
    "html_admonition",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#html-admonitions
    "html_image",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#html-images
    "linkify",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#linkify
    "smartquotes",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#typography
    "dollarmath",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#dollar-delimited-math
    "amsmath",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#math-shortcuts
    "fieldlist",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#field-lists
    "strikethrough",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#strikethrough
]
myst_heading_anchors = 4  # Numbered anchors for Markdown headings

# Define path to substitutions file
subs_path = os.path.join(os.path.dirname(__file__), '_substitutions.json')  # or .json

# Load the JSON content into myst_substitutions
with open(subs_path, encoding='utf-8') as f:
    myst_substitutions = json.load(f)

ext_path = os.path.join(os.path.dirname(__file__), '_external_links.json')

with open(ext_path, encoding='utf-8') as f:
    data = json.load(f)
    extlinks = {key: tuple(value) for key, value in data.items()}

# ------------ HTML settings --------------#
html_theme = 'furo'  # HTML theme to use for the docs
html_title = 'PFX documentation'  # Custom title for the documentation
html_static_path = ['_static']  # Path to static files like CSS/JS
# Assuming your `conf.py` has a sibling folder called `_static` with these files
html_theme_options = {
}

# ------------ TODO Ext. --------------#
todo_include_todos = True  # Include TODOs in the output


# Replace ~~~mermaid~~~ to ```{mermaid}...``` on the fly, i.e during the build process
def rewrite_mermaid_blocks(app, docname, source):
    text = source[0]

    # Replace ~~~mermaid with ```{mermaid}
    text = re.sub(
        r"~~~mermaid\s*\n", 
        "```{mermaid}\n", 
        text
    )

    # Replace closing ~~~ with ```
    # Note the raw string (r"...") here for the replacement string
    text = re.sub(
        r"\n~~~\s*(\n|$)", 
        r"\n```\1",  # use \1 instead of \g<1> here
        text
    )

    source[0] = text


def setup(app):
    app.connect("source-read", rewrite_mermaid_blocks)
