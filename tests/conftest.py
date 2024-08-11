from pathlib import Path

import pytest

from .helpers import prepare_files

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


@pytest.fixture(scope="session")
def rootdir() -> Path:
    return Path(__file__).parent / "roots"


@pytest.fixture
def builder() -> str:
    raise NotImplementedError("Define `builder` fixture in each test module")


@pytest.fixture()
def directory_name() -> str:
    raise NotImplementedError(
        "Define `directory_name` fixture in each test module"
    )


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
