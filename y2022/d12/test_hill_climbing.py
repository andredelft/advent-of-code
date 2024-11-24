from y2022.d12.hill_climbing import solve_a, solve_b

EXPECTED_SOLUTION_A = 31
EXPECTED_SOLUTION_B = 29


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
