from lib.regex import parse_numbers
from fractions import Fraction


def parse_input(input_string: str, offset=0):
    for block in input_string.split("\n\n"):
        a, b, price = [parse_numbers(line) for line in block.split("\n")]

        price[0] += offset
        price[1] += offset

        yield a, b, price


def solve_a(input_string: str, offset=0):
    machines = parse_input(input_string, offset)
    num_tokens = 0

    for a, b, price in machines:
        # We need to solve for n, m:
        #
        # n * a + m * b = price
        #
        # Which is a matrix equation that has a unique solution, if the determinant is non-zero

        determinant = a[0] * b[1] - b[0] * a[1]

        if determinant == 0:
            continue

        n = Fraction(1, determinant) * (b[1] * price[0] - b[0] * price[1])
        m = Fraction(1, determinant) * (a[0] * price[1] - a[1] * price[0])

        if n.is_integer() and m.is_integer():
            num_tokens += int(n * 3 + m)

    return num_tokens


def solve_b(input_string: str):
    return solve_a(input_string, offset=10000000000000)
