import shutil
from pathlib import Path

import pytest

from .helpers import assert_reference_attributes, extract_references


@pytest.fixture
def builder() -> str:
    return "html"


@pytest.fixture(params=["method-assignment", "dynamic-class"])
def directory_name(request) -> str:
    return request.param


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


def test_should_open_new_tab(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    assert len(references) == 1
    assert_reference_attributes(references[0])
