import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


@pytest.fixture(scope="session")
def rootdir() -> Path:
    return Path(__file__).parent / "roots"


def get_marker_value(request, marker_name: str):
    marker = request.node.get_closest_marker(marker_name)
    if marker is None:
        raise RuntimeError(f"Mark as `{marker_name}`")
    return marker.args[0]


@pytest.fixture
def parsed_built_html(
    request,
    make_app,
    sphinx_test_tempdir: Path,
    rootdir: Path,
):
    directory_name = get_marker_value(request, "sphinx_build_in_tempdir")

    srcdir = sphinx_test_tempdir / directory_name
    if not srcdir.exists():
        testroot_path = rootdir / f"test-{directory_name}"
        shutil.copytree(testroot_path, srcdir)

    app = make_app("html", srcdir=srcdir)
    app.build()

    html = (app.outdir / "index.html").read_text()
    return BeautifulSoup(html, "html.parser")
