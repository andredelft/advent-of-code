from lib.regex import parse_numbers
from functools import cache


@cache
def blink(n: int, num_blinks: int):
    if num_blinks == 0:
        return 1

    if n == 0:
        return blink(1, num_blinks - 1)

    n_str = str(n)
    if len(n_str) % 2 == 0:
        middle_index = len(n_str) // 2
        n1, n2 = map(int, [n_str[:middle_index], n_str[middle_index:]])

        return blink(n1, num_blinks - 1) + blink(n2, num_blinks - 1)

    return blink(2024 * n, num_blinks - 1)


def solve_a(input_string: str, num_blinks=25):
    return sum(blink(n, num_blinks) for n in parse_numbers(input_string))


def solve_b(input_string: str):
    return solve_a(input_string, num_blinks=75)
