import re

from lib.field import Field
from lib.array import product


def part_a(input_string: str):
    field = Field(input_string)

    part_number_sum = 0
    for y, line in enumerate(field.rows(joined=True)):
        for match in re.finditer(r"\d+", line):
            if any(
                re.match(r"[^\d\.]", field[j, i])
                for (j, i) in field.coords_around(y, match.span())
            ):
                part_number_sum += int(match.group())

    return part_number_sum


def part_b(input_string: str):
    field = Field(input_string)

    gears = {}
    for y, line in enumerate(field.rows(joined=True)):
        for match in re.finditer(r"\d+", line):
            number = int(match.group())
            for j, i in field.coords_around(y, match.span()):
                if field[j, i] == "*":
                    gears[j, i] = gears.get((j, i), []) + [number]

    return sum(product(nums) for nums in gears.values() if len(nums) == 2)
