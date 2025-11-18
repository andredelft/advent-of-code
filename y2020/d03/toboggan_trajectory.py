from lib.field import Field
from lib.array import product


def parse_input(input_string: str):
    return Field(input_string)


def solve_a(input_string: str, slope=(1, 3)):
    field = parse_input(input_string)

    position = (0, 0)
    num_trees = 0

    while True:
        try:
            if field[position] == "#":
                num_trees += 1

            position = (
                position[0] + slope[0],
                (position[1] + slope[1]) % field.width,
            )

        except IndexError:
            break

    return num_trees


def solve_b(input_string: str):
    return product(
        solve_a(input_string, slope)
        for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    )
