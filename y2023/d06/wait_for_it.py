from math import floor, ceil
import re

from lib.regex import parse_numbers
from lib.math import solve_quadratic


def find_num_record_times(time: int, record_distance: int):
    """
    When pressing the button `t < time` seconds, the boat will travel:

    ```
    d = (time - t) * t
    ```

    So we need to solve for which t holds `(time - t) * t > record_distance`.
    This comes down to solving the quadratic equation `-t**2 + time * t -
    record_distance == 0`. If there are two solutions `t_1` and `t_2`, the record
    will be beaten within this range. Thus we return the number of integers
    within this range.
    """

    sols = solve_quadratic(-1, time, -1 * record_distance)

    if len(sols) < 2:
        return 0

    # The number of record times equals the number of integers in the solution range
    return ceil(sols[1]) - floor(sols[0]) - 1


def parse_input(input_string: str):
    times, record_distances = input_string.split("\n")

    return parse_numbers(times), parse_numbers(record_distances)


def parse_kerned_input(input_string: str):
    lines = input_string.split("\n")

    time = int("".join(re.findall(r"\d", lines[0])))
    record_distance = int("".join(re.findall("\d", lines[1])))

    return time, record_distance


def solve_a(input_string: str):
    times, record_distances = parse_input(input_string)

    record_product = 1
    for time, record_distance in zip(times, record_distances):
        num_record_times = find_num_record_times(time, record_distance)

        if num_record_times == 0:
            record_product = 0
            break

        record_product *= num_record_times

    return record_product


def solve_b(input_string: str):
    time, record_distance = parse_kerned_input(input_string)

    return find_num_record_times(time, record_distance)
