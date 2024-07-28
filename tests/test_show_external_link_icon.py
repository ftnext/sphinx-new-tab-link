import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup


def test_see_external_link_icon(
    make_app,
    sphinx_test_tempdir: Path,
    rootdir: Path,
):
    srcdir = sphinx_test_tempdir / "external-link-icon"
    if not srcdir.exists():
        testroot_path = rootdir / "test-external-link-icon"
        shutil.copytree(testroot_path, srcdir)

    app = make_app("html", srcdir=srcdir)
    app.build()

    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[0]
    assert ref.text == "https://pypi.org/project/sphinx-new-tab-link/ "
    assert ref.svg
    assert ref["href"] == "https://pypi.org/project/sphinx-new-tab-link/"
    assert ref["target"] == "_blank"
    assert ref["rel"] == ["noopener", "noreferrer"]


@pytest.mark.skip("WIP issue #16")
def test_external_link_icon_as_image_target(
    make_app, sphinx_test_tempdir: Path, rootdir: Path
):
    srcdir = sphinx_test_tempdir / "external-link-icon"
    if not srcdir.exists():
        testroot_path = rootdir / "test-external-link-icon"
        shutil.copytree(testroot_path, srcdir)

    app = make_app("html", srcdir=srcdir)
    app.build()

    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    ref = references[1]
    assert (
        ref["href"]
        == "https://www.flickr.com/photos/pyconjp/48743997848/in/album-72157710870622516/"  # NOQA: E501
    )
    assert ref["target"] == "_blank"
    assert ref["rel"] == ["noopener", "noreferrer"]
    assert ref.img
