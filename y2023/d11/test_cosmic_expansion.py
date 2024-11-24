from y2023.d11.cosmic_expansion import solve_a, solve_b

TEST_INPUT = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

EXPECTED_SOLUTION_A = 374
EXPECTED_SOLUTION_B = 8410


def test_a():
    assert solve_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT, expansion_coefficient=100) == EXPECTED_SOLUTION_B
