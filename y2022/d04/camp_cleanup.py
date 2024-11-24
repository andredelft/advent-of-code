from lib.regex import parse_numbers
from collections.abc import Iterable

TEST_INPUT = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def parse_input(input_string):
    for line in input_string.split("\n"):
        a, b, c, d = parse_numbers(line)
        yield (a, b), (c, d)


def is_contained(first: tuple[int], second: tuple[int]) -> bool:
    """Check if the first range is contained in the second, or vice versa."""

    return (first[0] >= second[0] and first[1] <= second[1]) or (
        second[0] >= first[0] and second[1] <= first[1]
    )


def is_overlapping(first: tuple[int], second: tuple[int]) -> bool:
    """Check if ranges are overlapping."""

    return not (first[1] < second[0] or second[1] < first[0])


def part_a(input_string=TEST_INPUT):
    return sum(is_contained(*pair) for pair in parse_input(input_string))


def part_b(input_string=TEST_INPUT):
    return sum(is_overlapping(*pair) for pair in parse_input(input_string))
