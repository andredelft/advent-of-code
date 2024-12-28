from y2019.intcode import Intcode
from lib.geometry import Coordinate
from lib.array import SortedList
from lib.field import Field
import time

DIRECTIONS = {
    1: Coordinate(-1, 0),  # North
    2: Coordinate(1, 0),  # South
    3: Coordinate(0, -1),  # West
    4: Coordinate(0, 1),  # East
}


def visualize_field(
    path: set[Coordinate], walls: set[Coordinate], oxygen: set[Coordinate]
):
    field = Field.from_coords(path, walls, oxygen, char=".#O", blank_char=" ")
    print("\n" * 40, field, sep="\n")
    time.sleep(0.01)


def solve_a(input_string: str, return_data=False, visualize=True):
    intcode = Intcode.parse_input(input_string, pause_on_input=True)

    # Perform Dijkstra's algorithm
    start_node = Coordinate(0, 0)
    visited = set()
    walls = set()

    unvisited = SortedList([(start_node, intcode, 0)], key=lambda x: x[2])
    distance_map = {start_node: 0}
    end_node = None  # We expect to find it during the process

    while unvisited:
        node, intcode, distance = unvisited.pop(0)
        visited.add(node)

        for input_code, direction in reversed(list(DIRECTIONS.items())):
            output = intcode.run(input_code)

            neighbour = node + direction
            neighbour_distance = distance + 1

            if output == 0:
                walls.add(neighbour)

            if output == 0 or neighbour in visited:
                intcode.reset()
                continue

            if output == 2:
                end_node = neighbour

            if neighbour not in distance_map.keys():
                distance_map[neighbour] = neighbour_distance

                unvisited.add((neighbour, intcode.copy(), neighbour_distance))

            intcode.reset()

        if visualize:
            visualize_field(visited, walls, {end_node} if end_node else set())

    if return_data:
        oxygen = {end_node}
        path = visited - oxygen
        return path, walls, oxygen

    return distance_map[end_node]


def solve_b(input_string: str, visualize=True):
    path, walls, oxygen = solve_a(input_string, return_data=True, visualize=visualize)
    oxygen_border = oxygen.copy()
    counter = 0

    while path:
        new_oxygen_border = set()

        for coord in oxygen_border:
            for direction in DIRECTIONS.values():
                neighbour = coord + direction

                if neighbour not in path:
                    continue

                new_oxygen_border.add(neighbour)

        oxygen_border = new_oxygen_border
        path -= oxygen_border
        oxygen |= oxygen_border
        counter += 1

        if visualize:
            visualize_field(path, walls, oxygen)

    return counter
