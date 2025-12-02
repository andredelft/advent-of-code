import re
from itertools import batched

RE_RANGE = re.compile(r"(\d+)-(\d+)")


def parse_input(input_string: str):
    for m in RE_RANGE.finditer(input_string):
        a, b = m.groups()
        yield int(a), int(b)


def is_valid(n):
    n_str = str(n)
    length = len(n_str)

    if length % 2 != 0:
        return True

    return n_str[: length // 2] != n_str[length // 2 :]


def solve_a(input_string: str):
    invalid_ids = []
    for a, b in parse_input(input_string):
        pointer = a

        while pointer <= b:

            if is_valid(pointer):
                pointer += 1
                continue

            invalid_ids.append(pointer)
            pointer += 10 ** (len(str(pointer)) // 2)

    return sum(invalid_ids)


def is_really_valid(n):
    n_str = str(n)
    length = len(n_str)

    for p in range(1, length // 2 + 1):
        if length % p != 0:
            continue

        batches = batched(n_str, p)
        first_batch = next(batches)

        if all(batch == first_batch for batch in batches):
            return False

    return True


def solve_b(input_string: str):
    invalid_ids = []

    for a, b in parse_input(input_string):
        pointer = a

        while pointer <= b:
            is_valid = is_really_valid(pointer)

            if not is_valid:
                invalid_ids.append(pointer)

            pointer += 1

    return sum(invalid_ids)
