from y2022.d12.hill_climbing import part_a, part_b

EXPECTED_SOLUTION_A = 31
EXPECTED_SOLUTION_B = 29


def test_a():
    assert part_a() == EXPECTED_SOLUTION_A


def test_b():
    assert part_b() == EXPECTED_SOLUTION_B
