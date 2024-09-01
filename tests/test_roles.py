from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from .helpers import (
    assert_reference_is_external,
    assert_reference_is_external_with_icon,
    extract_references,
)

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def builder() -> str:
    return "html"


@pytest.fixture
def directory_name() -> str:
    return "roles"


def test_see_external_link_with_icon(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    ref = references[1]
    assert_reference_is_external_with_icon(ref, "https://httpbin.org/")
    assert ref.text == "httpbin "


def test_regression_1(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    ref = references[0]
    assert_reference_is_external(ref, "https://example.com/")
