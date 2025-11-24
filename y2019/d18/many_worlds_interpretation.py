from lib.field import Field
from lib.dijkstra import dijkstra, DistanceMap, NoPossiblePath
from lib.geometry import Coordinate
from functools import cache
from bisect import insort
import re
import time


def print_field(field, node=[""], hide_borders=False):
    *coords, available_keys = node

    new_field = field.copy()

    if hide_borders:
        for coord, char in new_field.enumerate():
            if char == "#":
                new_field[coord] = "."

    for coord in coords:
        new_field[coord] = "@"

    for key in available_keys:
        try:
            key_coord = new_field.find(key)
        except StopIteration:
            pass
        else:
            new_field[key_coord] = "."

        try:
            door_coord = new_field.find(key.upper())
        except StopIteration:
            pass
        else:
            new_field[door_coord] = "."
    print(new_field)
    print("Keys collected:", available_keys)
    time.sleep(1)


def visualize_path(field: Field, distance_map: DistanceMap, current_node):
    for node in reversed(list(distance_map.backtrace_path(current_node))):
        print_field(field, node)


def parse_input(input_string: str):
    return Field(input_string)


def solve_a(input_string: str, visualize=True):
    field = parse_input(input_string)

    start_coord = field.find("@")
    field[start_coord] = "."

    start_node = (start_coord, "")

    keys = set(char for char in field if re.match(r"[a-z]", char))

    def is_end_node(node: tuple[Coordinate, str]):
        return len(node[1]) == len(keys)

    def get_neighbours(node: tuple[Coordinate, str]):
        coord, available_keys = node

        for neighbour in field.coords_around(*coord, diagonal=False):
            char = field[neighbour]

            if char == "." or char in available_keys:
                yield (neighbour, available_keys), 1
            elif char in keys:
                new_keys = available_keys
                new_keys += char
                yield (neighbour, "".join(sorted(new_keys))), 1
            elif char.lower() in available_keys:
                yield (neighbour, available_keys), 1

    distance_map, current_node = dijkstra(start_node, is_end_node, get_neighbours)

    if visualize:
        visualize_path(field, distance_map, current_node)

    return distance_map.get_distance(current_node)


def solve_b(input_string: str, visualize=True):
    FIELD = parse_input(input_string)

    CENTER = FIELD.find("@")
    FIELD[CENTER] = "#"
    FIELD[CENTER + (1, 0)] = "#"
    FIELD[CENTER - (1, 0)] = "#"
    FIELD[CENTER + (0, 1)] = "#"
    FIELD[CENTER - (0, 1)] = "#"
    START_COORDS = [CENTER + offset for offset in [(1, 1), (1, -1), (-1, -1), (-1, 1)]]
    for coord in START_COORDS:
        FIELD[coord] = "."

    print_field(FIELD, hide_borders=True)
    print_field(FIELD)

    START_NODE = (*START_COORDS, "")

    QUADRANTS_DOORS: list[set[str]] = [set() for _ in range(4)]
    QUADRANTS_KEYS: list[set[str]] = [set() for _ in range(4)]
    KEYS: dict[str, Coordinate] = dict()

    for coord, char in FIELD.enumerate():
        if coord[0] > CENTER[0]:
            if coord[1] > CENTER[1]:
                i = 0
            else:
                i = 1
        else:
            if coord[1] < CENTER[1]:
                i = 2
            else:
                i = 3

        if re.match(r"[a-z]", char):
            QUADRANTS_KEYS[i].add(char)
            KEYS[char] = coord
        elif re.match(r"[A-Z]", char):
            QUADRANTS_DOORS[i].add(char.lower())

    # return quadrants_doors, quadrants_keys, len(keys)

    def is_end_node(node: tuple[Coordinate, str]):
        print(node)
        return len(node[-1]) == len(KEYS)

    @cache
    def get_quadrant_neighbours(
        coord: Coordinate,
        available_quadrant_keys: str,
        unlocked_doors: str,
        quadrant_index: int,
    ):
        print(
            FIELD[coord],
            coord,
            "keys:",
            available_quadrant_keys,
            "doors:",
            unlocked_doors,
            quadrant_index,
        )

        def get_neighbours(node: Coordinate):
            for neighbour in FIELD.coords_around(*node, diagonal=False):
                char = FIELD[neighbour]

                if (char == ".") or (char in KEYS) or (char.lower() in unlocked_doors):
                    yield neighbour, 1

        print(
            f"Searching for {QUADRANTS_KEYS[quadrant_index].difference(available_quadrant_keys)} in quadrant {quadrant_index} with {available_quadrant_keys} and {unlocked_doors.upper()}"
        )
        for key in QUADRANTS_KEYS[quadrant_index].difference(available_quadrant_keys):
            end_node = KEYS[key]

            try:
                distance_map = dijkstra(coord, end_node, get_neighbours, silent=True)
            except NoPossiblePath:
                pass
            else:
                print(f"{key} found!", end_node)
                yield end_node, distance_map.get_distance(end_node)

    # @cache
    def get_neighbours(node: tuple[Coordinate, str]):
        *coords, available_keys = node

        for i, (coord, quadrant_keys, quadrant_doors) in enumerate(
            zip(coords, QUADRANTS_KEYS, QUADRANTS_DOORS)
        ):
            available_quadrant_keys = "".join(
                sorted(quadrant_keys.intersection(available_keys))
            )
            unlocked_doors = "".join(
                sorted(quadrant_doors.intersection(available_keys))
            )

            for neighbour, distance in get_quadrant_neighbours(
                coord, available_quadrant_keys, unlocked_doors, i
            ):
                if FIELD[neighbour] in KEYS:
                    new_available_keys = list(available_keys)
                    insort(new_available_keys, FIELD[neighbour])
                    new_available_keys = "".join(new_available_keys)
                else:
                    new_available_keys = available_keys

                new_coords = [
                    neighbour if i == j else coord for j, coord in enumerate(coords)
                ]
                yield (*new_coords, new_available_keys), distance

    distance_map, current_node = dijkstra(START_NODE, is_end_node, get_neighbours)

    if visualize:
        visualize_path(FIELD, distance_map, current_node)

    return distance_map.get_distance(current_node)
