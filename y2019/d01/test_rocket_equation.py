from y2019.d01.rocket_equation import part_a, part_b

TEST_INPUT = """\
12
14
1969
100756"""

EXPECTED_SOLUTION_1 = 2 + 2 + 654 + 33583
EXPECTED_SOLUTION_2 = 2 + 2 + 966 + 50346


def test_part_a():
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_1


def test_part_b():
    assert part_b(TEST_INPUT) == EXPECTED_SOLUTION_2
