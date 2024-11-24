from y2023.d06.wait_for_it import part_a, part_b

TEST_INPUT = """\
Time:      7  15   30
Distance:  9  40  200"""

EXPECTED_SOLUTION_A = 288
EXPECTED_SOLUTION_B = 71503


def test_a():
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT) == EXPECTED_SOLUTION_B
