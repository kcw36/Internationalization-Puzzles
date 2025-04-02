# pylint: skip-file

from world_trip import get_travel_time


def test_get_travel_time(test_input):
    assert 3143 == get_travel_time(test_input)
