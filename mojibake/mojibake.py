"""Some doctsring"""


from os import path


def get_inputs_from_txt(target_file: str) -> tuple[list[str], list[str]]:
    """Return dictionary of words and crossword to solve from txt file"""
    directory_path = path.dirname(__file__)
    with open(f"{directory_path}/{target_file}", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        i = lines.index("")
    return (lines[:i], lines[i+1:])


def degarble():
    ...


def complete_crossword():
    ...


if __name__ == "__main__":
    words, crossword = get_inputs_from_txt("test_input.txt")
