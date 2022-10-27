# sphinx-new-tab-link
Open external links in new tabs of the browser in Sphinx HTML documents

## Overview

If you enable `sphinx_new_tab_link`, external links of built HTML are opened in new tabs of your browser.

The reST

```rst
External link: `Example <https://example.com/>`_
```

is converted into

```html
External link: <a class="reference external" href="https://example.com/" rel="noopener noreferrer" target="_blank">Example</a>
```

## Usage

First, create your Sphinx documentation.

Then edit `conf.py` to use this extension.

```python
extensions = [
    "sphinx_new_tab_link",
]
```

Enjoy documentation!🙌
