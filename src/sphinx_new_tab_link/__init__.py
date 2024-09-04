from typing import TypedDict

from docutils import nodes
from sphinx.application import Sphinx
from sphinxcontrib.kasane import new_translator_class_for_builder

from sphinx_new_tab_link.core import add_icon_to_reference
from sphinx_new_tab_link.roles import IconLinkRole

__VERSION__ = "0.6.0"


class NewTabLinkHTMLTranslatorMixin:
    """Patched translator to open an external link in a new tab of the browser.

    ref: https://stackoverflow.com/a/67153583
    """

    def starttag(self, node: nodes.Node, tagname: str, *args, **atts):
        if (
            tagname == "a"
            and "target" not in atts
            and (
                "external" in atts.get("class", "")
                or "external" in atts.get("classes", [])
            )
        ):
            assert isinstance(node, nodes.reference)
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
            if self.builder.config.new_tab_link_show_external_link_icon:  # type: ignore[attr-defined]  # noqa: E501
                node = add_icon_to_reference(node)
        return super().starttag(node, tagname, *args, **atts)  # type: ignore[misc]  # noqa: E501


class ExtensionMetadata(TypedDict):
    version: str
    parallel_read_safe: bool


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value("new_tab_link_show_external_link_icon", False, "html")
    app.add_role("icon-link", IconLinkRole())

    html_translator_handler = new_translator_class_for_builder(
        "html", NewTabLinkHTMLTranslatorMixin, "NewTabLinkHTMLTranslator"
    )
    app.connect("builder-inited", html_translator_handler)

    return {"version": __VERSION__, "parallel_read_safe": True}
