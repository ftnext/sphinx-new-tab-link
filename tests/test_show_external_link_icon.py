import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def parsed_built_html(
    request,
    make_app,
    sphinx_test_tempdir: Path,
    rootdir: Path,
):
    marker = request.node.get_closest_marker("sphinx_build_in_tempdir")
    if marker is None:
        raise RuntimeError("Mark as `sphinx_build_in_tempdir`")
    directory_name = marker.args[0]

    srcdir = sphinx_test_tempdir / directory_name
    if not srcdir.exists():
        testroot_path = rootdir / f"test-{directory_name}"
        shutil.copytree(testroot_path, srcdir)

    app = make_app("html", srcdir=srcdir)
    app.build()

    html = (app.outdir / "index.html").read_text()
    return BeautifulSoup(html, "html.parser")


def assert_is_external(reference, expected_url: str) -> None:
    assert reference["href"] == expected_url
    assert reference["target"] == "_blank"
    assert reference["rel"] == ["noopener", "noreferrer"]


@pytest.mark.sphinx_build_in_tempdir("external-link-icon")
def test_see_external_link_icon(parsed_built_html):
    references = parsed_built_html.find_all("a", {"class": "reference"})

    ref = references[0]
    assert ref.text == "https://pypi.org/project/sphinx-new-tab-link/ "
    assert ref.svg
    assert_is_external(ref, "https://pypi.org/project/sphinx-new-tab-link/")


@pytest.mark.sphinx_build_in_tempdir("external-link-icon")
def test_can_see_icon_with_image_directive_target(parsed_built_html):
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


@pytest.mark.sphinx_build_in_tempdir("external-link-icon")
def test_can_see_icon_with_figure_directive_target(parsed_built_html):
    references = parsed_built_html.find_all("a", {"class": "reference"})

    ref = references[2]
    assert_is_external(
        ref,
        "https://www.flickr.com/photos/pyconjp/48818171768/"
        "in/album-72157710870622516/",
    )
    assert ref.img
    assert ref.svg
