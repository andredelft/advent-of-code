from lib.regex import parse_number

TEST_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def parse_input(input_string):
    return [
        [parse_number(n) for n in group.split("\n")]
        for group in input_string.split("\n\n")
    ]


def part_a(input_string=TEST_INPUT):
    groups = parse_input(input_string)

    return max([sum(group) for group in groups])


def part_b(input_string=TEST_INPUT):
    groups = parse_input(input_string)

    return sum(sorted([sum(group) for group in groups])[-3:])
