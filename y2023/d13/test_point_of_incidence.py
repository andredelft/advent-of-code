from y2023.d13.point_of_incidence import solve_a, solve_b

TEST_INPUT = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

EXPECTED_SOLUTION_A = 405
EXPECTED_SOLUTION_B = 400


def test_a():
    assert solve_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT) == EXPECTED_SOLUTION_B
