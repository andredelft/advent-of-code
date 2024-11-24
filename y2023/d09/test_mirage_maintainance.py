from y2023.d09.mirage_maintainance import solve_a, solve_b

TEST_INPUT = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

EXPECTED_SOLUTION_A = 114
EXPECTED_SOLUTION_B = 2


def test_a():
    assert solve_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b(TEST_INPUT) == EXPECTED_SOLUTION_B
