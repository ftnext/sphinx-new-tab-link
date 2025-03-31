from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from .helpers import (
    assert_reference_is_external_with_referrer,
    extract_references,
)

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def builder() -> str:
    return "html"


@pytest.fixture
def directory_name() -> str:
    return "enable-referrer"


def test_should_enable_referrer_when_configured(built_html_path: Path) -> None:
    references = extract_references(built_html_path)

    assert_reference_is_external_with_referrer(
        references[0], "https://httpbin.org/"
    )
