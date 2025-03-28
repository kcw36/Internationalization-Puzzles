"""Find instances of multiple recording from gravitational wave signals"""

from os import path
from datetime import datetime, timezone
from collections import Counter


def get_recordings(recordings: list[str]) -> list[str]:
    """Return list of signals that were repeated more than 4 times"""
    datetime_r = [datetime.strptime(r[:-3]+r[-2:], r"%Y-%m-%dT%H:%M:%S%z")
                  for r in recordings]
    adjusted_r = [d.astimezone(timezone.utc).strftime(
        r"%Y-%m-%dT%H:%M:%S%z") for d in datetime_r]
    count_r = Counter(adjusted_r)
    multi_signals = [sig[:-2]+":"+sig[-2:]
                     for sig, c in count_r.items() if c >= 4]
    return multi_signals


def get_list_from_txt(path_to_file: str) -> list[str]:
    """Return list of signals from text data"""
    absolute_path = path.dirname(__file__)
    relative_path = f"{absolute_path}/{path_to_file}"
    with open(relative_path, "r", encoding="utf-8") as f:
        lines = f.read()
    return lines.split("\n")


if __name__ == "__main__":
    print(get_recordings(get_list_from_txt("input.txt")))
