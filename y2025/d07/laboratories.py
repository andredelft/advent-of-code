from lib.field import Field, Coordinate
from collections import Counter


def solve_a(input_string: str):
    field = Field(input_string)

    beam = [field.find("S")]
    num_splitters = 0

    while len(beam):
        new_beam: set[Coordinate] = set()

        for coord in beam:
            coord_below = coord + (1, 0)

            if not field.contains(coord_below):
                continue

            if field[coord_below] == "^":
                num_splitters += 1
                new_beam.add(coord_below - (0, 1))
                new_beam.add(coord_below + (0, 1))
            else:
                new_beam.add(coord_below)

        beam = new_beam

    return num_splitters


def solve_b(input_string: str):
    field = Field(input_string)

    beam = Counter([field.find("S")])

    while True:
        new_beam = Counter()

        for coord, count in beam.items():
            coord_below = coord + (1, 0)

            if not field.contains(coord_below):
                continue

            if field[coord_below] == "^":
                new_beam[coord_below - (0, 1)] += count
                new_beam[coord_below + (0, 1)] += count
            else:
                new_beam[coord_below] += count

        if len(new_beam) == 0:
            break

        beam = new_beam

    return sum(beam.values())
