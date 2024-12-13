from lib.field import Field, Coordinate


def find_xmas(field: Field, coord: Coordinate, neighbour: Coordinate):
    if field[neighbour] != "M":
        return False

    delta = neighbour - coord

    a_coordinate = neighbour + delta
    s_coordinate = a_coordinate + delta

    try:
        return field[a_coordinate] == "A" and field[s_coordinate] == "S"
    except IndexError:
        return False


def find_x_mas(field: Field, coord: Coordinate):
    if field[coord] != "A":
        return False

    corners = [coord for coord in field.coords_around(*coord, straight=False)]

    if sorted([field[corner] for corner in corners]) == ["M", "M", "S", "S"]:
        m_coords = [corner for corner in corners if field[corner] == "M"]

        # Check if m_coords share a coordinate, then they are on the same line
        return m_coords[0][0] == m_coords[1][0] or m_coords[0][1] == m_coords[1][1]

    return False


def solve_a(input_string: str):
    field = Field(input_string)

    num_xmas = 0

    for coord, value in field.enumerate():
        if value != "X":
            continue

        num_xmas += sum(
            find_xmas(field, coord, neighbour)
            for neighbour in field.coords_around(*coord)
        )

    return num_xmas


def solve_b(input_string: str):
    field = Field(input_string)

    num_x_mas = sum(find_x_mas(field, coord) for coord in field.coords())

    return num_x_mas
