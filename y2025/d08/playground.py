from lib.geometry import euclidean_distance, Coordinate
from lib.regex import parse_numbers
from lib.array import product
from itertools import combinations
from collections import Counter


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        yield tuple(parse_numbers(line))


def solve_a(input_string: str):
    coords = parse_input(input_string)
    circuit_dict: dict[Coordinate, int] = dict()
    circuit_id = 1

    sorted_pairs = sorted(combinations(coords, 2), key=lambda p: euclidean_distance(*p))

    for coord_1, coord_2 in sorted_pairs[:1000]:
        circuit_1 = circuit_dict.get(coord_1)
        circuit_2 = circuit_dict.get(coord_2)

        if not circuit_1 and not circuit_2:
            circuit_dict[coord_1] = circuit_id
            circuit_dict[coord_2] = circuit_id
            circuit_id += 1

        elif circuit_1 == circuit_2:
            pass

        elif not circuit_1 or not circuit_2:
            existing_circuit = circuit_1 if circuit_1 else circuit_2
            disconnected_coord = coord_1 if not circuit_1 else coord_2

            circuit_dict[disconnected_coord] = existing_circuit

        else:  # pair connects two existing circuits
            for coord, c_id in circuit_dict.items():
                if c_id == circuit_2:
                    circuit_dict[coord] = circuit_1

    return product(count for _, count in Counter(circuit_dict.values()).most_common(3))


def solve_b(input_string: str):
    coords = list(parse_input(input_string))
    circuit_dict: dict[Coordinate, int] = dict()
    num_circuits = 0
    circuit_id = 1

    sorted_pairs = sorted(combinations(coords, 2), key=lambda p: euclidean_distance(*p))

    for coord_1, coord_2 in sorted_pairs:
        circuit_1 = circuit_dict.get(coord_1)
        circuit_2 = circuit_dict.get(coord_2)

        if not circuit_1 and not circuit_2:
            num_circuits += 1
            circuit_dict[coord_1] = circuit_id
            circuit_dict[coord_2] = circuit_id
            circuit_id += 1

        elif circuit_1 == circuit_2:
            pass

        elif not circuit_1 or not circuit_2:
            existing_circuit = circuit_1 if circuit_1 else circuit_2
            disconnected_coord = coord_1 if not circuit_1 else coord_2

            circuit_dict[disconnected_coord] = existing_circuit

        else:  # pair connects two existing circuits
            num_circuits -= 1
            for coord, c_id in circuit_dict.items():
                if c_id == circuit_2:
                    circuit_dict[coord] = circuit_1

        if num_circuits == 1 and all(coord in circuit_dict for coord in coords):
            break

    return coord_1[0] * coord_2[0]
