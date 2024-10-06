from __future__ import annotations

from urllib.parse import urlparse

from docutils import nodes
from sphinx.util.docutils import ReferenceRole

from sphinx_new_tab_link.core import add_icon_to_reference


class IconLinkRole(ReferenceRole):
    """Role to create a external link with an icon.

    Of course, opened in new tabs of your browser.

    Usage::

        :icon-link:`title <target>`
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        parse_result = urlparse(self.target)
        if parse_result.scheme:
            node = nodes.reference(
                text=self.title, refuri=self.target, internal=False
            )
            reference_with_icon = add_icon_to_reference(node)
            return [reference_with_icon], []
        else:
            node = nodes.reference(
                text=self.title, refuri=f"#{self.target}", internal=True
            )
            return [node], []
