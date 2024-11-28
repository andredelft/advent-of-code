from lib.regex import parse_numbers
from itertools import pairwise
from collections import Counter


def parse_input(input_string: str):
    return parse_numbers(input_string)


def is_increasing(pw_str: str):
    return all(digit <= next_digit for (digit, next_digit) in pairwise(pw_str))


def has_double_char(pw_str: str):
    return len(set(pw_str)) < len(pw_str)


def has_strictly_double_char(pw_str: str):
    return 2 in Counter(pw_str).values()


def solve_a(input_string):
    pw_max, pw_min = parse_input(input_string)

    num_passwords = 0
    for pw in range(pw_max, pw_min + 1):
        pw_str = str(pw)

        if is_increasing(pw_str) and has_double_char(pw_str):
            print(pw_str)
            num_passwords += 1

    return num_passwords


def solve_b(input_string):
    pw_max, pw_min = parse_input(input_string)

    num_passwords = 0
    for pw in range(pw_max, pw_min + 1):
        pw_str = str(pw)

        if is_increasing(pw_str) and has_strictly_double_char(pw_str):
            num_passwords += 1

    return num_passwords
