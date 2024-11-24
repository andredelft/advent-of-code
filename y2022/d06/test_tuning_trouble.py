from y2022.d06.tuning_trouble import solve_a, solve_b

EXPECTED_SOLUTION_A = 7
EXPECTED_SOLUTION_B = 19


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
