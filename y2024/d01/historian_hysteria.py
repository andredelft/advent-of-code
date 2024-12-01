from lib.regex import parse_numbers
from itertools import batched
from collections import Counter


def parse_input(input_string: str):
    return zip(*batched(parse_numbers(input_string), 2))


def solve_a(input_string: str):
    left_list, right_list = parse_input(input_string)

    return sum(abs(n1 - n2) for (n1, n2) in zip(sorted(left_list), sorted(right_list)))


def solve_b(input_string: str):
    left_list, right_list = parse_input(input_string)

    right_counter = Counter(right_list)

    return sum(n * right_counter[n] for n in left_list)
