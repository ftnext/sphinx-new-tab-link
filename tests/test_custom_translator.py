from pathlib import Path

import pytest

from .helpers import assert_reference_attributes, extract_references


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
