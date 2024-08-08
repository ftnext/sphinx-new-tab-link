from pathlib import Path

from bs4 import BeautifulSoup


def extract_references(html_path: Path):
    contents = html_path.read_text()
    soup = BeautifulSoup(contents, "html.parser")
    return soup.find_all("a", {"class": "reference"})
