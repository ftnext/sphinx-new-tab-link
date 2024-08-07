from pathlib import Path

import pytest

from .helpers import (
    assert_reference_is_external,
    extract_references,
    prepare_files,
)


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
    prepare_files(rootdir / f"test-{directory_name}", srcdir)

    return srcdir


@pytest.fixture
def built_html_path(make_app, builder: str, prepared_srcdir: Path) -> Path:
    app = make_app(builder, srcdir=prepared_srcdir)
    app.build()

    return app.outdir / "index.html"


def test_see_external_link_icon(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    ref = references[0]
    assert ref.text == "https://pypi.org/project/sphinx-new-tab-link/ "
    assert ref.svg
    assert_reference_is_external(
        ref, "https://pypi.org/project/sphinx-new-tab-link/"
    )


def test_can_see_icon_with_image_directive_target(
    built_html_path: Path,
) -> None:
    # https://github.com/ftnext/sphinx-new-tab-link/issues/16
    references = extract_references(built_html_path)

    ref = references[1]
    assert_reference_is_external(
        ref,
        "https://www.flickr.com/photos/pyconjp/48743997848/"
        "in/album-72157710870622516/",
    )
    assert ref.img
    assert ref.svg


def test_can_see_icon_with_figure_directive_target(built_html_path) -> None:
    references = extract_references(built_html_path)

    ref = references[2]
    assert_reference_is_external(
        ref,
        "https://www.flickr.com/photos/pyconjp/48818171768/"
        "in/album-72157710870622516/",
    )
    assert ref.img
    assert ref.svg
