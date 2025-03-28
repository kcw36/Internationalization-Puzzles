"""Take message input and calculate cost for message"""

import os

def get_message_cost(messages: list[str]) -> int:
    """Return message cost based on content"""
    cost = 0
    for m in messages:
        m_bytes = len(str.encode(m, 'utf-8'))
        m_char = len(m)
        if m_bytes <= 160 and m_char <= 140:
            cost += 13
        elif m_bytes <= 160:
            cost += 11
        elif m_char <= 140:
            cost += 7
    return cost


def get_list_from_txt(path_to_file: str) -> list[str]:
    """Return list of strings from txt file"""
    absolute_path = os.path.dirname(__file__)
    path = f"{absolute_path}/{path_to_file}"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text.split("\n")


if __name__ == "__main__":
    message = get_list_from_txt("input.txt")
    print(get_message_cost(message))
