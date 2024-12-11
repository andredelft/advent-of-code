from lib.field import Field, Coordinate
from functools import cache


@cache
def get_distinct_peaks(coord: Coordinate, field: Field):
    value = field[coord]

    if value == "9":
        return {coord}

    next_value = str(int(value) + 1)

    peaks = set()
    for next_coord in field.coords_around(*coord, diagonal=False):
        if field[next_coord] == next_value:
            peaks |= get_distinct_peaks(next_coord, field)

    return peaks


@cache
def get_num_trails(coord: Coordinate, field: Field):
    value = field[coord]

    if value == "9":
        return 1

    next_value = str(int(value) + 1)

    num_trails = 0
    for next_coord in field.coords_around(*coord, diagonal=False):
        if field[next_coord] == next_value:
            num_trails += get_num_trails(next_coord, field)

    return num_trails


def solve_a(input_string: str):
    field = Field(input_string)
    trailheads = [coord for (coord, value) in field.enumerate() if value == "0"]

    return sum(len(get_distinct_peaks(trailhead, field)) for trailhead in trailheads)


def solve_b(input_string: str):
    field = Field(input_string)
    trailheads = [coord for (coord, value) in field.enumerate() if value == "0"]

    return sum(get_num_trails(trailhead, field) for trailhead in trailheads)
