from y2022.d01.calorie_counting import solve_a, solve_b

EXPECTED_SOLUTION_A = 24000
EXPECTED_SOLUTION_B = 45000


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
