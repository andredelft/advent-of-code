from y2022.d05.supply_stacks import solve_a, solve_b

EXPECTED_SOLUTION_A = "CMZ"
EXPECTED_SOLUTION_B = "MCD"


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
