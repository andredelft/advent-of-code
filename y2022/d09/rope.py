import time
from lib.coordinates import Coordinates, get_dimensions


class OutOfBounds(Exception):
    pass


class Rope(object):

    tail_history: Coordinates = set([(0, 0)])

    def __init__(self, num_knots: int):
        self.rope = [[0, 0] for _ in range(num_knots)]

    def print(self, vert=(-20, 20), hor=(-20, 20)):
        lines = [["." for _ in range(*hor)] for _ in range(*vert)]
        for n, (i, j) in reversed(list(enumerate(self.rope))):
            lines[i - vert[0]][j - hor[0]] = str(n) if n else "H"
        print("\n".join("".join(line) for line in lines))

    def print_visited(self):
        # Find dimensions of the field
        y, x = get_dimensions(self.tail_history)

        lines = []
        for i in range(*y):
            line = ""
            for j in range(*x):
                if (i, j) in self.tail_history:
                    line += "#"
                else:
                    line += "."
            lines.append(line)
        print("\n".join(lines))

    def move(self, direction, print_step=False):
        match direction:
            case "U":
                self.rope[0][0] -= 1
            case "R":
                self.rope[0][1] += 1
            case "D":
                self.rope[0][0] += 1
            case "L":
                self.rope[0][1] -= 1

        for i in range(1, len(self.rope)):
            delta_y = self.rope[i - 1][0] - self.rope[i][0]
            delta_x = self.rope[i - 1][1] - self.rope[i][1]

            match (delta_y, delta_x):
                case (2, 1) | (2, 2) | (1, 2):
                    # .....     .....
                    # .2...     .....
                    # ...1. --> ..21.
                    # ..11.     ..11.
                    # .....     .....
                    self.rope[i][0] += 1
                    self.rope[i][1] += 1
                case (2, 0):
                    # .....     .....
                    # ..2..     .....
                    # ..... --> ..2..
                    # ..1..     ..1..
                    # .....     .....
                    self.rope[i][0] += 1
                case (2, -1) | (2, -2) | (1, -2):
                    # .....     .....
                    # ...2.     .....
                    # .1... --> .12..
                    # .11..     .11..
                    # .....     .....
                    self.rope[i][0] += 1
                    self.rope[i][1] -= 1
                case (0, -2):
                    # .....     .....
                    # .....     .....
                    # .1.2. --> .12..
                    # .....     .....
                    # .....     .....
                    self.rope[i][1] -= 1
                case (-2, -1) | (-2, -2) | (-1, -2):
                    # .....     .....
                    # .11..     .11..
                    # .1... --> .12..
                    # ...2.     .....
                    # .....     .....
                    self.rope[i][0] -= 1
                    self.rope[i][1] -= 1
                case (-2, 0):
                    # .....     .....
                    # ..1..     ..1..
                    # ..... --> ..2..
                    # ..2..     .....
                    # .....     .....
                    self.rope[i][0] -= 1
                case (-2, 1) | (-2, 2) | (-1, 2):
                    # .....     .....
                    # ..11.     ..11.
                    # ...1. --> ..21.
                    # .2...     .....
                    # .....     .....
                    self.rope[i][0] -= 1
                    self.rope[i][1] += 1
                case (0, 2):
                    # .....     .....
                    # .....     .....
                    # .2.1. --> ..21.
                    # .....     .....
                    # .....     .....
                    self.rope[i][1] += 1

        self.tail_history.add(tuple(self.rope[-1]))

        if print_step:
            self.print()
            print("\n")
            time.sleep(0.1)

    def move_n(self, direction, num_moves, print_steps=False):
        for _ in range(num_moves):
            self.move(direction, print_steps)
