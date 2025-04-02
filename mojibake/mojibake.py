"""Methods for solving puzzles with corrupted strings."""

from curses.ascii import isalpha
from os import path


def get_inputs_from_txt(target_file: str) -> tuple[list[str], list[str]]:
    """Return dictionary of words and crossword to solve from txt file."""
    directory_path = path.dirname(__file__)
    with open(f"{directory_path}/{target_file}", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        i = lines.index("")
    return (lines[:i], lines[i+1:])


def degarble(words: list[str]) -> list[str]:
    """Return degarbled version of word list."""
    for i, w in enumerate(words, start=1):
        if i % 3 == 0:
            words[i-1] = w.encode("latin_1").decode("utf-8")
        if i % 5 == 0:
            words[i-1] = w.encode("latin_1").decode("utf-8")
        if i % 15 == 0:
            words[i-1] = w.encode("latin_1").decode(
                "utf-8").encode("latin_1").decode("utf-8")
    return words


def complete_crossword(words: list[str], puzzle: list[str]) -> int:
    """Return complete puzzle using word list."""
    count = 0
    for cryptic in puzzle:
        cryptic = cryptic.lstrip()
        size = len(cryptic)
        key = {}
        for i, c in enumerate(cryptic):
            if c.isalpha():
                key["letter"] = c
                key["index"] = i
        new_words = [w for w in words if len(w) == size]
        for i, w in enumerate(new_words):
            if w[key["index"]] == key["letter"]:
                count += words.index(w)+1
    return count


if __name__ == "__main__":
    words, crossword = get_inputs_from_txt("input.txt")
    degarbled_words = degarble(words)
    print(degarbled_words)
    print(complete_crossword(degarbled_words, crossword))
