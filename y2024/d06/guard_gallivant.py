from lib.field import Field
from lib.geometry import Coordinate, Direction
from tqdm import tqdm


class Historian:
    def __init__(
        self,
        field: Field,
        initial_position: Coordinate,
        initial_direction=Direction.UP,
    ):
        self.field = field
        self.position = initial_position
        self.direction = initial_direction
        self.history = {(self.position, self.direction)}
        self.path = {self.position}

        self.on_edge = False
        self.in_loop = False

    def rotate(self):
        match self.direction:
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.RIGHT:
                self.direction = Direction.DOWN
            case Direction.DOWN:
                self.direction = Direction.LEFT
            case Direction.LEFT:
                self.direction = Direction.UP

    def move(self):
        if self.on_edge:
            return

        next_position = self.position + self.direction.value

        if (next_position, self.direction) in self.history:
            self.in_loop = True
            return

        try:
            next_field_value = self.field[next_position]
        except IndexError:
            self.on_edge = True
        else:
            match next_field_value:
                case ".":
                    self.position = next_position
                    self.history.add((next_position, self.direction))
                    self.path.add(next_position)
                case "#":
                    self.rotate()
                    self.move()


def parse_input(input_string: str):
    field = Field(input_string)

    position = next(coord for coord, value in field.enumerate() if value == "^")
    field[position] = "."

    return field, position


def solve_a(input_string: str, return_path=False):
    field, position = parse_input(input_string)

    historian = Historian(field, position)

    while not historian.on_edge:
        historian.move()

    if return_path:
        return historian.path

    return len(historian.path)


def solve_b(input_string: str):
    path = solve_a(input_string, return_path=True)
    field, position = parse_input(input_string)

    num_loops = 0

    for coord in tqdm(path, desc="Obstructing the historians path"):
        if field[coord] != "." or coord == position:
            continue

        obstructed_field = field.copy()
        obstructed_field[coord] = "#"

        historian = Historian(obstructed_field, position)

        while not historian.on_edge and not historian.in_loop:
            historian.move()

        if historian.in_loop:
            num_loops += 1

    return num_loops
