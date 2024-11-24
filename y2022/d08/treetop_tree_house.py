from lib.array import product
from typing import Iterable

TEST_INPUT = """\
30373
25512
65332
33549
35390"""


Forest = list[list[int]]


def parse_input(input_string) -> Forest:
    return [[int(n) for n in line] for line in input_string.split("\n")]


def walk(forest: Forest):
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            yield i, j


def bidirectional_scan(n: int):
    return [range(0, n), reversed(range(0, n))]


VisiblePairs = set[tuple[int, int]]


def add_visible_pairs(
    forest: Forest,
    visible_pairs: VisiblePairs,
    n: int,
    scan_range: Iterable[int],
    axis: int,
):
    max_tree_height = -1
    for m in scan_range:
        scanned_tree_height = forest[m][n] if axis == 0 else forest[n][m]
        if scanned_tree_height > max_tree_height:
            visible_pairs.add((m, n) if axis == 0 else (n, m))
            max_tree_height = scanned_tree_height
            if max_tree_height == 9:
                break


def solve_a(input_string=TEST_INPUT):
    forest = parse_input(input_string)
    width, height = len(forest[0]), len(forest)

    visible_pairs: VisiblePairs = set(
        # Initialize with the corners of the grid, so we can skip the edges
        [(0, 0), (height - 1, 0), (0, width - 1), (height - 1, width - 1)]
    )

    for n_max, axis in [(height, 0), (width, 1)]:
        for n in range(1, n_max - 1):
            for scan_range in bidirectional_scan(width):
                add_visible_pairs(
                    forest,
                    visible_pairs,
                    n,
                    scan_range,
                    axis,
                )

    return len(visible_pairs)


def outward_scan(n: int, n_max: int):
    return [reversed(range(0, n)), range(n + 1, n_max)]


def get_view(
    forest: Forest,
    n: int,
    scan_range: Iterable[int],
    current_tree_height: int,
    axis: int,
):
    view = 0
    for m in scan_range:
        view += 1
        scanning_height = forest[m][n] if axis == 0 else forest[n][m]
        if scanning_height >= current_tree_height:
            break

    return view


def solve_b(input_string=TEST_INPUT):
    forest = parse_input(input_string)
    width, height = len(forest[0]), len(forest)
    max_scenic_score = 0
    for i, j in walk(forest):
        current_tree_height = forest[i][j]
        views = []

        for scan_ranges, axis in [
            (outward_scan(i, height), 0),
            (outward_scan(j, width), 1),
        ]:
            for scan_range in scan_ranges:
                view = get_view(
                    forest,
                    j if axis == 0 else i,
                    scan_range,
                    current_tree_height,
                    axis,
                )
                views.append(view)

        scenic_score = product(views)
        max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score
