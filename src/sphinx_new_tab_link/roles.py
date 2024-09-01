from docutils import nodes
from sphinx.util.docutils import ReferenceRole

from sphinx_new_tab_link.extras import external_link_icon_html


class IconLinkRole(ReferenceRole):
    def run(self):
        node = nodes.reference(text=self.title, refuri=self.target)
        node.append(nodes.Text(" "))
        node.append(nodes.raw(text=external_link_icon_html(), format="html"))
        return [node], []
