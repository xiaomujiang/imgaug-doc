# -*- coding: utf-8 -*-
#
# imgaug documentation build configuration file, created by
# sphinx-quickstart on Sat Aug 19 12:48:49 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys


# --------------
# We add the parent directory here, which must contain imgaug/.
# This is necessary to automatically generate APIs via autodoc.
# We use here a variation of abspath() that accounts for symlinks to find the parent directory's path.
# This allows to symlink imgaug-doc in e.g. imgaug-project/ (containing then imgaug-doc/ and imgaug/),
# and still use e.g. `cd imgaug-project && cd imgaug-doc && make html` in imgaug-doc without errors.


def logical_abspath(p):
    # taken from https://stackoverflow.com/questions/17805312/how-to-get-the-symbolic-path-instead-of-real-path
    curr_path = os.environ['PWD']
    return os.path.normpath(os.path.join(curr_path, p))


sys.path.insert(0, logical_abspath('../'))
# --------------

# --------------
# Currently we add imgaug/ source as a subfolder here, so that we can build the docs from the main directory
# and keep that main directory in a state where it only contains docs files.
# This allows us to link the imgaug-doc repository as doc/ from the main repo, but simultaneously also let RTD
# build the docs from imgaug-doc, including auto-generated API.
dir_path = os.path.abspath(os.path.dirname(__file__))
if os.path.exists(os.path.join(dir_path, "imgaug")):
    # the included directory must contain imgaug/ as a subdirectory, hence we do *not* add <current_dir>/imgaug
    sys.path.insert(0, dir_path)
# --------------


# unittest.mock is available in python 3.3+ by default
# in lower versions run 'pip install mock'
try:
    from unittest.mock import MagicMock
except ImportError as e:
    from mock import Mock as MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        if name == "sctypes":
            return {"float": []}
        else:
            return MagicMock()

# 'scipy.spatial', 'scipy.spatial.distance'
"""'numpy', 'pandas', 'scipy',
   'cv2', 'skimage', 'skimage.draw', 'skimage.measure', 'matplotlib',
   'matplotlib.pyplot', 'imageio'"""
MOCK_MODULES = ['argparse', 'cv2']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'numpydoc'
]

# !!!!!!!!!!!!!!!!!!!
# Deactivating this causes lots of warnings from files not being in TOCs.
# These seem to not really have any negative effects.
# Activating this (i.e. setting it to False) removes the warnings, but also
# removes the overviews of class member functions. These are important
# overviews in APIs.
# Activate/uncomment this during development until all other warnings/errors are
# fixed, then deactivate/comment this again.
# !!!!!!!!!!!!!!!!!!!
# numpydoc_show_class_members = False

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'imgaug'
copyright = u'2017, Alexander Jung'
author = u'Alexander Jung'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.2.7'
# The full version, including alpha/beta/rc tags.
release = u'0.2.7'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'imgaugdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'imgaug.tex', u'imgaug Documentation',
     u'Alexander Jung', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'imgaug', u'imgaug Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'imgaug', u'imgaug Documentation',
     author, 'imgaug', 'One line description of project.',
     'Miscellaneous'),
]
