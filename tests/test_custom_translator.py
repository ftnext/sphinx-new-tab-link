import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup


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
    html = built_html_path.read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    assert len(references) == 1
    ref = references[0]
    assert ref["target"] == "_blank"
    assert ref["rel"] == ["noopener", "noreferrer"]
