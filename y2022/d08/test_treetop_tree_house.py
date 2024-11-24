from y2022.d08.treetop_tree_house import solve_a, solve_b

EXPECTED_SOLUTION_A = 21
EXPECTED_SOLUTION_B = 8


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
