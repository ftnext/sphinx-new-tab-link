from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from .helpers import assert_reference_attributes, extract_references

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def builder() -> str:
    return "html"


@pytest.fixture(params=["method-assignment", "dynamic-class"])
def directory_name(request) -> str:
    return request.param


def test_should_open_new_tab(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    assert len(references) == 1
    assert_reference_attributes(references[0])
