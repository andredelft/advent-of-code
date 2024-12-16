from lib.regex import parse_numbers
from lib.geometry import Coordinate
from lib.math import product
from lib.field import Field, flood_fill


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        p1, p2, v1, v2 = parse_numbers(line, include_negative=True)

        yield [Coordinate(p2, p1), Coordinate(v2, v1)]


def solve_a(input_string: str, dimensions=(103, 101)):
    robots = parse_input(input_string)
    quadrants = 4 * [0]

    for p, v in robots:
        y = (p[0] + 100 * v[0]) % dimensions[0]
        x = (p[1] + 100 * v[1]) % dimensions[1]

        top = y < dimensions[1] // 2
        bottom = y > dimensions[1] // 2
        left = x < dimensions[0] // 2
        right = x > dimensions[0] // 2

        if top and left:
            quadrants[0] += 1
        elif top and right:
            quadrants[1] += 1
        elif bottom and left:
            quadrants[2] += 1
        elif bottom and right:
            quadrants[3] += 1

    return product(quadrants)


# 19: horizontal
# 70: vertical
# 122: horizontal
# 171: vertical
# 225: horizontal
# 272: vertical

# h: t_h = 103 * m + 19
# v: t_v = 101 * n + 70

# 7847: horizontal & vertical


def solve_b(input_string: str, dimensions=(103, 101)):
    robots = list(parse_input(input_string))
    seconds = 0

    while True:
        seconds += 1

        draw_field = seconds % 103 == 19

        if draw_field:
            field = Field.blank(*dimensions)

        for i, (p, v) in enumerate(robots):
            y = (p[0] + v[0]) % dimensions[0]
            x = (p[1] + v[1]) % dimensions[1]

            new_position = Coordinate(y, x)

            robots[i][0] = new_position

            if draw_field:
                field[new_position] = "#"

        if draw_field:
            print(field)
            print(seconds)
            input()
