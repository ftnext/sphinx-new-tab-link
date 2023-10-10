import shutil

import pytest
from bs4 import BeautifulSoup


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
