from y2022.d05.supply_stacks import part_a, part_b

EXPECTED_SOLUTION_A = "CMZ"
EXPECTED_SOLUTION_B = "MCD"


def test_a():
    assert part_a() == EXPECTED_SOLUTION_A


def test_b():
    assert part_b() == EXPECTED_SOLUTION_B
