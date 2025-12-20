from collections import Counter
from lib.regex import parse_numbers
from itertools import chain, product
from more_itertools import powerset
from functools import cache


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        end_node, *buttons, joltage_requirements = line.split(" ")

        indicators = [(1 if char == "#" else 0) for char in end_node[1:-1]]
        buttons = [parse_numbers(button) for button in buttons]
        joltage_requirements = parse_numbers(joltage_requirements, cast_as=tuple)

        yield indicators, buttons, joltage_requirements


def get_button_combination(indicators: list[int], buttons: list[list[int]]):
    for button_subset in powerset(buttons):
        c = Counter(chain(*button_subset))

        if all(c[i] % 2 == n for (i, n) in enumerate(indicators)):
            len(button_subset)


def solve_a(input_string: str):
    return sum(
        get_button_combination(indicators, buttons)[1]
        for indicators, buttons, _ in parse_input(input_string)
    )


def get_by_parity(buttons: list[list[int]], length: int):
    parity_costs = {p: [] for p in product([0, 1], repeat=length)}

    for button_subset in powerset(buttons):
        c = Counter(chain(*button_subset))

        parity = tuple(c[i] % 2 for i in range(length))

        parity_costs[parity].append((c, len(button_subset)))

    return parity_costs


def solve_b(input_string: str):
    total = 0

    for _, buttons, joltage_requirements in parse_input(input_string):
        parity_costs = get_by_parity(buttons, len(joltage_requirements))

        @cache
        def get_joltage_requirements(*joltage_requirements: int):
            min_presses = 1_000_000

            if all(n == 0 for n in joltage_requirements):
                return 0

            if any(n < 0 for n in joltage_requirements):
                return min_presses

            parity = tuple(n % 2 for n in joltage_requirements)

            for c, num_presses in parity_costs[parity]:
                remaining_joltage_requirements = [
                    (n - c[i]) // 2 for (i, n) in enumerate(joltage_requirements)
                ]

                min_presses = min(
                    min_presses,
                    2 * get_joltage_requirements(*remaining_joltage_requirements)
                    + num_presses,
                )

            return min_presses

        total += get_joltage_requirements(*joltage_requirements)

    return total
