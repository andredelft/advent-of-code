from lib.field import Field
from lib.geometry import Coordinate
import time
from functools import cache


def parse_input(input_string: str):
    return Field(input_string)


def step_a(field: Field):
    new_field = field.copy()

    for coord, char in field.enumerate():
        match char:
            case "L":
                if all(field[c] != "#" for c in field.coords_around(*coord)):
                    new_field[coord] = "#"
            case "#":
                if sum(field[c] == "#" for c in field.coords_around(*coord)) >= 4:
                    new_field[coord] = "L"

    # print("", new_field, sep="\n")
    # time.sleep(0.1)

    return new_field


def solve_a(input_string: str):
    field = parse_input(input_string)

    while True:
        new_field = step_a(field)

        if new_field == field:
            break

        field = new_field

    return sum(char == "#" for char in field)


DIRECTIONS = [
    Coordinate(1, 1),
    Coordinate(1, 0),
    Coordinate(1, -1),
    Coordinate(0, -1),
    Coordinate(-1, -1),
    Coordinate(-1, 0),
    Coordinate(-1, 1),
    Coordinate(0, 1),
]


@cache
def sees_occupied_chair(field: Field, coord: Coordinate, direction: Coordinate):
    neighbour = coord + direction

    try:
        neighbour_char = field[neighbour]
    except IndexError:
        return False

    match neighbour_char:
        case "#":
            return True
        case "L":
            return False
        case ".":
            return sees_occupied_chair(field, neighbour, direction)


def step_b(field: Field, sight_lines: dict[Coordinate, list[Coordinate]]):
    new_field = field.copy()

    for coord, char in field.enumerate():
        if char == ".":
            continue

        num_visible_occupied_chars = sum(field[c] == "#" for c in sight_lines[coord])

        if char == "L" and num_visible_occupied_chars == 0:
            new_field[coord] = "#"
        elif char == "#" and num_visible_occupied_chars >= 5:
            new_field[coord] = "L"

    # print("", new_field, sep="\n")
    # time.sleep(0.1)

    return new_field


def solve_b(input_string: str):
    field = parse_input(input_string)

    sight_lines: dict[Coordinate, list[Coordinate]] = dict()

    for coord, char in field.enumerate():
        if char != "L":
            continue

        sight_lines[coord] = []

        for direction in DIRECTIONS:
            try:
                neighbour = next(
                    c
                    for c, ch in field.enumerate_direction(coord, direction)
                    if ch == "L"
                )
            except StopIteration:
                continue

            sight_lines[coord].append(neighbour)

    while True:
        new_field = step_b(field, sight_lines)

        if new_field == field:
            break

        field = new_field

    return sum(char == "#" for char in field)
