"""Sphinx configuration for the firstpr documentation.

You'll edit and build these docs in Session 4. To build locally:
    python -m pip install -e ".[docs]"
    sphinx-build -b html docs docs/_build/html
    # then open docs/_build/html/index.html
"""

project = "firstpr"
copyright = "2026, Python Open Source Workshop contributors"
author = "Workshop contributors"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",   # pull docstrings out of the code
    "sphinx.ext.napoleon",  # understand Google-style docstrings
    "sphinx.ext.doctest",   # run the >>> examples as tests
    "myst_parser",          # let us write pages in Markdown
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "alabaster"

autodoc_member_order = "bysource"
