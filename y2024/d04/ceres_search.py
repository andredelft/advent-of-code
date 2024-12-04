from lib.field import Field, Coordinate


def find_xmas(field: Field, coord: Coordinate, neighbour: Coordinate):
    delta = neighbour - coord

    a_coordinate = neighbour + delta
    s_coordinate = a_coordinate + delta

    try:
        return field[a_coordinate] == "A" and field[s_coordinate] == "S"
    except IndexError:
        return False


def find_x_mas(field: Field, coord: Coordinate):
    corners = list(field.coords_around(*coord, horizontal=False))

    if sorted([field[corner] for corner in corners]) == ["M", "M", "S", "S"]:
        m_coords = [corner for corner in corners if field[corner] == "M"]

        # Check if m_coords share a coordinate, then they are on the same line
        return m_coords[0][0] == m_coords[1][0] or m_coords[0][1] == m_coords[1][1]


def parse_input(input_string: str):
    return Field(input_string)


def solve_a(input_string: str):
    field = parse_input(input_string)
    num_xmas = 0

    for coord, value in field.enumerate():
        if value == "X":
            for neighbour in field.coords_around(*coord):
                if field[neighbour] == "M":
                    if find_xmas(field, coord, neighbour):
                        num_xmas += 1

    return num_xmas


def solve_b(input_string: str):
    field = parse_input(input_string)
    num_x_mas = 0

    for coord, value in field.enumerate():
        if value == "A":
            if find_x_mas(field, coord):
                num_x_mas += 1

    return num_x_mas
