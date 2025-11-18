from lib.field import Field


def parse_input(input_string: str):
    return input_string.split("\n")


def get_seat_coord(boarding_pass: str):
    max_row = 127
    min_row = 0

    for char in boarding_pass[:7]:
        middle = (max_row + min_row) // 2

        match char:
            case "F":
                max_row = middle
            case "B":
                min_row = middle + 1

    max_column = 7
    min_column = 0

    for char in boarding_pass[7:]:
        middle = (max_column + min_column) // 2

        match char:
            case "L":
                max_column = middle
            case "R":
                min_column = middle + 1

    return (min_row, min_column)


def get_seat_id(coord: tuple[int, int]):
    return coord[0] * 8 + coord[1]


def solve_a(input_string: str):
    max_seat_id = 0
    boarding_passes = parse_input(input_string)

    for boarding_pass in boarding_passes:
        coord = get_seat_coord(boarding_pass)
        max_seat_id = max(max_seat_id, get_seat_id(coord))

    return max_seat_id


def solve_b(input_string: str):
    coords = [
        get_seat_coord(boarding_pass) for boarding_pass in parse_input(input_string)
    ]

    field = Field.from_coords(coords)

    for coord, char in field.enumerate():
        if char == "." and all(
            field[c] == "#" for c in field.coords_around(*coord, diagonal=False)
        ):
            return get_seat_id(coord)
