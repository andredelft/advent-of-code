from y2022.d13.distress_signal import solve_a, solve_b

EXPECTED_SOLUTION_A = 13
EXPECTED_SOLUTION_B = 140


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
