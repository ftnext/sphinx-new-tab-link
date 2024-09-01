from __future__ import annotations

from docutils import nodes
from sphinx.util.docutils import ReferenceRole

from sphinx_new_tab_link.core import add_icon_to_reference


class IconLinkRole(ReferenceRole):
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.reference(text=self.title, refuri=self.target)
        reference_with_icon = add_icon_to_reference(node)
        return [reference_with_icon], []
