from y2022.d07.no_space import solve_a, solve_b

EXPECTED_SOLUTION_A = 95437
EXPECTED_SOLUTION_B = 24933642


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
