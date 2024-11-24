import math
from copy import deepcopy


class InvalidSnailfishNumber(Exception):
    def __init__(self, value="Invalid snailfish number", *args, **kwargs):
        super().__init__(value, *args, **kwargs)


def _validate_snailfish_number(value):
    if isinstance(value, list) and len(value) == 2:
        for child in value:
            if isinstance(child, list):
                _validate_snailfish_number(child)
            elif not isinstance(child, int):
                raise InvalidSnailfishNumber
    else:
        raise InvalidSnailfishNumber


def _iter_over_snailfish_number(lst, trail=[]):
    for i, value in enumerate(lst):
        if isinstance(value, list):
            for value in _iter_over_snailfish_number(value, trail + [i]):
                yield value
        else:
            yield value, trail + [i]


def _snailfish_number_quantity(value):
    quantity = 0
    for i, child in enumerate(value):
        quantity_factor = 2 if i else 3
        if isinstance(child, int):
            quantity += quantity_factor * child
        else:  # isisntance(child, list)
            quantity += quantity_factor * _snailfish_number_quantity(child)
    return quantity


def _find_next_pair_of_level(level, value, trail=[]):
    for i, child in enumerate(value):
        if isinstance(child, list):
            if level == 1:
                # Make sure we get the deepest pair
                deepest_trail = []
                for _, _trail in _iter_over_snailfish_number(value):
                    if len(_trail) > len(deepest_trail):
                        deepest_trail = _trail
                deepest_trail.pop(-1)  # Found the deepest int, so go one level higher
                return trail + deepest_trail
            else:
                child_trail = _find_next_pair_of_level(level - 1, child, trail + [i])
                if child_trail:
                    return child_trail


def _find_next_value_geq(n, value):
    return next(
        (trail for value, trail in _iter_over_snailfish_number(value) if value >= n),
        None,
    )


class SnailfishNumber:
    def __init__(self, value):
        _validate_snailfish_number(value)
        self.__value__ = value

    def explode(self, trail: list):
        value = self[trail]
        if not isinstance(value, list):
            raise TypeError("Explode function called on an integer")
        left_value, right_value = value

        left_neighbour_index = next(
            (
                len(trail) - (i + 1)
                for i, trail_value in enumerate(reversed(trail))
                if trail_value == 1
            ),
            None,
        )
        if left_neighbour_index != None:
            neighbour_trail = trail[:left_neighbour_index] + [0]
            while isinstance(self[neighbour_trail], list):
                neighbour_trail.append(1)
            self[neighbour_trail] += left_value

        right_neighbour_index = next(
            (
                len(trail) - (i + 1)
                for i, trail_value in enumerate(reversed(trail))
                if trail_value == 0
            ),
            None,
        )
        if right_neighbour_index != None:
            neighbour_trail = trail[:right_neighbour_index] + [1]
            while isinstance(self[neighbour_trail], list):
                neighbour_trail.append(0)
            self[neighbour_trail] += right_value

        self[trail] = 0

    def split(self, trail: list):
        value = self[trail]
        if not isinstance(value, int):
            raise TypeError("Split function called on a list")
        self[trail] = [math.floor(value / 2), math.ceil(value / 2)]

    def reduce(self):
        reduced = False
        while not reduced:
            trail_to_deep_pair = _find_next_pair_of_level(4, self.__value__)
            if trail_to_deep_pair:
                self.explode(trail_to_deep_pair)
                continue

            trail_to_high_number = _find_next_value_geq(10, self.__value__)
            if trail_to_high_number:
                self.split(trail_to_high_number)
                continue

            reduced = True

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__class__(self.__value__[key])
        elif isinstance(key, tuple | list):
            value = self.__value__
            for i in key:
                value = value[i]
            return value

    def __setitem__(self, key, item):
        if isinstance(key, int):
            self.__value__[key] = item
        elif isinstance(key, tuple | list):
            value = self.__value__
            for i in key[:-1]:
                value = value[i]

            value[key[-1]] = item

    def _iter_with_trail(self):
        for value, trail in _iter_over_snailfish_number(self.__value__):
            yield value, trail

    def __iter__(self):
        for value, _ in _iter_over_snailfish_number(self.__value__):
            yield value

    def __str__(self):
        return str(self.__value__)

    def __repr__(self):
        return f"<SnailfishNumber {self}>"

    def __add__(self, other):
        if not isinstance(other, SnailfishNumber):
            raise TypeError("Only two snailfish numbers can be added together")

        snailfish_sum = self.__class__(
            [deepcopy(self.__value__), deepcopy(other.__value__)]
        )
        snailfish_sum.reduce()
        return snailfish_sum

    def __len__(self):
        return _snailfish_number_quantity(self.__value__)
