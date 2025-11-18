from itertools import combinations


def parse_input(input_string: str):
    return [int(n) for n in input_string.split("\n")]


def solve_a(input_string: str):
    numbers = parse_input(input_string)

    return next(n1 * n2 for (n1, n2) in combinations(numbers, 2) if n1 + n2 == 2020)


def solve_b(input_string: str):
    numbers = parse_input(input_string)

    return next(
        n1 * n2 * n3
        for (n1, n2, n3) in combinations(numbers, 3)
        if n1 + n2 + n3 == 2020
    )
