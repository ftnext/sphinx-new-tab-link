from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from pathlib import Path


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
    assert reference["rel"] == ["noreferrer"]


def assert_reference_is_external_with_icon(
    reference, expected_url: str
) -> None:
    assert_reference_is_external(reference, expected_url)
    assert reference.svg


def assert_reference_is_not_external(reference) -> None:
    assert "internal" in reference["class"]  # not external == internal
    assert "target" not in reference.attrs
    assert "rel" not in reference.attrs
