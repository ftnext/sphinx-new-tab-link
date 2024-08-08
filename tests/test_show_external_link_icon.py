import shutil
from pathlib import Path

import pytest

from .helpers import extract_references


@pytest.fixture
def builder() -> str:
    return "html"


@pytest.fixture()
def directory_name() -> str:
    return "external-link-icon"


@pytest.fixture
def prepared_srcdir(
    sphinx_test_tempdir: Path, rootdir: Path, directory_name: str
) -> Path:
    srcdir = sphinx_test_tempdir / directory_name
    if not srcdir.exists():
        testroot_path = rootdir / f"test-{directory_name}"
        shutil.copytree(testroot_path, srcdir)

    return srcdir


@pytest.fixture
def built_html_path(make_app, builder: str, prepared_srcdir: Path) -> Path:
    app = make_app(builder, srcdir=prepared_srcdir)
    app.build()

    return app.outdir / "index.html"


def assert_is_external(reference, expected_url: str) -> None:
    assert reference["href"] == expected_url
    assert reference["target"] == "_blank"
    assert reference["rel"] == ["noopener", "noreferrer"]


def test_see_external_link_icon(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    ref = references[0]
    assert ref.text == "https://pypi.org/project/sphinx-new-tab-link/ "
    assert ref.svg
    assert_is_external(ref, "https://pypi.org/project/sphinx-new-tab-link/")


@pytest.mark.sphinx_builder("html")
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


@pytest.mark.sphinx_builder("html")
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
