"""Calculate number of poo hits in a park."""


from os import path


def get_poos_hit(park: list[list]) -> int:
    """Return number of poos hit in park."""


def get_park_from_txt(path_to_file: str) -> list[list]:
    """Return park matrix from txt."""
    absolute_path = path.dirname(__file__)
    rel_path = f"{absolute_path}/{path_to_file}"
    park = []
    with open(rel_path, "r", encoding="utf-8") as f:
        for line in f:
            unicode_chars = [format(ord(c), '#08x') for c in line]
            park.append(unicode_chars)
    return park


if __name__ == "__main__":
    print(get_park_from_txt("test_input.txt"))
