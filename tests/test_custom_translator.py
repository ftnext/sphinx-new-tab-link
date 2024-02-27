import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.mark.parametrize("testroot", ["method-assignment", "dynamic-class"])
def test_should_open_new_tab(
    make_app, sphinx_test_tempdir: Path, rootdir: str, testroot: str
):
    srcdir = sphinx_test_tempdir / testroot
    if not srcdir.exists():
        testroot_path = rootdir / f"test-{testroot}"
        shutil.copytree(testroot_path, srcdir)

    app = make_app("html", srcdir=srcdir)
    app.build()

    html = (app.outdir / "index.html").read_text()
    soup = BeautifulSoup(html, "html.parser")
    references = soup.find_all("a", {"class": "reference"})

    assert len(references) == 1
    ref = references[0]
    assert ref["target"] == "_blank"
    assert ref["rel"] == ["noopener", "noreferrer"]
