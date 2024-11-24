from y2022.d01.calorie_counting import part_a, part_b

EXPECTED_SOLUTION_A = 24000
EXPECTED_SOLUTION_B = 45000


def test_a():
    assert part_a() == EXPECTED_SOLUTION_A


def test_b():
    assert part_b() == EXPECTED_SOLUTION_B
