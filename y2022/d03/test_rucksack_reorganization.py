from y2022.d03.rucksack_reorganization import solve_a, solve_b

EXPECTED_SOLUTION_A = 157
EXPECTED_SOLUTION_B = 70


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
