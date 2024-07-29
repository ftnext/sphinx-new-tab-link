import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def parsed_built_html(
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
    return BeautifulSoup(html, "html.parser")


def assert_is_external(reference, expected_url: str) -> None:
    assert reference["href"] == expected_url
    assert reference["target"] == "_blank"
    assert reference["rel"] == ["noopener", "noreferrer"]


def test_see_external_link_icon(parsed_built_html):
    references = parsed_built_html.find_all("a", {"class": "reference"})

    ref = references[0]
    assert ref.text == "https://pypi.org/project/sphinx-new-tab-link/ "
    assert ref.svg
    assert_is_external(ref, "https://pypi.org/project/sphinx-new-tab-link/")


def test_external_link_icon_as_image_target(parsed_built_html):
    # https://github.com/ftnext/sphinx-new-tab-link/issues/16
    references = parsed_built_html.find_all("a", {"class": "reference"})

    ref = references[1]
    assert_is_external(
        ref,
        "https://www.flickr.com/photos/pyconjp/48743997848/"
        "in/album-72157710870622516/",
    )
    assert ref.img
    assert ref.svg
