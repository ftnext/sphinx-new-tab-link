from io import StringIO

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.parametrize(
    "index,expected_url",
    [(0, "https://example.com/"), (1, "http://abehiroshi.la.coocan.jp")],
    ids=["markup_external_link", "raw_external_link"],
)
@pytest.mark.sphinx("html", testroot="default")
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


@pytest.mark.sphinx("html", testroot="default")
def test_internal_link_should_not_open_new_tab(
    app: SphinxTestApp, status: StringIO, warning: StringIO
):
    app.build()
    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[2]
    assert "internal" in ref["class"]
    assert "target" not in ref.attrs
    assert "rel" not in ref.attrs
