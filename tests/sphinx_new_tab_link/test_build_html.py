from io import StringIO

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="default")
def test_markup_external_link_should_open_new_tab(
    app: SphinxTestApp, status: StringIO, warning: StringIO
):
    app.build()
    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[0]
    assert ref["href"] == "https://example.com/"
    assert "external" in ref["class"]
    assert ref["target"] == "_blank"
    assert ref["rel"] == ["noopener", "noreferrer"]


@pytest.mark.sphinx("html", testroot="default")
def test_raw_external_link_should_open_new_tab(
    app: SphinxTestApp, status: StringIO, warning: StringIO
):
    app.build()
    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[1]
    assert ref["href"] == "http://abehiroshi.la.coocan.jp"
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
