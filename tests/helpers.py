import shutil
from pathlib import Path

from bs4 import BeautifulSoup


def prepare_files(test_root: Path, test_tempdir: Path) -> None:
    if not test_tempdir.exists():
        shutil.copytree(test_root, test_tempdir)


def extract_references(html_path: Path):
    contents = html_path.read_text()
    soup = BeautifulSoup(contents, "html.parser")
    return soup.find_all("a", {"class": "reference"})


def assert_reference_is_external(reference, expected_url: str) -> None:
    assert reference["href"] == expected_url
    assert_reference_attributes(reference)


def assert_reference_attributes(reference) -> None:
    assert "external" in reference["class"]
    assert reference["target"] == "_blank"
    assert reference["rel"] == ["noopener", "noreferrer"]
