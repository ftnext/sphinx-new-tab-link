from typing import TypedDict

from docutils.nodes import Text, raw
from sphinx.application import Sphinx
from sphinxcontrib.kasane import new_translator_class_for_builder

__VERSION__ = "0.4.0"


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
                node[0] = Text(node[0].astext() + " ")
                node.append(
                    raw(
                        # https://primer.style/foundations/icons/link-external-16/
                        text='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path d="M3.75 2h3.5a.75.75 0 0 1 0 1.5h-3.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-3.5a.75.75 0 0 1 1.5 0v3.5A1.75 1.75 0 0 1 12.25 14h-8.5A1.75 1.75 0 0 1 2 12.25v-8.5C2 2.784 2.784 2 3.75 2Zm6.854-1h4.146a.25.25 0 0 1 .25.25v4.146a.25.25 0 0 1-.427.177L13.03 4.03 9.28 7.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.75-3.75-1.543-1.543A.25.25 0 0 1 10.604 1Z"></path></svg>',
                        format="html",
                    )
                )
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
