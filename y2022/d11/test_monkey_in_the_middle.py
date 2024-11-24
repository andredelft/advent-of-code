from y2022.d11.monkey_in_the_middle import solve_a, solve_b

EXPECTED_SOLUTION_A = 10605
EXPECTED_SOLUTION_B = 2713310158


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
