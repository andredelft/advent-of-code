TEST_INPUT = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


def solve_a(input_string=TEST_INPUT):
    for i in range(4, len(input_string)):
        if len(set(input_string[i - 4 : i])) == 4:
            return i


def solve_b(input_string=TEST_INPUT):
    for i in range(14, len(input_string)):
        if len(set(input_string[i - 14 : i])) == 14:
            return i
