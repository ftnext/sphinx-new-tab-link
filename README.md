# sphinx-new-tab-link
![testing workflow](https://github.com/ftnext/sphinx-new-tab-link/actions/workflows/testing.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/sphinx-new-tab-link.svg)](https://badge.fury.io/py/sphinx-new-tab-link)
[![Python Versions](https://img.shields.io/pypi/pyversions/sphinx-new-tab-link.svg)](https://pypi.org/project/sphinx-new-tab-link/)

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

## Configuration

### `new_tab_link_show_external_link_icon`

* Type: `bool`
* Default: `False`

If you want to show external links with icons, set this to `True` in your `conf.py`.

```python
new_tab_link_show_external_link_icon = True
```

## Roles

### External link with icon (Experimental)

```rst
External link: :icon-link:`Example <https://example.com/>`
```

Enjoy documentation!🙌
