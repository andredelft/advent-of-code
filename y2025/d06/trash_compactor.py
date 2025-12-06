from lib.regex import parse_numbers
from lib.math import product
import re


def perform_operation(numbers: list[int], operation: str):
    match operation:
        case "+":
            return sum(numbers)
        case "*":
            return product(numbers)
        case _:
            raise ValueError(f"Wrong operation: '{operation}'")


def solve_a(input_string: str):
    lines = input_string.split("\n")

    operations = re.split(r"\s+", lines[-1])
    number_rows = [[] for _ in range(len(operations))]

    for line in lines[:-1]:
        numbers = parse_numbers(line)

        for i, n in enumerate(numbers):
            number_rows[i].append(n)

    return sum(
        perform_operation(number_row, operation)
        for number_row, operation in zip(number_rows, operations)
        if operation
    )


def solve_b(input_string: str):
    lines = input_string.split("\n")

    totals = []
    numbers = []
    current_operation = None

    for row in zip(*lines):
        *n_parts, operation = row

        try:
            n = int("".join(n_parts))
        except ValueError:
            continue

        if operation != " ":
            if len(numbers):
                totals.append(perform_operation(numbers, current_operation))

            numbers = [n]
            current_operation = operation
        else:
            numbers.append(n)

    totals.append(perform_operation(numbers, current_operation))

    return sum(totals)
