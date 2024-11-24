import re

SPELLED_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

RE_DIGIT = rf"(?=(\d|{'|'.join(SPELLED_DIGITS.keys())}))"


def parse_input(input_string: str):
    return input_string.split("\n")


def part_a(input_string):
    calibration_value = 0

    for line in parse_input(input_string):
        digits = re.findall("\d", line)
        calibration_value += int(digits[0] + digits[-1])

    return calibration_value


def part_b(input_string):
    calibration_value = 0

    for line in parse_input(input_string):
        digits = re.findall(RE_DIGIT, line)

        first_digit = SPELLED_DIGITS.get(digits[0], digits[0])
        last_digit = SPELLED_DIGITS.get(digits[-1], digits[-1])

        calibration_value += int(f"{first_digit}{last_digit}")

    return calibration_value
