def external_link_icon_html() -> str:
    # Keep the icon light enough to sit alongside prose, like MDN's external
    # link indicator.
    return (
        # https://github.com/executablebooks/sphinx-design/blob/v0.6.0/sphinx_design/icons.py#L21-L26
        '<svg version="1.1" width="1em" height="1em" viewBox="0 0 24 24" aria-hidden="true" style="display: inline-block; margin-left: 0.125em; vertical-align: -0.125em; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;">'  # NOQA: E501
        '<path d="M15 3h6v6m-11 5L21 3m-3 10v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>'  # NOQA: E501
        "</svg>"
    )
