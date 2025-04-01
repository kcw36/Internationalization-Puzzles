"""Calculate number of valid passwords are present in list of passwords"""

from os import path


def get_valid_passwords(passwords: list[str]) -> int:
    """Return number of valid passwords in list"""
    count = 0
    return count


def get_list_from_txt(path_to_file: str) -> list[str]:
    """Return list of signals from text data"""
    absolute_path = path.dirname(__file__)
    relative_path = f"{absolute_path}/{path_to_file}"
    with open(relative_path, "r", encoding="utf-8") as f:
        lines = f.read()
    return lines.split("\n")


if __name__ == "__main__":
    print(get_valid_passwords(get_list_from_txt("input.txt")))
