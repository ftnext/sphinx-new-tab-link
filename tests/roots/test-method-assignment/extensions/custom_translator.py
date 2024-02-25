from sphinx.writers.html5 import HTML5Translator

from sphinx_new_tab_link import NewTabLinkHTMLTranslator


class MyTranslator(HTML5Translator): ...


MyTranslator.starttag = NewTabLinkHTMLTranslator.starttag


def setup(app):
    app.set_translator("html", MyTranslator)
