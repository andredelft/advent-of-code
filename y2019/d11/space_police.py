from y2019.intcode import Intcode
from lib.field import Field, Coordinate


class Robot:
    def __init__(self):
        self.position = Coordinate(0, 0)
        self.direction = Coordinate(-1, 0)

    def move(self, instruction: int):
        match instruction:
            case 0:
                self.direction = self.direction.rotate_left()
            case 1:
                self.direction = self.direction.rotate_right()

        self.position += self.direction


def solve_a(input_string: str, white_panels: set[Coordinate] = set()):
    black_panels: set[Coordinate] = set()
    intcode = Intcode.parse_input(
        input_string, pause_on_input=True, output_as_array=True
    )

    robot = Robot()

    while True:
        current_color = int(robot.position in white_panels)
        intcode.run(current_color)

        if intcode.current_instruction == 99:
            break

        color, direction = intcode.value[-2:]

        if color:
            white_panels.add(robot.position)

            if robot.position in black_panels:
                black_panels.remove(robot.position)

        else:
            black_panels.add(robot.position)

            if robot.position in white_panels:
                white_panels.remove(robot.position)

        robot.move(direction)

    field = Field.from_coords(white_panels)
    print(field)

    return len(black_panels | white_panels)


def solve_b(input_string: str):
    solve_a(input_string, white_panels={Coordinate(0, 0)})
