from typing import TypedDict

from docutils.nodes import Text, raw
from sphinx.application import Sphinx
from sphinxcontrib.kasane import new_translator_class_for_builder

from sphinx_new_tab_link.extras import external_link_icon_html

__VERSION__ = "0.5.1"


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
            if self.builder.config.new_tab_link_show_external_link_icon:
                node.append(Text(" "))
                node.append(raw(text=external_link_icon_html(), format="html"))
        return super().starttag(node, tagname, *args, **atts)


class ExtensionMetadata(TypedDict):
    version: str
    parallel_read_safe: bool


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value("new_tab_link_show_external_link_icon", False, "html")

    html_translator_handler = new_translator_class_for_builder(
        "html", NewTabLinkHTMLTranslatorMixin, "NewTabLinkHTMLTranslator"
    )
    app.connect("builder-inited", html_translator_handler)

    return {"version": __VERSION__, "parallel_read_safe": True}
