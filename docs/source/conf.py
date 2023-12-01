
import os
import sys
sys.path.insert(0, os.path.abspath('../../src/PDFReport'))
sys.path.insert(0, os.path.abspath('../../samples'))


# -- Project information -----------------------------------------------------

project = 'PDFReport'
copyright = '2023, Michael Hodel'
author = 'Michael Hodel'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
]

templates_path = ['_templates']
exclude_patterns = []
add_module_names = False

autodoc_class_signature = "separated"
autodoc_member_order = "bysource"
autodoc_typehints_format = "short"

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']

html_title = "PDFReport"

latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    }
