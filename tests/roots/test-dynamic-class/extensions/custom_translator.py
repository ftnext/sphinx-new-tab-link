# https://github.com/ftnext/sphinx-new-tab-link/issues/11
import types

from sphinx_new_tab_link import NewTabLinkHTMLTranslator


class StartTagMixin:
    def starttag(self, *args, **kwargs):
        return super().starttag(*args, **kwargs)


def setup(app):
    app.set_translator("html", NewTabLinkHTMLTranslator)

    translator_class = types.new_class(
        "MyTranslator",
        (StartTagMixin, app.registry.translators["html"]),
        {},
    )
    app.set_translator("html", translator_class, override=True)
