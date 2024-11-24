from pathlib import Path
import re


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    coordinates = set(
        (int(coords[0]), int(coords[1]))
        for coords in re.findall(r"(\d+),(\d+)", input_string)
    )
    folds = [
        (fold[0], int(fold[1]))
        for fold in re.findall(r"fold along (x|y)=(\d+)", input_string)
    ]
    return coordinates, folds


def perform_fold(coordinates, fold):
    new_coordinates = set()
    axis = {"x": 0, "y": 1}[fold[0]]
    pos = fold[1]
    for coord in coordinates:
        coord_list = list(coord)
        if coord_list[axis] > pos:
            coord_list[axis] = 2 * pos - coord_list[axis]

        new_coordinates.add(tuple(coord_list))
    return new_coordinates


def print_paper(coordinates):
    x_max, y_max = 0, 0
    for x, y in coordinates:
        x_max = max(x, x_max)
        y_max = max(y, y_max)

    paper = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    for i in range(x_max + 1):
        for j in range(y_max + 1):
            if (i, j) in coordinates:
                paper[j][i] = 1

    print(
        "\n".join("".join("#" if point else "." for point in line) for line in paper),
        end="\n\n",
    )


def solve_a(input_string=INPUT_STRING):
    coordinates, folds = parse_input(input_string)

    coordinates = perform_fold(coordinates, folds[0])

    print(f"{len(coordinates)} dots left after 1 fold")

    return len(coordinates)


def solve_b(input_string=INPUT_STRING):
    coordinates, folds = parse_input(input_string)

    for fold in folds:
        coordinates = perform_fold(coordinates, fold)

    print("Final message:")
    print_paper(coordinates)


if __name__ == "__main__":
    solve_a()
    solve_b()
