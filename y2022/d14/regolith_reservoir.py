from lib.regex import parse_numbers
from itertools import pairwise
from more_itertools import chunked
import time

Coordinate = tuple[int, int]
Coordinates = set[Coordinate]

Dimensions = tuple[list[int, int], list[int, int]]


def get_dimensions(
    coordinates: Coordinates, initial_coordinate: Coordinate | None = None
) -> Dimensions:
    coordinate_list = list(coordinates)
    if not initial_coordinate:
        initial_coordinate = coordinate_list[0]
        coordinate_list = coordinate_list[1:]

    y = [initial_coordinate[0], initial_coordinate[0]]
    x = [initial_coordinate[1], initial_coordinate[1]]

    for coord in coordinate_list:
        y[0] = min(coord[0] - 1, y[0])
        y[1] = max(coord[0] + 2, y[1])
        x[0] = min(coord[1] - 1, x[0])
        x[1] = max(coord[1] + 2, x[1])

    return y, x


TEST_INPUT = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def parse_input(input_string: str):
    rock: Coordinates = set()
    for line in input_string.split("\n"):
        numbers = parse_numbers(line)
        for pair, next_pair in pairwise(chunked(numbers, 2)):
            if pair[0] == next_pair[0]:
                for n in range(
                    min(pair[1], next_pair[1]), max(pair[1], next_pair[1]) + 1
                ):
                    rock.add((n, pair[0]))  # x and y are switched on purpose
            elif pair[1] == next_pair[1]:
                for n in range(
                    min(pair[0], next_pair[0]), max(pair[0], next_pair[0]) + 1
                ):
                    rock.add((pair[1], n))

    return rock


def print_field(rock: Coordinates, sand: Coordinates, dimensions: Dimensions):
    lines = []
    for i in range(*dimensions[0]):
        line = ""
        for j in range(*dimensions[1]):
            if (i, j) in rock:
                line += "#"
            elif (i, j) in sand:
                line += "o"
            else:
                line += "."
        lines.append(line)
    print("\n".join(lines))


def drop_sand(
    obstacles: Coordinates,
    dimensions: Dimensions,
    start_position: Coordinate,
):
    new_sand = start_position
    while not new_sand[0] >= dimensions[0][1] - 1:
        if (new_sand[0] + 1, new_sand[1]) not in obstacles:
            new_sand = (new_sand[0] + 1, new_sand[1])
        elif (new_sand[0] + 1, new_sand[1] - 1) not in obstacles:
            new_sand = (new_sand[0] + 1, new_sand[1] - 1)
        elif (new_sand[0] + 1, new_sand[1] + 1) not in obstacles:
            new_sand = (new_sand[0] + 1, new_sand[1] + 1)
        else:
            break

    return new_sand


def solve_a(input_string=TEST_INPUT, visualize=False):
    rock = parse_input(input_string)
    start_position = (0, 500)
    dimensions = get_dimensions(rock, initial_coordinate=start_position)
    sand: Coordinates = set()
    last_sand = start_position
    while not last_sand[0] >= dimensions[0][1]:
        last_sand = drop_sand(sand | rock, dimensions, start_position)
        sand.add(last_sand)
        if visualize:
            print_field(rock, sand, dimensions)
            print("\n\n")
            time.sleep(0.2)

    print_field(rock, sand, dimensions)
    return len(sand) - 1


def solve_b(input_string=TEST_INPUT, visualize=False):
    rock = parse_input(input_string)
    start_position = (0, 500)
    dimensions = get_dimensions(rock, initial_coordinate=start_position)
    sand: Coordinates = set()
    last_sand = None
    obstacles = sand | rock
    while not last_sand == start_position:
        last_sand = drop_sand(obstacles, dimensions, start_position)
        sand.add(last_sand)
        obstacles.add(last_sand)
        if visualize:
            print_field(rock, sand, dimensions)
            print(last_sand)
            print("\n\n")
            time.sleep(0.2)

    print_field(rock, sand, dimensions)
    return len(sand)
