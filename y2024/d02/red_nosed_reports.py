from lib.regex import parse_numbers
from itertools import pairwise


def parse_input(input_string: str):
    return [parse_numbers(line) for line in input_string.split("\n")]


def check_is_safe(report: list[int]):
    differences = [m - n for (n, m) in pairwise(report)]

    is_not_too_large = all((1 <= abs(d) <= 3) for d in differences)

    if not is_not_too_large:
        return False

    all_decreasing = all(d < 0 for d in differences)
    all_increasing = False if all_decreasing else all(d > 0 for d in differences)

    return all_decreasing or all_increasing


def solve_a(input_string: str):
    reports = parse_input(input_string)

    return sum(check_is_safe(report) for report in reports)


def solve_b(input_string: str):
    reports = parse_input(input_string)
    num_safe = 0

    for report in reports:
        is_safe = check_is_safe(report)

        pop_index = 0
        while (not is_safe) and pop_index < len(report):
            dampened_report = report.copy()
            dampened_report.pop(pop_index)

            pop_index += 1
            is_safe = check_is_safe(dampened_report)

        if is_safe:
            num_safe += 1

    return num_safe
