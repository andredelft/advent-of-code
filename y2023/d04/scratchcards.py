import re
from math import floor
from collections import Counter

from lib.regex import parse_numbers


def parse_input(input_string: str):
    cards = []

    for line in input_string.split("\n"):
        _, winning_numbers, my_numbers = [
            set(parse_numbers(part)) for part in re.split(r"[\:\|]", line)
        ]
        cards.append((winning_numbers, my_numbers))
    return cards


def part_a(input_string: str):
    cards = parse_input(input_string)

    return sum(floor(2 ** (len(set.intersection(*nums)) - 1)) for nums in cards)


def part_b(input_string: str):
    cards = parse_input(input_string)
    wins = Counter()

    for card_number, (winning_numbers, my_numbers) in enumerate(cards, 1):
        num_cards = wins[card_number] + 1
        num_wins = len(my_numbers.intersection(winning_numbers))

        for i in range(num_wins):
            wins[card_number + (i + 1)] += num_cards

    return len(cards) + sum(wins.values())
