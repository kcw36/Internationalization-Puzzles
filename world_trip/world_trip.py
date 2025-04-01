"""Calculate travel itinery travel time"""

from os import path
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

def get_travel_time(itinery: list[dict]) -> int:
    """Return travel minutes from itinery list"""
    travel_time = 0
    for leg in itinery:
        print(leg["arr_date"], leg["dep_date"])
        arrival = datetime.strptime(leg["arr_date"], r"%b %j, %Y, %H:%M").replace(tzinfo=ZoneInfo(leg["arr_location"]))
        departure = datetime.strptime(leg["dep_date"], r"%b %j, %Y, %H:%M").replace(tzinfo=ZoneInfo(leg["dep_location"]))
        print(arrival, departure)
        delta = arrival - departure
        print(delta)
        travel_time += delta.total_seconds() / 60
    return travel_time

def get_dicts_from_txt(path_to_file: str) -> list[dict]:
    """Return list of dicts of travel legs from text data"""
    absolute_path = path.dirname(__file__)
    relative_path = f"{absolute_path}/{path_to_file}"
    with open(relative_path, "r", encoding="utf-8") as f:
        lines = f.read()
    full_lines = [l for l in lines.split("\n") if l != '']
    itinery = []
    for i in range(0, len(full_lines), 2):
        departure = full_lines[i].split()
        arrival = full_lines[i+1].split()
        leg = {"dep_location": departure[1],
               "dep_date": " ".join(departure[2:]),
               "arr_location": arrival[1],
               "arr_date": " ".join(arrival[2:])}
        itinery.append(leg)
    return itinery


if __name__ == "__main__":
    #print(get_travel_time(get_dicts_from_txt("input.txt")))
    print(get_dicts_from_txt("input.txt"))
