from y2023.d07.camel_cards import part_a, part_b

TEST_INPUT = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

EXPECTED_SOLUTION_A = 6440
EXPECTED_SOLUTION_B = 5905


def test_a():
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT) == EXPECTED_SOLUTION_B
