from lib.regex import parse_numbers
from itertools import product
from tqdm import tqdm


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        test, *numbers = parse_numbers(line)

        yield (test, numbers)


def is_valid_equation(
    expected_result: int, numbers: list[int], available_operations: str
):
    for operations in product(available_operations, repeat=len(numbers) - 1):
        result = numbers[0]

        for number, operation in zip(numbers[1:], operations):
            match operation:
                case "M":  # Multiply
                    result *= number
                case "A":  # Add
                    result += number
                case "C":  # Concatenate
                    result = int(str(result) + str(number))
                case _:
                    raise ValueError("Operation not recognized")

            if result > expected_result:
                break

        if result == expected_result:
            return True

    return False


def solve_a(input_string: str):
    calibration_equations = parse_input(input_string)

    return sum(
        expected_result
        for expected_result, numbers in calibration_equations
        if is_valid_equation(expected_result, numbers, available_operations="MA")
    )


def solve_b(input_string: str):
    calibration_equations = parse_input(input_string)

    # Track with progress bar
    equation_iterator = tqdm(
        calibration_equations,
        total=len(input_string.split("\n")),
        desc="Testing equations",
    )

    return sum(
        expected_result
        for expected_result, numbers in equation_iterator
        if is_valid_equation(expected_result, numbers, available_operations="MAC")
    )
