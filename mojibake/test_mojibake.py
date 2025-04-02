# pylint: skip-file

from mojibake import complete_crossword


def test_complete_crossword(crossword, degarbled):
    assert 50 == complete_crossword(crossword, degarbled)
