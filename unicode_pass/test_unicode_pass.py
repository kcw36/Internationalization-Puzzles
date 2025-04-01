# pylint: skip-file

from unicode_pass import get_valid_passwords


def test_get_valid_passwords():
    assert 2 == get_valid_passwords(
        ['d9Ō', 'uwI.E9GvrnWļbzO', 'ž-2á', 'Ģ952W*F4', '?O6JQf', 'xi~Rťfsa', 'r_j4XcHŔB', '71äĜ3'])
