from lib.regex import parse_numbers
from lib.geometry import square_area
from itertools import combinations


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        print(line)
        yield parse_numbers(line, cast_as=tuple)


def solve_a(input_string: str):
    coords = parse_input(input_string)
    return max(square_area(*pair) for pair in combinations(coords, 2))


def solve_b(input_string: str):
    pass
