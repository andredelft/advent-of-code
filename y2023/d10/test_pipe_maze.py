from y2023.d10.pipe_maze import solve_a, solve_b

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
    assert solve_a(TEST_INPUT_A) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT_B) == EXPECTED_SOLUTION_B
