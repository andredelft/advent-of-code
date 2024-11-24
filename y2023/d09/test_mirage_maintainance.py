from y2023.d09.mirage_maintainance import part_a, part_b

TEST_INPUT = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

EXPECTED_SOLUTION_A = 114
EXPECTED_SOLUTION_B = 2


def test_a():
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT) == EXPECTED_SOLUTION_B
