from y2023.d03.gear_ratios import part_a, part_b

TEST_INPUT = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

EXPECTED_SOLUTION_A = 4361
EXPECTED_SOLUTION_B = 467835


def test_a():
    assert part_a(TEST_INPUT) == EXPECTED_SOLUTION_A


def test_b():
    assert part_b(TEST_INPUT) == EXPECTED_SOLUTION_B
