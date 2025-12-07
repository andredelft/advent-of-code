from lib.field import Field, Coordinate


def is_accessible(coord: Coordinate, field: Field):
    return sum(field[neighbour] == "@" for neighbour in field.coords_around(*coord)) < 4


def solve_a(input_string: str):
    field = Field(input_string)

    return sum(
        is_accessible(coord, field) for coord, char in field.enumerate() if char == "@"
    )


def solve_b(input_string: str):
    field = Field(input_string)
    num_rolls = field.count("@")

    while True:
        new_field = field.copy()

        for coord, char in field.enumerate():
            if char == "@" and is_accessible(coord, field):
                new_field[coord] = "."

        if field == new_field:
            break

        field = new_field

    return num_rolls - field.count("@")
