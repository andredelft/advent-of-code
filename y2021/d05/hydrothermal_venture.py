from pathlib import Path
import re

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    LINES = f.read()

TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parse_input(lines=LINES):
    coordinates = []

    for line in lines.split("\n"):
        x1, y1, x2, y2 = [int(n) for n in re.findall(r"\d+", line)]
        coordinates.append([(x1, y1), (x2, y2)])

    return coordinates


def gen_field(coordinates):
    x_max = 0
    y_max = 0

    for (x1, y1), (x2, y2) in coordinates:
        x = max(x1, x2)
        y = max(y1, y2)

        x_max = max(x, x_max)
        y_max = max(y, y_max)

    print(f"Field dimensions: {x_max + 1} x {y_max + 1}")

    return [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]


def print_field(field):
    field_transposed = [[0 for _ in range(len(field))] for _ in range(len(field[0]))]

    for i in range(len(field)):
        for j in range(len(field[0])):
            field_transposed[j][i] = field[i][j]

    print(
        "\n".join(
            " ".join(str(cell) if cell else "." for cell in row)
            for row in field_transposed
        )
    )


def solve_a(lines=LINES):
    coordinates = parse_input(lines)

    field = gen_field(coordinates)

    for (x1, y1), (x2, y2) in coordinates:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                field[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                field[x][y1] += 1

    num_crossroads = 0

    for row in field:
        for cell in row:
            if cell >= 2:
                num_crossroads += 1

    print(f"{num_crossroads} number of crossroads found")


def solve_b(lines=LINES):
    coordinates = parse_input(lines)

    field = gen_field(coordinates)

    for (x1, y1), (x2, y2) in coordinates:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                field[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                field[x][y1] += 1
        else:
            if x1 > x2:
                # Swap coordinates, such that x1 < x2 is guaranteed
                x3, y3 = (x1, y1)
                x1, y1 = (x2, y2)
                x2, y2 = (x3, y3)

            y_coord_iterator = (
                range(y1, y2 + 1) if (y1 < y2) else reversed(list(range(y2, y1 + 1)))
            )

            for x, y in zip(range(x1, x2 + 1), y_coord_iterator):
                field[x][y] += 1

    num_crossroads = 0

    for row in field:
        for cell in row:
            if cell >= 2:
                num_crossroads += 1

    # print_field(field)
    print(f"{num_crossroads} number of crossroads found")


if __name__ == "__main__":
    solve_a()
    solve_b()
