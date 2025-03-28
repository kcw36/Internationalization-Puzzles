"""Take message input and calculate cost for message"""

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
            

if __name__ == "__main__":
    message = input("Please input message to check: ")
    msg_cost = get_message_cost(message)