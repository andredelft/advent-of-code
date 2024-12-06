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
        self.visited = {self.position}

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
        next_position = self.position + self.direction.value

        try:
            next_field_value = self.field[next_position]
        except IndexError:
            self.on_edge = True
        else:
            match next_field_value:
                case ".":
                    self.position = next_position
                    self._update_history(next_position, self.direction)
                case "#":
                    self.rotate()
                    self.move()

    def walk(self):
        while not (self.on_edge or self.in_loop):
            self.move()

    def _update_history(self, position: Coordinate, direction: Direction):
        history_entry = (position, direction)

        if history_entry in self.history:
            self.in_loop = True
        else:
            self.history.add(history_entry)
            self.visited.add(position)


def parse_input(input_string: str):
    field = Field(input_string)

    position = next(coord for coord, value in field.enumerate() if value == "^")
    field[position] = "."

    return field, position


def solve_a(input_string: str, return_visited=False):
    field, position = parse_input(input_string)

    historian = Historian(field, position)

    historian.walk()

    if return_visited:
        return historian.visited

    return len(historian.visited)


def solve_b(input_string: str):
    field, position = parse_input(input_string)
    visited = solve_a(input_string, return_visited=True)
    visited.remove(position)  # Don't obstruct the historian's initial position

    num_loops = 0

    for coord in tqdm(visited, desc="Obstructing the historian's path"):
        obstructed_field = field.copy()
        obstructed_field[coord] = "#"

        historian = Historian(obstructed_field, position)

        historian.walk()

        if historian.in_loop:
            num_loops += 1

    return num_loops
