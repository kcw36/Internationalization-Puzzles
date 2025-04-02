# pylint: skip-file

from step_in.step_in import get_poos_hit


def test_get_poos_hit(test_park):
    assert 2 == get_poos_hit(test_park)
