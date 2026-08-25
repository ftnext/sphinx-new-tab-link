from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def builder() -> str:
    return "html"


@pytest.fixture
def directory_name() -> str:
    return "default"


def test_image_link_stylesheet_is_included(built_html_path: Path) -> None:
    contents = built_html_path.read_text()
    soup = BeautifulSoup(contents, "html.parser")

    stylesheet = soup.select_one(
        'link[href^="_static/sphinx-new-tab-link.css"]'
    )

    assert stylesheet is not None


def test_image_link_stylesheet_is_built(built_html_path: Path) -> None:
    stylesheet_path = (
        built_html_path.parent / "_static" / "sphinx-new-tab-link.css"
    )

    contents = stylesheet_path.read_text()

    assert "a.reference.external.image-reference:hover img" in contents
    assert "a.reference.external.image-reference:focus-visible img" in contents
    assert "filter: brightness(1.1)" in contents
