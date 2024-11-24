from y2022.d04.camp_cleanup import solve_a, solve_b

EXPECTED_SOLUTION_A = 2
EXPECTED_SOLUTION_B = 4


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
