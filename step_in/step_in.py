"""Calculate number of poo hits in a park."""

from os import path


def get_poo_hit(park: list[list]) -> int:
    """Return number of poos hit in park."""
    x = 0
    y = 0
    poo_count = 0
    columns = len(park[0])
    while y < len(park):
        if park[y][x] == "0x01f4a9":
            poo_count += 1
        x += 2
        if x >= columns:
            x = x - columns
        y += 1
    return poo_count


def get_park_from_txt(path_to_file: str) -> list[list]:
    """Return park matrix from txt."""
    absolute_path = path.dirname(__file__)
    rel_path = f"{absolute_path}/{path_to_file}"
    park = []
    with open(rel_path, "r", encoding="utf-8") as f:
        # removes the \n char from line end
        data = f.read().splitlines()
        for line in data:
            unicode_chars = [format(ord(c), '#08x') for c in line]
            park.append(unicode_chars)
    return park


if __name__ == "__main__":
    park = get_park_from_txt("input.txt")
    print(get_poo_hit(park))
