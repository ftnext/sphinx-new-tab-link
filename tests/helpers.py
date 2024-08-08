from pathlib import Path

from bs4 import BeautifulSoup


def extract_references(html_path: Path):
    contents = html_path.read_text()
    soup = BeautifulSoup(contents, "html.parser")
    return soup.find_all("a", {"class": "reference"})


def assert_reference_is_external(reference, expected_url: str) -> None:
    assert reference["href"] == expected_url
    assert "external" in reference["class"]
    assert reference["target"] == "_blank"
    assert reference["rel"] == ["noopener", "noreferrer"]
