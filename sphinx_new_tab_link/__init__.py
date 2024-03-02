import types

from sphinx.application import Sphinx
from sphinx.writers.html import HTMLTranslator

__VERSION__ = "0.2.3"


class NewTabLinkHTMLTranslatorMixin:
    """Patched translator to open an external link in a new tab of the browser.

    ref: https://stackoverflow.com/a/67153583
    """

    def starttag(self, node, tagname, *args, **atts):
        if (
            tagname == "a"
            and "target" not in atts
            and (
                "external" in atts.get("class", "")
                or "external" in atts.get("classes", [])
            )
        ):
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
        return super().starttag(node, tagname, *args, **atts)


class NewTabLinkHTMLTranslator(HTMLTranslator):
    def starttag(self, node, tagname, *args, **atts):
        if (
            tagname == "a"
            and "target" not in atts
            and (
                "external" in atts.get("class", "")
                or "external" in atts.get("classes", [])
            )
        ):
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
        # Support method assignment like the following (But hack)
        # SomeTranslator.starttag = NewTabLinkHTMLTranslator.starttag
        if not isinstance(self, NewTabLinkHTMLTranslator):
            return super(self.__class__, self).starttag(
                node, tagname, *args, **atts
            )
        return super().starttag(node, tagname, *args, **atts)


def inherit_mixin(translator_class):
    return types.new_class(
        "NewTabLinkHTMLTranslatorV2",
        (NewTabLinkHTMLTranslatorMixin, translator_class),
        {},
    )


def setup_translator(app: Sphinx) -> None:
    builder_name = app.builder.name
    if app.builder.format != "html":
        return
    if translator_class := app.registry.translators.get(builder_name):
        app.set_translator(
            builder_name, inherit_mixin(translator_class), override=True
        )
    else:
        app.set_translator(
            builder_name, inherit_mixin(app.builder.default_translator_class)
        )


def setup(app):
    app.set_translator("html", NewTabLinkHTMLTranslator)
    app.set_translator("dirhtml", NewTabLinkHTMLTranslator)
    app.set_translator("singlehtml", NewTabLinkHTMLTranslator)

    return {"version": __VERSION__}
