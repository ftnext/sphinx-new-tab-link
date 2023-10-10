import shutil

import pytest
from bs4 import BeautifulSoup


@pytest.mark.parametrize("builder", ["html", "singlehtml", "dirhtml"])
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
def test_should_open_new_tab(
    make_app,
    sphinx_test_tempdir: str,
    rootdir: str,
    builder: str,
    index: int,
    expected_url: str,
):
    testroot = "default"
    srcdir = sphinx_test_tempdir / testroot
    if not srcdir.exists():
        testroot_path = rootdir / f"test-{testroot}"
        shutil.copytree(testroot_path, srcdir)

    app = make_app(builder, srcdir=srcdir)
    app.build()

    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[index]
    assert ref["href"] == expected_url
    assert "external" in ref["class"]
    assert ref["target"] == "_blank"
    assert ref["rel"] == ["noopener", "noreferrer"]


@pytest.mark.parametrize("builder", ["html", "singlehtml", "dirhtml"])
def test_internal_link_should_not_open_new_tab(
    make_app, sphinx_test_tempdir: str, rootdir: str, builder: str
):
    testroot = "default"
    srcdir = sphinx_test_tempdir / testroot
    if not srcdir.exists():
        testroot_path = rootdir / f"test-{testroot}"
        shutil.copytree(testroot_path, srcdir)

    app = make_app(builder, srcdir=srcdir)
    app.build()

    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[-1]
    assert "internal" in ref["class"]
    assert "target" not in ref.attrs
    assert "rel" not in ref.attrs
