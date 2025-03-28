# pylint: skip-file

import pytest

from grav_waves import get_recordings


def test_get_recordings_valid(test_recordings):
    assert get_recordings(test_recordings) == ["2019-06-05T12:15:00+00:00"]
