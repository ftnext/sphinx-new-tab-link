from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from .helpers import assert_reference_is_external, extract_references

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture(params=["html", "singlehtml", "dirhtml"])
def builder(request) -> str:
    return request.param


@pytest.fixture
def directory_name() -> str:
    return "default"


@pytest.mark.parametrize(
    "index,expected_url",
    [
        (0, "http://abehiroshi.la.coocan.jp"),
        (1, "https://pypi.org/project/sphinx-new-tab-link/"),
        (
            2,
            "https://www.sphinx-doc.org/en/master/usage/restructuredtext/"
            "basics.html",
        ),
        (3, "https://example.com/"),
        (4, "https://httpbin.org/"),
        (5, "https://example.com/"),
        (6, "https://github.com/ftnext/sphinx-new-tab-link"),
        (
            7,
            "https://www.flickr.com/photos/pyconjp/48743997848/in/album-72157710870622516/",  # NOQA: E501
        ),
    ],
    ids=[
        "url_only_line",
        "inline_external_link",
        "refer_external_link_target",
        "embed_external_link_with_target_definition",
        "embed_anonymous_external_link",
        "refer_embedded_external_link_target_again",
        "refer_anonymous_external_link_target",
        "image_directive_target",
    ],
)
def test_should_open_new_tab(
    built_html_path: Path,
    index: int,
    expected_url: str,
) -> None:
    references = extract_references(built_html_path)

    assert_reference_is_external(references[index], expected_url)


def test_internal_link_should_not_open_new_tab(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    ref = references[-1]
    assert "internal" in ref["class"]
    assert "target" not in ref.attrs
    assert "rel" not in ref.attrs
