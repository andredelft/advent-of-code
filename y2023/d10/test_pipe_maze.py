from y2023.d10.pipe_maze import part_a, part_b

TEST_INPUT_A = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

TEST_INPUT_B = """\
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

EXPECTED_SOLUTION_A = 8
EXPECTED_SOLUTION_B = 4


def test_a():
    assert part_a(TEST_INPUT_A) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT_B) == EXPECTED_SOLUTION_B
