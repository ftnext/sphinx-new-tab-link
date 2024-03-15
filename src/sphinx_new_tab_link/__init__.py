from typing import TypedDict

from sphinx.application import Sphinx

from sphinx_new_tab_link.kasane import MixinDynamicInheritance, TranslatorSetUp

__VERSION__ = "0.3.1"


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


class ExtensionMetadata(TypedDict):
    version: str
    parallel_read_safe: bool


def setup(app: Sphinx) -> ExtensionMetadata:
    inheritance = MixinDynamicInheritance(
        NewTabLinkHTMLTranslatorMixin, "NewTabLinkHTMLTranslator"
    )
    app.connect("builder-inited", TranslatorSetUp("html", inheritance))

    return {"version": __VERSION__, "parallel_read_safe": True}
