# pylint: skip-file

import pytest
from length_limits import get_message_cost

def test_get_message_cost_valid(test_message):
    assert get_message_cost(test_message) == 31