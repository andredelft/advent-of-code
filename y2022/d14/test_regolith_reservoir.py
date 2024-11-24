from y2022.d14.regolith_reservoir import part_a, part_b

EXPECTED_SOLUTION_A = 24
EXPECTED_SOLUTION_B = 93


def test_a():
    assert part_a() == EXPECTED_SOLUTION_A


def test_b():
    assert part_b() == EXPECTED_SOLUTION_B
