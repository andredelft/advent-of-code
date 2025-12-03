from typing import Literal
from lib.array import product
from lib.math import sieve


def parse_input(input_string: str):
    earliest_timestamp, busses = input_string.split("\n")

    busses: list[int | Literal["x"]] = [
        int(n) if n != "x" else "x" for n in busses.split(",")
    ]

    return (int(earliest_timestamp), busses)


def solve_a(input_string: str):
    earliest_timestamp, busses = parse_input(input_string)

    return product(min((n - (earliest_timestamp % n), n) for n in busses if n != "x"))


def solve_b(input_string: str):
    _, busses = parse_input(input_string)

    indexed_busses = sorted(
        ((-i % bus, bus) for (i, bus) in enumerate(busses) if bus != "x"),
        key=lambda x: x[1],
        reverse=True,
    )

    return sieve(*indexed_busses)
