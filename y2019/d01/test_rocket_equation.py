from y2019.d01.rocket_equation import solve_a, solve_b

TEST_INPUT = """\
12
14
1969
100756"""

EXPECTED_SOLUTION_1 = 2 + 2 + 654 + 33583
EXPECTED_SOLUTION_2 = 2 + 2 + 966 + 50346


def test_solve_a():
    assert solve_a(TEST_INPUT) == EXPECTED_SOLUTION_1


def test_solve_b():
    assert solve_b(TEST_INPUT) == EXPECTED_SOLUTION_2
