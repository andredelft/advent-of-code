from lib.regex import parse_numbers
from bisect import insort


def parse_input(input_string: str):
    ranges_str, ids_str = input_string.split("\n\n")

    ranges: list[tuple[int, int]] = []

    for line in ranges_str.split("\n"):
        n_min, n_max = parse_numbers(line)
        insort(ranges, (n_min, n_max))

    ids: list[int] = []

    for line in ids_str.split("\n"):
        insort(ids, int(line))

    return ranges, ids


def solve_a(input_string: str):
    ranges, ids = parse_input(input_string)
    num_fresh = 0

    id_pointer = 0
    ranges_pointer = 0

    while id_pointer <= len(ids) - 1 and ranges_pointer <= len(ranges) - 1:
        n = ids[id_pointer]
        n_min, n_max = ranges[ranges_pointer]

        if n < n_min:
            id_pointer += 1
        elif n > n_max:
            ranges_pointer += 1
        else:
            num_fresh += 1
            id_pointer += 1

    return num_fresh


def solve_b(input_string: str):
    ranges, _ = parse_input(input_string)

    num_fresh = 0
    max_fresh = 0

    for n_min, n_max in ranges:
        if n_max <= max_fresh:
            continue

        num_fresh += n_max - max(n_min, max_fresh + 1) + 1
        max_fresh = n_max

    return num_fresh
