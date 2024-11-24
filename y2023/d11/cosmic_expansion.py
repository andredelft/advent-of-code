from itertools import combinations

from lib.field import Field


def cosmic_expansion(cosmos):
    expanded_cosmos = []

    for row in cosmos.rows():
        expanded_cosmos.append([*row])
        if all(space == "." for space in row):
            expanded_cosmos.append([*row])

    for i, col in reversed(list(enumerate(cosmos.cols()))):
        if all(space == "." for space in col):
            for j in range(len(expanded_cosmos)):
                expanded_cosmos[j].insert(i, ".")

    return Field(expanded_cosmos)


def part_a(input_string: str):
    cosmos = Field(input_string)
    expanded_cosmos = cosmic_expansion(cosmos)
    print(expanded_cosmos)

    galaxies = [coord for coord, space in expanded_cosmos.enumerate() if space == "#"]

    distance_sum = 0
    for g_1, g_2 in combinations(galaxies, 2):
        distance_sum += abs(g_1[0] - g_2[0]) + abs(g_1[1] - g_2[1])

    return distance_sum


def part_b(input_string: str, expansion_coefficient=1_000_000):
    cosmos = Field(input_string)

    empty_rows = set(
        j for j, row in enumerate(cosmos.rows()) if all(char == "." for char in row)
    )
    empty_cols = set(
        i for i, col in enumerate(cosmos.cols()) if all(char == "." for char in col)
    )

    galaxies = [coord for coord, space in cosmos.enumerate() if space == "#"]

    distance_sum = 0

    for g_1, g_2 in combinations(galaxies, 2):
        row_min, row_max = sorted([g_1[0], g_2[0]])
        col_min, col_max = sorted([g_1[1], g_2[1]])

        num_empty_rows = len([row for row in empty_rows if row_min < row < row_max])
        num_empty_cols = len([col for col in empty_cols if col_min < col < col_max])

        row_dist = row_max - row_min + num_empty_rows * (expansion_coefficient - 1)
        col_dist = col_max - col_min + num_empty_cols * (expansion_coefficient - 1)

        distance_sum += row_dist + col_dist

    return distance_sum
