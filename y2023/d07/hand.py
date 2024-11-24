from functools import total_ordering
from collections import Counter


CARD_VALUE_MAP = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

CARD_VALUE_MAP_WITH_JOKERS = {
    **CARD_VALUE_MAP,
    "J": 1,
}


@total_ordering
class Hand(object):
    def __init__(self, cards_str: str, with_jokers=False):
        self.cards_str = cards_str
        self.cards = Counter(cards_str)

        if with_jokers:
            try:
                num_jokers = self.cards.pop("J")
            except KeyError:
                pass
            else:
                if num_jokers == 5:
                    # Reset hand, since there is no other card to turn the joker into
                    self.cards["J"] = 5
                elif num_jokers > 0:
                    most_common_card = self.cards.most_common(1)[0][0]
                    self.cards[most_common_card] += num_jokers

        card_value_map = CARD_VALUE_MAP_WITH_JOKERS if with_jokers else CARD_VALUE_MAP

        self.pairs = tuple(sorted(self.cards.values(), reverse=True))
        self.card_values = tuple(card_value_map[card] for card in self.cards_str)

    def __eq__(self, other):
        return self.card_values == other.card_values

    def __lt__(self, other):
        if self.pairs == other.pairs:
            return self.card_values < other.card_values

        return self.pairs < other.pairs

    def __str__(self):
        return self.cards_str

    def __repr__(self):
        return f"<Hand: {self}>"
