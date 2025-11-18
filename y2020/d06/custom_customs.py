from itertools import chain


def parse_input(input_string: str):
    return [line.split("\n") for line in input_string.split("\n\n")]


def solve_a(input_string: str):
    return sum(len(set().union(*group)) for group in parse_input(input_string))


def solve_b(input_string: str):
    return sum(
        len(set(group[0]).intersection(*group[1:]))
        for group in parse_input(input_string)
    )
