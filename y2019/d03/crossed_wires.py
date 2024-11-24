from itertools import pairwise, product

from lib.geometry import manhattan_distance, segment_intersection, Coordinate
from lib.math import defined_min


def parse_input(input_string: str):
    wires: list[list[Coordinate]] = []
    wire_lengths: list[dict[Coordinate, int]] = []
    for wire in input_string.split("\n"):
        j, i = (0, 0)
        wire_length = 0
        wire_length_map = {(j, i): wire_length}
        coords = [(j, i)]
        for segment in wire.split(","):
            direction = segment[0]
            num_steps = int(segment[1:])

            match direction:
                case "R":
                    i += num_steps
                case "D":
                    j += num_steps
                case "L":
                    i -= num_steps
                case "U":
                    j -= num_steps

            wire_length += num_steps
            wire_length_map[(j, i)] = wire_length

            coords.append((j, i))

        wires.append(coords)
        wire_lengths.append(wire_length_map)

    return wires, wire_lengths


def solve_a(input_string):
    wires, _ = parse_input(input_string)
    segments = [pairwise(wire) for wire in wires]

    least_intersection_distance = None
    for segment_1, segment_2 in product(segments[0], segments[1]):
        intersection = segment_intersection(segment_1, segment_2)

        if intersection and intersection != (0, 0):
            intersection_distance = manhattan_distance(intersection)

            least_intersection_distance = defined_min(
                least_intersection_distance, intersection_distance
            )

    return int(least_intersection_distance)


def solve_b(input_string):
    wires, wire_lengths = parse_input(input_string)
    segments = [pairwise(wire) for wire in wires]

    least_intersection_length = None
    for segment_1, segment_2 in product(segments[0], segments[1]):
        intersection = segment_intersection(segment_1, segment_2)

        if intersection and intersection != (0, 0):
            intersection_length = (
                wire_lengths[0][segment_1[0]]
                + manhattan_distance(segment_1[0], intersection)
                + wire_lengths[1][segment_2[0]]
                + manhattan_distance(segment_2[0], intersection)
            )

            least_intersection_length = defined_min(
                least_intersection_length, intersection_length
            )

    return int(least_intersection_length)
