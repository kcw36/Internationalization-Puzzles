"""Calculate number of valid passwords are present in list of passwords"""

from os import path
from re import search


def get_valid_passwords(passwords: list[str]) -> int:
    """Return number of valid passwords in list"""
    count = 0
    for p in passwords:
        if check_valid(p):
            count += 1
    return count


def check_valid(word: str) -> bool:
    """Return true if word is valid"""
    if not 12 >= len(word) >= 4:
        return False
    if not has_digit(word):
        return False
    if word.lower() == word:
        return False
    if word.upper() == word:
        return False
    if not has_unicode_non_standard(word):
        return False
    return True


def has_digit(word: str) -> bool:
    """Return true if digit in word"""
    return True if search(r"\d", word) else False


def has_unicode_non_standard(word: str) -> bool:
    """Return true if no standard ascii char in word"""
    return True if search(r"[^\u0000-\u007F]", word) else False


def get_list_from_txt(path_to_file: str) -> list[str]:
    """Return list of signals from text data"""
    absolute_path = path.dirname(__file__)
    relative_path = f"{absolute_path}/{path_to_file}"
    with open(relative_path, "r", encoding="utf-8") as f:
        lines = f.read()
    return lines.split("\n")


if __name__ == "__main__":
    print(get_valid_passwords(get_list_from_txt("input.txt")))
