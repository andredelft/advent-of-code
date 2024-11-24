from .hand import Hand


def get_rank(hands_with_bidding: list[Hand, int]):
    sorted_hands_with_bidding = sorted(hands_with_bidding, key=lambda hwb: hwb[0])

    return sum(
        rank * bid for (rank, (_, bid)) in enumerate(sorted_hands_with_bidding, 1)
    )


def parse_input(input_string: str, with_jokers=False):
    for line in input_string.split("\n"):
        cards, bid = line.split(" ")
        yield Hand(cards, with_jokers), int(bid)


def solve_a(input_string: str):
    hands_with_bidding = parse_input(input_string)
    return get_rank(hands_with_bidding)


def solve_b(input_string: str):
    hands_with_bidding = parse_input(input_string, with_jokers=True)
    return get_rank(hands_with_bidding)
