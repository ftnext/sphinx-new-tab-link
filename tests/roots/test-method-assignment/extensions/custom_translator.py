"""There is no need of method assignment.

v0.3.0 or later, sphinx_new_tab_link supports dynamic inheritance to add
functionality to open an external link in a new tab of the browser.
"""

from sphinx.writers.html5 import HTML5Translator


class MyTranslator(HTML5Translator): ...  # NOQA: E701


# MyTranslator.starttag = NewTabLinkHTMLTranslator.starttag


def setup(app):
    app.set_translator("html", MyTranslator)
