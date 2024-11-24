import re

from lib.field import Coordinate
from lib.math import hex_value, polygon_area

RE_HEX = re.compile(r"#([a-z0-9]{6})")


def get_area(boundary_nodes: list[Coordinate], num_boundary: int):
    area = polygon_area(boundary_nodes)
    num_interior = area + 1 - num_boundary // 2  # Pick's theorem
    return num_boundary + num_interior


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        direction, num_steps, color = line.split()
        yield direction, int(num_steps), RE_HEX.search(color).group(1)


def part_a(input_string: str):
    j, i = (0, 0)
    boundary_nodes = [(j, i)]
    boundary_length = 0
    for direction, num_steps, _ in parse_input(input_string):
        boundary_length += num_steps
        match direction:
            case "R":
                i += num_steps
            case "D":
                j += num_steps
            case "L":
                i -= num_steps
            case "U":
                j -= num_steps

        boundary_nodes.append((j, i))

    return get_area(boundary_nodes, boundary_length)


def part_b(input_string: str):
    j, i = (0, 0)
    boundary_nodes = [(j, i)]
    boundary_length = 0
    for *_, value in parse_input(input_string):
        num_steps = hex_value(value[:-1])
        boundary_length += num_steps
        match value[-1]:
            case "0":  # Right
                i += num_steps
            case "1":  # Down
                j += num_steps
            case "2":  # Left
                i -= num_steps
            case "3":  # Up
                j -= num_steps

        boundary_nodes.append((j, i))

    return get_area(boundary_nodes, boundary_length)
