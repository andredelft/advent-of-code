from lib.field import Field, Coordinate
from lib.math import gcd
from itertools import combinations


def parse_input(input_string: str):
    field = Field(input_string)
    antennas: dict[str, list[Coordinate]] = dict()

    for coord, value in field.enumerate():
        if value != ".":
            antennas[value] = antennas.get(value, [])
            antennas[value].append(coord)

    return field, antennas


def solve_a(input_string: str):
    field, antennas = parse_input(input_string)
    antinodes: set[Coordinate] = set()

    for coords in antennas.values():
        for coord_1, coord_2 in combinations(coords, 2):
            delta = coord_2 - coord_1
            antinode_1 = coord_1 - delta
            antinode_2 = coord_2 + delta

            antinodes.update(
                antinode
                for antinode in [antinode_1, antinode_2]
                if field.contains(antinode)
            )

    return len(antinodes)


def solve_b(input_string: str):
    field, antennas = parse_input(input_string)
    antinodes: set[Coordinate] = set()

    for coords in antennas.values():
        for coord_1, coord_2 in combinations(coords, 2):
            delta = coord_2 - coord_1
            divider = gcd(*delta)
            delta //= divider

            current_antinode = coord_1
            while field.contains(current_antinode):
                antinodes.add(current_antinode)
                current_antinode -= delta

            current_antinode = coord_1 + delta
            while field.contains(current_antinode):
                antinodes.add(current_antinode)
                current_antinode += delta

    return len(antinodes)
