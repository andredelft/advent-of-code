from lib.field import Field, Coordinate


class WallEncounter(Exception):
    pass


def get_direction(instruction: str):
    match instruction:
        case "^":
            return Coordinate(-1, 0)
        case ">":
            return Coordinate(0, 1)
        case "v":
            return Coordinate(1, 0)
        case "<":
            return Coordinate(0, -1)


def parse_input(input_string: str):
    field, instructions = input_string.split("\n\n")

    return Field(field), instructions


def push(field: Field, coord: Coordinate, direction: Coordinate):
    num_boxes = 0

    lookahead = coord
    while field[lookahead] == "O":
        num_boxes += 1
        lookahead += direction

    if field[lookahead] == "#":
        raise WallEncounter

    if num_boxes:
        field[lookahead] = "O"
        field[coord] = "."


def gps(field: Field, char="O"):
    return sum(100 * y + x for ((y, x), value) in field.enumerate() if value == char)


def solve_a(input_string: str):
    field, instructions = parse_input(input_string)
    current_position = next(coord for coord, value in field.enumerate() if value == "@")
    field[current_position] = "."

    for instruction in instructions:
        direction = get_direction(instruction)

        if not direction:
            continue

        next_position = current_position + direction

        try:
            push(field, next_position, direction)
        except WallEncounter:
            continue

        current_position = next_position

    return gps(field)


LARGE_FIELD_MAPPING = {
    "O": "[]",
    "#": "##",
    "@": "@.",
}


def parse_large(input_string: str):
    field, instructions = parse_input(input_string)

    large_field = Field.blank(field.height, 2 * field.width)

    for coord, value in field.enumerate():
        new_values = LARGE_FIELD_MAPPING.get(value)

        if not new_values:
            continue

        for i in range(2):
            large_field[coord[0], 2 * coord[1] + i] = new_values[i]

    return large_field, instructions


def push_large(field: Field, coord: Coordinate, direction: Coordinate):

    if field[coord] == ".":
        return

    to_move = set()

    # Horizontal
    if direction[0] == 0:
        lookahead = coord

        while True:
            match field[lookahead]:
                case ".":
                    break
                case "#":
                    raise WallEncounter
                case "[" | "]":
                    to_move.add(lookahead)

            lookahead += direction

    # Vertical
    else:
        to_check = {coord}

        while to_check:
            next_to_check = set()
            for coord in to_check:
                if coord in to_move:
                    continue

                match field[coord]:
                    case "#":
                        raise WallEncounter
                    case ".":
                        continue
                    case "[" | "]" as value:
                        other_box_coord = Coordinate(
                            coord[0], coord[1] + (1 if value == "[" else -1)
                        )

                        box_coords = [coord, other_box_coord]
                        to_move.update(box_coords)
                        next_to_check.update(coord + direction for coord in box_coords)

            to_check = next_to_check

    to_move = sorted(to_move, reverse=direction in [(0, 1), (1, 0)])

    for coord in to_move:
        field[coord + direction] = field[coord]
        field[coord] = "."


class InvalidField(Exception):
    pass


def validate_field(field: Field):
    for coord, value in field.enumerate():
        if (value == "[" and not field[coord + (0, 1)] == "]") or (
            value == "]" and not field[coord - (0, 1)] == "["
        ):
            return False

    return True


def solve_b(input_string: str):
    field, instructions = parse_large(input_string)

    current_position = next(coord for coord, value in field.enumerate() if value == "@")
    field[current_position] = "."

    for instruction in instructions:
        direction = get_direction(instruction)

        if not direction:
            continue

        next_position = current_position + direction

        try:
            push_large(field, next_position, direction)
        except WallEncounter:
            continue

        # field[current_position] = "@"
        # print(field)
        # time.sleep(0.01)
        # field[current_position] = "."

        current_position = next_position

    return gps(field, char="[")
