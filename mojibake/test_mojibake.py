# pylint: skip-file

from mojibake.mojibake import complete_crossword


def test_complete_crossword(test_mojibake):
    degarbled, crossword = test_mojibake
    assert 50 == complete_crossword(degarbled, crossword)
