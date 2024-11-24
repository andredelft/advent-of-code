from y2022.d02.rock_paper_scissors import solve_a, solve_b

EXPECTED_SOLUTION_A = 15
EXPECTED_SOLUTION_B = 12


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
