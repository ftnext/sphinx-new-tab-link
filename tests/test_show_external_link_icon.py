from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from .helpers import assert_reference_is_external_with_icon, extract_references

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def builder() -> str:
    return "html"


@pytest.fixture
def directory_name() -> str:
    return "external-link-icon"


def test_see_external_link_icon(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    ref = references[0]
    assert ref.text == "https://pypi.org/project/sphinx-new-tab-link/ "
    assert_reference_is_external_with_icon(
        ref, "https://pypi.org/project/sphinx-new-tab-link/"
    )


def test_can_see_icon_with_image_directive_target(
    built_html_path: Path,
) -> None:
    # https://github.com/ftnext/sphinx-new-tab-link/issues/16
    references = extract_references(built_html_path)

    ref = references[1]
    assert_reference_is_external_with_icon(
        ref,
        "https://www.flickr.com/photos/pyconjp/48743997848/"
        "in/album-72157710870622516/",
    )
    assert ref.img


def test_can_see_icon_with_figure_directive_target(
    built_html_path: Path,
) -> None:
    references = extract_references(built_html_path)

    ref = references[2]
    assert_reference_is_external_with_icon(
        ref,
        "https://www.flickr.com/photos/pyconjp/48818171768/"
        "in/album-72157710870622516/",
    )
    assert ref.img
