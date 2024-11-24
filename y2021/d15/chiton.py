from pathlib import Path
import re
import numpy as np
from dijkstra import dijkstra_array


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    array = np.array(
        [
            [int(n) for n in re.findall(r"\d", line)]
            for line in input_string.split("\n")
            if line
        ]
    )
    if not all(len(line) == len(array[0]) for line in array):
        raise ValueError("Not all lines are equal")
    return array


def find_path_in_array(array):
    """Find shortest path in array from top left to bottom right"""
    height, length = array.shape
    initial_position = (0, 0)
    target_position = (height - 1, length - 1)
    distance_table = dijkstra_array(array, initial_position)
    distance_entry = distance_table[target_position]
    print(f"Shortest route to end is {distance_entry.shortest_distance} units long")
    return distance_entry.shortest_distance


def solve_a(input_string=INPUT_STRING):
    array = parse_input(input_string)
    return find_path_in_array(array)


def solve_b(input_string=INPUT_STRING):
    array = parse_input(input_string)

    extended_array = array.copy()
    for n in range(4):
        extended_array = np.append(extended_array, (array + n) % 9 + 1, axis=0)
    vertical_slice = extended_array.copy()
    for n in range(4):
        extended_array = np.append(extended_array, (vertical_slice + n) % 9 + 1, axis=1)

    return find_path_in_array(extended_array)


if __name__ == "__main__":
    solve_a()
    solve_b()
