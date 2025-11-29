from collections import Counter
from itertools import pairwise
from functools import cache


def parse_input(input_string: str):
    numbers = sorted(int(n) for n in input_string.split("\n"))

    return [0, *numbers, numbers[-1] + 3]


def solve_a(input_string: str):
    joltage_ratings = parse_input(input_string)
    jolt_differences = Counter()

    for a, b in pairwise(joltage_ratings):
        jolt_differences[b - a] += 1

    return jolt_differences[1] * jolt_differences[3]


def solve_b(input_string: str):
    joltage_ratings = parse_input(input_string)

    @cache
    def num_arrangements(index: int = -1):
        index %= len(joltage_ratings)
        total_arrangements = 0

        if index == 0:
            return 1

        for i in range(1, 4):
            if index - i < 0:
                continue

            if joltage_ratings[index] - joltage_ratings[index - i] <= 3:
                total_arrangements += num_arrangements(index - i)

        return total_arrangements

    return num_arrangements()
