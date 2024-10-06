# Markdown example / Markdownの例

*Here is an example of how `sphinx-new-tab-link` works with HTML built from a Markdown file.*  
*MarkdownファイルからビルドされたHTMLでも`sphinx-new-tab-link`が機能する例です。*

```{note} reST version: [reST example](guide.en.rst) / [reSTの例](guide.rst)
```

## Links / リンク集

* PyPI <https://pypi.org/project/sphinx-new-tab-link/>
* [GitHub Repository](https://github.com/ftnext/sphinx-new-tab-link)

## Installation / インストール

```shell
$ pip install sphinx-new-tab-link myst-parser
```

## How to use / 使い方

`conf.py`

```python
    extensions = [
        "myst_parser",
        "sphinx_new_tab_link",
    ]
```

## Supported notations / 対応している記法

It supports various notations of a external link possible in MyST.  
MySTで可能なさまざまな記法による外部リンクをサポートしています。

ref: <https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#default-destination-resolution>

✅Autolinks

See *PyPI* at ['Links / リンク集' section](#links--リンク集)

```md
<https://pypi.org/project/sphinx-new-tab-link/>
```

✅Inline links (to external target)

See *GitHub Repository* at ['Links / リンク集' section](#links--リンク集)

```md
[GitHub Repository](https://github.com/ftnext/sphinx-new-tab-link)
```

✅Reference links (to external target)

[公開版ガイド(ja)][guide-ja]

[guide-ja]: https://ftnext.github.io/sphinx-new-tab-link/guide.html

```md
[公開版ガイド(ja)][guide-ja]

[guide-ja]: https://ftnext.github.io/sphinx-new-tab-link/guide.html
```

Enjoy documentation!🙌
