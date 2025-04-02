# pylint: skip-file

import pytest
from world_trip import get_dicts_from_txt


@pytest.fixture
def test_input():
    return get_dicts_from_txt("test_input.txt")
