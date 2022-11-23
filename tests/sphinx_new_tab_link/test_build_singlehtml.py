from io import StringIO

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.parametrize(
    "index,expected_url",
    [
        (0, "http://abehiroshi.la.coocan.jp"),
        (1, "https://pypi.org/project/sphinx-new-tab-link/"),
        (
            2,
            "https://www.sphinx-doc.org/en/master/usage/restructuredtext/"
            "basics.html",
        ),
        (3, "https://example.com/"),
        (4, "https://httpbin.org/"),
        (5, "https://example.com/"),
        (6, "https://github.com/ftnext/sphinx-new-tab-link"),
    ],
    ids=[
        "url_only_line",
        "inline_external_link",
        "refer_external_link_target",
        "embed_external_link_with_target_definition",
        "embed_anonymous_external_link",
        "refer_embedded_external_link_target_again",
        "refer_anonymous_external_link_target",
    ],
)
@pytest.mark.sphinx("singlehtml", testroot="default")
def test_should_open_new_tab(
    app: SphinxTestApp,
    status: StringIO,
    warning: StringIO,
    index: int,
    expected_url: str,
):
    app.build()
    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[index]
    assert ref["href"] == expected_url
    assert "external" in ref["class"]
    assert ref["target"] == "_blank"
    assert ref["rel"] == ["noopener", "noreferrer"]


@pytest.mark.sphinx("singlehtml", testroot="default")
def test_internal_link_should_not_open_new_tab(
    app: SphinxTestApp, status: StringIO, warning: StringIO
):
    app.build()
    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[-1]
    assert "internal" in ref["class"]
    assert "target" not in ref.attrs
    assert "rel" not in ref.attrs
