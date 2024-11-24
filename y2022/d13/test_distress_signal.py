from y2022.d13.distress_signal import part_a, part_b

EXPECTED_SOLUTION_A = 13
EXPECTED_SOLUTION_B = 140


def test_a():
    assert part_a() == EXPECTED_SOLUTION_A


def test_b():
    assert part_b() == EXPECTED_SOLUTION_B
