from docutils import nodes

from sphinx_new_tab_link.extras import external_link_icon_html


def add_icon_to_reference(node: nodes.reference) -> nodes.reference:
    node.append(nodes.Text(" "))
    node.append(nodes.raw(text=external_link_icon_html(), format="html"))
    return node
