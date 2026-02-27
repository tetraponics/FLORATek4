# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FLORATek 4'
copyright = '2026, Tetraponics'
author = 'Tetraponics'

release = 'v2.x.x'
version = 'v2.x.x'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Theme options for branding
html_theme_options = {
    'logo_only': False,
    'version_selector': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2ecc71',  # Your brand color
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add custom CSS and logo
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]


# Logo and favicon (add your logo files to _static folder)
html_logo = '_static/tetraponicslogo.png'
html_favicon = '_static/favicon.ico'

# Custom sidebar
html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
    ]
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
