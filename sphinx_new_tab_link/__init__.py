from sphinx.writers.html import HTMLTranslator


class NewTabLinkHTMLTranslator(HTMLTranslator):
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
        # Support method assignment like the following (But hack)
        # SomeTranslator.starttag = NewTabLinkHTMLTranslator.starttag
        return super(self.__class__, self).starttag(
            node, tagname, *args, **atts
        )


def setup(app):
    app.set_translator("html", NewTabLinkHTMLTranslator)
    app.set_translator("dirhtml", NewTabLinkHTMLTranslator)
    app.set_translator("singlehtml", NewTabLinkHTMLTranslator)
